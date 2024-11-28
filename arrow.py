from manim import *

class Arrow(Scene):
    def construct(self):
        rect = Rectangle(color=WHITE, fill_opacity=0.5, height=2, width=2.5)
        circ = Circle().to_edge(DOWN)
        #add tip
        arrow = Line(start=rect.get_bottom(),end=circ.get_top()).add_tip()

        self.play(Create(VGroup(rect,circ,arrow)))
        self.wait()

