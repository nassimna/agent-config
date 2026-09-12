---
name: record-screen-flow
description: Use when the user asks to record, capture, film, or make a video of a browser flow, app workflow, desktop, screen, window, demo, or the work the agent performed.
---

# Record Screen Flow

Resolve `scripts/record-screen-flow` relative to this file and use it to manage the local X11 recording. Run it with `--help` if an option is unclear instead of reproducing or guessing the command interface.

## Default: record without interrupting the user

For browser and app demos, use an isolated background display with its own browser, pointer, and keyboard focus. Set this up automatically; the user should not need to repeat this preference. A private/incognito window on the user's active desktop does not provide this isolation.

- Respect an explicitly requested browser and the host's browser-tool rules. Verify that its capture supports the required cursor and pacing; explain any capability mismatch before substituting a different browser.
- When using a virtual X11 display, resolve an available display and bind the browser, every input command, and the recorder to that same display explicitly. Never let an omitted `DISPLAY` or recorder option fall back to the user's desktop.
- Do not move the user's physical cursor, steal keyboard focus, rearrange their windows, or capture their desktop unless they explicitly request that surface. Being AFK is not permission to use it. If isolation is unavailable, report the limitation instead of silently using the active desktop.
- Stop the task's recorder, isolated browser, and virtual display when finished; preserve shared services and requested review previews.

## Record the flow

1. Determine what the viewer should see and where the artifact belongs. Follow the current workspace's artifact rules and pass an explicit absolute `.mp4` output path.
2. Select the isolated capture environment first, then run `scripts/record-screen-flow probe` against that display. A Wayland user desktop does not rule out an available isolated X11 display. If the selected capture environment is unsupported or lacks a dependency, report the specific blocker.
3. Prepare and dry-run the flow before recording. Put the app in its intended starting state and remove unrelated windows, banners, and notifications from the isolated capture surface.
   - Capture a real headed browser on the isolated display, or use a permitted browser-native recorder after a short test proves that its exported video preserves the visible cursor, smooth motion, and the requested frame rate.
4. Capture the smallest useful surface: `active-window` for one app, `primary` for one monitor, `desktop` for all monitors, or an exact `--region` when needed.
5. Start recording before performing the requested browser or desktop flow. Audio stays off unless the user requests `system` or `mic` audio.
6. Unless the user requests another style, record a continuous, human-paced walkthrough at 30 fps:
   - Keep the real mouse pointer visible. Move it deliberately to each target before clicking; do not simulate interaction with a hidden cursor or assemble a slideshow from screenshots.
   - Use smooth, distance-appropriate movement for every pointer reposition, including between typing, scrolling, and navigation. Keep the pointer near the current task; avoid unnecessary side-to-side travel or decorative movement.
   - Type at a readable pace instead of injecting whole values instantly. Use controlled scrolling that lets the viewer follow where the page moved.
   - Begin with a brief hold on the meaningful starting state, pause after actions so their result is visible, and hold the completed state before stopping.
   - Keep the flow concise and free of setup, retries, long idle periods, frantic pointer movement, or unrelated desktop activity.
   - Prepare the complete action sequence before starting and run capture, actions, and stop together so tool orchestration does not create dead time. Wait for visible app readiness, then use brief reading holds. Show navigation through a click or keyboard action rather than an unexplained URL change.
7. If the recording is interrupted, contaminated by another window, or materially differs from the intended flow, discard it and record a clean take rather than presenting it as finished evidence.
8. Stop in cleanup even if the flow or browser interaction fails. Never leave the recorder running for the next task.
9. Use `ffprobe` to confirm nonzero duration, expected dimensions, a video stream, 30 fps unless overridden, and audio only when requested. Scrub representative frames from the beginning, middle, and end to confirm the intended app is readable, the cursor appears during interaction, and no unrelated content entered the capture. Give the user the video path or workspace-required reachable link and a short statement of what it shows.

Example shape after resolving the isolated display and its geometry:

```bash
scripts/record-screen-flow status || true
scripts/record-screen-flow start --output /absolute/path/to/flow.mp4 --display "$recording_display" --region "$recording_region"
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
