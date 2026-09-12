---
name: record-screen-flow
description: Use when the user asks to record, capture, film, or make a video of a browser flow, app workflow, desktop, screen, window, demo, or the work the agent performed.
---

# Record Screen Flow

Resolve `scripts/record-screen-flow` relative to this file and use it to manage the local X11 recording. Run it with `--help` if an option is unclear instead of reproducing or guessing the command interface.

## Record the flow

1. Determine what the viewer should see and where the artifact belongs. Follow the current workspace's artifact rules and pass an explicit absolute `.mp4` output path.
2. Run `scripts/record-screen-flow probe`. If it reports Wayland or a missing dependency, stop and report the specific blocker.
3. Prepare and dry-run the flow before recording. Put the app in its intended starting state, close or hide unrelated windows and notifications, and use a dedicated browser window or isolated display when focus changes could enter the capture.
4. Capture the smallest useful surface: `active-window` for one app, `primary` for one monitor, `desktop` for all monitors, or an exact `--region` when needed.
5. Start recording before performing the requested browser or desktop flow. Audio stays off unless the user requests `system` or `mic` audio.
6. Unless the user requests another style, record a continuous, human-paced walkthrough at 30 fps:
   - Keep the real mouse pointer visible. Move it deliberately to each target before clicking; do not simulate interaction with a hidden cursor or assemble a slideshow from screenshots.
   - Type at a readable pace instead of injecting whole values instantly. Use controlled scrolling that lets the viewer follow where the page moved.
   - Begin with a brief hold on the meaningful starting state, pause after actions so their result is visible, and hold the completed state before stopping.
   - Keep the flow concise and free of setup, retries, long idle periods, frantic pointer movement, or unrelated desktop activity.
7. If the recording is interrupted, contaminated by another window, or materially differs from the intended flow, discard it and record a clean take rather than presenting it as finished evidence.
8. Stop in cleanup even if the flow or browser interaction fails. Never leave the recorder running for the next task.
9. Use `ffprobe` to confirm nonzero duration, expected dimensions, a video stream, 30 fps unless overridden, and audio only when requested. Scrub representative frames from the beginning, middle, and end to confirm the intended app is readable and no unrelated content entered the capture. Give the user the video path or workspace-required reachable link and a short statement of what it shows.

Example shape:

```bash
scripts/record-screen-flow status || true
scripts/record-screen-flow start --output /absolute/path/to/flow.mp4 --target active-window
# Perform the requested flow.
scripts/record-screen-flow stop
ffprobe -v error -show_entries stream=codec_type,width,height,avg_frame_rate -show_entries format=duration /absolute/path/to/flow.mp4
```

## Boundaries

- A request to record a named flow authorizes only that flow. Ask before starting when the capture target or stopping point would materially change what is exposed.
- Avoid passwords, API keys, private messages, unrelated windows, and notification contents. The recorder captures the real visible screen.
- Keep the helper's 15-minute automatic limit unless the requested flow needs longer.
- Do not overwrite an existing recording or signal an unrelated process.
- Do not upload, publish, or embed the result unless the user separately asks. Recording and file sharing are separate capabilities.
- Do not use OpenAI Record & Replay here; it teaches a reusable workflow rather than exporting the requested screen video.
