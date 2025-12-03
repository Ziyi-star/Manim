from manim import *
import math

class Teilfolgen(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Dimmer – über Standard-Objekten, aber hinter Bubble/Icon/Text
        dimmer = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_color=WHITE, fill_opacity=0.85, stroke_width=0
        ).move_to(ORIGIN).set_z_index(50)

        aufgabenStellung1 = MathTex(r"\text{Beweisen Sie, dass eine Folge } (a_n)_{n \in \mathbb{N}} \text{ genau dann gegen }", color=BLACK)
        aufgabenStellung2 = MathTex(r"\text{eine Wert } a \text{ konvergiert, wenn alle Teilfolgen}", color=BLACK)
        aufgabenStellung3 = MathTex(r"(a_{n_k})_{k \in \mathbb{N}} \text{ der Folge } (a_n)_{n \in \mathbb{N}} \text{ gegen } a \text{ konvergieren.}", color=BLACK)

        aufgabenStellungGroup = VGroup(aufgabenStellung1,aufgabenStellung2,aufgabenStellung3).arrange(direction=DOWN,aligned_edge=LEFT)

        self.play(Write(aufgabenStellung1))
        self.play(Write(aufgabenStellung2))
        self.play(Write(aufgabenStellung3))
        self.wait(4)
        self.play(FadeOut(aufgabenStellungGroup))
        self.wait(0.5)

        # Definition Teilfolge in drei Zeilen
        definitionTeilfolgeGroup = VGroup(
            MathTex(
                r"\text{Sei } (a_n)_{n \in \mathbb{N}} \text{ eine Folge und } "
                r"(n_k)_{k \in \mathbb{N}} \text{ eine}",
                color=BLACK
            ),
            MathTex(
                r"\text{monoton wachsende Folge natürlicher Zahlen.}",
                color=BLACK
            ),
            MathTex(
                r"\text{Dann heißt } (a_{n_k})_{k \in \mathbb{N}} "
                r"\text{ Teilfolge der Folge } (a_n)_{n \in \mathbb{N}}.",
                color=BLACK
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        # Box mit runden Ecken und hellblauer Füllung
        box_defTeilfolge = SurroundingRectangle(
            definitionTeilfolgeGroup,
            color=BLUE,
            buff=0.5,
            corner_radius=0.2
        ).set_fill(color=BLUE, opacity=0.2).set_z_index(100)

        # Text auch ganz nach vorne
        definitionTeilfolgeGroup.set_z_index(101)

        # Alles als eine Gruppe zentriert
        boxed_defTeilfolge = VGroup(box_defTeilfolge, definitionTeilfolgeGroup).move_to(ORIGIN)

        # Einblenden
        self.play(FadeIn(boxed_defTeilfolge))
        self.wait(2)

        # Ausblenden für nächste Szene
        self.play(FadeOut(boxed_defTeilfolge))

        folge1Tex = MathTex(r"a_n=1+\frac{1}{n}", color=BLACK).to_edge(UP * 2)

        # Box mit runden Ecken um den Text
        box1 = SurroundingRectangle(
            folge1Tex,
            color=BLACK,
            buff=0.3,  # Abstand Text ↔ Box
            corner_radius=0.2  # Rundung der Ecken
        )

        # beides zusammen gruppieren
        boxed_folge1 = VGroup(box1, folge1Tex)

        ax = Axes(
                x_range=[0, 9],
                y_range=[0, 2.5, 0.5],
                y_axis_config={"numbers_to_include": [0,0.5,1,1.5,2]},
                tips=True,
                axis_config={
                        'color' : BLACK}
            ).shift(UP*0.5)
        xAxis = ax.get_x_axis()
        ax.get_x_axis().add_labels(dict_values={i : MathTex(r"n="+str(i), color=BLACK) for i in range(1,9)})

        ax.get_y_axis().numbers.set_color(BLACK)

        self.play(FadeIn(boxed_folge1))
        self.play(FadeIn(ax))

        DotGroup1 = VGroup()

        for i in range(1,9):
            d = Dot(ax.c2p(i,1+1/i),color=BLUE_E)
            DotGroup1.add(d)
        self.play(ShowIncreasingSubsets(DotGroup1), run_time=2, rate_functions=linear)

        pos = MathTex(r"n", color=BLACK).move_to([4, 1.5, 0])
        folge2Tex = MathTex(r"n_k = 2k", color=RED).next_to(pos,direction=DOWN,aligned_edge=LEFT)

        self.play(FadeIn(folge2Tex))

        n2label = MathTex(r"n_1 = 1.5", color=RED_E).scale(0.7).next_to(ax.get_x_axis().labels[1], direction=DOWN,aligned_edge=ORIGIN, buff=0.2)
        n4label = MathTex(r"n_2 = 1.25", color=RED_E).scale(0.7).next_to(ax.get_x_axis().labels[3], direction=DOWN,aligned_edge=ORIGIN, buff=0.2)
        n6label = MathTex(r"n_3 = 1.167", color=RED_E).scale(0.7).next_to(ax.get_x_axis().labels[5], direction=DOWN,aligned_edge=ORIGIN, buff=0.2)
        n8label = MathTex(r"n_4 = 1.125", color=RED_E).scale(0.7).next_to(ax.get_x_axis().labels[7], direction=DOWN,aligned_edge=ORIGIN, buff=0.2)

        self.play(DotGroup1[1].animate.scale(2).set_color(RED_E))
        self.play(FadeIn(n2label))
        self.play(DotGroup1[3].animate.scale(2).set_color(RED_E))
        self.play(FadeIn(n4label))
        self.play(DotGroup1[5].animate.scale(2).set_color(RED_E))
        self.play(FadeIn(n6label))
        self.play(DotGroup1[7].animate.scale(2).set_color(RED_E))
        self.play(FadeIn(n8label))

        self.play(FadeOut(DotGroup1[0],DotGroup1[2],DotGroup1[4],DotGroup1[6]))

        ax2 = Axes(
                x_range=[0, 9],
                y_range=[0, 2.5, 0.5],
                y_axis_config={"numbers_to_include": [0,0.5,1,1.5,2]},
                tips=True,
                axis_config={
                        'color' : BLACK}
            ).shift(UP*0.5)
        xAxis = ax2.get_x_axis()
        ax2.get_x_axis().add_labels(dict_values={i : MathTex(r"k="+str(i), color=BLACK) for i in range(1,9)})
        ax2.get_y_axis().numbers.set_color(BLACK)

        self.play(Transform(ax,ax2))

        DotGroup2 = VGroup()

        for i in range(1,5):
            d = Dot(ax2.c2p(i,1+1/(2*i)),color=RED_E).scale(2)
            DotGroup2.add(d)

        self.play(Transform(DotGroup1[1],DotGroup2[0]),Transform(DotGroup1[3],DotGroup2[1]),Transform(DotGroup1[5],DotGroup2[2]),Transform(DotGroup1[7],DotGroup2[3]))
        self.play(n2label.animate.scale(0.8).next_to(ax2.get_x_axis().labels[0], direction=DOWN,aligned_edge=ORIGIN, buff=0.2),
            n4label.animate.scale(0.8).next_to(ax2.get_x_axis().labels[1], direction=DOWN,aligned_edge=ORIGIN, buff=0.2),
            n6label.animate.scale(0.8).next_to(ax2.get_x_axis().labels[2], direction=DOWN,aligned_edge=ORIGIN, buff=0.2),
            n8label.animate.scale(0.8).next_to(ax2.get_x_axis().labels[3], direction=DOWN,aligned_edge=ORIGIN, buff=0.2))

        others = VGroup(
            boxed_folge1, folge2Tex,
            n2label, n4label, n6label, n8label,
            DotGroup1[1], DotGroup1[3], DotGroup1[5], DotGroup1[7],
            DotGroup2, ax
        )

        # Alles außer dem Achsenkreuz ausblenden
        self.play(FadeOut(others))
        self.wait(1)



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


        # gerade Indices hervorheben (→ 1)
        gerade = [folgeDots[i] for i in range(1, 9, 2)]  # n=2,4,6,8
        self.play(FadeIn(folge3Tex1))
        self.play(*[d.animate.set_color(GREEN).scale(1.3) for d in gerade])

        # ungerade Indices hervorheben (→ -1)
        ungerade = [folgeDots[i] for i in range(0, 9, 2)]  # n=1,3,5,7,9
        self.play(FadeIn(folge3Tex2))
        self.play(*[d.animate.set_color(RED).scale(1.3) for d in ungerade])

        self.wait(2)

        # ========== SZENE 14 ==========

        # Definitionstext in drei Zeilen
        defHaeuf = VGroup(
            MathTex(r"\text{Sei } (a_n)_{n\in\mathbb{N}} \text{ eine Folge mit Teilfolge } (a_{n_k})_{k\in\mathbb{N}}.",
                    color=BLACK),
            MathTex(r"\text{Konvergiert } (a_{n_k})_{k\in\mathbb{N}} \text{ gegen einen Wert } a \in \mathbb{R},",
                    color=BLACK),
            MathTex(r"\text{so heißt } a \text{ \emph{Häufungspunkt} der Folge } (a_n)_{n\in\mathbb{N}}.", color=BLACK)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        
        self.play(FadeIn(dimmer))

        # Box mit runden Ecken und hellblauer Füllung
        box = SurroundingRectangle(
            defHaeuf,
            color=BLUE,
            buff=0.5,
            corner_radius=0.2
        ).set_fill(color=BLUE, opacity=0.3).set_z_index(100)  # höher als dimmer

        # Text selbst auch nach vorne holen
        defHaeuf.set_z_index(101)

        # Gruppe für Animation
        boxed_def_haeufungsPunkt = VGroup(box, defHaeuf).move_to(ORIGIN)

        self.play(FadeIn(boxed_def_haeufungsPunkt))
        self.wait(2)

        # Aufräumen für nächste Szene
        self.play(FadeOut(dimmer, boxed_folge3, ax, folgeDots, boxed_def_haeufungsPunkt, folge3Tex1, folge3Tex2))

        # ========== SZENE 15 ==========
        # Kein Bild, nur kurze Pause laut Bildspur
        self.wait(1)

        # ========== SZENE 16 ==========
        # ---------- Überschrift ----------
        folge1Tex = MathTex(r"a_n = 1 + \tfrac{1}{n}", color=BLACK).to_edge(UP * 2)
        box1 = SurroundingRectangle(folge1Tex, color=BLACK, buff=0.3, corner_radius=0.2)
        boxed_folge1 = VGroup(box1, folge1Tex)
        self.play(FadeIn(boxed_folge1))

        # ---------- Achsen ----------
        ax = Axes(
            x_range=[0, 12, 2],
            y_range=[0, 2.5, 0.5],
            tips=True,
            axis_config={"color": BLACK}
        ).shift(UP * 0.5)

        ax.get_x_axis().add_labels({i: MathTex(str(i), color=BLACK) for i in range(0, 13, 2)})
        ax.get_y_axis().add_labels({1: MathTex("a", color=BLACK)})

        self.play(Create(ax))

        # ---------- Folgepunkte ----------
        folgeDots = VGroup(*[Dot(ax.c2p(n, 1 + 1 / n), color=BLUE_E) for n in range(1, 13)])
        self.play(LaggedStartMap(FadeIn, folgeDots, lag_ratio=0.1))


        # ---------- ε-Umgebung ----------
        a = 1
        eps_start = 0.4
        eps_end = 0.15

        upper_start = ax.plot(lambda x: a + eps_start, x_range=[0.1, 12.1])
        lower_start = ax.plot(lambda x: a - eps_start, x_range=[0.1, 12.1])
        band_start = ax.get_area(upper_start, x_range=[0.1, 12.5], bounded_graph=lower_start,
                                 color=YELLOW, opacity=0.2)

        upper_end = ax.plot(lambda x: a + eps_end, x_range=[0.1, 12.1])
        lower_end = ax.plot(lambda x: a - eps_end, x_range=[0.1, 12.1])
        band_end = ax.get_area(upper_end, x_range=[0.1, 12.1], bounded_graph=lower_end,
                               color=YELLOW, opacity=0.2)

        self.play(FadeIn(band_start))
        self.wait(1)

        # ---------- N-Linie + Label ----------
        N_line = DashedLine(
            start=ax.c2p(3, 0),  # Start auf x-Achse bei N=3
            end=ax.c2p(3, 1.4),
            color=BLUE
        )
        N_label = MathTex("N", color=BLUE).next_to(ax.c2p(3, 0), DOWN * 1.5)  # etwas weiter nach unten

        self.play(Create(N_line), FadeIn(N_label))
        self.wait(1)

        # ---------- später verschieben (z. B. zu N=7) ----------
        new_line = DashedLine(
            start=ax.c2p(7, 0),
            end=ax.c2p(7, 1.15),
            color=BLUE
        )
        self.play(
            Transform(band_start, band_end),  # ε-Schlauch enger
            Transform(N_line, new_line),
            N_label.animate.next_to(ax.c2p(7, 0), DOWN * 1.5),
            run_time=2
        )
        self.wait(2)
        pos2 = MathTex(r"n", color=BLACK).move_to([4, 2.5, 0])

        folge4Tex1 = MathTex(r"n_k = 2k", color=GREEN).next_to(pos2, direction=DOWN, aligned_edge=LEFT).shift(
            RIGHT * 0.1)
        folge4Tex2 = MathTex(r"n_k = 2k - 1", color=RED).next_to(pos2, direction=DOWN, aligned_edge=LEFT).shift(
            DOWN * 0.7 + RIGHT * 0.1)
        folge4Tex3 = MathTex(r"n_k = k^2", color=PURPLE).next_to(pos2, direction=DOWN, aligned_edge=LEFT).shift(
            DOWN * 1.3 + RIGHT * 0.1)
        folge4Tex4 = MathTex(r"n_k = k", color=RED).next_to(pos2, direction=DOWN, aligned_edge=LEFT).shift(
            DOWN * 0.7 + RIGHT * 0.1)

        # ---------- Teilfolgen markieren ----------
        # n_k = 2k (gerade)
        geradeDots = VGroup(*[folgeDots[i] for i in range(1, 12, 2)])  # n=2,4,6,...
        self.play(geradeDots.animate.set_color(GREEN))
        self.play(FadeIn(folge4Tex1))
        self.wait(1)

        # n_k = 2k-1 (ungerade)
        ungeradeDots = VGroup(*[folgeDots[i] for i in range(0, 12, 2)])  # n=1,3,5,...
        self.play(ungeradeDots.animate.set_color(RED))
        self.play(FadeIn(folge4Tex2))
        self.wait(1)

        # n_k = k^2
        quadratDots = VGroup(*[folgeDots[k ** 2 - 1] for k in range(1, 4)])  # n=1,4,9
        self.play(quadratDots.animate.set_color(PURPLE))
        self.play(FadeIn(folge4Tex3))
        self.wait(2)

        # ---------- Aufräumen ----------
        self.play(
            FadeOut(band_start, N_line, N_label, folge4Tex1, folge4Tex2, folge4Tex3),
            folgeDots.animate.set_color(BLUE_E)  # alle Punkte zurückfärben
        )

        # n_k = k
        quadratDots = VGroup(*[folgeDots[k] for k in range(0, 12)])
        self.play(quadratDots.animate.set_color(RED))
        self.play(FadeIn(folge4Tex4))
        self.wait(2)
        self.play(FadeOut(ax, boxed_folge1, folgeDots, folge4Tex4))

        # ---------- Szene 24 ----------
        # Original-Aussage
        aussage_orig = MathTex(
            r"(a_n) \to a \;\;\Leftrightarrow\;\; \text{alle Teilfolgen } (a_{n_k}) \to a",
            color=BLACK
        ).scale(1).to_edge(UP)

        # Negierte Aussage
        neg_label = Tex("Negation:", color=RED).scale(1).next_to(aussage_orig, DOWN, buff=0.5)

        aussage_neg = MathTex(
            r"(a_n) \text{ divergiert } \;\;\Leftrightarrow\;\; \exists \text{ eine Teilfolge } (a_{n_k}) \text{ divergiert}",
            color=BLACK
        ).scale(1).next_to(neg_label, DOWN, buff=0.5)

        # Box um beide Aussagen
        box24 = SurroundingRectangle(
            VGroup(aussage_orig, aussage_neg),
            color=BLUE, corner_radius=0.2, buff=0.7
        ).set_fill(BLUE, opacity=0.2)

        group24 = VGroup(box24, aussage_orig, aussage_neg, neg_label).move_to(ORIGIN)


        self.play(FadeIn(box24))
        self.play(FadeIn(aussage_orig))
        self.wait(1)
        self.play(FadeIn(neg_label))
        self.wait(0.5)
        self.play(FadeIn(aussage_neg))
        self.wait(2)
        self.play(FadeOut(group24))

        # ---------- Szene 30 ----------
        # ---------- Folge-Formel oben ----------
        folge30Tex = MathTex(r"a_n = (-1)^n", color=BLACK).to_edge(UP * 2)
        box30 = SurroundingRectangle(folge30Tex, color=BLACK, buff=0.3, corner_radius=0.2)
        boxed_folge30 = VGroup(box30, folge30Tex)

        # Zuerst in der Mitte einblenden
        self.play(FadeIn(boxed_folge30))
        self.wait(0.5)

        # Dann leicht nach links verschieben

        # ---------- Achsen ----------
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[-1.5, 1.5, 1],
            tips=True,
            axis_config={"color": BLACK}
        ).shift(DOWN * 0.5)
        ax.get_x_axis().add_labels({i: MathTex(str(i), color=BLACK) for i in range(1, 10)})
        ax.get_y_axis().add_labels({-1: MathTex("-1", color=BLACK), 1: MathTex("1", color=BLACK)})
        self.play(Create(ax))

        # Folgepunkte
        folgeDots = VGroup()
        for n in range(1, 10):
            y = (-1) ** n
            d = Dot(ax.c2p(n, y), color=BLUE)
            folgeDots.add(d)
        self.play(LaggedStartMap(FadeIn, folgeDots, lag_ratio=0.1))

        self.play(boxed_folge30.animate.shift(LEFT * 1.8))

        # ---------- Teilfolge 1: n_k = 2k (rechts vom boxed_folge30) ----------
        folge30Tex1 = MathTex(r"n_k = 2k", color=GREEN).next_to(boxed_folge30, RIGHT, buff=1).shift(UP * 0.4)
        self.play(FadeIn(folge30Tex1))
        gerade = [folgeDots[i] for i in range(1, 9, 2)]  # n=2,4,6,8
        self.play(*[d.animate.set_color(GREEN) for d in gerade])

        # ---------- Teilfolge 2: n_k = 4k-3 (darunter, ebenfalls rechts) ----------
        folge30Tex2 = MathTex(r"n_k = 4k - 3", color=RED).next_to(folge30Tex1, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(folge30Tex2))
        teilfolge2 = [folgeDots[i] for i in [0, 4, 8]]  # n=1,5,9
        self.play(*[d.animate.set_color(RED) for d in teilfolge2])

        # Grenzwerte a=1 und b=-1 beschriften
        grenzwert_pos = MathTex("a=1", color=GREEN).next_to(ax.c2p(9.5, 1), RIGHT).shift(LEFT * 0.2)
        grenzwert_neg = MathTex("b=-1", color=RED).next_to(ax.c2p(9.5, -1), RIGHT).shift(LEFT * 0.2)
        self.play(FadeIn(grenzwert_pos), FadeIn(grenzwert_neg))

        self.wait(1)

        # Neue Teilfolge
        neue_teilfolge = [folgeDots[i] for i in [0,1,3,4,5,7,8]]  # gemischt ausgewählt
        self.play(*[d.animate.set_color(PURPLE) for d in neue_teilfolge])


        self.play( grenzwert_pos.animate.set_color(PURPLE), grenzwert_neg.animate.set_color(PURPLE))

        self.wait(2)

        # ---------- Aufräumen ----------
        self.play(
            FadeOut(
                boxed_folge30,
                ax,
                folgeDots,
                folge30Tex1,
                folge30Tex2,
                grenzwert_pos,
                grenzwert_neg
            )
        )
        self.wait(1.5)

        # ---------- Szene 31 ----------
        # Formel der Folge oben
        folge31Tex = MathTex(r"a_n = \tfrac{1}{4}n^3 - \tfrac{5}{2}n^2 + 7n - 4", color=BLACK).to_edge(UP * 2)
        box31 = SurroundingRectangle(folge31Tex, color=BLACK, buff=0.3, corner_radius=0.2)
        boxed_folge31 = VGroup(box31, folge31Tex)
        self.play(FadeIn(boxed_folge31))

        # Achsen
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[-10, 40, 5],
            tips=True,
            axis_config={"color": BLACK}
        ).shift(DOWN * 0.5)
        ax.get_x_axis().add_labels({i: MathTex(str(i), color=BLACK) for i in range(1, 10)})
        self.play(Create(ax))

        # Folgepunkte
        folgeDots = VGroup()
        for n in range(1, 10):
            y = 0.25 * n ** 3 - 2.5 * n ** 2 + 7 * n - 4
            d = Dot(ax.c2p(n, y), color=BLUE)
            folgeDots.add(d)

        self.play(LaggedStartMap(FadeIn, folgeDots, lag_ratio=0.1))

        self.wait(1)

        # Einige Werte "herausstreichen" (= ausblenden)
        to_remove = [folgeDots[i] for i in [0, 2, 4, 6]]  # z.B. die Punkte bei n=1,3,5,7

        # Punkte nacheinander verschwinden lassen
        self.play(LaggedStartMap(FadeOut, VGroup(*to_remove), lag_ratio=0.75))

        self.wait(2)

        # ---------- Aussage Divergenz ----------
        aussage_div = VGroup(
            MathTex(
                r"\text{Eine Folge } (a_n)_{n \in \mathbb{N}} \text{ divergiert genau dann,}",
                color=BLACK
            ),
            MathTex(
                r"\text{wenn eine Teilfolge } (a_{n_k})_{k \in \mathbb{N}} \text{ von } (a_n)_{n \in \mathbb{N}}",
                color=BLACK
            ),
            MathTex(
                r"\text{existiert, welche divergent ist.}",
                color=BLACK
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).scale(1)

        # Box mit runden Ecken und hellblauer Füllung
        box_div = SurroundingRectangle(
            aussage_div,
            color=BLUE,
            buff=0.5,
            corner_radius=0.2
        ).set_fill(color=BLUE, opacity=0.2).set_index(101)

        aussage_div.set_z_index(101)
        self.play(FadeIn(dimmer))

        boxed_aussage_div = VGroup(box_div, aussage_div).move_to(ORIGIN).set_z_index(101)

        # Animation
        self.play(FadeIn(boxed_aussage_div))
        self.wait(2)

        # Aufräumen: nur noch die verbleibenden Punkte + Achsen + Box
        remaining = VGroup(*[d for i, d in enumerate(folgeDots) if d not in to_remove])
        self.play(FadeOut(ax, remaining, boxed_folge31, boxed_aussage_div, dimmer))


