from manim import *


class Sprache_S2_1(Scene):

    def construct(self):
        # Configuration
        self.camera.background_color = WHITE

        # Farben (nah am Screenshot)
        c_alltag = ManimColor("#8c0f3d")
        c_bildung = ManimColor("#5a215c")
        c_fach = ManimColor("#00205b")

        # Geometrie
        h = 1.4  # Höhe des Strahls
        w = 4.0  # Breite je Segment (ohne Spitze)
        tip = 1.0  # Tiefe der Pfeilspitze / Einkerbung
        x0 = -6.0  # Start links

        y_top = h / 2
        y_bot = -h / 2

        # ---------- Segmente ----------
        # 1) Alltagssprache (links, ohne Einkerbung)
        seg1 = (
            Polygon(
                [x0, y_top, 0],
                [x0 + w, y_top, 0],
                [x0 + w + tip, 0, 0],
                [x0 + w, y_bot, 0],
                [x0, y_bot, 0],
            )
            .set_fill(c_alltag, 1)
            .set_stroke(width=0)
        )

        # 2) Bildungssprache (mit linker Einkerbung + rechter Spitze)
        x1 = x0 + w
        seg2 = (
            Polygon(
                [x1, y_top, 0],
                [x1 + w, y_top, 0],
                [x1 + w + tip, 0, 0],
                [x1 + w, y_bot, 0],
                [x1, y_bot, 0],
                [x1 + tip, 0, 0],
            )
            .set_fill(c_bildung, 1)
            .set_stroke(width=0)
        )

        # 3) Fachsprache (mit linker Einkerbung + finaler Spitze)
        x2 = x1 + w
        seg3 = (
            Polygon(
                [x2, y_top, 0],
                [x2 + w, y_top, 0],
                [x2 + w + tip, 0, 0],
                [x2 + w, y_bot, 0],
                [x2, y_bot, 0],
                [x2 + tip, 0, 0],
            )
            .set_fill(c_fach, 1)
            .set_stroke(width=0)
        )

        # ---------- Trennlinien (weiße "Chevron"-Knicke) ----------
        # zwischen Segment 1 und 2
        div1_a = Line([x1, y_top, 0], [x1 + tip, 0, 0], color=WHITE, stroke_width=3)
        div1_b = Line([x1 + tip, 0, 0], [x1, y_bot, 0], color=WHITE, stroke_width=3)

        # zwischen Segment 2 und 3
        div2_a = Line([x2, y_top, 0], [x2 + tip, 0, 0], color=WHITE, stroke_width=3)
        div2_b = Line([x2 + tip, 0, 0], [x2, y_bot, 0], color=WHITE, stroke_width=3)

        # ---------- Labels ----------
        t1 = (
            Tex(r"\textbf{Alltagssprache}", color=WHITE)
            .scale(0.75)
            .move_to(seg1.get_center() + LEFT * 0.2)
        )
        t2 = (
            Tex(r"\textbf{Bildungssprache}", color=WHITE)
            .scale(0.75)
            .move_to(seg2.get_center() + RIGHT * 0.1)
        )
        t3 = (
            Tex(r"\textbf{Fachsprache}", color=WHITE)
            .scale(0.75)
            .move_to(seg3.get_center() + LEFT * 0.10)
        )

        # Gesamtgruppe zentrieren
        strahl = VGroup(seg1, seg2, seg3, div1_a, div1_b, div2_a, div2_b, t1, t2, t3)
        strahl.move_to(ORIGIN)

        # Helper: one rounded card with label
        def make_card(pos, text):
            box = RoundedRectangle(
                corner_radius=0.16,
                width=3.5,
                height=1.2,
                fill_color=ManimColor("#f2f2f2"),
                fill_opacity=1,
                stroke_color=ManimColor("#c7c7c7"),
                stroke_width=2,
            )
            label = Tex(text, color=BLACK).scale(0.7).move_to(box.get_center())
            return VGroup(box, label).move_to(pos)

        # 5 cards in different positions
        card_f_1 = make_card(LEFT * 4.5 + UP * 2.5, text=r"Fachliche\\Lerngelegenheit")
        card_f_2 = make_card(ORIGIN + UP * 2.5, text=r"Fachliche\\Lerngelegenheit")
        card_f_3 = make_card(RIGHT * 4.5 + UP * 2.5, text=r"Fachliche\\Lerngelegenheit")
        card_s_1 = make_card(
            LEFT * 2 + DOWN * 2.5, text=r"Sprachliche\\Lerngelegenheit"
        )
        card_s_2 = make_card(
            RIGHT * 3 + DOWN * 2.5, text=r"Sprachliche\\Lerngelegenheit"
        )

        # Helper: one curved arrow
        def make_arrow(
            start_obj,
            end_obj,
            start_dir=DOWN,
            end_dir=UP,
            angle=1.1,
            start_shift=ORIGIN,
            end_shift=ORIGIN,
        ):
            return CurvedArrow(
                start_point=start_obj.get_edge_center(start_dir)
                + start_dir * 0.05
                + start_shift,
                end_point=end_obj.get_edge_center(end_dir) + end_dir * 0.05 + end_shift,
                angle=angle,
                color=ManimColor("#0996d7"),
                stroke_width=7,
                tip_length=0.25,
            )

        # Arrows
        arrow_1 = make_arrow(card_f_1, seg1, start_dir=DOWN, end_dir=UP, angle=1.2)
        arrow_2 = make_arrow(
            seg1,
            card_s_1,
            start_dir=DOWN,
            end_dir=UP,
            angle=1,
            start_shift=RIGHT * 0.35,
            end_shift=LEFT * 0.5,
        )
        arrow_3 = make_arrow(seg2, card_f_2, start_dir=UP, end_dir=DOWN, angle=-1.1)
        arrow_4 = make_arrow(
            seg2,
            card_s_2,
            start_dir=DOWN,
            end_dir=UP,
            angle=0.6,
            start_shift=RIGHT * 0.5,
            end_shift=LEFT * 0.7,
        )
        arrow_5 = make_arrow(seg3, card_f_3, start_dir=UP, end_dir=DOWN, angle=-1.1)

        # ---------- Animation (nacheinander) ----------
        self.play(FadeIn(card_f_1), run_time=1)
        self.wait(1)

        self.play(Create(arrow_1), run_time=1)

        self.play(FadeIn(seg1), FadeIn(t1), run_time=1)
        self.wait(1)

        self.play(Create(arrow_2), run_time=1)

        self.play(FadeIn(card_s_1), run_time=1)
        self.wait(1)

        self.play(FadeIn(seg2), Create(div1_a), Create(div1_b), FadeIn(t2), run_time=1)
        self.wait(1)

        self.play(Create(arrow_3), run_time=1)

        self.play(FadeIn(card_f_2), run_time=1)
        self.wait(1)

        self.play(Create(arrow_4), run_time=1)

        self.play(FadeIn(card_s_2), run_time=1)
        self.wait(1)

        self.play(FadeIn(seg3), Create(div2_a), Create(div2_b), FadeIn(t3), run_time=1)
        self.wait(1)

        self.play(Create(arrow_5), run_time=1)

        self.play(FadeIn(card_f_3), run_time=1)
        self.wait(1)
