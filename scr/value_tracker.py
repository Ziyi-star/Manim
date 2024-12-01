from manim import *

class ValueTracker_example(Scene):
    def construct(self):
        key = ValueTracker(3.5)

        # Create a DecimalNumber and link it to the ValueTracker
        num = always_redraw(lambda: DecimalNumber(key.get_value()))

        self.play(FadeIn(num))
        self.wait(1)
        self.play(key.animate.set_value(0), run_time = 3)