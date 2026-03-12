---
name: manim-skill
description: Create voiced-over videos and animations using Manim + ElevenLabs TTS. Trigger on requests like "make a video about X" or "create a 30s explainer on Y".
---

## Setup

```bash
pip install manim "manim-voiceover-plus[elevenlabs]"
brew install sox  # macOS (apt install sox for Linux)
```

Requires `ELEVEN_API_KEY` env var.

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

## Gotchas

- **Use `voice_id`, never `voice_name`** — name lookup is unreliable
- **Bookmarks** for word-level timing: `<bookmark mark='A'/>` in text, then `self.wait_until_bookmark("A")`
- **JSONDecodeError** — delete `media/voiceover/` cache folder and re-render

## Known Voice IDs

Fetch with:
```python
from elevenlabs import ElevenLabs
client = ElevenLabs()
for v in client.voices.get_all().voices:
    print(f'{v.name}: {v.voice_id}')
```

Defaults:
- `JBFqnCBsd6RMkjVDRZzb` — George (warm storyteller)
- `EXAVITQu4vr4xnSDxMaL` — Sarah (mature, confident)
- `Xb7hH8MSUJpSbSDYk0k2` — Alice (clear educator)
- `pFZP5JQG7iQjIQuC4Bku` — Lily (expressive)
