from manim import *

class NameWithRectangle(Scene):
    def construct(self):
        num = MathTex("ln(2)")
        box = SurroundingRectangle(num,color=BLUE, fill_opacity=0.5, fill_color=RED, buff=2)
        name = Tex("Ziyi Liu").next_to(box, DOWN, buff=1)

        self.play(Create(VGroup(num,box,name)), run_time = 3)
        self.wait()

