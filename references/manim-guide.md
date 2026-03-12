# Manim + ElevenLabs Full Reference

## ElevenLabs Models

| Model | Speed | Quality | Cost | Best For |
|-------|-------|---------|------|----------|
| `eleven_flash_v2_5` | ~75ms | Good | 0.5 c/char | use this almost all the time |
| `eleven_turbo_v2_5` | ~250ms | High | 0.5 c/char | or this |
| `eleven_multilingual_v2` | ~500ms | Highest | 1 c/char | Premium final renders |

## Voice Selection

### Male Voices
| Voice | Description | Best For |
|-------|-------------|----------|
| Adam | Deep, warm American | General narration |
| Antoni | Warm, conversational | Casual content |
| Josh | Deep, narrative | Documentaries |
| Arnold | Crisp, authoritative | Technical content |
| Daniel | British, authoritative | Formal education |
| Clyde | Warm, friendly | Approachable explainers |

### Female Voices
| Voice | Description | Best For |
|-------|-------------|----------|
| Rachel | Calm, clear American | Professional narration |
| Bella | Warm, expressive | Engaging content |
| Elli | Young, enthusiastic | Energetic explainers |
| Domi | Confident, clear | Technical tutorials |
| Emily | Soft, soothing | Gentle topics |
| Charlotte | British, sophisticated | Formal content |

### Fetching Voice IDs

Voice IDs change per account. Fetch yours:
```python
from elevenlabs import ElevenLabs
client = ElevenLabs()
for v in client.voices.get_all().voices:
    print(f'{v.name}: {v.voice_id}')
```

Known defaults:
- `JBFqnCBsd6RMkjVDRZzb` — George (warm storyteller)
- `EXAVITQu4vr4xnSDxMaL` — Sarah (mature, confident)
- `Xb7hH8MSUJpSbSDYk0k2` — Alice (clear educator)
- `pFZP5JQG7iQjIQuC4Bku` — Lily (expressive)

## ElevenLabsService Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `voice_id` | Voice ID (**required**) | `"JBFqnCBsd6RMkjVDRZzb"` |
| `model` | TTS model | `"eleven_turbo_v2_5"` |
| `voice_settings` | Fine-tune (optional) | `{"stability": 0.5, "similarity_boost": 0.75}` |

## Voiceover Context Manager

```python
with self.voiceover(text="Narration text here") as tracker:
    # tracker.duration = total audio length
    self.play(animation, run_time=tracker.duration)
```

- Animation finishes before voiceover → Manim waits for audio
- Use `run_time=tracker.duration` for sync
- Multiple animations in one block play sequentially

## Bookmarks

```python
with self.voiceover(
    text="Hello <bookmark mark='A'/> world <bookmark mark='B'/> end"
) as tracker:
    self.play(FadeIn(hello_text))
    self.wait_until_bookmark("A")
    self.play(FadeIn(world_text))
    self.wait_until_bookmark("B")
    self.play(FadeIn(end_text))
```

## Common Manim Objects

### Text & Math
```python
Text("Hello", font_size=48, color=BLUE)
MathTex(r"E = mc^2", font_size=72)
Tex(r"LaTeX text with $math$")
```

### Shapes
```python
Circle(radius=1, color=RED, fill_opacity=0.5)
Rectangle(width=4, height=2, color=BLUE)
Square(side_length=2)
Arrow(start=LEFT, end=RIGHT)
Line(start=ORIGIN, end=UP*2)
```

### Positioning
```python
obj.shift(UP * 2 + RIGHT * 3)
obj.to_edge(UP)
obj.to_corner(UL)
obj.next_to(other_obj, DOWN, buff=0.5)
obj.move_to(ORIGIN)
```

### Animations
```python
self.play(Write(text))           # Write text
self.play(Create(shape))         # Draw shape
self.play(FadeIn(obj))           # Fade in
self.play(FadeOut(obj))          # Fade out
self.play(Transform(a, b))       # Morph a into b
self.play(obj.animate.shift(UP)) # Animate property
self.wait(2)                     # Pause
```

### Colors
`RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE, WHITE, BLACK, GRAY`
Shades: `RED_A` (light) through `RED_E` (dark)

## Rendering Flags

- `-p` = preview after render
- `-q` = quality: `l`=480p, `m`=720p, `h`=1080p, `k`=4K
- `-a` = render all scenes in file

## Troubleshooting

| Problem | Fix |
|---------|-----|
| "SoX not found" | `brew install sox` (macOS) / `apt install sox` (Linux) |
| ElevenLabs API errors | Verify `ELEVEN_API_KEY` is set, check credits at elevenlabs.io |
| Audio not syncing | Use `run_time=tracker.duration`, break long narrations into shorter segments |
| JSONDecodeError in cache | Delete `media/voiceover/` and re-render |

## Caching

manim-voiceover-plus caches audio via SHA-256 hash. Same text + voice = reuses cache. Cache lives in `media/voiceover/`.

## Quality Checklist

- [ ] Audio is clear and well-paced
- [ ] Animations sync with narration
- [ ] Text is readable (appropriate font size)
- [ ] Colors have good contrast
- [ ] No overlapping elements
- [ ] Smooth transitions between sections
