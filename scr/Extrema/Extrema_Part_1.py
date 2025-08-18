from manim import *


class Extrema_Part_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        # ------- SCENE 1 - 4 ------- #
        AufgabenstellungText1 = MathTex(
            r"\text{Gegeben sei die Funktion } f:\mathbb{R}  \rightarrow \mathbb{R} \text{ mit } f(x) = \frac{1}{3}x^3-x+2.",
            color=BLACK)
        AufgabenstellungText2 = MathTex(r"\text{a) Berechnen Sie alle Extremstellen der Funktion.} ", color=BLACK)
        AufgabenstellungText3 = MathTex(
            r"\text{b) Begründen Sie, ob es sich bei den in a) berechneten Extrema nur um lokale oder }", color=BLACK)
        AufgabenstellungText4 = MathTex(r"\text{auch um globale Extrema handelt.}", color=BLACK)

        AufgabenstellungTextGroup = VGroup(AufgabenstellungText1, AufgabenstellungText2, AufgabenstellungText3,
                                           AufgabenstellungText4).arrange(direction=DOWN, aligned_edge=LEFT).scale(0.7)
        BubblePicture1 = SVGMobject(fill_opacity=1, fill_color=BLUE_A, should_center=True,
                                    file_name="media/images/Bubble.svg", stroke_width=5, stroke_color=BLUE_D,
                                    stroke_opacity=1).scale(3)

        BubbleText1 = Tex("Hoch- und Tiefpunkte?", color=BLACK).shift(UP * 2 + LEFT).scale(0.9)
        BubbleText2 = Tex("Erste Ableitung?", color=BLACK).shift(UP + RIGHT * 2).scale(0.9)
        BubbleText3 = Tex("Bedingungen?", color=BLACK).shift(LEFT * 3).scale(0.9)
        BubbleText4 = Tex("lokal vs. global?", color=BLACK).shift(DOWN * 1 + RIGHT).scale(0.9)

        self.play(FadeIn(AufgabenstellungTextGroup))
        self.wait(0.5)
        self.play(FadeIn(BubblePicture1))
        self.wait(0.5)
        self.play(FadeIn(BubbleText1))
        self.play(FadeIn(BubbleText2))
        self.play(FadeIn(BubbleText3))
        self.play(FadeIn(BubbleText4))
        self.wait(0.5)
        self.play(FadeOut(BubblePicture1, BubbleText1, BubbleText2, BubbleText3, BubbleText4))
        self.wait(0.5)
        self.play(FadeOut(AufgabenstellungTextGroup))
        # ------- SCENE 5 ------- #
        DefinitionText1 = MathTex(r"\text{Sei } f:D \rightarrow \mathbb{R} \text{ eine Funktion.}", color=BLACK)
        DefinitionText2 = MathTex(
            r"\text{Die Funktion } f \text{ hat in } x_0 \in D \text{ ein lokales Maximum (bzw. Minimum),}",
            color=BLACK)
        DefinitionText3 = MathTex(
            r"\text{wenn ein } \epsilon > 0 \text{ existiert, sodass } f(x_0) \geq f(x) \text{ (bzw. } f(x_0) \leq f(x))",
            color=BLACK)
        DefinitionText4 = MathTex(r"\text{ für alle } x \text{ mit } x \in U_{\epsilon}(x_0) \cap D. ", color=BLACK)
        DefinitionText5 = MathTex(
            r"\text{Gilt } f(x_0) \geq f(x) \text{ (bzw. } f(x_0) \leq f(x)) \text{ für alle } x \in D,", color=BLACK)
        DefinitionText6 = MathTex(r"\text{so heißt } x_0 \text{ globales Maximum (bzw. Minimum).}", color=BLACK)

        DefinitionGroup = VGroup(DefinitionText1, DefinitionText2, DefinitionText3, DefinitionText4, DefinitionText5,
                                 DefinitionText6).arrange(direction=DOWN, aligned_edge=LEFT).scale(0.6)

        self.play(Write(DefinitionText1), run_time=3)
        self.play(Write(DefinitionText2), run_time=3)
        self.play(Write(DefinitionText3), run_time=3)
        self.play(Write(DefinitionText4), run_time=3)
        self.play(Write(DefinitionText5), run_time=3)
        self.play(Write(DefinitionText6), run_time=3)
        self.wait(0.5)
        self.play(FadeOut(DefinitionGroup))

        # ------- SCENE 6 - 7------- #

        GebirsZugPicture = ImageMobject("media/images/Mountain.jpg").scale(2).set_z_index(-10)
        ellipse_Hochpunkt = Ellipse(width=.3, height=0.3, color=PURE_RED).shift(UP * 1.4 + LEFT * 0.4)
        ellipse_Hochpunkt2 = Ellipse(width=.3, height=0.3, color=PURE_RED).shift(LEFT * 2 + UP * .4)

        # ellipse_Tiefpunkt = Ellipse(width=1.25, height=0.75, color=RED_A).shift(DOWN*2.7+RIGHT)

        self.play(FadeIn(GebirsZugPicture))
        self.play(FadeIn(ellipse_Hochpunkt, ellipse_Hochpunkt2))
        # self.play(GebirsZugPicture.animate.scale(2),ellipse_Hochpunkt.animate.scale(2).shift(UP*1.34+LEFT*0.35),ellipse_Hochpunkt2.animate.scale(2).shift(LEFT*1.95+UP*0.5))

        dottedLine2 = DashedLine(ellipse_Hochpunkt2.get_center(), ellipse_Hochpunkt2.get_center() + DOWN * 2.75,
                                 color=BLACK, stroke_width=6, dash_length=0.2)

        yDifference = ellipse_Hochpunkt.get_center()[1] - ellipse_Hochpunkt2.get_center()[1]
        dottedLine1 = DashedLine(ellipse_Hochpunkt.get_center(),
                                 ellipse_Hochpunkt.get_center() + (yDifference + 2.75) * DOWN, color=BLACK,
                                 stroke_width=6, dash_length=0.2)

        LineEpsilon1 = Line(start=ellipse_Hochpunkt2.get_center() + DOWN * 2.75 + LEFT * 0.3,
                            end=ellipse_Hochpunkt2.get_center() + DOWN * 2.75 - LEFT * 0.3, color=BLACK, stroke_width=6)
        LineEpsilon2 = Line(start=ellipse_Hochpunkt.get_center() + (2.75 + yDifference) * DOWN + LEFT * 0.6,
                            end=ellipse_Hochpunkt.get_center() + (2.75 + yDifference) * DOWN - LEFT * 0.6, color=BLACK,
                            stroke_width=6)
        Epsilon = MathTex(r"\mathbf{\varepsilon}", color=BLACK).next_to(LineEpsilon1, direction=DOWN, buff=0.15)
        Epsilon2 = Epsilon.copy().next_to(LineEpsilon2, direction=DOWN, buff=0.15)

        self.play(Create(dottedLine1), Create(dottedLine2))
        self.play(Create(LineEpsilon1), Create(LineEpsilon2), FadeIn(Epsilon, Epsilon2))
        self.wait(0.5)
        self.play(FadeOut(GebirsZugPicture, ellipse_Hochpunkt, ellipse_Hochpunkt2, dottedLine1, dottedLine2, Epsilon,
                          Epsilon2, LineEpsilon2, LineEpsilon1))

        GlobePic = ImageMobject("media/images/Globe.jpg").scale(0.7).set_z_index(-10)
        Everest1 = Triangle(color=DARK_GRAY, fill_color=DARK_GRAY, fill_opacity=1)
        Everest2 = Triangle(color=GRAY, fill_color=GRAY, fill_opacity=1).scale(0.6).move_to(Everest1, aligned_edge=UP)
        Everest3 = Triangle(color=GRAY_A, fill_color=GRAY_A, fill_opacity=1).scale(0.2).move_to(Everest1,
                                                                                                aligned_edge=UP)

        EverestGroup = VGroup(Everest1, Everest2, Everest3).rotate(angle=-71 * DEGREES).scale(0.3).move_to(
            [3.2, 1.1, 0])
        EverestLabel = Text("Mount Everest", color=BLACK).scale(0.4).next_to(Everest3, aligned_edge=UP + RIGHT,
                                                                             buff=1.2).shift(UP)
        EverestArrow = Arrow(start=EverestLabel.get_bottom(), end=Everest1.get_left(), color=BLACK, buff=0.12)

        MariannenLabel = Text("Marianengraben", color=BLACK).scale(0.4).move_to([-5, 0, 0])

        MariannenArrow = Arrow(start=MariannenLabel.get_bottom(), end=MariannenLabel.get_bottom() + DOWN + RIGHT * 2,
                               color=BLACK, buff=0.12)

        HeadLine = Tex(r"Globale Extrempunkte", color=BLACK).scale(0.9).shift(UP * 3.5)
        self.play(FadeIn(GlobePic, HeadLine))
        self.wait(0.5)
        self.play(FadeIn(EverestLabel))
        self.wait(0.5)
        self.play(GrowArrow(EverestArrow))
        self.wait(0.5)
        self.play(FadeIn(MariannenLabel))
        self.wait(0.5)
        self.play(GrowArrow(MariannenArrow))
        self.wait(0.5)
        self.play(FadeOut(GlobePic, EverestLabel, EverestArrow, MariannenLabel, MariannenArrow, HeadLine))

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

        # ------- SCENE 39 ------- #

        AufgabenstellungTextScene39_1 = MathTex(
            r"\text{Gegeben sei die Funktion } f:\mathbb{R}  \rightarrow \mathbb{R} \text{ mit } f(x) = \frac{1}{3}x^3-x+2.",
            color=BLACK)
        AufgabenstellungTextScene39_2 = MathTex(r"\text{a) Berechnen Sie alle Extremstellen der Funktion.} ",
                                                color=BLACK)
        AufgabenstellungTextScene39_3 = MathTex(
            r"\text{b) Begründen Sie, ob es sich bei den in a) berechneten Extrema nur um lokale oder }", color=BLACK)
        AufgabenstellungTextScene39_4 = MathTex(r"\text{auch um globale Extrema handelt.}", color=BLACK)

        LösungTextPlaceholder = MathTex(r"t", color=WHITE)

        LösungText1 = MathTex(r"f'(x)=x^2-1", color=BLACK)
        LösungText2 = MathTex(r"f'(x)=0", r"\Leftrightarrow x^2-1=0", r"\Leftrightarrow x_1=1 \text{ oder } x_2=-1",
                              color=BLACK)
        LösungText3 = MathTex(r"f''(x)=2x", color=BLACK)
        LösungText4 = MathTex(r"f''(x_1)", r"=2 \cdot 1", r"= 2 \neq 0", r"\Rightarrow x_1 \text{ lokales Minimum}",
                              color=BLACK)
        LösungText5 = MathTex(r"f''(x_2)", r"=2 \cdot (-1)", r"= -2 \neq 0", r"\Rightarrow x_2 \text{ lokales Maximum}",
                              color=BLACK)

        AufgabenstellungTextGroup = VGroup(AufgabenstellungTextScene39_1, AufgabenstellungTextScene39_2,
                                           AufgabenstellungTextScene39_3, AufgabenstellungTextScene39_4,
                                           LösungTextPlaceholder, LösungText1, LösungText2, LösungText3, LösungText4,
                                           LösungText5).arrange(direction=DOWN, aligned_edge=LEFT).scale(0.7).shift(
            UP * 0.8)

        # LösungTextGroup = VGroup(LösungText1,LösungText2,LösungText3,LösungText4,LösungText5).arrange(direction=DOWN,aligned_edge=LEFT).scale(0.7)

        self.play(FadeIn(
            VGroup(AufgabenstellungTextScene39_1, AufgabenstellungTextScene39_2, AufgabenstellungTextScene39_3,
                   AufgabenstellungTextScene39_4)))
        self.wait(0.5)
        self.play(FadeIn(LösungText1))
        self.wait(0.5)
        self.play(FadeIn(LösungText2[0]))
        self.wait(0.5)
        self.play(FadeIn(LösungText2[1]))
        self.wait(0.5)
        self.play(FadeIn(LösungText2[2]))
        self.wait(0.5)
        self.play(Indicate(LösungText2[2], color=BLACK, scale_factor=1.5))
        self.wait(0.5)
        self.play(FadeIn(LösungText3))
        self.wait(0.5)
        self.play(FadeIn(LösungText4[0]))
        self.wait(0.5)
        self.play(FadeIn(LösungText4[1]))
        self.wait(0.5)
        self.play(FadeIn(LösungText4[2]))
        self.wait(0.5)
        self.play(FadeIn(LösungText5[0]))
        self.wait(0.5)
        self.play(FadeIn(LösungText5[1]))
        self.wait(0.5)
        self.play(FadeIn(LösungText5[2]))
        self.wait(0.5)
        self.play(FadeIn(LösungText5[3]))
        self.wait(0.5)
        self.play(FadeIn(LösungText4[3]))
        self.wait(0.5)
        self.play(FadeOut(AufgabenstellungTextGroup))

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

        self.play(Create(ax2), Write(axis_labels2))

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
        self.add(ax2, axis_labels2)
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
