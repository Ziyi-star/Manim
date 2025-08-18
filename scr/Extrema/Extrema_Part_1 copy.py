from manim import *


class ExtremaSceneFourtytwo(Scene):
    def construct(self):
        # ------- SCENE 42 ------- #
        ax2 = Axes(
            x_range=[-2, 2],
            y_range=[-4, 4],
            tips=True,
            x_length=6,
            axis_config={
                'color': BLACK,
                'include_numbers': True}).shift(RIGHT * 2)
        axis_labels = ax2.get_axis_labels(MathTex("x"), MathTex("y")).set_color(BLACK)

        self.play(Create(ax2), Write(axis_labels))

        curve_xPower4 = ax2.plot(lambda x: x ** 4 + 1, x_range=[-2, 2], color=BLUE_C).set_z_index(1)

        curveText1 = MathTex(r"f(x)=x^4+1 ", color=BLACK)
        curveText2 = MathTex(r"f'(x)=4x^3 ", color=BLACK)
        curveText3 = MathTex(r"f''(x)=12x^2 ", color=BLACK)
        curveText4 = MathTex(r"f'(x_0)=0", r"\Leftrightarrow 4x_0^3=0", r"\Leftrightarrow x_0=0", color=BLACK)
        curveText5 = MathTex(r"f''(x_0) = f''(0)", r"= 12 \cdot 0^2 = 0", color=BLACK)

        curveTextGroup = VGroup(curveText1, curveText2, curveText3, curveText4, curveText5).arrange(direction=DOWN,
                                                                                                    aligned_edge=LEFT).scale(
            0.8).shift(LEFT * 4)

        curve_Szene30 = ax2.plot(lambda x: 1 / 3 * x ** 3 - 2 * x + 2, x_range=[-2.5, 2.5], color=BLUE_C)
        tangentcurve_Szene30 = TangentLine(curve_Szene30, alpha=0.9, length=3.95, color=GREEN_E)  # left

        trackerTangent = ValueTracker(0.3)

        def updatetangentcurve_Szene30(obj):
            obj.become(TangentLine(curve_Szene30, alpha=0.9 - trackerTangent.get_value(), length=3.95, color=GREEN_E))

        def updatetangentcurve_Szene30_xhoch4(obj):
            obj.become(TangentLine(curve_xPower4, alpha=0.25 + trackerTangent.get_value(), length=3.95, color=RED_E))

        tangentcurve_Szene30.add_updater(updatetangentcurve_Szene30)
        self.add(ax2, axis_labels)
        self.play(FadeIn(curveText1))
        self.play(Create(curve_xPower4))
        self.play(FadeIn(curveText2))
        self.play(FadeIn(curveText3))
        self.play(FadeIn(curveText4[0]))
        self.play(FadeIn(curveText4[1]))
        self.play(FadeIn(curveText4[2]))
        self.play(FadeIn(curveText5[0]))
        self.play(FadeIn(curveText5[1]))
        self.wait(0.5)
        self.play(FadeOut(curve_xPower4, curveTextGroup))
        self.play(Create(curve_Szene30))
        self.play(Create(tangentcurve_Szene30))
        self.wait(0.5)
        self.play(trackerTangent.animate.set_value(0), rate_functions=linear, run_time=3)
        self.wait(0.5)
        tangentcurve_Szene30.remove_updater(updatetangentcurve_Szene30)
        self.play(FadeOut(tangentcurve_Szene30))
        trackerTangent.set_value(0.8)
        tangentcurve_Szene30.add_updater(updatetangentcurve_Szene30)
        self.play(Create(tangentcurve_Szene30))
        self.play(trackerTangent.animate.set_value(0.5), rate_functions=linear, run_time=3)
        self.wait(0.5)
        tangentcurve_Szene30.remove_updater(updatetangentcurve_Szene30)
        trackerTangent.set_value(0.18)
        self.play(FadeOut(curve_Szene30, tangentcurve_Szene30))
        tangentcurve_Szene30.set_color(RED_E)
        tangentcurve_Szene30.add_updater(updatetangentcurve_Szene30_xhoch4)
        self.wait(0.5)

        curve_xPower4Tex = MathTex(r"f(x)=x^4+1", color=BLACK).scale(0.9).shift(UP * 3 + LEFT * 4)
        self.play(Create(curve_xPower4), FadeIn(curve_xPower4Tex))
        self.play(Create(tangentcurve_Szene30))
        self.play(trackerTangent.animate.set_value(0.33), rate_functions=linear, run_time=3)
