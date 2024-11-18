from manim import *

class hello(Scene):
    def construct(self):
        text = Text("Hello World")
        self.play(Write(text))
        self.wait(3)
