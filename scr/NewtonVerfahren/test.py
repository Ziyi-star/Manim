from manim import *
from reactive_manim import *


class Test(Scene):
    def construct(self):

        x_n = MathTex("x_n").set_color(YELLOW)
        x_n_plus_1 = MathTex("x_{n+1}").set_color(GREEN)
        eqn = MathTex(
            ["f(x_n)", "+", [ "f'(x_n)", "(", [x_n_plus_1, "-", x_n] , ")" ]],
            "=", 
            "0"
        )
        self.add(eqn).wait(1)

        f_xn = eqn[0][0]
        eqn[0] = eqn[0][2]
        eqn[2] = MathTex( "-", f_xn)

        anim = TransformInStages.progress(eqn, lag_ratio=0.4)
        anim.intercept(f_xn).set_animation(lambda source, target: Transform(source, target, path_arc=PI/2))
        self.play(anim)
        self.wait(1)

        f_xn_prime = eqn[0][0]
        eqn[0] = eqn[0][2]
        eqn[2] = MathTex( "-", Fraction(eqn[2][1], f_xn_prime))

        self.play(TransformInStages.progress(eqn, lag_ratio=0.4))
        self.wait(1)

        eqn[0] = eqn[0][0]
        eqn[2] = MathTex(eqn[2], "+", x_n)

        anim = TransformInStages.progress(eqn, lag_ratio=0.4)
        anim.intercept(x_n).set_animation(lambda source, target: Transform(source, target, path_arc=PI/2))
        self.play(anim)
        self.wait(1)


