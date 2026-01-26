from manim import *
import math

class TeilfolgenS12(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        pos = MathTex(r"n", color=BLACK).move_to([4, 1.5, 0])


        # ========== SZENE 12 ==========
        folge3Tex = MathTex(r"a_n=(-1)^n", color=BLACK).to_edge(UP * 2)

        # Box um den Text, mit runden Ecken
        box = SurroundingRectangle(
            folge3Tex,
            color=BLACK,
            buff=0.3,  # Abstand Text ↔ Box
            corner_radius=0.2  # Rundung der Ecken
        )

        # Text + Box zusammenfassen
        boxed_folge3 = VGroup(box, folge3Tex)

        self.play(FadeIn(boxed_folge3))

        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[-1.5, 1.5, 1],
            tips=True,
            axis_config={"color": BLACK}
        ).shift(DOWN * 0.5)
        ax.get_x_axis().add_labels({i: MathTex(str(i), color=BLACK) for i in range(1, 10)})
        ax.get_y_axis().add_labels({-1: MathTex("-1", color=BLACK), 1: MathTex("1", color=BLACK)})
        self.play(Create(ax))

        folgeDots = VGroup()
        for n in range(1, 10):
            y = (-1) ** n
            d = Dot(ax.c2p(n, y), color=BLUE)
            folgeDots.add(d)
        self.play(LaggedStartMap(FadeIn, folgeDots, lag_ratio=0.1))

        folge3Tex1 = MathTex(r"n_k = 2k", color=GREEN).next_to(pos,direction=DOWN,aligned_edge=LEFT).shift(RIGHT * 0.1)
        folge3Tex2 = MathTex(r"n_k = 2k - 1", color=RED).next_to(pos,direction=DOWN,aligned_edge=LEFT).shift(DOWN * 4 + RIGHT * 0.1)
        folge3Tex3 = MathTex(r"n_k = 4k - 3", color=PURPLE).next_to(folge3Tex2,direction=DOWN,aligned_edge=LEFT).shift(UP * 2)


        # gerade Indices hervorheben (→ 1)
        gerade = [folgeDots[i] for i in range(1, 9, 2)]  # n=2,4,6,8
        self.play(FadeIn(folge3Tex1))
        self.play(*[d.animate.set_color(GREEN).scale(1.3) for d in gerade])
        self.wait(2)

        # ungerade Indices hervorheben (→ -1)
        ungerade = [folgeDots[i] for i in range(0, 9, 2)]  # n=1,3,5,7,9

        # n_k = 4k-3: n=1,5,9 (k=1,2,3)
        vierer = [folgeDots[i] for i in range(0, 9, 4)]  # n=1,5,9
        # Umkreise um die vierer-Punkte
        vierer_circles = VGroup()
        for d in vierer:
            circle = Circle(color=PURPLE, stroke_width=2, radius=0.15).move_to(d.get_center())
            vierer_circles.add(circle)
        
        self.play(FadeIn(folge3Tex2))
        self.play(*[d.animate.set_color(RED).scale(1.3) for d in ungerade])
        self.play(FadeIn(folge3Tex3))
        self.play(
            *[Create(c) for c in vierer_circles]
        )
        self.wait(2)

