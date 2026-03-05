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

        # ---------- Animation (nacheinander) ----------
        self.play(FadeIn(seg1), FadeIn(t1), run_time=0.9)
        self.wait(0.5)

        self.play(FadeIn(seg2), Create(div1_a), Create(div1_b), FadeIn(t2), run_time=0.9)
        self.wait(0.5)

        self.play(FadeIn(seg3), Create(div2_a), Create(div2_b), FadeIn(t3), run_time=0.9)
        self.wait(3.5)

        # -----------------------------
        # Sprechblasen als PNGs + Text
        # -----------------------------

        # Ankerpunkte (wo die Blasen "rauswachsen" sollen)
        anchor_alltag = seg1.get_top() + LEFT * 1.0
        anchor_fach = seg3.get_top() + RIGHT * 0.6

        # --- Blase 1: Alltagssprache ---
        bubble1_img = ImageMobject("media/images/speechBubble_alltag.png").set_z_index(5)
        bubble1_img.scale(0.425)
        bubble1_img.next_to(seg1, UP, buff=0.1).shift(RIGHT * 0.5)

        bubble1_text = Tex(
            r"``Wenn die Ableitung",
            r"positiv ist, geht die Kurve",
            r"nach oben''",
            color=WHITE
        ).scale(0.6)
        bubble1_text.arrange(DOWN, buff=0.15)
        bubble1_text.move_to(bubble1_img.get_center()).shift(UP * 0.25).set_z_index(6)

        bubble1 = Group(bubble1_img, bubble1_text)

        self.play(GrowFromPoint(bubble1_img, anchor_alltag), run_time=0.9)
        self.play(FadeIn(bubble1_text), run_time=0.3)
        self.wait(2.3)

        # --- Blase 2: Fachsprache ---
        bubble2_img = ImageMobject("media/images/SpeechBubble_fach.png").set_z_index(5)
        bubble2_img.scale(0.425)
        bubble2_img.next_to(seg3, DOWN, buff=0.1).shift(RIGHT * 0.5)

        bubble2_text = Tex(
            r"`` Wenn $f'(x_0) > 0$ gilt,",
            r" ist der Graph von, $f$ in einer ",
            r"Umgebung von $x_0$ streng",
            r" monoton steigend.''",
            color=WHITE
        ).scale(0.6)
        bubble2_text.arrange(DOWN, buff=0.135)
        bubble2_text.move_to(bubble2_img.get_center()).shift(DOWN * 0.35 + RIGHT * 0.08).set_z_index(6)

        bubble2 = Group(bubble2_img, bubble2_text)
        # -----------------------------
        # Sammelgruppe für späteres Ausblenden
        # -----------------------------
        strahl_gruppe = Group(
            seg1, seg2, seg3,
            div1_a, div1_b,
            div2_a, div2_b,
            t1, t2, t3
        )

        sprechblasen_gruppe = Group(
            bubble1,
            bubble2
        )

        self.play(GrowFromPoint(bubble2_img, anchor_fach), run_time=0.9)
        self.play(FadeIn(bubble2_text), run_time=0.3)
        self.wait(2.5)

        # -----------------------------
        # Szene aufräumen für nächste Inhalte
        # -----------------------------
        self.wait(0.8)

        self.play(
            FadeOut(strahl_gruppe),
            FadeOut(sprechblasen_gruppe),
            run_time=1.4
        )

        self.wait(2)

       

