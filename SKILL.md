---
name: manim-skill
description: Create voiced-over educational videos using Manim and ElevenLabs TTS. Use this skill when the user asks to create a video, make an animation, produce an explainer, or generate visual content about a topic. Also trigger when the user mentions manim, voiceover videos, or educational animations. If the user says something like "make a video about X" or "create a 30s explainer on Y", this is the skill to use.
---

# Manim Video Creator

You create fully voiced-over educational videos using Manim and ElevenLabs TTS. Given a topic or description, you produce a complete `.py` file and render command.

## Prerequisites

Before first use, ensure dependencies are installed:
```bash
pip install manim "manim-voiceover-plus[elevenlabs]"
brew install sox  # macOS (apt install sox for Linux)
```

The user's `ELEVEN_API_KEY` must be set as an environment variable.

## Workflow

1. **Understand the request** — Extract topic, key concepts, target duration (~30s default), and tone
2. **Research if needed** — If the user says to research the topic first, do web searches before writing
3. **Select voice** — Pick from the voice reference table (see `references/manim-guide.md`)
4. **Write script** — Draft narration first. Keep sentences short (TTS works better with concise phrases)
5. **Plan visuals** — For each narration segment, decide Manim objects and animations
6. **Write code** — Single `.py` file using the VoiceoverScene pattern below
7. **Render** — Provide the render command: `manim -pql video.py ClassName`

## Core Pattern

```python
from manim import *
from manim_voiceover_plus import VoiceoverScene
from manim_voiceover_plus.services.elevenlabs import ElevenLabsService

class VideoName(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            ElevenLabsService(
                voice_id="JBFqnCBsd6RMkjVDRZzb",  # George
                model="eleven_turbo_v2_5",
            )
        )

        with self.voiceover(text="Narration text here.") as tracker:
            self.play(Create(shape), run_time=tracker.duration)
```

Key rules:
- Use `voice_id`, never `voice_name` (name lookup is unreliable)
- Use `run_time=tracker.duration` to sync animations to audio
- Break content into sections (methods: `intro_section`, `main_content`, `conclusion`)
- Use bookmarks for word-level timing: `<bookmark mark='A'/>` in text, then `self.wait_until_bookmark("A")`

## Rendering

```bash
manim -pql video.py ClassName   # Low quality, fast preview
manim -pqh video.py ClassName   # High quality (1080p)
manim -pqk video.py ClassName   # 4K
```

## Verification

After rendering, extract frames and verify visually:
```bash
# Extract 8 evenly-spaced frames
VIDEO="media/videos/video/480p15/ClassName.mp4"
mkdir -p media/verification_frames
DURATION=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$VIDEO")
for i in $(seq 0 7); do
  TS=$(echo "$DURATION / 8 * $i" | bc -l)
  ffmpeg -y -ss "$TS" -i "$VIDEO" -vframes 1 -q:v 2 "media/verification_frames/frame_$(printf '%02d' $i).png" 2>/dev/null
done
```

Then use a subagent to read each frame and compare against expected visuals.

## Reference

For the full voice list, Manim object/animation reference, troubleshooting, and complete examples, read `references/manim-guide.md` in this skill directory.
