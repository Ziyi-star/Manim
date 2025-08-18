from manim import *

class ExtremaSceneOneToFour(Scene):
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