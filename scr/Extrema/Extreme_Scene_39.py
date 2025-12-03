from manim import *

class ExtremaSceneThirtynine(Scene):
    def construct(self):
        self.camera.background_color = WHITE
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