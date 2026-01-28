# Manim Voiceover Video Agent Guide

This guide enables an AI agent to create fully voiced-over educational videos using Manim and ElevenLabs TTS. Given only a video description and an ElevenLabs API key, follow this guide to produce a complete video.

## Prerequisites

### Installation
```bash
# Install manim and manim-voiceover-plus with ElevenLabs support
pip install manim "manim-voiceover-plus[elevenlabs]"

# System dependency for audio processing (required)
brew install sox  # macOS
# apt install sox  # Linux
```

### API Key Setup
Set the environment variable before running manim:
```bash
export ELEVEN_API_KEY="your_api_key_here"
```

Or create a `.env` file in the project directory:
```
ELEVEN_API_KEY=your_api_key_here
```

## ElevenLabs Models

Choose based on your needs:

| Model | Speed | Quality | Cost | Best For |
|-------|-------|---------|------|----------|
| `eleven_flash_v2_5` | ~75ms | Good | 0.5 credits/char | Fast iteration, drafts, long videos |
| `eleven_turbo_v2_5` | ~250ms | High | 0.5 credits/char | **Recommended balance** of quality and speed |
| `eleven_multilingual_v2` | ~500ms | Highest | 1 credit/char | Final renders, premium quality |

**Recommendation:** Use `eleven_turbo_v2_5` for most videos. Use `eleven_flash_v2_5` for quick previews. Use `eleven_multilingual_v2` only for final high-quality renders.

## Voice Selection Guide

### Male Voices (Educational/Narration)
| Voice Name | Description | Best For |
|------------|-------------|----------|
| `Adam` | Deep, warm American male | General narration, explainers |
| `Antoni` | Warm, conversational American | Casual educational content |
| `Josh` | Deep, narrative American | Documentaries, serious topics |
| `Arnold` | Crisp, authoritative American | Technical content, tutorials |
| `Daniel` | British, authoritative | Formal educational, documentaries |
| `Clyde` | Warm, friendly American | Approachable explainers |

### Female Voices (Educational/Narration)
| Voice Name | Description | Best For |
|------------|-------------|----------|
| `Rachel` | Calm, clear American | Professional narration |
| `Bella` | Warm, expressive American | Engaging educational content |
| `Elli` | Young, enthusiastic American | Energetic explainers |
| `Domi` | Confident, clear American | Technical tutorials |
| `Emily` | Soft, soothing American | Wellness, gentle topics |
| `Charlotte` | British, sophisticated | Formal content, documentaries |

### Voice Selection Tips
- **Technical/Educational:** Adam, Rachel, Arnold, Daniel
- **Casual/Engaging:** Antoni, Bella, Elli, Clyde
- **Documentary/Serious:** Josh, Charlotte, Daniel
- **Approachable/Friendly:** Antoni, Bella, Clyde, Emily

## Core Pattern: VoiceoverScene

```python
from manim import *
from manim_voiceover_plus import VoiceoverScene
from manim_voiceover_plus.services.elevenlabs import ElevenLabsService

class MyVideo(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            ElevenLabsService(
                voice_id="JBFqnCBsd6RMkjVDRZzb",  # George
                model="eleven_turbo_v2_5",
            )
        )
        
        with self.voiceover(text="This is what I'm saying.") as tracker:
            self.play(Create(circle), run_time=tracker.duration)
```

## ElevenLabsService Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `voice_id` | Voice ID from ElevenLabs (**required**) | `"JBFqnCBsd6RMkjVDRZzb"` |
| `model` | TTS model | `"eleven_turbo_v2_5"` |
| `voice_settings` | Fine-tune voice (optional) | `{"stability": 0.5, "similarity_boost": 0.75}` |

**Important:** Use `voice_id`, not `voice_name`. The name lookup is unreliable.

### Fetching Available Voice IDs

Run this to list your available voices:
```python
from elevenlabs import ElevenLabs
client = ElevenLabs()
for v in client.voices.get_all().voices:
    print(f'{v.name}: {v.voice_id}')
```

Example voices (IDs may vary by account):
- `JBFqnCBsd6RMkjVDRZzb` - George (warm storyteller, good for narration)
- `EXAVITQu4vr4xnSDxMaL` - Sarah (mature, confident)
- `Xb7hH8MSUJpSbSDYk0k2` - Alice (clear educator)

## The Voiceover Context Manager

```python
with self.voiceover(text="Narration text here") as tracker:
    # tracker.duration - total duration of the audio
    # Animations inside this block sync to the voiceover
    self.play(animation, run_time=tracker.duration)
```

**Key behaviors:**
- If animation finishes before voiceover → Manim waits for audio to complete
- Use `run_time=tracker.duration` to sync animation length to audio
- Multiple animations inside one block play sequentially during that voiceover

## Bookmarks for Word-Level Timing

Trigger animations at specific words:

```python
with self.voiceover(
    text="Hello <bookmark mark='A'/> world <bookmark mark='B'/> example"
) as tracker:
    self.play(FadeIn(hello_text))
    self.wait_until_bookmark("A")
    self.play(FadeIn(world_text))
    self.wait_until_bookmark("B")
    self.play(FadeIn(example_text))
```

## Video Structure Template

```python
from manim import *
from manim_voiceover_plus import VoiceoverScene
from manim_voiceover_plus.services.elevenlabs import ElevenLabsService

class EducationalVideo(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            ElevenLabsService(
                voice_id="JBFqnCBsd6RMkjVDRZzb",  # George
                model="eleven_turbo_v2_5",
            )
        )
        
        self.intro_section()
        self.main_content()
        self.conclusion()
    
    def intro_section(self):
        title = Text("Video Title", font_size=72)
        
        with self.voiceover(text="Welcome to this video about...") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        
        self.play(FadeOut(title))
    
    def main_content(self):
        # Main educational content here
        pass
    
    def conclusion(self):
        with self.voiceover(text="Thanks for watching!"):
            self.wait()
```

## Rendering Commands

```bash
# Preview (low quality, fast)
manim -pql video.py ClassName

# Medium quality
manim -pqm video.py ClassName

# High quality (1080p)
manim -pqh video.py ClassName

# 4K quality
manim -pqk video.py ClassName

# Render without preview
manim -ql video.py ClassName
```

**Flags:**
- `-p` = preview after render
- `-q` = quality (l=480p, m=720p, h=1080p, k=4K)
- `-a` = render all scenes in file

## Agent Workflow: From Description to Video

### Step 1: Parse the Video Description
Extract:
- **Topic/title** - main subject
- **Key concepts** - what to explain
- **Visual elements** - what to show on screen
- **Target duration** - how long should it be
- **Tone** - educational, casual, formal

### Step 2: Select Voice and Model
Based on tone:
- **Professional/Educational:** Adam, Rachel, Daniel + `eleven_turbo_v2_5`
- **Casual/Engaging:** Antoni, Bella, Elli + `eleven_turbo_v2_5`
- **Premium/Documentary:** Josh, Charlotte + `eleven_multilingual_v2`

### Step 3: Write the Script
Create narration text for each section. Keep sentences concise (TTS works better with shorter phrases).

### Step 4: Plan Visual Elements
For each narration segment, decide:
- What Manim objects to create (Text, MathTex, Circle, Rectangle, Arrow, etc.)
- What animations to use (Write, Create, FadeIn, Transform, etc.)
- Positioning and colors

### Step 5: Write the Code
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
        # Sections here...
```

### Step 6: Render and Verify
```bash
# Quick preview first
manim -pql video.py VideoName

# Final high-quality render
manim -pqh video.py VideoName
```

## Common Manim Objects & Animations

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
self.wait(2)                     # Pause 2 seconds
```

### Colors
`RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE, WHITE, BLACK, GRAY`
`RED_A` through `RED_E` for shades (A=light, E=dark)

## Example: Complete Simple Video

```python
from manim import *
from manim_voiceover_plus import VoiceoverScene
from manim_voiceover_plus.services.elevenlabs import ElevenLabsService

class PythagorasExplainer(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            ElevenLabsService(
                voice_id="JBFqnCBsd6RMkjVDRZzb",  # George
                model="eleven_turbo_v2_5",
            )
        )
        
        # Title
        title = Text("The Pythagorean Theorem", font_size=56, color=BLUE)
        with self.voiceover(text="The Pythagorean Theorem.") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        self.play(title.animate.to_edge(UP).scale(0.6))
        
        # Triangle
        triangle = Polygon(
            ORIGIN, RIGHT*3, RIGHT*3 + UP*4,
            color=WHITE, stroke_width=3
        ).move_to(ORIGIN)
        
        with self.voiceover(
            text="Consider a right triangle with sides a, b, and hypotenuse c."
        ) as tracker:
            self.play(Create(triangle), run_time=tracker.duration)
        
        # Labels
        a_label = MathTex("a").next_to(triangle, DOWN)
        b_label = MathTex("b").next_to(triangle, RIGHT)
        c_label = MathTex("c").move_to(triangle.get_center() + LEFT*0.5 + UP*0.3)
        
        with self.voiceover(text="We label the sides a, b, and c."):
            self.play(Write(a_label), Write(b_label), Write(c_label))
        
        # Formula
        formula = MathTex(r"a^2 + b^2 = c^2", font_size=72, color=YELLOW)
        formula.shift(DOWN * 2)
        
        with self.voiceover(
            text="The theorem states that a squared plus b squared equals c squared."
        ) as tracker:
            self.play(Write(formula), run_time=tracker.duration)
        
        self.wait(1)
        
        # Outro
        with self.voiceover(text="Thanks for watching!"):
            self.play(FadeOut(triangle), FadeOut(a_label), FadeOut(b_label), 
                      FadeOut(c_label), FadeOut(title))
            self.play(formula.animate.move_to(ORIGIN).scale(1.2))
        
        self.wait(2)
```

## Troubleshooting

### "SoX not found"
Install SoX: `brew install sox` (macOS) or `apt install sox` (Linux)

### ElevenLabs API errors
- Verify `ELEVEN_API_KEY` environment variable is set
- Check you have API credits remaining at elevenlabs.io
- Ensure voice name is spelled correctly

### Audio not syncing
- Use `run_time=tracker.duration` for precise sync
- Break long narrations into shorter segments

### JSONDecodeError in cache
Delete the `media/voiceover` cache folder and re-render

## Caching Behavior

manim-voiceover-plus caches generated audio using SHA-256 hashing:
- Same text + same voice settings = reuses cached audio
- Change the text = regenerates audio
- Cache stored in `media/voiceover/` by default

This saves API calls and time on re-renders.

## Quality Checklist

Before finalizing:
- [ ] Audio is clear and well-paced
- [ ] Animations sync with narration
- [ ] Text is readable (appropriate font size)
- [ ] Colors have good contrast
- [ ] No overlapping elements
- [ ] Smooth transitions between sections
- [ ] Proper wait times at end of sections

## Autonomous Video Verification

Use this workflow to self-verify rendered videos without human review.

### Step 1: Extract Key Frames

After rendering, extract frames at key timestamps using ffmpeg:

```bash
# Extract 8 evenly-spaced frames from video
./verify_video.sh media/videos/scene_name/720p30/SceneName.mp4 8
```

Or manually:
```bash
mkdir -p media/verification_frames
ffmpeg -ss 30 -i video.mp4 -vframes 1 frame_30s.png  # Extract frame at 30s
```

### Step 2: Define Expected Visuals

Before verification, document what each section should show:

```
Section 1 (0-15s): Title "Topic Name" centered, subtitle below
Section 2 (15-40s): Diagram with labeled elements A, B, C connected by arrows
Section 3 (40-70s): Two side-by-side boxes comparing X vs Y
Section 4 (70-100s): Conclusion text, call to action
```

### Step 3: Verify with Subagent

Use the Task tool to dispatch a verification subagent:

```
Task: Verify video frames against expected layout

Expected visuals:
- Frame at 0s: Black screen or title appearing
- Frame at 15s: "SECTION TITLE" in orange at top, human/AI icons with arrow
- Frame at 30s: Text "Key Concept" visible and fully readable (not cut off)
- Frame at 60s: Circle containing two text lines, both fully visible
- Frame at 90s: Two comparison boxes side by side, "Both are X" text at bottom

Instructions:
1. Use look_at tool on each frame in media/verification_frames/
2. Compare actual content against expected visuals above
3. Report ONLY issues found (text cut off, elements missing, overlap, etc.)
4. If no issues, report "All frames verified successfully"

Frame paths:
- media/verification_frames/frame_00_at_0s.png
- media/verification_frames/frame_01_at_15s.png
- ... etc
```

### Step 4: Fix and Re-verify

Common issues and fixes:
| Issue | Fix |
|-------|-----|
| Text cut off | Reduce `font_size` or adjust position with `.move_to()` |
| Elements overlap | Increase `buff` spacing or use `.shift()` |
| Text not readable | Increase `font_size`, improve color contrast |
| Missing elements | Check animation timing, ensure `run_time` is sufficient |

After fixing, delete old frames and re-extract:
```bash
rm -rf media/verification_frames
./verify_video.sh media/videos/.../SceneName.mp4 8
```

### Verification Script

The `verify_video.sh` script extracts evenly-spaced frames:

```bash
#!/bin/bash
# Usage: ./verify_video.sh <video_path> [num_frames]
VIDEO_PATH="$1"
NUM_FRAMES="${2:-5}"
OUTPUT_DIR="media/verification_frames"

mkdir -p "$OUTPUT_DIR"
DURATION=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$VIDEO_PATH")

for i in $(seq 0 $((NUM_FRAMES - 1))); do
    TIMESTAMP=$(echo "scale=2; $DURATION * $i / ($NUM_FRAMES - 1)" | bc)
    ffmpeg -y -ss "$TIMESTAMP" -i "$VIDEO_PATH" -vframes 1 -q:v 2 "$OUTPUT_DIR/frame_$(printf '%02d' $i)_at_${TIMESTAMP}s.png" 2>/dev/null
done
```

---

**To create a video:** Give this agent a video description and your ELEVEN_API_KEY. The agent will write the Manim code, save it to a `.py` file, and provide the render command.
