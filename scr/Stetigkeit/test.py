from manim import *

class BlinkingText(Scene):
    def construct(self):
        text = Tex(r"\textbf{Blinking Text}").scale(1.5)
        self.play(Write(text))
        
        for _ in range(3):  # Adjust the number of blinks
            self.play(FadeOut(text, run_time=0.5))
            self.play(FadeIn(text, run_time=0.5))
        
        self.wait()
