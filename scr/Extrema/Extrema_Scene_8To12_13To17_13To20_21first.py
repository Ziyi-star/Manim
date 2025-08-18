from manim import *

class ExtremaScene_8To12_13To17_13To20_21first(Scene):
    def construct(self):
        # ------- SCENE 8 - 12 ------- #
        DefinitionsBereichTex = MathTex(r"f: [-6, +\infty) \rightarrow \mathbb{R}", color=BLACK).scale(0.8).shift(
            UP * 3 + LEFT * 4)
        ax1 = Axes(
            x_range=[-6, 4],
            y_range=[-2, 5],
            tips=True,
            axis_config={
                'color': BLACK,
                'include_numbers': True
            }
        ).add_coordinates()

        # Farbe der Achsen-Beschriftungen
        ax1.get_x_axis().numbers.set_color(BLACK)
        ax1.get_y_axis().numbers.set_color(BLACK)
        axis_labels = ax1.get_axis_labels(MathTex("x"), MathTex("y")).set_color(BLACK)

        curve_1 = ax1.plot(lambda x: 1 / 3 * x ** 3 - 2 * x + 2, x_range=[-3, 3], color=BLUE_C)
        curve_2 = ax1.plot(lambda x: -x - 4, x_range=[-6, -3], color=BLUE_C)

        maximaA = Dot(ax1.c2p(-6, 2), color=RED)
        minimaB = Dot(ax1.c2p(-3, -1), color=RED)
        minimaD = Dot(ax1.c2p(1.414, 0.114), color=RED)
        maximaC = Dot(ax1.c2p(-1.414, 3.886), color=RED)

        BackgroundRect = Rectangle(color=RED_B, width=3, height=5, fill_color=RED_B, fill_opacity=1).move_to(
            ax1.c2p(2.83, 0), aligned_edge=DL).set_z_index(-30)

        self.play(Create(ax1), Write(axis_labels), FadeIn(DefinitionsBereichTex))
        self.play(Create(curve_2))
        self.play(Create(curve_1))

        self.play(Create(minimaD))
        self.play(Create(minimaB))
        self.play(Create(maximaC))
        self.play(Create(maximaA))

         # ------- SCENE 13 -17 ------- #

        self.play(Indicate(maximaA, scale_factor=2, color=RED), Indicate(maximaC, scale_factor=2, color=RED),
                  Indicate(minimaD, scale_factor=2, color=RED), Indicate(minimaB, scale_factor=2, color=RED))
        self.wait(0.5)
        self.play(Indicate(minimaB, scale_factor=2, color=RED))
        self.wait(0.5)
        self.play(Indicate(maximaC, scale_factor=2, color=RED))
        self.wait(0.5)
        self.play(FadeIn(BackgroundRect))
        self.wait(0.5)
        self.play(FadeOut(BackgroundRect))
        self.wait(0.5)
        self.play(Indicate(maximaC, scale_factor=2, color=RED))
        self.wait(0.5)

         # ------- SCENE 13 - 20 ------- #
        tracker = ValueTracker(0)

        tangent1 = TangentLine(curve_1, alpha=0.25 + (tracker.get_value() * 1.45), length=6, color=RED_E)

        xPointTangenteLine = ax1.get_vertical_line(
            ax1.input_to_graph_point(-3 + 7 * (0.107 + tracker.get_value() * 2.1), curve_1), color=BLACK).set_z_index(
            -1)
        xPointTangente = Dot(ax1.c2p(-3 + 7 * (0.107 + tracker.get_value() * 2.1), 0), color=RED)

        def updateTangent(obj):
            obj.become(TangentLine(curve_1, alpha=0.25 + (tracker.get_value() * 1.45), length=6, color=RED_E))

        def updatexPointTangenteLine(obj):
            obj.become(
                ax1.get_vertical_line(ax1.input_to_graph_point(-3 + 7 * (0.107 + tracker.get_value() * 2.1), curve_1),
                                      color=BLACK).set_z_index(-1))

        def updatexPointTangente(obj):
            obj.become(Dot(ax1.c2p(-3 + 7 * (0.107 + tracker.get_value() * 2.1), 0), color=RED))

        self.play(FadeIn(tangent1), FadeIn(xPointTangente, xPointTangenteLine))
        tangent1.add_updater(updateTangent)
        xPointTangenteLine.add_updater(updatexPointTangenteLine)
        xPointTangente.add_updater(updatexPointTangente)
        self.wait(0.5)
        self.play(tracker.animate.set_value(0.1), rate_functions=linear, run_time=3)
        self.wait(0.5)
        self.play(tracker.animate.set_value(0), rate_functions=linear, run_time=3)
        self.wait(0.5)
        self.play(tracker.animate.set_value(0.057), rate_functions=linear, run_time=3)
        self.wait(0.5)
        self.play(FadeOut(tangent1, xPointTangente, xPointTangenteLine))

        
        # ------- SCENE 21 ------- #

        FunctionPlusPointsGroup = VGroup(ax1, curve_1, curve_2, minimaB, minimaD, maximaA, maximaC, axis_labels)
        SatzText1 = MathTex(r"\text{Notwendige Bedingung für Extrema: }", color=BLACK)
        SatzText2 = MathTex(r"\text{Sei }f:", r"(a,b)", r"\rightarrow \mathbb{R}", r" \text{ differenzierbar}",
                            r"\text{ in } x_0 \in (a,b).", color=BLACK)
        SatzText3 = MathTex(r"\text{Wenn } f \text{ ein Extremum in } x_0 \text{ besitzt, dann gilt } f'(x_0)=0.",
                            color=BLACK)

        SatzTextPlaceholder = MathTex(r"t", color=WHITE)
        SatzTextDefinitionsbereich = MathTex(r"f: ", r"[-6, +\infty)", r"\rightarrow \mathbb{R}", color=BLACK)

        SatzTextDefinitionsbereich2 = MathTex(r"f: (-6, +6) \rightarrow \mathbb{R}", color=BLACK)

        SatzGroup = VGroup(SatzText1, SatzText2, SatzText3, SatzTextPlaceholder, SatzTextDefinitionsbereich,
                           SatzTextDefinitionsbereich2).arrange(direction=DOWN, aligned_edge=LEFT).scale(0.8).shift(
            UP * 2).set_z_index(2)
        SatzTextDefinitionsbereich2.move_to(SatzTextDefinitionsbereich, aligned_edge=LEFT)
        self.play(FunctionPlusPointsGroup.animate.scale(0.6).shift(DOWN * 1 + LEFT * 1), FadeOut(DefinitionsBereichTex))

        xA = Dot(ax1.c2p(-6, 0), color=BLUE)
        xB = Dot(ax1.c2p(-3, 0), color=BLUE)
        xC = Dot(ax1.c2p(1.414, 0), color=BLUE)
        xD = Dot(ax1.c2p(-1.414, 0), color=BLUE)

        self.wait(0.5)
        self.play(FadeIn(SatzText1, SatzText2, SatzText3))
        self.wait(0.5)
        self.play(FadeIn(SatzTextPlaceholder, SatzTextDefinitionsbereich))
        self.wait(0.5)
        self.play(Create(xA))
        self.play(Create(xB))
        self.play(Create(xD))
        self.play(Create(xC))
        self.wait(0.5)
        self.play(Indicate(xC, scale_factor=2, color=BLUE))
        self.play(Indicate(xD, scale_factor=2, color=BLUE))
        self.play(Indicate(xB, scale_factor=2, color=BLUE))
        # self.play(Indicate(SatzText2[3], scale_factor=1.5, color=BLUE))

        FailedTangent1 = Line(start=ax1.c2p(-4, -2), end=ax1.c2p(-2, 0), color=RED_E)
        FailedTangent2 = Line(start=ax1.c2p(-4, -0.5), end=ax1.c2p(-2, -1.5), color=RED_E)

        self.play(Create(FailedTangent1))
        self.play(Create(FailedTangent2))
        self.wait(0.5)
        self.play(FadeOut(FailedTangent1, FailedTangent2))

        self.play(Circumscribe(SatzText2[3], fade_out=True, run_time=2, color=BLUE))
        self.play(Indicate(xA, scale_factor=2, color=BLUE))

        IntervallBackgroundRect = BackgroundRectangle(VGroup(xA, xB), color=RED_B)
        self.play(FadeIn(IntervallBackgroundRect))
        self.play(FadeOut(IntervallBackgroundRect))
        self.play(curve_2.animate.set_color(GREEN_E), Wiggle(curve_2))
        self.play(Indicate(maximaA, scale_factor=2, color=RED), Indicate(minimaB, scale_factor=2, color=RED))
        self.play(curve_2.animate.set_color(BLUE_C))
        self.play(Circumscribe(SatzText2[1], fade_out=True, run_time=2, color=BLUE))
        self.play(Indicate(SatzTextDefinitionsbereich[1], color=BLACK, scale_factor=1.5))
        # self.play(Indicate(SatzText2[1], scale_factor=1.5, color=BLUE))#
        self.play(FadeTransform(SatzTextDefinitionsbereich, SatzTextDefinitionsbereich2))
        self.wait(0.5)
        self.play(Circumscribe(SatzText2[3], fade_out=True, run_time=2, color=BLUE),
                  Circumscribe(SatzText2[1], fade_out=True, run_time=2, color=BLUE))

        whiteRect1 = Rectangle(fill_color=WHITE, fill_opacity=1, height=4, width=20).shift(UP * 3).set_z_index(1)
        whiteRect2 = Rectangle(fill_color=WHITE, fill_opacity=1, height=20, width=3).shift(LEFT * 6.2).set_z_index(1)
        whiteRect3 = Rectangle(fill_color=WHITE, fill_opacity=1, height=20, width=3).shift(RIGHT * 6.2).set_z_index(1)

        # rectEinschränkung = Polygon(ax1.c2p(-2.5,-2),ax1.c2p(-2.5,5.5), ax1.c2p(3,5.5), ax1.c2p(3,-2),color=WHITE, fill_color=GREY, fill_opacity=0.5, )
        self.play(FadeIn(whiteRect1, whiteRect2, whiteRect3),
                  VGroup(FunctionPlusPointsGroup, xA, xB, xC, xD).animate.scale(2.2).shift(LEFT + DOWN * 0.85))
        # self.play(Create(rectEinschränkung))
        self.wait(0.5)

        self.play(Indicate(xC, scale_factor=2, color=BLUE), Indicate(xD, scale_factor=2, color=BLUE))
        self.wait(0.5)

        ExtremaBedingungTex = MathTex(
            r"&x \text{ Extremum } \Rightarrow \text{ Ableitung 0} \\ &\text{Ableitung 0} \nRightarrow x \text{ Extremum } ",
            color=BLACK).scale(0.8).shift(RIGHT * 3 + UP * 0.5).set_z_index(100)
        ExtremaBedingungTexBackground = BackgroundRectangle(ExtremaBedingungTex, color=WHITE, fill_opacity=1, buff=0.2)

        self.play(FadeIn(ExtremaBedingungTex, ExtremaBedingungTexBackground))
        self.wait(0.5)
        self.play(FadeOut(
            VGroup(ExtremaBedingungTex, ExtremaBedingungTexBackground, ax1, axis_labels, xA, xB, xC, xD, whiteRect1,
                   whiteRect2,
                   whiteRect3, minimaB, minimaD, maximaA, maximaC, SatzText1, SatzText2, SatzText3, SatzTextPlaceholder,
                   SatzTextDefinitionsbereich2, curve_1, curve_2)))
        self.wait(0.5)

        