from manim import *

class ValueTracker_example(Scene):
    def construct(self):
        key = ValueTracker(3.5)

        # Create a DecimalNumber and link it to the ValueTracker
        num = always_redraw(lambda: DecimalNumber().set_value(key.get_value()))

        # Text gradually becomes visible
        self.play(FadeIn(num))
        self.wait()
        self.play(key.animate.set_value(0), run_time = 3, rate_func = linear)