from manim import *


class Sprache_S1(Scene): 

    def construct(self):
        self.camera.background_color = WHITE

        zielposition = np.array([5.5, 2.75, 0])

        # -----------------------------
        # Titelkarte: Vier Prinzipien
        # -----------------------------

        titel = Tex(
            r"\textbf{Sprache im Mathematikunterricht}",
            color=BLACK
        ).scale(1.1)

        untertitel = Tex(
            r"Vier Prinzipien sprachbildenden Unterrichts",
            color=BLACK
        ).scale(0.8)

        # --- Icons statt Kacheln ---
        ICON1_PATH = "media/images/Icon 1.png"
        ICON2_PATH = "media/images/Icon 2.png"
        ICON3_PATH = "media/images/Icon 3.png"
        ICON4_PATH = "media/images/Icon 4.png"

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

        self.play(FadeIn(titel, shift=DOWN), run_time=1.5)
        self.play(FadeIn(untertitel), run_time=1)
        self.wait(1)

        for k in [k1, k2, k3, k4]:
            self.play(FadeIn(k, shift=RIGHT * 0.2), run_time=0.5)

        self.wait(2)

        titelkarte = Group(titel, untertitel, k1, k2, k3, k4)

        # # -----------------------------
        # # Hervorhebung: Makro-Scaffolding
        # # -----------------------------
        # self.play(
        #     k1.animate.scale(1.1),
        #     run_time=0.4
        # )
        # self.play(
        #     k1.animate.scale(1.0),
        #     run_time=0.3
        # )
        # self.wait(1)

        # # Alles, was verschwinden soll (außer k1)
        # alles_andere = Group(
        #     titel,
        #     untertitel,
        #     k2,
        #     k3,
        #     k4
        # )
        # # parallele Bewegung + Ausblenden
        # self.play(
        #     k1.animate.move_to(zielposition).scale(0.8),
        #     FadeOut(alles_andere),
        #     run_time=1.6,
        #     rate_func=smooth
        # )

        # self.wait(1.5)
