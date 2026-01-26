from manim import *
import math


class TeilfolgenS11(Scene):
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
        n2label = MathTex(r"n_1 = 2", color=RED_E).scale(0.7).next_to(ax.get_x_axis().labels[1], direction=DOWN,aligned_edge=ORIGIN, buff=0.2)
        # n_2 entspricht n=4: a_4 = 1 + 1/4 = 1.25
        n4label = MathTex(r"n_2 = 4", color=RED_E).scale(0.7).next_to(ax.get_x_axis().labels[3], direction=DOWN,aligned_edge=ORIGIN, buff=0.2)
        # n_3 entspricht n=6: a_6 = 1 + 1/6 ≈ 1.167
        n6label = MathTex(r"n_3 = 6", color=RED_E).scale(0.7).next_to(ax.get_x_axis().labels[5], direction=DOWN,aligned_edge=ORIGIN, buff=0.2)
        # n_4 entspricht n=8: a_8 = 1 + 1/8 = 1.125
        n8label = MathTex(r"n_4 = 8", color=RED_E).scale(0.7).next_to(ax.get_x_axis().labels[7], direction=DOWN,aligned_edge=ORIGIN, buff=0.2)
    
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

        self.wait(2) 

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

        folge3Tex = MathTex(r"(a_{2k})_{", r"k\in\mathbb{N}", r"}", color=BLACK).next_to(folge2Tex,direction=DOWN,aligned_edge=LEFT)
        self.play(FadeIn(folge3Tex))
        self.wait(1)
        self.play(Indicate(folge3Tex[1], color=RED, scale_factor=1.3))

        
        others = VGroup(
            boxed_folge1, folge2Tex,folge3Tex,
            n2label, n4label, n6label, n8label,
            DotGroup1[1], DotGroup1[3], DotGroup1[5], DotGroup1[7],
            DotGroup2, ax
        )

        # Alles außer dem Achsenkreuz ausblenden
        self.play(FadeOut(others))
        self.wait(2)



