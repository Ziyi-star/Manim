from manim import *

class EquationTransformTest(Scene):
    def construct(self):
        # Create initial equation
        eq3_initial = MathTex(
            "=>", "f(x_n)", "+", "f'(x_n)", "(x_{n+1}-x_n)", "=", "0",
            color=WHITE
        ).scale(0.6)

        # Show initial equation
        self.play(Write(eq3_initial), run_time=2)
        self.wait(1)

        # Isolate "f(x_n)" and animate its movement
        f_xn = eq3_initial[1]  # "f(x_n)" in the initial equation


        # Animate "f(x_n)" moving to the right
        self.play(
            f_xn.animate.next_to(eq3_initial[6], RIGHT),  # Move next to "="
            FadeOut(eq3_initial[2], eq3_initial[-1]),  # Remove "+" and "0"
            run_time=3
        )
        minus_sign = MathTex("-").next_to(f_xn, LEFT, buff=0.1).scale(0.6)

        self.play(Write(minus_sign), run_time=1)
        self.wait(2)


