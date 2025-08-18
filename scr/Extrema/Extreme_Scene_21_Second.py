from manim import *

class ExtremaSceneTwentyoneSecond(Scene):
    def construct(self):
        ax2 = Axes(
            x_range=[-2, 2],
            y_range=[-4, 4],
            tips=True,
            x_length=6,
            axis_config={
                'color': BLACK,
                'include_numbers': True}).shift(RIGHT * 2)
        axis_labels2 = ax2.get_axis_labels(MathTex("x"), MathTex("y")).set_color(BLACK)

        ax22 = Axes(
            x_range=[-3, 3],
            y_range=[-4, 4],
            tips=True,
            x_length=6,
            axis_config={
                'color': BLACK,
                'include_numbers': True}).shift(RIGHT * 2)
        axis_labels22 = ax22.get_axis_labels(MathTex("x"), MathTex("y")).set_color(BLACK)

        curve_xCubed = ax2.plot(lambda x: x ** 3 + 1, x_range=[-2, 2], color=BLUE_C).set_z_index(1)
        curve_xCubed2 = ax22.plot(lambda x: 1 / 3 * x ** 3 - 2 * x + 2, x_range=[-3, 3], color=BLUE_C).set_z_index(1)

        x0 = Dot(ax2.c2p(0, 1), color=BLUE_E).set_z_index(2)
        tangent00Punkt = TangentLine(curve_xCubed, alpha=0.5, length=6, color=GREEN_E).set_z_index(2)
        tangent0Punkt = TangentLine(curve_xCubed2, alpha=0.3345, length=6, color=GREEN_E).set_z_index(2)
        tangent1Punkt = TangentLine(curve_xCubed2, alpha=1 - 0.3345, length=6, color=RED_E).set_z_index(2)

        HinreichendeBedingung1 = MathTex(
            r"\text{Wenn die hinreichende Bedingung an } x_0 \text{ erfüllt ist,}",
            color=BLACK
        ).shift(UP)

        HinreichendeBedingung2 = MathTex(
            r"\text{dann ist } x_0 \text{ eine Extremstelle von } f.",
            color=BLACK
        )

        HinreichendeBedingung3 = MathTex(r"\text{Sei } f:(a,b) \rightarrow W \text{ eine differenzierbare Funktion.}",
                                         color=BLACK).shift(UP)
        HinreichendeBedingung4 = MathTex(
            r"\text{Im Punkt } x_0 \in (a,b) \text{ sei } f \text{ zweimal differenzierbar und es gelte }",
            color=BLACK).shift(UP)
        HinreichendeBedingung5 = MathTex(r"f'(x_0) = 0 \text{ und } f''(x_0) > 0 \text{ bzw. } f''(x_0) < 0.",
                                         color=BLACK).shift(UP)
        HinreichendeBedingung6 = MathTex(
            r"\text{Dann besitzt } f \text{ in } x \text{ ein lokales Minimum (bzw. Maximum.)}",
            color=BLACK
        ).shift(UP)
        DefinitionGroup = VGroup(HinreichendeBedingung1, HinreichendeBedingung2).arrange(direction=DOWN,
                                                                                         aligned_edge=LEFT).scale(
            0.8).shift(LEFT * 2.5 + UP * 2)

        DefinitionGroup2 = VGroup(HinreichendeBedingung3, HinreichendeBedingung4, HinreichendeBedingung5,
                                  HinreichendeBedingung6).arrange(
            direction=DOWN, aligned_edge=LEFT).scale(0.6).shift(LEFT * 3 + UP * 2)

        # curve_xCubedLeft = ax2.plot(lambda x: x**3, x_range=[-2, 0], color=RED_E).set_z_index(3)
        # curve_xCubedRight = ax2.plot(lambda x: x**3, x_range=[0, 2], color=GREEN_E).set_z_index(3)

        # curve_transformed = ax2.plot(lambda x: (x+0.66)**3-2*(x+0.66)**2+1.58, x_range=[-2, 2], color=BLUE_C).set_z_index(1)

        tangentLeft = TangentLine(curve_xCubed2, alpha=0.6, length=3.95, color=RED_E).set_z_index(5)
        tangentRight = TangentLine(curve_xCubed2, alpha=0.2, length=3.95, color=GREEN_E).set_z_index(5)

        LineLeftX = Line(start=ax2.c2p(-2, 0), end=ax2.c2p(0, 0), color=GREEN_E).set_z_index(5)
        LineRightX = Line(start=ax2.c2p(0, 0), end=ax2.c2p(2, 0), color=RED_E).set_z_index(5)

        self.play(Create(ax2), Write(axis_labels2))
        self.play(Create(curve_xCubed))
        self.play(Create(x0))
        self.play(Create(tangent00Punkt))
        self.wait(0.5)
        self.play(FadeOut(x0, tangent00Punkt))
        self.play(FadeIn(DefinitionGroup))
        self.wait(1.5)
        self.play(FadeOut(HinreichendeBedingung1, HinreichendeBedingung2), FadeIn(DefinitionGroup2))
        self.wait(1.5)
        # self.play(FadeOut(DefinitionGroup2))
        self.play(Transform(curve_xCubed, curve_xCubed2), Transform(ax2, ax22))
        self.play(Create(LineLeftX))
        self.play(FadeIn(LineRightX))
        self.play(Create(tangentLeft))
        tangentValueTracker = ValueTracker(0)

        def updatetangentcurve_XXX(obj):
            obj.become(TangentLine(curve_xCubed2, alpha=0.6 + tangentValueTracker.get_value(), length=3.95,
                                   color=RED_E).set_z_index(5))

        tangentLeft.add_updater(updatetangentcurve_XXX)

        self.wait(0.5)
        self.play(tangentValueTracker.animate.set_value(0.4 - 0.3345), rate_functions=linear, run_time=2)
        tangentLeft.remove_updater(updatetangentcurve_XXX)
        tangentValueTracker.set_value(0)
        self.wait(0.5)
        self.play(Create(tangentRight))

        def updatetangentcurve_XXX(obj):
            obj.become(TangentLine(curve_xCubed2, alpha=0.2 + tangentValueTracker.get_value(), length=3.95,
                                   color=GREEN_E).set_z_index(5))

        tangentRight.add_updater(updatetangentcurve_XXX)

        self.wait(0.5)
        self.play(tangentValueTracker.animate.set_value(0.3345 - 0.2), rate_functions=linear, run_time=2)
        tangentRight.remove_updater(updatetangentcurve_XXX)
        self.wait(0.5)
        self.play(FadeOut(LineLeftX, LineRightX, tangentLeft, tangentRight, curve_xCubed, ax2, axis_labels2, DefinitionGroup2))
        self.wait(0.5)
