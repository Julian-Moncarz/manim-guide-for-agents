from manim import *
from manim_voiceover_plus import VoiceoverScene
from manim_voiceover_plus.services.elevenlabs import ElevenLabsService
import numpy as np

class CircleAreaExplainer(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            ElevenLabsService(
                voice_id="JBFqnCBsd6RMkjVDRZzb",  # George
                model="eleven_turbo_v2_5",
                transcription_model=None,
            )
        )
        
        # Title
        title = Text("Area of a Circle", font_size=56, color=BLUE)
        with self.voiceover(text="Area of a Circle.") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        self.play(title.animate.to_edge(UP).scale(0.6))
        
        # Create circle with pizza slices
        num_slices = 12
        radius = 2
        circle_center = ORIGIN
        
        slices = VGroup()
        colors = [RED, BLUE] * (num_slices // 2)
        
        for i in range(num_slices):
            angle_start = i * TAU / num_slices
            slice = Sector(
                radius=radius,
                start_angle=angle_start,
                angle=TAU / num_slices,
                color=colors[i],
                fill_opacity=0.7,
                stroke_width=2,
                stroke_color=WHITE
            )
            slices.add(slice)
        
        with self.voiceover(text="Slice a circle into wedges.") as tracker:
            self.play(Create(slices), run_time=tracker.duration)
        
        self.wait(0.5)
        
        # Rearrange slices into wavy rectangle pattern
        with self.voiceover(text="Rearrange them...") as tracker:
            arranged_slices = VGroup()
            slice_width = (PI * radius) / (num_slices / 2)
            
            animations = []
            for i, slice in enumerate(slices):
                new_slice = slice.copy()
                if i % 2 == 0:
                    # Point up
                    new_slice.rotate(-PI/2 - (i * TAU / num_slices))
                    x_pos = -PI * radius / 2 + (i // 2) * slice_width + slice_width / 2
                    new_slice.move_to([x_pos, 0, 0])
                else:
                    # Point down
                    new_slice.rotate(PI/2 - (i * TAU / num_slices))
                    x_pos = -PI * radius / 2 + (i // 2) * slice_width + slice_width / 2
                    new_slice.move_to([x_pos, 0, 0])
                
                animations.append(Transform(slice, new_slice))
            
            self.play(*animations, run_time=tracker.duration)
        
        self.wait(0.5)
        
        # Transition to more slices (showing it approaches rectangle)
        with self.voiceover(text="More slices, and it becomes a rectangle.") as tracker:
            # Fade out old slices
            self.play(FadeOut(slices), run_time=0.5)
            
            # Create rectangle representation
            rect_width = PI * radius
            rect_height = radius
            rectangle = Rectangle(
                width=rect_width,
                height=rect_height,
                color=PURPLE,
                fill_opacity=0.7,
                stroke_width=2
            )
            self.play(FadeIn(rectangle), run_time=tracker.duration - 0.5)
        
        self.wait(0.5)
        
        # Label the rectangle
        with self.voiceover(text="Height is r. Width is half the circumference: pi r.") as tracker:
            # Height label
            height_brace = Brace(rectangle, LEFT)
            height_label = Text("r", font_size=36).next_to(height_brace, LEFT)
            
            # Width label  
            width_brace = Brace(rectangle, DOWN)
            width_label = Text("πr", font_size=36).next_to(width_brace, DOWN)
            
            self.play(
                Create(height_brace), Write(height_label),
                Create(width_brace), Write(width_label),
                run_time=tracker.duration
            )
        
        self.wait(0.5)
        
        # Show formula
        formula = Text("A = πr²", font_size=72, color=YELLOW)
        formula.to_edge(DOWN, buff=1)
        
        with self.voiceover(text="Area: pi r squared.") as tracker:
            self.play(Write(formula), run_time=tracker.duration)
        
        self.wait(2)
        
        # Cleanup
        self.play(
            FadeOut(rectangle), FadeOut(height_brace), FadeOut(height_label),
            FadeOut(width_brace), FadeOut(width_label), FadeOut(title)
        )
        self.play(formula.animate.move_to(ORIGIN).scale(1.3))
        self.wait(2)
