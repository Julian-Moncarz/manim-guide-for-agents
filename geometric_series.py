from manim import *
from manim_voiceover_plus import VoiceoverScene
from manim_voiceover_plus.services.elevenlabs import ElevenLabsService

class GeometricSeriesExplained(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            ElevenLabsService(
                voice_id="JBFqnCBsd6RMkjVDRZzb",  # George
                model="eleven_turbo_v2_5",
                transcription_model=None,
            )
        )
        
        # Set background to black
        self.camera.background_color = BLACK
        
        # ===== BEAT 1: The Setup (0s–3s) =====
        # Top equation - build using simple Text with fractions as Unicode
        eq_text = "½ + ¼ + ⅛ + 1/16 + ..."
        equation = Text(eq_text, font_size=44, color=WHITE)
        equation.to_edge(UP, buff=0.5)
        
        with self.voiceover(text="What happens if you add one half, plus one quarter, plus one eighth, and keep going forever?") as tracker:
            self.play(Write(equation), run_time=tracker.duration)
        
        # ===== BEAT 2: The Square Appears (3s–7s) =====
        square = Rectangle(width=4, height=4, color=WHITE, stroke_width=3, fill_opacity=0)
        square.move_to(ORIGIN)
        
        label_equals_1 = Text("= 1", font_size=40, color=WHITE).next_to(square, RIGHT, buff=0.5)
        
        with self.voiceover(text="Start with a square. This represents one whole.") as tracker:
            self.play(Create(square), run_time=1.5)
            self.play(FadeIn(label_equals_1), run_time=0.5)
            remaining = tracker.duration - 2.0
            if remaining > 0:
                self.wait(remaining)
        
        # ===== BEAT 3: First Half (1/2) (7s–11s) =====
        # Vertical line dividing left and right
        mid_line = Line(start=[0, -2, 0], end=[0, 2, 0], color=WHITE, stroke_width=2)
        
        left_half = Rectangle(width=2, height=4, color=BLUE, stroke_width=0, fill_opacity=0.7)
        left_half.move_to([-1, 0, 0])
        
        label_1_2 = Text("1/2", font_size=36, color=WHITE).move_to([-1, 0, 0])
        
        with self.voiceover(text="Take half.") as tracker:
            self.play(Create(mid_line), run_time=0.5)
            self.play(FadeIn(left_half), run_time=1.0)
            self.play(Write(label_1_2), run_time=0.5)
            remaining = tracker.duration - 2.0
            if remaining > 0:
                self.wait(remaining)
        
        # ===== BEAT 4: One Quarter (1/4) (11s–15s) =====
        # Horizontal line dividing right half (top and bottom)
        horiz_line_1 = Line(start=[0, 0, 0], end=[2, 0, 0], color=WHITE, stroke_width=2)
        
        top_right_quad = Rectangle(width=2, height=2, color=GREEN, stroke_width=0, fill_opacity=0.7)
        top_right_quad.move_to([1, 1, 0])
        
        label_1_4 = Text("1/4", font_size=30, color=WHITE).move_to([1, 1, 0])
        
        with self.voiceover(text="Then half of what's left.") as tracker:
            self.play(Create(horiz_line_1), run_time=0.5)
            self.play(FadeIn(top_right_quad), run_time=0.8)
            self.play(Write(label_1_4), run_time=0.5)
            remaining = tracker.duration - 1.8
            if remaining > 0:
                self.wait(remaining)
        
        # ===== BEAT 5: One Eighth (1/8) (15s–18s) =====
        # Vertical line dividing bottom-right quadrant
        vert_line_2 = Line(start=[1, -2, 0], end=[1, 0, 0], color=WHITE, stroke_width=2)
        
        left_of_bottom_right = Rectangle(width=1, height=2, color=YELLOW, stroke_width=0, fill_opacity=0.7)
        left_of_bottom_right.move_to([0.5, -1, 0])
        
        label_1_8 = Text("1/8", font_size=24, color=WHITE).move_to([0.5, -1, 0])
        
        with self.voiceover(text="And half again.") as tracker:
            self.play(Create(vert_line_2), run_time=0.4)
            self.play(FadeIn(left_of_bottom_right), run_time=0.6)
            self.play(Write(label_1_8), run_time=0.5)
            remaining = tracker.duration - 1.5
            if remaining > 0:
                self.wait(remaining)
        
        # ===== BEAT 6: Rapid Continuation (18s–21s) =====
        # 1/16 (ORANGE) - horizontal line dividing bottom-right remainder
        horiz_line_2 = Line(start=[1, -1, 0], end=[2, -1, 0], color=WHITE, stroke_width=2)
        top_of_remainder_1 = Rectangle(width=1, height=1, color=ORANGE, stroke_width=0, fill_opacity=0.7)
        top_of_remainder_1.move_to([1.5, -0.5, 0])
        label_1_16 = Text("1/16", font_size=18, color=WHITE).move_to([1.5, -0.5, 0])
        
        # 1/32 (RED) - vertical line
        vert_line_3 = Line(start=[1.5, -2, 0], end=[1.5, -1, 0], color=WHITE, stroke_width=2)
        left_of_remainder_2 = Rectangle(width=0.5, height=1, color=RED, stroke_width=0, fill_opacity=0.7)
        left_of_remainder_2.move_to([1.25, -1.5, 0])
        label_1_32 = Text("1/32", font_size=14, color=WHITE).move_to([1.25, -1.5, 0])
        
        # 1/64 (PURPLE) - horizontal line
        horiz_line_3 = Line(start=[1.5, -1.5, 0], end=[2, -1.5, 0], color=WHITE, stroke_width=2)
        top_of_remainder_3 = Rectangle(width=0.5, height=0.5, color=PURPLE, stroke_width=0, fill_opacity=0.7)
        top_of_remainder_3.move_to([1.75, -1.25, 0])
        
        # 1/128 (PINK) - vertical line
        vert_line_4 = Line(start=[1.75, -2, 0], end=[1.75, -1.5, 0], color=WHITE, stroke_width=2)
        left_of_remainder_4 = Rectangle(width=0.25, height=0.5, color=PINK, stroke_width=0, fill_opacity=0.7)
        left_of_remainder_4.move_to([1.625, -1.75, 0])
        
        # 1/256 (BLUE_A) - horizontal line
        horiz_line_4 = Line(start=[1.75, -1.75, 0], end=[2, -1.75, 0], color=WHITE, stroke_width=1)
        top_of_remainder_4 = Rectangle(width=0.25, height=0.25, color=BLUE_A, stroke_width=0, fill_opacity=0.7)
        top_of_remainder_4.move_to([1.875, -1.625, 0])
        
        # 1/512 (PURPLE_A) - vertical line
        vert_line_5 = Line(start=[1.875, -2, 0], end=[1.875, -1.75, 0], color=WHITE, stroke_width=1)
        left_of_remainder_5 = Rectangle(width=0.125, height=0.25, color=PURPLE_A, stroke_width=0, fill_opacity=0.7)
        left_of_remainder_5.move_to([1.8125, -1.875, 0])
        
        # 1/1024 (GREEN_A) - horizontal line
        horiz_line_5 = Line(start=[1.875, -1.875, 0], end=[2, -1.875, 0], color=WHITE, stroke_width=1)
        top_of_remainder_5 = Rectangle(width=0.125, height=0.125, color=GREEN_A, stroke_width=0, fill_opacity=0.7)
        top_of_remainder_5.move_to([1.9375, -1.8125, 0])
        
        # 1/2048 (RED_A) - vertical line
        vert_line_6 = Line(start=[1.9375, -2, 0], end=[1.9375, -1.875, 0], color=WHITE, stroke_width=0.5)
        left_of_remainder_6 = Rectangle(width=0.0625, height=0.125, color=RED_A, stroke_width=0, fill_opacity=0.7)
        left_of_remainder_6.move_to([1.90625, -1.9375, 0])
        
        with self.voiceover(text="And again... and again... and again...") as tracker:
            # 1/16
            self.play(Create(horiz_line_2), run_time=0.3)
            self.play(FadeIn(top_of_remainder_1), run_time=0.5)
            self.play(Write(label_1_16), run_time=0.2)
            
            # 1/32
            self.play(Create(vert_line_3), run_time=0.25)
            self.play(FadeIn(left_of_remainder_2), run_time=0.4)
            self.play(Write(label_1_32), run_time=0.2)
            
            # 1/64
            self.play(Create(horiz_line_3), run_time=0.2)
            self.play(FadeIn(top_of_remainder_3), run_time=0.3)
            
            # 1/128
            self.play(Create(vert_line_4), run_time=0.15)
            self.play(FadeIn(left_of_remainder_4), run_time=0.25)
            
            # 1/256
            self.play(Create(horiz_line_4), run_time=0.1)
            self.play(FadeIn(top_of_remainder_4), run_time=0.2)
            
            # 1/512
            self.play(Create(vert_line_5), run_time=0.1)
            self.play(FadeIn(left_of_remainder_5), run_time=0.2)
            
            # 1/1024
            self.play(Create(horiz_line_5), run_time=0.08)
            self.play(FadeIn(top_of_remainder_5), run_time=0.15)
            
            # 1/2048
            self.play(Create(vert_line_6), run_time=0.08)
            self.play(FadeIn(left_of_remainder_6), run_time=0.15)
            
            remaining = tracker.duration - 4.8
            if remaining > 0:
                self.wait(remaining)
        
        # ===== BEAT 7: The Revelation (21s–25s) =====
        with self.voiceover(text="You never overshoot. You're always inside the square. You just arrive at one.") as tracker:
            # Brief glow
            self.play(square.animate.set_stroke(width=4, color=WHITE), run_time=0.5)
            self.play(square.animate.set_stroke(width=3, color=WHITE), run_time=0.5)
            
            # Fade out labels inside square
            self.play(
                FadeOut(label_1_2),
                FadeOut(label_1_4),
                FadeOut(label_1_8),
                FadeOut(label_1_16),
                FadeOut(label_1_32),
                run_time=1.0
            )
            
            remaining = tracker.duration - 2.0
            if remaining > 0:
                self.wait(remaining)
        
        # ===== BEAT 8: The Payoff (25s–30s) =====
        # Add equals 1
        equals = Text("=", font_size=48, color=WHITE).next_to(equation, RIGHT, buff=0.3)
        result = Text("1", font_size=56, color=GOLD).next_to(equals, RIGHT, buff=0.3)
        
        with self.voiceover(text="The infinite sum equals exactly one.") as tracker:
            self.play(Write(equals), Write(result), run_time=1.0)
            
            # Pulse the result
            self.play(label_equals_1.animate.set_color(GOLD), run_time=0.5)
            self.play(label_equals_1.animate.set_color(WHITE), run_time=0.5)
            
            remaining = tracker.duration - 2.0
            if remaining > 0:
                self.wait(remaining)
        
        # ===== OUTRO: Fade to black =====
        self.play(
            FadeOut(equation),
            FadeOut(equals),
            FadeOut(result),
            FadeOut(square),
            FadeOut(mid_line),
            FadeOut(left_half),
            FadeOut(horiz_line_1),
            FadeOut(top_right_quad),
            FadeOut(vert_line_2),
            FadeOut(left_of_bottom_right),
            FadeOut(horiz_line_2),
            FadeOut(top_of_remainder_1),
            FadeOut(vert_line_3),
            FadeOut(left_of_remainder_2),
            FadeOut(horiz_line_3),
            FadeOut(top_of_remainder_3),
            FadeOut(vert_line_4),
            FadeOut(left_of_remainder_4),
            FadeOut(horiz_line_4),
            FadeOut(top_of_remainder_4),
            FadeOut(vert_line_5),
            FadeOut(left_of_remainder_5),
            FadeOut(horiz_line_5),
            FadeOut(top_of_remainder_5),
            FadeOut(vert_line_6),
            FadeOut(left_of_remainder_6),
            FadeOut(label_equals_1),
            run_time=1.0
        )
        self.wait(1)
