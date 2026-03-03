from manim import *


class Sprache_S0(Scene): 

    def construct(self):
        self.camera.background_color = "#0090d4"

        def notes_box(notes, buff=0.25, corner_radius=0.2):
            # Schatten (leicht nach rechts-unten versetzt)
            shadow = SurroundingRectangle(
                notes,
                buff=buff,
                corner_radius=corner_radius,
                stroke_width=0,
                fill_color=BLACK,
                fill_opacity=0.18,
            ).shift(RIGHT * 0.08 + DOWN * 0.08)

            # Vordergrund-Box
            box = SurroundingRectangle(
                notes,
                buff=buff,
                corner_radius=corner_radius,
                stroke_color=BLACK,
                stroke_width=2,
                fill_color=WHITE,
                fill_opacity=1,
            )

            return Group(shadow, box, notes)

        BG_PATH = "media/images/tafelbild.png"
        bg = ImageMobject(BG_PATH).set_z_index(-10).scale(0.4364)

        self.play(FadeIn(bg), run_time=0.8)

        HAND_FONT = 'Agency FB'

        # ---------- Block 1: Aufgabenstellung ----------
        aufgabe_zeilen = VGroup(
            Text("Aufgabe:", font=HAND_FONT, weight=BOLD, color=BLACK),
            Text(
                "Erläutern Sie, ob die gegebene Funktion einen Wendepunkt hat",
                font=HAND_FONT,
                color=BLACK
            ),
            Text(
                "und diskutieren Sie das Krümmungsverhalten des Graphen ...",
                font=HAND_FONT,
                color=BLACK
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).scale(0.6)

        # ---------- Block 2: Erklärung (in 3 Teilen) ----------
        erklaerung_part1 = VGroup(
            Text("Wir bestimmen die Ableitungen: ...", font=HAND_FONT, color=BLACK),
            Text("und untersuchen die Funktion auf Wendepunkte.", font=HAND_FONT, color=BLACK),
            Text(
                "In x₁ liegt ein Wendepunkt vor, weil die zweite Ableitung",
                font=HAND_FONT,
                color=BLACK
            ),
            Text(
                "an dieser Stelle ihr Vorzeichen wechselt.",
                font=HAND_FONT,
                color=BLACK
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).scale(0.6)

        # ---------- Teil 2: Punkte ----------
        erklaerung_part2 = VGroup(
            Text("...", font=HAND_FONT, color=BLACK),
        ).arrange(DOWN, buff=0.35).scale(0.6)

        # ---------- Teil 3 ----------
        erklaerung_part3 = VGroup(
            Text(
                "Weil f''(x) auf diesem Intervall nur Werte größer Null annimmt,",
                font=HAND_FONT,
                color=BLACK
            ),
            Text(
                "ist f dort konvex, d. h. die Tangentensteigung ...",
                font=HAND_FONT,
                color=BLACK
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).scale(0.6)

        # ---------- Layout ----------
        block = VGroup(
            aufgabe_zeilen,
            erklaerung_part1,
            erklaerung_part2,
            erklaerung_part3
        ).arrange(DOWN, buff=0.65, aligned_edge=LEFT)

        # Teil 2 mittig unter Teil 1
        erklaerung_part2.move_to(
            [erklaerung_part1.get_center()[0] + 0.5,
            erklaerung_part2.get_center()[1],
            0]
        )
        erklaerung_part2.shift(UP * 0.2)
        erklaerung_part3.shift(UP * 0.4)

        # Gesamtblock zentrieren
        block.scale(0.6)
        block.move_to(ORIGIN).shift(UP * 0.6)

        aufgabe_box = SurroundingRectangle(
            aufgabe_zeilen,
            corner_radius=0.25,
            buff=0.15,
            stroke_color=BLACK,
            stroke_width=2,
            fill_opacity=0
        )

        # ---------- Animation ----------
        self.play(Write(aufgabe_zeilen), FadeIn(aufgabe_box), run_time=3)
        self.wait(0.5)

        self.play(Write(erklaerung_part1), run_time=3.2)
        self.wait(0.4)

        self.play(FadeIn(erklaerung_part2), run_time=0.8)
        self.wait(0.4)

        self.play(Write(erklaerung_part3), run_time=2.2)
        self.wait(2)

        # Übergang zur Titelkarte
        self.play(FadeOut(block, bg, aufgabe_box), run_time=1.5)
        self.camera.background_color = WHITE