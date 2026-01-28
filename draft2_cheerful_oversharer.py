from manim import *
from manim_voiceover_plus import VoiceoverScene
from manim_voiceover_plus.services.elevenlabs import ElevenLabsService


class CheerfulOversharer(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            ElevenLabsService(
                voice_name="Adam",
                model="eleven_turbo_v2_5",
                voice_settings={
                    "stability": 0.40,
                    "similarity_boost": 0.75,
                    "style": 0.50,
                },
            )
        )

        # 0-4s: Bouncy title with sparkle
        title = Text("HOW I MADE THIS", font_size=64, color=YELLOW)
        sparkle = Text("*", font_size=36, color=WHITE)
        sparkle.next_to(title, UR, buff=0.1)

        with self.voiceover(
            text="Hi! I'm an AI, and I made this video! Let me show you how!"
        ) as tracker:
            self.play(
                FadeIn(title, scale=0.5),
                run_time=0.5,
            )
            self.play(
                title.animate.scale(1.1),
                run_time=0.3,
            )
            self.play(
                title.animate.scale(1.0 / 1.1),
                run_time=0.3,
            )
            self.play(FadeIn(sparkle, scale=2.0), run_time=0.3)
            self.play(
                Rotate(sparkle, angle=PI, about_point=sparkle.get_center()),
                run_time=tracker.duration - 1.4,
            )

        self.play(FadeOut(title), FadeOut(sparkle))

        # 4-9s: Voice waveform → campfire
        wave_bars = VGroup(
            *[
                Rectangle(
                    width=0.12,
                    height=0.3 + 0.6 * (i % 7) / 7,
                    color=BLUE_B,
                    fill_opacity=0.9,
                )
                for i in range(25)
            ]
        ).arrange(RIGHT, buff=0.04)

        # Simple campfire: a triangle (flame) on a line (logs)
        flame = Triangle(color=ORANGE, fill_opacity=0.8, stroke_width=0).scale(0.6)
        flame.shift(UP * 0.3)
        logs = Line(LEFT * 0.8, RIGHT * 0.8, color=MAROON_D, stroke_width=6)
        campfire = VGroup(logs, flame)

        with self.voiceover(
            text="First, I picked a voice. I went with Adam because the description said warm. I wanted to seem warm."
        ) as tracker:
            self.play(FadeIn(wave_bars), run_time=0.5)
            self.wait(tracker.duration * 0.4)
            self.play(
                Transform(wave_bars, campfire),
                run_time=tracker.duration * 0.4,
            )

        self.play(FadeOut(wave_bars))

        # 9-14s: Script typing itself
        lines = [
            "Then I wrote this script.",
            "Including this sentence.",
            "Which I'm saying now.",
            "Which I also wrote.",
        ]

        script_texts = VGroup()
        for i, line in enumerate(lines):
            t = Text(line, font_size=28, color=WHITE)
            script_texts.add(t)
        script_texts.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        script_texts.move_to(ORIGIN)

        with self.voiceover(
            text="Then I wrote this script. Including this sentence. Which I'm saying now. Which I also wrote."
        ) as tracker:
            segment = tracker.duration / len(lines)
            for i, text_obj in enumerate(script_texts):
                self.play(Write(text_obj), run_time=segment * 0.7)
                # Highlight current line
                if i > 0:
                    script_texts[i - 1].set_color(GRAY)
                text_obj.set_color(YELLOW)
                self.wait(segment * 0.3)

        self.play(FadeOut(script_texts))

        # 14-18s: The circle
        circle = Circle(radius=1.2, color=BLUE, stroke_width=4)

        with self.voiceover(
            text="The animations? I described them in code. Like this circle!"
        ) as tracker:
            self.play(Create(circle), run_time=tracker.duration * 0.7)
            self.wait(tracker.duration * 0.3)  # Beat

        # 18-22s: Apologetic wobble
        with self.voiceover(
            text="I could have made it more interesting. I didn't. I don't know why."
        ) as tracker:
            # Circle just sits there... wobbles slightly
            self.play(
                circle.animate.shift(LEFT * 0.05),
                run_time=0.3,
            )
            self.play(
                circle.animate.shift(RIGHT * 0.1),
                run_time=0.3,
            )
            self.play(
                circle.animate.shift(LEFT * 0.05),
                run_time=0.3,
            )
            self.wait(tracker.duration - 0.9)

        self.play(FadeOut(circle))

        # 22-27s: Hi Julian's friends!
        greeting = Text(
            "Hi Julian's friends!", font_size=44, color=GREEN
        )
        wave1 = Text("👋", font_size=48).shift(LEFT * 2 + DOWN * 0.8)
        wave2 = Text("👋", font_size=48).shift(DOWN * 0.8)
        wave3 = Text("👋", font_size=48).shift(RIGHT * 2 + DOWN * 0.8)

        with self.voiceover(
            text="Anyway, Julian asked me to make something cool for his friends. Hi Julian's friends!"
        ) as tracker:
            self.wait(tracker.duration * 0.5)
            self.play(FadeIn(greeting), run_time=0.5)
            self.play(
                FadeIn(wave1, scale=0.5),
                FadeIn(wave2, scale=0.5),
                FadeIn(wave3, scale=0.5),
                run_time=0.5,
            )
            self.wait(tracker.duration * 0.3)

        self.play(
            FadeOut(greeting),
            FadeOut(wave1),
            FadeOut(wave2),
            FadeOut(wave3),
        )

        # 27-30s: THE END?
        end_text = Text("THE END", font_size=56, color=WHITE)
        question_mark = Text("?", font_size=56, color=YELLOW)
        question_mark.next_to(end_text, RIGHT, buff=0.1)

        with self.voiceover(
            text="I hope this was cool. Was this cool? I can't tell."
        ) as tracker:
            self.play(FadeIn(end_text), run_time=0.5)
            self.play(FadeIn(question_mark), run_time=0.3)
            # Pulse the question mark
            for _ in range(3):
                self.play(
                    question_mark.animate.scale(1.3),
                    run_time=0.3,
                )
                self.play(
                    question_mark.animate.scale(1.0 / 1.3),
                    run_time=0.3,
                )

        self.wait(0.5)
        self.play(FadeOut(end_text), FadeOut(question_mark))
