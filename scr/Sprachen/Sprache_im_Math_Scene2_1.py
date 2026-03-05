from manim import *

class Sprache_S2_1(Scene): 

    def construct(self):
        # Configuration
        self.camera.background_color = WHITE

        # Farben (nah am Screenshot)
        c_alltag = ManimColor("#8c0f3d")
        c_bildung = ManimColor("#5a215c")
        c_fach = ManimColor("#00205b")
        c_arrow = ManimColor("#0996d7")
        c_card = ManimColor("#f2f2f2")

        # Geometrie
        h = 1.4  # Höhe des Strahls
        w = 4.0  # Breite je Segment (ohne Spitze)
        tip = 1.0  # Tiefe der Pfeilspitze / Einkerbung
        x0 = -6.0  # Start links

        y_top = h / 2
        y_bot = -h / 2

        # ---------- Segmente ----------
        # 1) Alltagssprache (links, ohne Einkerbung)
        seg1 = Polygon(
            [x0, y_top, 0],
            [x0 + w, y_top, 0],
            [x0 + w + tip, 0, 0],
            [x0 + w, y_bot, 0],
            [x0, y_bot, 0],
        ).set_fill(c_alltag, 1).set_stroke(width=0)

        # 2) Bildungssprache (mit linker Einkerbung + rechter Spitze)
        x1 = x0 + w
        seg2 = Polygon(
            [x1, y_top, 0],
            [x1 + w, y_top, 0],
            [x1 + w + tip, 0, 0],
            [x1 + w, y_bot, 0],
            [x1, y_bot, 0],
            [x1 + tip, 0, 0],
        ).set_fill(c_bildung, 1).set_stroke(width=0)

        # 3) Fachsprache (mit linker Einkerbung + finaler Spitze)
        x2 = x1 + w
        seg3 = Polygon(
            [x2, y_top, 0],
            [x2 + w, y_top, 0],
            [x2 + w + tip, 0, 0],
            [x2 + w, y_bot, 0],
            [x2, y_bot, 0],
            [x2 + tip, 0, 0],
        ).set_fill(c_fach, 1).set_stroke(width=0)

        # ---------- Trennlinien (weiße "Chevron"-Knicke) ----------
        # zwischen Segment 1 und 2
        div1_a = Line([x1, y_top, 0], [x1 + tip, 0, 0], color=WHITE, stroke_width=3)
        div1_b = Line([x1 + tip, 0, 0], [x1, y_bot, 0], color=WHITE, stroke_width=3)

        # zwischen Segment 2 und 3
        div2_a = Line([x2, y_top, 0], [x2 + tip, 0, 0], color=WHITE, stroke_width=3)
        div2_b = Line([x2 + tip, 0, 0], [x2, y_bot, 0], color=WHITE, stroke_width=3)

        # ---------- Labels ----------
        t1 = Tex(r"\textbf{Alltagssprache}", color=WHITE).scale(0.75).move_to(seg1.get_center() + LEFT * 0.2)
        t2 = Tex(r"\textbf{Bildungssprache}", color=WHITE).scale(0.75).move_to(seg2.get_center() + RIGHT * 0.1)
        t3 = Tex(r"\textbf{Fachsprache}", color=WHITE).scale(0.75).move_to(seg3.get_center() + LEFT * 0.10)

        # Gesamtgruppe zentrieren
        strahl = VGroup(seg1, seg2, seg3, div1_a, div1_b, div2_a, div2_b, t1, t2, t3)
        strahl.move_to(ORIGIN)


        box = RoundedRectangle(
            corner_radius=0.16,
            width=4,
            height=1.2,
            fill_color=LIGHTER_GRAY,
            fill_opacity=1,
            stroke_color=DARK_GRAY,
            stroke_width=2,
        )
        label = Tex(r"Fachliche\\Lerngelegenheit", color=BLACK).scale(0.7).move_to(box.get_center())
        card = VGroup(box, label).move_to(UP * 2.5)  # top row position

        # ---------- Animation (nacheinander) ----------
        self.play(FadeIn(box), FadeIn(label), run_time=1)

        self.play(FadeIn(seg1), FadeIn(t1), run_time=1)
        self.wait(1)

        self.play(FadeIn(seg2), Create(div1_a), Create(div1_b), FadeIn(t2), run_time=1)
        self.wait(1)

        self.play(FadeIn(seg3), Create(div2_a), Create(div2_b), FadeIn(t3), run_time=1)
        self.wait(4)




       

