from manim import *

class Hello(Scene):
    def construct(self):
        text = Text("Hello World")
        self.play(Write(text))
        self.wait(3)
