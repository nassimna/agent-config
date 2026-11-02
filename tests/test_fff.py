import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

FFF = Path(__file__).resolve().parents[1] / "scripts/fff"


class AutoIndexTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="fff-test-", dir=Path.home() / ".cache")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo"
        self.root.mkdir()
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        self.file = self.root / "session.rs"
        self.file.write_text("pub fn session_alpha() {}\n")

    def query(self, pattern, expected=0, root=None):
        result = subprocess.run([str(FFF), "-C", str(root or self.root), "grep", pattern, "--json"], capture_output=True, text=True)
        self.assertEqual(result.returncode, expected, result.stderr)
        return [json.loads(line) for line in result.stdout.splitlines()]

    def test_refreshes_file_changes_and_reuses_unchanged_index(self):
        self.assertEqual(self.query("session_alpha")[0]["path"], "session.rs")
        found = subprocess.check_output([str(FFF), "-C", str(self.root), "search", "session.rs", "--json"], text=True)
        self.assertEqual(json.loads(found)["path"], "session.rs")
        manifest = self.root / ".fff/manifest.bin"
        before = manifest.stat().st_mtime_ns
        self.query("session_alpha")
        self.assertEqual(manifest.stat().st_mtime_ns, before)
        previous = self.file.stat()
        self.file.write_text("pub fn session_bravo() {}\n")
        os.utime(self.file, ns=(previous.st_atime_ns, previous.st_mtime_ns))
        self.assertIn("session_bravo", self.query("session_bravo")[0]["line"])
        self.query("session_alpha", expected=1)
        new = self.root / "new handler.rs"
        new.write_text("pub fn created_handler() {}\n")
        self.assertEqual(self.query("created_handler")[0]["path"], new.name)
        renamed = self.root / "renamed.rs"
        new.rename(renamed)
        self.assertEqual(self.query("created_handler")[0]["path"], renamed.name)
        renamed.unlink()
        self.query("created_handler", expected=1)
        result = subprocess.check_output(["git", "-C", str(self.root), "ls-files", "--others", "--exclude-standard", ".fff"])
        self.assertEqual(result, b"")

    def test_parallel_searches_share_one_rebuild(self):
        command = [str(FFF), "-C", str(self.root), "grep", "session_alpha", "--json"]
        processes = [subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) for _ in range(2)]
        outputs = [p.communicate(timeout=30) for p in processes]
        for process, (stdout, stderr) in zip(processes, outputs):
            self.assertEqual(process.returncode, 0, stderr)
            self.assertEqual(json.loads(stdout)["path"], "session.rs")
        self.assertEqual(sum(stderr.count("Indexing ") for _, stderr in outputs), 1)

    def test_linked_worktree_keeps_its_own_index(self):
        subprocess.run(["git", "-C", str(self.root), "add", "session.rs"], check=True)
        subprocess.run(["git", "-C", str(self.root), "-c", "user.name=FFF test", "-c", "user.email=fff-test@example.invalid", "commit", "-qm", "fixture"], check=True)
        worktree = Path(self.temp.name) / "worktree"
        subprocess.run(["git", "-C", str(self.root), "worktree", "add", "-qb", "test-worktree", str(worktree)], check=True)
        self.query("session_alpha")
        (worktree / "session.rs").write_text("pub fn isolated_worktree() {}\n")
        self.assertIn("isolated_worktree", self.query("isolated_worktree", root=worktree)[0]["line"])
        self.query("isolated_worktree", expected=1)
        self.assertTrue((worktree / ".fff/manifest.bin").exists())


if __name__ == "__main__":
    unittest.main()
