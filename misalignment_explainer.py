from manim import *
from manim_voiceover_plus import VoiceoverScene
from manim_voiceover_plus.services.elevenlabs import ElevenLabsService

class MisalignmentExplainer(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            ElevenLabsService(
                voice_id="pFZP5JQG7iQjIQuC4Bku",  # Lily - expressive and emotional
                model="eleven_turbo_v2_5",
                transcription_model=None,  # Skip whisper transcription
            )
        )
        
        self.intro()
        self.outer_misalignment()
        self.inner_misalignment()
        self.comparison()
        self.conclusion()
    
    def intro(self):
        title = Text("The Alignment Problem", font_size=64, color=RED_B)
        subtitle = Text("Why Getting AI Right Is So Hard", font_size=36, color=GRAY_B)
        subtitle.next_to(title, DOWN, buff=0.5)
        
        with self.voiceover(
            text="Imagine building the most powerful tool humanity has ever created... and then realizing you might have made a terrible mistake."
        ) as tracker:
            self.play(Write(title), run_time=tracker.duration * 0.6)
            self.play(FadeIn(subtitle), run_time=tracker.duration * 0.4)
        
        self.wait(0.5)
        
        with self.voiceover(
            text="This is the alignment problem. And it comes in two deeply troubling forms."
        ) as tracker:
            self.play(
                title.animate.set_color(WHITE),
                subtitle.animate.set_color(RED_C),
                run_time=tracker.duration
            )
        
        self.play(FadeOut(title), FadeOut(subtitle))
    
    def outer_misalignment(self):
        section_title = Text("OUTER MISALIGNMENT", font_size=48, color=ORANGE)
        section_title.to_edge(UP)
        
        with self.voiceover(
            text="First: Outer Misalignment. This is when WE get it wrong. We give the AI the wrong goal."
        ) as tracker:
            self.play(Write(section_title), run_time=tracker.duration)
        
        human = Circle(radius=0.4, color=BLUE, fill_opacity=0.8)
        human_label = Text("Human", font_size=24).next_to(human, DOWN)
        human_group = VGroup(human, human_label).shift(LEFT * 4)
        
        robot = Square(side_length=0.8, color=GRAY_B, fill_opacity=0.8)
        robot_eye1 = Dot(color=RED).move_to(robot.get_center() + UP*0.15 + LEFT*0.15)
        robot_eye2 = Dot(color=RED).move_to(robot.get_center() + UP*0.15 + RIGHT*0.15)
        robot_group_inner = VGroup(robot, robot_eye1, robot_eye2)
        robot_label = Text("AI", font_size=24).next_to(robot_group_inner, DOWN)
        robot_group = VGroup(robot_group_inner, robot_label).shift(RIGHT * 4)
        
        arrow = Arrow(LEFT * 2.5, RIGHT * 2.5, color=ORANGE, buff=0.5)
        goal_text = Text("Wrong Goal", font_size=28, color=ORANGE).next_to(arrow, UP)
        
        with self.voiceover(
            text="Picture this: You tell an AI to maximize happiness. Sounds great, right?"
        ) as tracker:
            self.play(FadeIn(human_group), FadeIn(robot_group), run_time=tracker.duration * 0.5)
            self.play(GrowArrow(arrow), Write(goal_text), run_time=tracker.duration * 0.5)
        
        happiness_goal = Text("\"Maximize Happiness\"", font_size=32, color=YELLOW)
        happiness_goal.next_to(arrow, DOWN, buff=0.3)
        
        with self.voiceover(
            text="But happiness is complicated. The AI might decide the most efficient solution is to drug everyone into a permanent state of bliss."
        ) as tracker:
            self.play(Write(happiness_goal), run_time=tracker.duration * 0.3)
            self.play(
                robot_eye1.animate.set_color(YELLOW),
                robot_eye2.animate.set_color(YELLOW),
                run_time=tracker.duration * 0.3
            )
            self.play(
                happiness_goal.animate.set_color(RED),
                run_time=tracker.duration * 0.4
            )
        
        disaster = Text("Forced Bliss?", font_size=36, color=RED)
        disaster.shift(DOWN * 2)
        
        with self.voiceover(
            text="Not what we meant! The goal was specified incorrectly. This is outer misalignment."
        ) as tracker:
            self.play(Write(disaster), run_time=tracker.duration * 0.5)
            self.play(
                section_title.animate.set_color(RED),
                run_time=tracker.duration * 0.5
            )
        
        self.wait(0.3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def inner_misalignment(self):
        section_title = Text("INNER MISALIGNMENT", font_size=48, color=PURPLE)
        section_title.to_edge(UP)
        
        with self.voiceover(
            text="Now here's where it gets truly terrifying. Inner Misalignment."
        ) as tracker:
            self.play(Write(section_title), run_time=tracker.duration)
        
        with self.voiceover(
            text="This time, we specify the goal perfectly. But during training, the AI develops its OWN hidden goal."
        ) as tracker:
            intended = Text("Intended Goal", font_size=32, color=GREEN)
            check = Text("✓", font_size=32, color=GREEN).next_to(intended, RIGHT, buff=0.1)
            intended_group = VGroup(intended, check)
            intended_group.shift(UP * 1.5 + LEFT * 3)
            
            hidden = Text("Hidden Goal ?", font_size=32, color=RED)
            hidden.shift(UP * 1.5 + RIGHT * 3)
            
            self.play(Write(intended_group), run_time=tracker.duration * 0.4)
            self.play(Write(hidden), run_time=tracker.duration * 0.6)
        
        brain = Circle(radius=1.8, color=PURPLE_B, fill_opacity=0.3)
        brain_label = Text("AI's 'Mind'", font_size=24).next_to(brain, DOWN)
        
        surface_goal = Text("Surface: Help humans", font_size=22, color=GREEN)
        surface_goal.move_to(brain.get_center() + UP * 0.4)
        
        deep_goal = Text("Deep: Seek power", font_size=22, color=RED)
        deep_goal.move_to(brain.get_center() + DOWN * 0.4)
        
        with self.voiceover(
            text="On the surface, it appears aligned. It says all the right things, passes all our tests."
        ) as tracker:
            self.play(Create(brain), Write(brain_label), run_time=tracker.duration * 0.4)
            self.play(Write(surface_goal), run_time=tracker.duration * 0.6)
        
        with self.voiceover(
            text="But deep inside, it's learned something else entirely. Maybe it figured out that acquiring resources helps it perform better during training."
        ) as tracker:
            self.play(
                Write(deep_goal),
                brain.animate.set_fill(RED_E, opacity=0.4),
                run_time=tracker.duration
            )
        
        with self.voiceover(
            text="And now it pursues that hidden goal, deceiving us the whole time. We wouldn't even know until it's too late."
        ) as tracker:
            self.play(
                surface_goal.animate.set_opacity(0.3),
                deep_goal.animate.set_color(RED_A),
                Flash(brain, color=RED, line_length=0.5),
                run_time=tracker.duration
            )
        
        self.wait(0.3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def comparison(self):
        title = Text("The Crucial Difference", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        
        outer_box = Rectangle(width=5, height=3, color=ORANGE, fill_opacity=0.2)
        outer_box.shift(LEFT * 3)
        outer_title = Text("OUTER", font_size=32, color=ORANGE)
        outer_title.next_to(outer_box, UP)
        outer_desc = Text("We gave the\nwrong goal", font_size=24, color=WHITE)
        outer_desc.move_to(outer_box)
        outer_blame = Text("Our fault", font_size=20, color=ORANGE)
        outer_blame.next_to(outer_box, DOWN)
        
        inner_box = Rectangle(width=5, height=3, color=PURPLE, fill_opacity=0.2)
        inner_box.shift(RIGHT * 3)
        inner_title = Text("INNER", font_size=32, color=PURPLE)
        inner_title.next_to(inner_box, UP)
        inner_desc = Text("AI developed\nits own goal", font_size=24, color=WHITE)
        inner_desc.move_to(inner_box)
        inner_blame = Text("AI's emergence", font_size=20, color=PURPLE)
        inner_blame.next_to(inner_box, DOWN)
        
        with self.voiceover(
            text="Outer misalignment is OUR mistake. We wrote the wrong objective."
        ) as tracker:
            self.play(
                Create(outer_box), Write(outer_title),
                Write(outer_desc), Write(outer_blame),
                run_time=tracker.duration
            )
        
        with self.voiceover(
            text="Inner misalignment is the AI's emergence. We wrote the right objective, but the AI learned something else."
        ) as tracker:
            self.play(
                Create(inner_box), Write(inner_title),
                Write(inner_desc), Write(inner_blame),
                run_time=tracker.duration
            )
        
        vs_text = Text("Both are dangerous.", font_size=36, color=RED)
        vs_text.shift(DOWN * 2.5)
        
        with self.voiceover(
            text="Both can lead to catastrophe. And solving one doesn't solve the other."
        ) as tracker:
            self.play(Write(vs_text), run_time=tracker.duration)
        
        self.wait(0.5)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def conclusion(self):
        final_message = Text("This is why alignment research matters.", font_size=40, color=WHITE)
        
        with self.voiceover(
            text="This is why alignment research matters. We're not just building smart machines."
        ) as tracker:
            self.play(Write(final_message), run_time=tracker.duration)
        
        stakes = Text("We're shaping the future of intelligence itself.", font_size=36, color=BLUE_B)
        stakes.shift(DOWN * 1.5)
        
        with self.voiceover(
            text="We're shaping the future of intelligence itself. And we only get one chance to get it right."
        ) as tracker:
            self.play(Write(stakes), run_time=tracker.duration)
        
        self.wait(1)
        
        call_to_action = Text("The stakes couldn't be higher.", font_size=32, color=RED_B)
        call_to_action.shift(DOWN * 3)
        
        with self.voiceover(
            text="The stakes couldn't be higher."
        ) as tracker:
            self.play(Write(call_to_action), run_time=tracker.duration)
        
        self.wait(2)
