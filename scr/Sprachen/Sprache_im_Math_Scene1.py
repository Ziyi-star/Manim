from manim import *


class Sprache_S1(Scene): 

    def construct(self):
        # Configuration
        self.camera.background_color = WHITE
        ICON1_PATH = "media/images/Icon 1.png"
        ICON2_PATH = "media/images/Icon 2.png"
        ICON3_PATH = "media/images/Icon 3.png"
        ICON4_PATH = "media/images/Icon 4.png"
        zielposition = np.array([5.5, 2.75, 0])

        #######################################################################
        # Scene 1.1 - Titelkarte mit Prinzipien
        # Titelkarte: Vier Prinzipien
        titel = Tex(
            r"\textbf{Sprache im Mathematikunterricht}",
            color=BLACK
        ).scale(1.1)

        untertitel = Tex(
            r"Vier Prinzipien sprachbildenden Unterrichts",
            color=BLACK
        ).scale(0.8)

        # --- Icons statt Kacheln ---
        k1 = ImageMobject(ICON1_PATH)
        k2 = ImageMobject(ICON2_PATH)
        k3 = ImageMobject(ICON3_PATH)
        k4 = ImageMobject(ICON4_PATH)

        for k in [k1, k2, k3, k4]:
            k.set_height(2.5)

        # Alle vier Icons in einer Zeile
        prinzipien_grid = Group(k1, k2, k3, k4).arrange(
            RIGHT,
            buff=0.2,
            aligned_edge=DOWN
        )

        # Startpositionen sichern
        k1_start = k1.get_center()
        k2_start = k2.get_center()
        k3_start = k3.get_center()
        k4_start = k4.get_center()

        titel_group = Group(titel, untertitel).arrange(DOWN, buff=0.3).shift(UP * 2)
        prinzipien_grid.next_to(titel_group, DOWN, buff=1.3)

        titelkarte = Group(titel, untertitel, k1, k2, k3, k4)

        # Play animations
        self.play(FadeIn(titel, shift=DOWN), run_time=1.5)
        self.play(FadeIn(untertitel), run_time=1)
        self.wait(1)

        for k in [k1, k2, k3, k4]:
            self.play(FadeIn(k, shift=RIGHT * 0.2), run_time=0.5)
        self.wait(2)

        self.play(
            titelkarte.animate.scale(0.6).shift(UP * 2),
            run_time=1.5
        )
        self.wait(1)

        ###############################################################################
        # Scene 1.2 - Prinzipien in Aktion

        # Nur zur schnellen Komplilieren: Titelkarte nach oben verschieben und Größe reduzieren
        # titelkarte = Group(titel, untertitel, k1, k2, k3, k4)
        # titelkarte.scale(0.7).shift(UP * 2)
        # self.add(titelkarte)
        # self.wait(1)

        # Brace unter allen vier Icons
        brace_bottom = Brace(prinzipien_grid, DOWN, color=BLACK)

        # Text unter dem Brace
        text_1 = Tex("Auf Beispiele anwenden", color=BLACK).scale(0.7)
        text_1.next_to(brace_bottom, DOWN, buff=0.3).shift(LEFT * 3)
        text_2 = Tex(r"Mathematischer \textbf{Kern} der Aufgabe", color=BLACK).scale(0.65)
        text_2.next_to(text_1, DOWN*4, buff=0.3).shift(RIGHT * 3)

        # Pfeil von text 1 zu text 2 (Step 1)
        arrow1 = CurvedArrow(text_1.get_bottom(), text_2.get_left(), color=MAROON_D, stroke_width=4)
        label1 = VGroup(
            Tex("1. Basis", color=BLACK).scale(0.6),
        ).next_to(arrow1.get_center(), RIGHT, buff=0.1)

        # Pfeil von Kern zu Prinzip (Step 2)
        text_3 = Tex(r"Aufgabe bedient \textbf{Prinzip}", color=BLACK).scale(0.65)
        text_3.next_to(text_2, DOWN*4, buff=0.3).shift(RIGHT * 3)

        # Pfeil von text 2 zu text 3 (Step 2)
        arrow2 = CurvedArrow(text_2.get_bottom(), text_3.get_left(), color=MAROON_D, stroke_width=4)
        label2 = VGroup(
            Tex("2. anpassen", color=BLACK).scale(0.6),
        ).next_to(arrow2.get_center(), RIGHT, buff=0.1)


        # Play animations
        self.play(FadeIn(brace_bottom), run_time=1)
        self.play(FadeIn(text_1), run_time=1)
        self.play(Create(arrow1), FadeIn(label1), run_time=1)
        self.play(FadeIn(text_2), run_time=1)
        self.play(Create(arrow2), FadeIn(label2), run_time=1)
        self.play(FadeIn(text_3), run_time=1)
        self.wait(2)

