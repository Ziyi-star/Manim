from manim import *
import math


class TeilfolgenOne(Scene):
    def construct(self):
        # Weißer Hintergrund für bessere Sichtbarkeit
        self.camera.background_color = WHITE
        
        # ========== SZENE 11: Teilfolgen-Demonstration ==========

        # Formel der ursprünglichen Folge: a_n = 1 + 1/n
        folge1Tex = MathTex(r"a_n=1+\frac{1}{n}", color=BLACK).to_edge(UP * 2)

        # Box mit runden Ecken um den Text
        box1 = SurroundingRectangle(
            folge1Tex,
            color=BLACK,
            buff=0.3,  # Abstand Text ↔ Box
            corner_radius=0.2  # Rundung der Ecken
        )

        # Formel und Box zusammen gruppieren für gemeinsame Animationen
        boxed_folge1 = VGroup(box1, folge1Tex)

        # Koordinatensystem erstellen
        # x-Achse: n von 0 bis 9 (Folgenindex)
        # y-Achse: Werte von 0 bis 2.5 mit Markierungen bei 0.5er-Schritten
        ax = Axes(
                x_range=[0, 9],
                y_range=[0, 2.5, 0.5],
                y_axis_config={"numbers_to_include": [0,0.5,1,1.5,2]},
                tips=True,  # Achsenspitzen anzeigen
                axis_config={
                        'color' : BLACK}
            ).shift(UP*0.5)
        xAxis = ax.get_x_axis()
        
        # Beschriftung der x-Achse mit n=1, n=2, ..., n=8
        ax.get_x_axis().add_labels(dict_values={i : MathTex(r"n="+str(i), color=BLACK) for i in range(1,9)})

        # y-Achsen-Zahlen schwarz färben
        ax.get_y_axis().numbers.set_color(BLACK)

        # Einblenden der Formel und des Koordinatensystems
        self.play(FadeIn(boxed_folge1))
        self.play(FadeIn(ax))

        # Gruppe für alle Folgenpunkte erstellen
        DotGroup1 = VGroup()

        # Punkte für n = 1 bis 8 berechnen und zur Gruppe hinzufügen
        # Formel: a_n = 1 + 1/n
        for i in range(1,9):
            d = Dot(ax.c2p(i,1+1/i),color=BLUE_E)  # c2p = coordinates to point
            DotGroup1.add(d)
        
        # Alle Punkte nacheinander einblenden (von links nach rechts)
        self.play(ShowIncreasingSubsets(DotGroup1), run_time=2, rate_functions=linear)

        # Platzhalter-Text und Formel für die Teilfolge
        pos = MathTex(r"n", color=BLACK).move_to([4, 1.5, 0])
        folge2Tex = MathTex(r"n_k = 2k", color=RED).next_to(pos,direction=DOWN,aligned_edge=LEFT)

        # Formel der Teilfolge einblenden (nur gerade Indizes)
        self.play(FadeIn(folge2Tex))

        # Labels für die ausgewählten Teilfolgenpunkte erstellen
        # n_1 entspricht n=2: a_2 = 1 + 1/2 = 1.5
        n2label = MathTex(r"n_1 = 1.5", color=RED_E).scale(0.7).next_to(ax.get_x_axis().labels[1], direction=DOWN,aligned_edge=ORIGIN, buff=0.2)
        # n_2 entspricht n=4: a_4 = 1 + 1/4 = 1.25
        n4label = MathTex(r"n_2 = 1.25", color=RED_E).scale(0.7).next_to(ax.get_x_axis().labels[3], direction=DOWN,aligned_edge=ORIGIN, buff=0.2)
        # n_3 entspricht n=6: a_6 = 1 + 1/6 ≈ 1.167
        n6label = MathTex(r"n_3 = 1.167", color=RED_E).scale(0.7).next_to(ax.get_x_axis().labels[5], direction=DOWN,aligned_edge=ORIGIN, buff=0.2)
        # n_4 entspricht n=8: a_8 = 1 + 1/8 = 1.125
        n8label = MathTex(r"n_4 = 1.125", color=RED_E).scale(0.7).next_to(ax.get_x_axis().labels[7], direction=DOWN,aligned_edge=ORIGIN, buff=0.2)

        # Punkt bei n=2 hervorheben (vergrößern und rot färben) und Label anzeigen
        self.play(DotGroup1[1].animate.scale(2).set_color(RED_E))
        self.play(FadeIn(n2label))
        # Punkt bei n=4 hervorheben und Label anzeigen
        self.play(DotGroup1[3].animate.scale(2).set_color(RED_E))
        self.play(FadeIn(n4label))
        # Punkt bei n=6 hervorheben und Label anzeigen
        self.play(DotGroup1[5].animate.scale(2).set_color(RED_E))
        self.play(FadeIn(n6label))
        # Punkt bei n=8 hervorheben und Label anzeigen
        self.play(DotGroup1[7].animate.scale(2).set_color(RED_E))
        self.play(FadeIn(n8label))

        # Alle ungeraden Indizes ausblenden (n=1, 3, 5, 7)
        # nur die geraden Indizes (n=2, 4, 6, 8) bleiben sichtbar
        self.play(FadeOut(DotGroup1[0],DotGroup1[2],DotGroup1[4],DotGroup1[6]))

        self.wait(1)  

        # Ungerade Punkte blinken lassen
        self.play(
            Indicate(DotGroup1[1], color=RED_E, scale_factor=1.5),
            Indicate(DotGroup1[3], color=RED_E, scale_factor=1.5),
            Indicate(DotGroup1[5], color=RED_E, scale_factor=1.5),
            Indicate(DotGroup1[7], color=RED_E, scale_factor=1.5),
            run_time=1.5
        )

        self.wait(2)  # Kurze Pause am Ende


