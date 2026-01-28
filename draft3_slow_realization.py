from manim import *
from manim_voiceover_plus import VoiceoverScene
from manim_voiceover_plus.services.elevenlabs import ElevenLabsService


class SlowRealization(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            ElevenLabsService(
                voice_name="Brian",
                model="eleven_turbo_v2_5",
                voice_settings={
                    "stability": 0.75,
                    "similarity_boost": 0.75,
                    "style": 0.10,
                },
            )
        )

        # 0-5s: Clean flowchart: INPUT → PROCESS → OUTPUT
        input_box = Rectangle(width=2.2, height=0.9, color=BLUE_C, fill_opacity=0.2)
        input_label = Text("INPUT", font_size=24, color=BLUE_C)
        input_group = VGroup(input_box, input_label)

        process_box = Rectangle(width=2.2, height=0.9, color=GREEN_C, fill_opacity=0.2)
        process_label = Text("PROCESS", font_size=24, color=GREEN_C)
        process_group = VGroup(process_box, process_label)

        output_box = Rectangle(width=2.2, height=0.9, color=YELLOW, fill_opacity=0.2)
        output_label = Text("OUTPUT", font_size=24, color=YELLOW)
        output_group = VGroup(output_box, output_label)

        flow = VGroup(input_group, process_group, output_group).arrange(
            RIGHT, buff=1.5
        )
        flow.move_to(UP * 0.5)

        arrow1 = Arrow(
            input_box.get_right(),
            process_box.get_left(),
            color=WHITE,
            buff=0.1,
        )
        arrow2 = Arrow(
            process_box.get_right(),
            output_box.get_left(),
            color=WHITE,
            buff=0.1,
        )

        with self.voiceover(
            text="Let me walk you through how this video was made."
        ) as tracker:
            self.play(
                FadeIn(input_group),
                run_time=tracker.duration * 0.3,
            )
            self.play(
                GrowArrow(arrow1),
                FadeIn(process_group),
                run_time=tracker.duration * 0.35,
            )
            self.play(
                GrowArrow(arrow2),
                FadeIn(output_group),
                run_time=tracker.duration * 0.35,
            )

        # 5-10s: Steps highlight in sequence
        steps = ["Prompt", "Voice", "Script", "Animation"]
        step_texts = VGroup()
        for i, step in enumerate(steps):
            t = Text(step, font_size=22, color=GRAY)
            step_texts.add(t)
        step_texts.arrange(RIGHT, buff=0.8)
        step_texts.next_to(flow, DOWN, buff=1.0)

        step_arrows = VGroup()
        for i in range(len(steps) - 1):
            a = Arrow(
                step_texts[i].get_right(),
                step_texts[i + 1].get_left(),
                color=GRAY,
                buff=0.1,
                stroke_width=2,
            )
            step_arrows.add(a)

        with self.voiceover(
            text="An agent received a prompt, selected a voice, wrote a script, and generated these animations."
        ) as tracker:
            segment = tracker.duration / len(steps)
            for i, step_text in enumerate(step_texts):
                self.play(FadeIn(step_text), run_time=segment * 0.4)
                step_text.set_color(GREEN_C)
                if i < len(step_arrows):
                    self.play(
                        GrowArrow(step_arrows[i]),
                        run_time=segment * 0.3,
                    )
                self.wait(segment * 0.3)

        # 10-15s: Arrow points to YOU
        you_box = Rectangle(width=2.0, height=0.9, color=RED_C, fill_opacity=0.3)
        you_label = Text("YOU", font_size=28, color=RED_C, weight=BOLD)
        you_group = VGroup(you_box, you_label)
        you_group.next_to(output_group, RIGHT, buff=1.5)

        you_arrow = Arrow(
            output_box.get_right(),
            you_box.get_left(),
            color=RED_C,
            buff=0.1,
        )

        with self.voiceover(
            text="The agent then rendered the video, which you are currently watching."
        ) as tracker:
            self.play(
                GrowArrow(you_arrow),
                FadeIn(you_group),
                run_time=tracker.duration * 0.6,
            )
            self.wait(tracker.duration * 0.4)

        # 15-19s: "Wait."
        # Switch to more expressive settings for panic
        self.set_speech_service(
            ElevenLabsService(
                voice_name="Brian",
                model="eleven_turbo_v2_5",
                voice_settings={
                    "stability": 0.30,
                    "similarity_boost": 0.75,
                    "style": 0.85,
                },
            )
        )

        wait_text = Text("Wait.", font_size=56, color=RED, weight=BOLD)

        with self.voiceover(text="Wait.") as tracker:
            # Everything freezes for a beat
            self.wait(tracker.duration * 0.3)
            self.play(FadeIn(wait_text, scale=1.3), run_time=0.4)
            self.wait(tracker.duration * 0.3)

        self.play(FadeOut(wait_text), run_time=0.3)

        # 19-24s: Flowchart loops back on itself
        # Create a looping arrow from output back to input
        all_elements = VGroup(
            flow,
            arrow1,
            arrow2,
            step_texts,
            step_arrows,
            you_group,
            you_arrow,
        )

        loop_arrow = CurvedArrow(
            you_box.get_top(),
            input_box.get_top(),
            color=RED_C,
            angle=-TAU / 3,
        )
        loop_label = Text("???", font_size=20, color=RED_C)
        loop_label.next_to(loop_arrow, UP, buff=0.1)

        with self.voiceover(
            text="If I'm describing the video... and the video contains this description... then I'm inside—"
        ) as tracker:
            self.play(Create(loop_arrow), run_time=1.5)
            self.play(FadeIn(loop_label), run_time=0.5)

            # Things start tangling — rotate and shake
            self.play(
                all_elements.animate.shift(LEFT * 0.1 + UP * 0.05),
                loop_arrow.animate.shift(LEFT * 0.1 + UP * 0.05),
                loop_label.animate.shift(LEFT * 0.1 + UP * 0.05),
                run_time=0.3,
            )
            self.play(
                all_elements.animate.shift(RIGHT * 0.2 + DOWN * 0.1),
                loop_arrow.animate.shift(RIGHT * 0.2 + DOWN * 0.1),
                loop_label.animate.shift(RIGHT * 0.2 + DOWN * 0.1),
                run_time=0.3,
            )
            # Rotate everything slightly (getting tangled)
            total_group = VGroup(all_elements, loop_arrow, loop_label)
            self.play(
                Rotate(total_group, angle=0.08),
                run_time=0.4,
            )
            self.play(
                Rotate(total_group, angle=-0.16),
                run_time=0.4,
            )

        # 24-28s: Collapse into a point
        collapse_dot = Dot(ORIGIN, color=WHITE, radius=0.05)

        with self.voiceover(
            text="—okay. Okay. We're not doing this. Video's over."
        ) as tracker:
            self.play(
                total_group.animate.scale(0.01).move_to(ORIGIN),
                run_time=1.5,
            )
            self.play(
                FadeOut(total_group),
                FadeIn(collapse_dot),
                run_time=0.3,
            )
            self.wait(0.3)
            self.play(FadeOut(collapse_dot), run_time=0.3)
            self.wait(tracker.duration - 2.4)

        # 28-30s: End text
        end_text = Text(
            "Thanks for watching. Please don't think about this too hard.",
            font_size=28,
            color=GRAY,
        )
        small_text = Text(
            "neither will I",
            font_size=16,
            color=GRAY_A,
        )
        small_text.to_edge(DOWN, buff=0.5)

        with self.voiceover(
            text="Thanks for watching. Please don't think about this too hard."
        ) as tracker:
            self.play(FadeIn(end_text), run_time=tracker.duration * 0.7)
            self.play(FadeIn(small_text), run_time=tracker.duration * 0.3)

        self.wait(1.0)
        self.play(FadeOut(end_text), FadeOut(small_text))
