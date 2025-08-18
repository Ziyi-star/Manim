from manim import *

class ExtremaSceneSixToSeven(Scene):
    def construct(self):
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