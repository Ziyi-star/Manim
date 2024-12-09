from manim import *

class NameWithRectangle_updaters(Scene):
    def construct(self):
        num = MathTex("ln(2)")
        #box und name zusammenbewegen
        box = always_redraw(lambda: 
        SurroundingRectangle(num,color=BLUE, fill_opacity=0.5, fill_color=RED, buff=2)
        )

        name = always_redraw(lambda:Tex("Ziyi Liu").next_to(box, DOWN, buff=1))

        self.play(Create(VGroup(num,box,name)))
        self.play(num.animate.shift(RIGHT*2), run_time = 2)
        self.wait()

