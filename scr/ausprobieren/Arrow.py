from manim import *

class Arrow(Scene):
    def construct(self):
        rect = Rectangle(color=WHITE, fill_opacity=0.5, height=2, width=2.5)
        circ = Circle().to_edge(DOWN)
        #arrow follows
        arrow = always_redraw(lambda: Line(start=rect.get_bottom(),end=circ.get_top()).add_tip())
        #animation
        self.play(Create(VGroup(rect,circ,arrow)))
        self.wait()
        # animate moving arrow
        self.play(rect.animate.to_edge(UR),circ.animate.scale(0.5),run_time=2)


