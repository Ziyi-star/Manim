from manim import *

class LabelSinus(Scene):
    def construct(self):
        text = Text("Sinusfunktion", font="Arial", font_size=36, color=YELLOW)

        self.play(Write(text))
        self.wait(2)