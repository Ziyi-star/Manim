from manim import *


class Sprache_im_Mathematikunterricht(Scene):

    def construct(self):

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

        # -----------------------------
        # Hervorhebung: Makro-Scaffolding
        # -----------------------------
        self.play(
            k1.animate.scale(1.1),
            run_time=0.4
        )
        self.play(
            k1.animate.scale(1.0),
            run_time=0.3
        )
        self.wait(1)

        # Alles, was verschwinden soll (außer k1)
        alles_andere = Group(
            titel,
            untertitel,
            k2,
            k3,
            k4
        )
        # parallele Bewegung + Ausblenden
        self.play(
            k1.animate.move_to(zielposition).scale(0.8),
            FadeOut(alles_andere),
            run_time=1.6,
            rate_func=smooth
        )

        self.wait(1.5)

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

        blue = ManimColor("#1f5aa6")

        # Zentralbegriffe
        u_plan = Tex(r"\textbf{Unterrichtsplanung}", color=BLACK).scale(0.95)
        s_hand = Tex(r"\textbf{Sprachhandlungen}", color=BLACK).scale(0.95)

        core = VGroup(u_plan, s_hand).arrange(DOWN, buff=0.8).move_to(ORIGIN)

        # Verschränkte Pfeile (zwei Richtungen)
        # Pfeil 1: oben -> unten (rechts herum)
        a1 = CurvedArrow(
            start_point=u_plan.get_right() + RIGHT * 0.2,
            end_point=s_hand.get_right() + RIGHT * 0.2,
            angle=-TAU / 2.3,
            color=BLACK,
            stroke_width=6,
            tip_length=0.18,
        )

        # Pfeil 2: unten -> oben (links herum)
        a2 = CurvedArrow(
            start_point=s_hand.get_left() + LEFT * 0.2,
            end_point=u_plan.get_left() + LEFT * 0.2,
            angle=-TAU / 2.3,
            color=BLACK,
            stroke_width=6,
            tip_length=0.18,
        )

        # Beispielbegriffe um die Pfeile herum
        ex1 = Tex(r"Aufgaben formulieren", color=BLACK).scale(0.8)
        ex2 = Tex(r"Begründungen einfordern", color=BLACK).scale(0.8)
        ex3 = Tex(r"sprachliche Hilfestellungen\\formulieren", color=BLACK).scale(0.8)

        # Positionen
        ex2.next_to(u_plan, UP, buff=0.6)
        ex1.next_to(a1, DOWN, buff=0.6).shift(RIGHT * 1.8)
        ex3.next_to(a2, DOWN, buff=0.8).shift(LEFT * 1.6)

        # Animation
        self.play(Write(u_plan), run_time=1.0)
        self.play(Write(s_hand), run_time=1.0)

        self.play(Create(a1), Create(a2), run_time=1.2)
        self.wait(1)

        self.play(FadeIn(ex2, shift=UP * 0.15), run_time=0.7)
        self.wait(1)
        self.play(FadeIn(ex1, shift=UP * 0.15), run_time=0.7)
        self.wait(1)
        self.play(FadeIn(ex3, shift=UP * 0.15), run_time=0.7)

        self.wait(1.5)

        # Layout: Grafik oben, Aufgabenblock unten
        grafik = Group(core, a1, a2, ex1, ex2, ex3)
        self.play(FadeOut(grafik))

        # Notizen darunter (erscheinen passend zur Sprecherin)
        note1 = Tex(r"- Schrittweise Sprachentwicklung", color=blue).scale(0.7)
        note2 = Tex(r"- Spontane Unterstützung durch Impulse", color=blue).scale(0.7)
        notes_1 = VGroup(note1, note2).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        notes_1.move_to(np.array([0, 1.4, 0]))
        notes_1_boxed = notes_box(notes_1, buff=0.25)

        # Aufgabenstellungen (alt -> angepasst)
        aufgabe_alt = Tex(
            r"\textbf{Aufgabe: }",
            r"Berechne die Ableitung der Funktion $f(x)=x^2-3x+2$",
            color=BLACK
        ).scale(0.7)
        aufgabe_alt.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        aufgabe_alt.next_to(notes_1, DOWN, buff=1.2)

        aufgabe_neu = VGroup(
            Tex(r"\textbf{Angepasste Aufgabe:}", color=BLACK),
            Tex(r"\textbf{Skizziere} den Graphen der Funktion $f(x)=x^2-3x+2$ und \textbf{beschreibe}, wie",
                color=BLACK),
            Tex(r"  sich die Steigung der Funktion verhält. Berechne anschließend die Ableitung ", color=BLACK),
            Tex(r"  $f'(x)$ und die Werte der ersten Ableitung an den Stellen $x=1$, $x=1{,}5$ und", color=BLACK),
            Tex(r"  $x=2$. \textbf{Was sagen diese Werte über das Verhalten von $f(x)$ an diesen}", color=BLACK),
            Tex(r"  Stellen?}", color=BLACK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).scale(0.64)

        aufgabe_neu.next_to(notes_1_boxed, DOWN, buff=0.8)
        aufgabe_alt_box = SurroundingRectangle(
            aufgabe_alt,
            corner_radius=0.25,
            buff=0.25,
            stroke_color=BLACK,
            stroke_width=2,
            fill_opacity=0
        )
        aufgabe_neu_box = SurroundingRectangle(
            aufgabe_neu,
            corner_radius=0.25,
            buff=0.25,
            stroke_color=BLACK,
            stroke_width=2,
            fill_opacity=0
        )

        # Box schon sichtbar, Text erstmal unsichtbar
        for m in notes_1.submobjects:
            m.set_opacity(0)

        self.add(notes_1_boxed)
        self.play(FadeIn(notes_1_boxed[0]), FadeIn(notes_1_boxed[1]), run_time=0.5)  # shadow + box

        # Dann Zeile für Zeile rein
        for m in notes_1.submobjects:
            self.play(m.animate.set_opacity(1), run_time=0.35)
            self.wait(1)

        self.play(FadeIn(aufgabe_alt, aufgabe_alt_box, shift=UP * 0.1), run_time=0.8)
        self.wait(3)

        self.play(
            TransformMatchingTex(aufgabe_alt, aufgabe_neu),
            Transform(aufgabe_alt_box, aufgabe_neu_box),
            run_time=1.4
        )

        self.wait(6)

        self.play(FadeOut(Group(notes_1_boxed, aufgabe_neu, aufgabe_alt_box, k1)), run_time=1.0)
        self.wait(1)

        k1.move_to(k1_start).scale(1.1364).shift(DOWN * 1.15)
        self.play(FadeIn(titelkarte))
        # -----------------------------
        # Hervorhebung: k2
        # -----------------------------

        # kurzer Fokus-Effekt
        self.play(
            k2.animate.scale(1.1),
            run_time=0.4
        )
        self.play(
            k2.animate.scale(1.0),
            run_time=0.3
        )
        self.wait(1)

        # Alles, was verschwinden soll (außer k2)
        alles_andere = Group(
            titel,
            untertitel,
            k1,
            k3,
            k4
        )
        # parallele Bewegung + Ausblenden
        self.play(
            k2.animate.move_to(zielposition).scale(0.8),
            FadeOut(alles_andere),
            run_time=1.6,
            rate_func=smooth
        )

        self.wait(1.5)

        bubble_path = "media/images/bubble.png"

        def bubble_with_text(text, scale_img=0.3, text_scale=0.65, text_shift=UP * 0.25):
            bubble_img = ImageMobject(bubble_path).scale(scale_img)

            label = Tex(rf"\textbf{{{text}}}", color=WHITE).scale(text_scale)
            label.move_to(bubble_img.get_center()).shift(text_shift)

            return Group(bubble_img, label)

        # Sprechblasen erzeugen
        begruenden = bubble_with_text("Begründe!")
        erklaeren = bubble_with_text("Erkläre!")
        beschreiben = bubble_with_text("Beschreibe!")
        warum = bubble_with_text("Warum?")
        points1 = bubble_with_text("...")
        points2 = bubble_with_text("...")

        # Anordnung wie Skizze
        begruenden.move_to(UP * 1.5)
        erklaeren.move_to(DOWN * 0.9 + LEFT * 3)
        beschreiben.move_to(DOWN * 0.9 + RIGHT * 3)
        warum.move_to(UP * 1 + LEFT * 4)
        points1.move_to(UP * 1 + RIGHT * 4)
        points2.move_to(DOWN * 2)

        bubbles = Group(begruenden, erklaeren, beschreiben, warum, points1, points2)

        # Animation
        self.play(FadeIn(begruenden, shift=UP * 0.2), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(erklaeren, shift=UP * 0.2), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(beschreiben, shift=UP * 0.2), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(warum, shift=UP * 0.2), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(points1, shift=UP * 0.2), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(points2, shift=UP * 0.2), run_time=0.6)
        self.wait(2)

        self.play(FadeOut(bubbles))

        # -----------------------------
        # Notizen unter der Grafik
        # -----------------------------
        note1 = Tex(r"- Arbeitsaufträge zur Sprachproduktion", color=blue).scale(0.7)
        note2 = Tex(r"- Einsatz von Satzanfängen", color=blue).scale(0.7)
        note3 = Tex(r"- Lehrkraft-Impulse für reichhaltige Sprache", color=blue).scale(0.7)

        notes_2 = VGroup(note1, note2, note3).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        notes_2.move_to(np.array([0, 1.4, 0]))
        notes_2_boxed = notes_box(notes_2, buff=0.25)

        # -----------------------------
        # Aufgaben (alt -> angepasst)
        # -----------------------------
        aufgabe_alt = Tex(r"\textbf{Aufgabe: }",
                          r"Berechne die Nullstellen der Funktion $f(x)=x^2-3x+2$",
                          color=BLACK
                          ).scale(0.7)
        aufgabe_alt.arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        aufgabe_neu = VGroup(
            Tex(r"\textbf{Angepasste Aufgabe:}", color=BLACK),
            Tex(r"Berechne die Nullstellen der Funktion und \textbf{beschreibe} Dein Vorgehen.", color=BLACK),
            Tex(r"\textbf{Erläutere}, wie du überprüfen kannst, ob Deine Lösung korrekt ist.", color=BLACK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).scale(0.7)

        aufgabe_alt.next_to(notes_2_boxed, DOWN, buff=1.2)
        aufgabe_neu.next_to(notes_2_boxed, DOWN, buff=0.9)

        aufgabe_alt_box = SurroundingRectangle(
            aufgabe_alt,
            corner_radius=0.25,
            buff=0.25,
            stroke_color=BLACK,
            stroke_width=2,
            fill_opacity=0
        )
        aufgabe_neu_box = SurroundingRectangle(
            aufgabe_neu,
            corner_radius=0.25,
            buff=0.25,
            stroke_color=BLACK,
            stroke_width=2,
            fill_opacity=0
        )

        # Notizen parallel zur Erwähnung
        for m in notes_2.submobjects:
            m.set_opacity(0)

        self.add(notes_2_boxed)
        self.play(FadeIn(notes_2_boxed[0]), FadeIn(notes_2_boxed[1]), run_time=0.5)  # shadow + box

        # Dann Zeile für Zeile rein
        for m in notes_2.submobjects:
            self.play(m.animate.set_opacity(1), run_time=0.35)
            self.wait(1)
        self.wait(2)

        self.play(FadeIn(aufgabe_alt, aufgabe_alt_box, shift=UP * 0.1), run_time=0.8)
        self.wait(1.2)

        self.play(
            TransformMatchingTex(aufgabe_alt, aufgabe_neu),
            Transform(aufgabe_alt_box, aufgabe_neu_box),
            run_time=1.4
        )
        self.wait(2.0)

        # Aufräumen für nächste Szene
        self.play(FadeOut(Group(notes_2_boxed, aufgabe_neu, aufgabe_alt_box)), run_time=1.0)
        self.wait(2)

        k2.move_to(k2_start).scale(1.1364).shift(DOWN * 1.15)

        self.play(FadeIn(titelkarte))
        # -----------------------------
        # Hervorhebung: k3
        # -----------------------------

        # kurzer Fokus-Effekt
        self.play(
            k3.animate.scale(1.1),
            run_time=0.4
        )
        self.play(
            k3.animate.scale(1.0),
            run_time=0.3
        )
        self.wait(1)

        # Alles, was verschwinden soll (außer k3)
        alles_andere = Group(
            titel,
            untertitel,
            k1,
            k2,
            k4
        )
        # parallele Bewegung + Ausblenden
        self.play(
            k3.animate.move_to(zielposition).scale(0.8),
            FadeOut(alles_andere),
            run_time=1.6,
            rate_func=smooth
        )
        self.wait(2)

        # -----------------------------
        # (1) Grafik als Bild + Quellenangabe
        # -----------------------------
        schema = ImageMobject("media/images/Schema_Leiss_2023.png").scale(0.4)
        quelle = Tex(r"\textit{Abbildung in Anlehnung an Leiss et al. (2023)}", color=BLACK).scale(0.55)

        schema_block = Group(schema, quelle).arrange(DOWN, buff=0.25).move_to(ORIGIN).shift(DOWN * 0.75)

        self.play(FadeIn(schema_block), run_time=1.0)
        self.wait(2.5)
        self.play(FadeOut(schema_block), run_time=1.0)

        # -----------------------------
        # (2) Notizen erscheinen
        # -----------------------------
        note1 = Tex(r"- Verknüpfung von Darstellungsebenen ", color=blue).scale(0.7)
        note2 = Tex(r"- Begründung von strukturellen Zusammenhängen ", color=blue).scale(0.7)
        note3 = Tex(r"- Explizite Nutzung mathematischer Begriffe", color=blue).scale(0.7)

        notes_3 = VGroup(note1, note2, note3).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        notes_3.move_to(np.array([0, 1.4, 0]))
        notes_3_boxed = notes_box(notes_3, buff=0.25)

        # Notizen parallel zur Erwähnung
        for m in notes_3.submobjects:
            m.set_opacity(0)

        self.add(notes_3_boxed)
        self.play(FadeIn(notes_3_boxed[0]), FadeIn(notes_3_boxed[1]), run_time=0.5)  # shadow + box

        # Dann Zeile für Zeile rein
        for m in notes_3.submobjects:
            self.play(m.animate.set_opacity(1), run_time=0.35)
            self.wait(1)
        self.wait(2)

        # -----------------------------
        # (3) Aufgabenstellung (alt -> angepasst)
        # -----------------------------
        aufgabe_alt = Tex(
            r"\textbf{Aufgabe: }",
            r"Zeichne den Graphen der Funktion $f(x)=x^2-3x+2$",
            color=BLACK
        ).scale(0.7)
        aufgabe_alt.arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        aufgabe_alt.next_to(notes_3_boxed, DOWN, buff=1.2)

        aufgabe_neu = Tex(
            rf"""
            \begin{{minipage}}{{{12.5}cm}}
            \raggedright
            \textbf{{Angepasste Aufgabe:}}\\
            Zeichne den Graphen der Funktion $f(x)=x^2-3x+2$ und \textbf{{beschreibe den Verlauf so in eigenen Worten}},
            dass jemand anderes den Graphen anhand Deiner Beschreibung zeichnen könnte.
            \textbf{{Welche Zusammenhänge erkennst du}} zwischen dem Graphen, der Funktionsgleichung und Deiner Beschreibung?
            \textbf{{Begründe}}, inwiefern die Darstellungen in den verschiedenen Darstellungsebenen
            (Graph, Funktionsgleichung, Beschreibung in Worten) zusammenhängen?
            \end{{minipage}}
            """,
            color=BLACK,
        ).scale(0.62)

        aufgabe_neu.next_to(notes_3_boxed, DOWN, buff=0.6)

        aufgabe_alt_box = SurroundingRectangle(
            aufgabe_alt,
            corner_radius=0.25,
            buff=0.25,
            stroke_color=BLACK,
            stroke_width=2,
            fill_opacity=0
        )
        aufgabe_neu_box = SurroundingRectangle(
            aufgabe_neu,
            corner_radius=0.25,
            buff=0.25,
            stroke_color=BLACK,
            stroke_width=2,
            fill_opacity=0
        )

        self.play(FadeIn(aufgabe_alt, aufgabe_alt_box, shift=UP * 0.1), run_time=0.8)
        self.wait(1.2)

        self.play(
            Transform(aufgabe_alt, aufgabe_neu),
            Transform(aufgabe_alt_box, aufgabe_neu_box),
            run_time=1.4
        )

        self.wait(4)

        # -----------------------------
        # (4) Aufräumen
        # -----------------------------
        self.play(FadeOut(Group(notes_3_boxed, aufgabe_alt, aufgabe_alt_box)), run_time=1.0)
        self.wait(0.5)

        # -----------------------------
        # Hervorhebung: k4
        # -----------------------------
        k3.move_to(k3_start).scale(1.1364).shift(DOWN * 1.15)

        self.play(FadeIn(titelkarte))

        # kurzer Fokus-Effekt
        self.play(
            k4.animate.scale(1.1),
            run_time=0.4
        )
        self.play(
            k4.animate.scale(1.0),
            run_time=0.3
        )
        self.wait(1)

        # Alles, was verschwinden soll (außer k4)
        alles_andere = Group(
            titel,
            untertitel,
            k1,
            k2,
            k3
        )
        # parallele Bewegung + Ausblenden
        self.play(
            k4.animate.move_to(zielposition).scale(0.8),
            FadeOut(alles_andere),
            run_time=1.6,
            rate_func=smooth
        )

        self.wait(1.5)

        self.camera.background_color = "#0090d4"
        # -----------------------------
        # Hintergrund
        # -----------------------------
        BG_PATH = "media/images/Klassenraum.png"
        bg = ImageMobject(BG_PATH).set_z_index(-10).scale(0.4364)

        self.play(FadeIn(bg), run_time=0.8)

        # -----------------------------
        # Tafel-Inhalt (Graph + Tangente + Labels)
        # -----------------------------
        board_title = VGroup(
            Text(
                "Beschreibe das Verhalten des Graphen an der",
                font=HAND_FONT,
                color=BLACK
            ),
            Text(
                "markierten Stelle!",
                font=HAND_FONT,
                color=BLACK
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).scale(0.38)

        # kleines Koordinatensystem für die Tafel
        axes = Axes(
            x_range=[-0.5, 3.5, 1],
            y_range=[-1.5, 3, 1],
            x_length=5,
            y_length=2.5,
            tips=True,
            axis_config={"color": BLACK, "include_ticks": False, "include_numbers": False},
        ).shift(UP * 2)

        f = lambda x: x ** 2 - 3 * x + 2
        df = lambda x: 2 * x - 3

        graph = axes.plot(f, x_range=[-0.2, 3.0], color=BLUE_E)

        # Tangente bei x=1
        x0 = 1.0
        y0 = f(x0)
        m = df(x0)

        tangent = axes.plot(
            lambda x: m * (x - x0) + y0,
            x_range=[-0.2, 2.25],
            color=GREEN_E
        )

        dot = Dot(axes.c2p(x0, y0), color=RED_E).scale(0.9)

        # Beschriftungen (handschriftlich)
        label_f = Text(
            "f(x) = x² − 3x + 2",
            font=HAND_FONT,
            color=BLACK
        ).scale(0.27)

        label_tan = Text(
            "Tangente an den Graphen in x = 1",
            font=HAND_FONT,
            color=BLACK
        ).scale(0.27)

        label_f.next_to(graph, RIGHT, buff=0.15).shift(UP * 1 + LEFT * 2)
        label_tan.next_to(label_f, DOWN, buff=0.1).align_to(label_f, ORIGIN)

        board_title.next_to(
            VGroup(label_f, label_tan, axes),
            UP * 2,
            buff=0.25
        )

        board_content = Group(
            board_title,
            axes,
            graph,
            tangent,
            dot,
            label_f,
            label_tan
        ).scale(0.8)

        # -----------------------------
        # Positionierung auf der Tafel im Hintergrund
        # -----------------------------
        board_content.scale(0.85)
        board_content.move_to(UP * 1.8)  # Tafelbereich
        board_content.shift(RIGHT * 0.2)
        board_title.shift(LEFT * 0.35)

        self.play(FadeIn(board_title, shift=UP * 0.05), run_time=0.6)
        self.play(Create(axes), run_time=0.8)
        self.play(Create(graph), run_time=1.0)
        self.play(Create(tangent), FadeIn(dot), run_time=0.8)
        self.play(FadeIn(label_f), FadeIn(label_tan), run_time=0.6)

        # -----------------------------
        # Sprechblasen (links / rechts)
        # -----------------------------

        BUBBLE_LEFT_PATH = "media/images/SpeechBubble_alltag.png"
        BUBBLE_RIGHT_PATH = "media/images/SpeechBubble_alltag_gespiegelt.png"

        def bubble(img_path, text_lines, scale_img=0.55, text_scale=0.55, text_shift=UP * 0.1):
            img = ImageMobject(img_path).scale(scale_img).set_z_index(5)
            txt = Tex(*text_lines, color=WHITE).scale(text_scale).set_z_index(6)
            txt.arrange(DOWN, buff=0.12)
            txt.move_to(img.get_center()).shift(text_shift)
            return Group(img, txt)

        # Linker Schüler – Alltagssprache
        bubble_left = bubble(
            BUBBLE_LEFT_PATH,
            [
                r"Die Steigung ist da",
                r"negativ."
            ],
            scale_img=0.35,
            text_scale=0.7
        )

        # Rechter Schüler – formalere Formulierung
        bubble_right = bubble(
            BUBBLE_RIGHT_PATH,
            [
                r"Die Ableitung ist da",
                r"$-1$."
            ],
            scale_img=0.35,
            text_scale=0.7
        )

        # Positionierung
        bubble_left.move_to(LEFT * 3 + UP * 1.5)
        bubble_right.move_to(RIGHT * 1.75 + UP * 1.5)

        # -----------------------------
        # Animation synchron zur Tonspur
        # -----------------------------

        # erste Aussage (Alltagssprache)
        self.wait(2.0)
        self.play(
            FadeIn(bubble_left[0], shift=UP * 0.1),
            FadeIn(bubble_left[1]),
            run_time=0.6
        )

        # zweite Aussage (formaler)
        self.wait(2.5)
        self.play(
            FadeIn(bubble_right[0], shift=UP * 0.1),
            FadeIn(bubble_right[1]),
            run_time=0.6
        )
        self.wait(4)

        # -----------------------------
        # Aufräumen für nächste Szene
        # -----------------------------
        self.play(
            FadeOut(Group(bubble_left, bubble_right)),
        )
        self.play(
            FadeOut(Group(board_content, bg)),
        )
        self.camera.background_color = WHITE
        self.wait(1)

        # -----------------------------
        # Notizen
        # -----------------------------
        note1 = Tex(r"- Vergleich unterschiedlicher Formulierungen", color=blue).scale(0.7)
        note2 = Tex(r"- Reflexion über sprachliche Präzision", color=blue).scale(0.7)
        note3 = Tex(r"- Einsatz von Sprachscaffolds", color=blue).scale(0.7)

        notes_4 = VGroup(note1, note2, note3).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        notes_4.move_to(np.array([0, 1.95, 0]))
        notes_4_boxed = notes_box(notes_4, buff=0.25)

        # -----------------------------
        # Aufgabe alt
        # -----------------------------
        aufgabe_alt = VGroup(
            Tex(r"\textbf{Aufgabe:}", color=BLACK),
            Tex(r"Bestimme die Steigung der Funktion $f(x)=x^2-3x+2$ an", color=BLACK),
            Tex(r"der Stelle $x=1$.", color=BLACK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).scale(0.75)

        aufgabe_alt.next_to(notes_4_boxed, DOWN, buff=0.9)

        block_width_cm = 13

        aufgabe_neu = Tex(
            rf"""
            \begin{{minipage}}{{{block_width_cm}cm}}
            \raggedright
            \setlength{{\baselineskip}}{{0.85\baselineskip}}
            \textbf{{Angepasste Aufgabe:}}\\

            Gegeben ist der Graph der Funktion $f(x)=x^2-3x+2$, sowie \textbf{{die folgenden Aussagen zur Steigung an der Stelle $x=1$:}}
            \vspace{{0.035em}}

            \renewcommand{{\labelitemi}}{{$\bullet$}}
            \begin{{itemize}}
              \setlength{{\itemsep}}{{0.035em}}
              \setlength{{\parsep}}{{0em}}
              \setlength{{\topsep}}{{0.035em}}
              \setlength{{\partopsep}}{{0em}}

              \item An der Stelle $x=1$ fällt der Graph leicht.
              \item Die Steigung bei $x=1$ ist negativ, das heißt, der Graph sinkt an dieser Stelle.
              \item Die erste Ableitung nimmt hier den Wert $-1$ ein, d.\,h. die Steigung der Funktion ist hier ebenfalls negativ.
              \item An dieser Stelle ist die momentane Änderungsrate der Funktion $-1$.
            \end{{itemize}}

            \vspace{{0.035em}}
            \textbf{{Vergleiche die Aussagen}} und \textbf{{begründe}}, ob die Aussagen alle fachlich präzise sind.
            \end{{minipage}}
            """,
            color=BLACK
        ).scale(0.64)

        aufgabe_neu.next_to(notes_4_boxed, DOWN, buff=0.3)

        # -----------------------------
        # Animation
        # -----------------------------

        # Notizen parallel zur Erwähnung
        for m in notes_4.submobjects:
            m.set_opacity(0)

        self.add(notes_4_boxed)
        self.play(FadeIn(notes_4_boxed[0]), FadeIn(notes_4_boxed[1]), run_time=0.5)  # shadow + box

        # Dann Zeile für Zeile rein
        for m in notes_4.submobjects:
            self.play(m.animate.set_opacity(1), run_time=0.35)
            self.wait(1)
        self.wait(2)

        aufgabe_alt_box = SurroundingRectangle(
            aufgabe_alt,
            corner_radius=0.25,
            buff=0.25,
            stroke_color=BLACK,
            stroke_width=2,
            fill_opacity=0
        )
        aufgabe_neu_box = SurroundingRectangle(
            aufgabe_neu,
            corner_radius=0.25,
            buff=0.25,
            stroke_color=BLACK,
            stroke_width=2,
            fill_opacity=0
        )

        self.play(FadeIn(aufgabe_alt, aufgabe_alt_box, shift=UP * 0.1), run_time=0.9)
        self.wait(2)

        self.play(
            Transform(aufgabe_alt, aufgabe_neu),
            Transform(aufgabe_alt_box, aufgabe_neu_box),
            run_time=1.4
        )
        self.wait(5)

        self.play(FadeOut(Group(notes_4_boxed, aufgabe_alt, aufgabe_alt_box, k4)), run_time=1.0)
        self.wait(2)

        k1.scale(0.715 * 1.1)
        k2.scale(0.715 * 1.1)
        k3.scale(0.715 * 1.1)
        k4.scale(0.715 * 1.1 * 1.1364)

        # -----------------------------
        # Bildschirm-Viertel (2 Linien)
        # -----------------------------
        v_line = Line(UP * 3.8, DOWN * 3.8, color=BLACK, stroke_width=2)
        h_line = Line(LEFT * 7.2, RIGHT * 7.2, color=BLACK, stroke_width=2)

        self.play(Create(v_line), Create(h_line), run_time=0.8)

        # Zielpunkte in die vier Quadranten
        q_ul = np.array([-3.6, 2.7, 0])  # oben links
        q_ur = np.array([3.6, 2.7, 0])  # oben rechts
        q_ll = np.array([-3.6, -1.1, 0])  # unten links
        q_lr = np.array([3.6, -1.1, 0])  # unten rechts

        k1.move_to(q_ul)
        k2.move_to(q_ur)
        k3.move_to(q_ll)
        k4.move_to(q_lr)

        self.play(FadeIn(k1, shift=UP * 0.2), FadeIn(k2, shift=UP * 0.2), run_time=0.7)
        self.play(FadeIn(k3, shift=UP * 0.2), FadeIn(k4, shift=UP * 0.2), run_time=0.7)
        self.wait(0.3)

        # -----------------------------
        # Notizen
        # -----------------------------
        # Beispiel-Layout: Notizen unter jeder Kachel
        def place_notes(notes, tile):
            notes.arrange(DOWN, aligned_edge=LEFT, buff=0.18)
            notes.scale(0.85)
            notes.next_to(tile, DOWN, buff=0.35)
            return notes

        notes_1 = place_notes(notes_1, k1)
        notes_2 = place_notes(notes_2, k2)
        notes_3 = place_notes(notes_3, k3)
        notes_4 = place_notes(notes_4, k4)

        # Notizen-Zeilen je Prinzip als Liste
        n1_lines = notes_1.submobjects
        n2_lines = notes_2.submobjects
        n3_lines = notes_3.submobjects
        n4_lines = notes_4.submobjects

        # -----------------------------
        # Animation: Zeile 1 bei allen, dann Zeile 2 bei allen, etc.
        # -----------------------------
        max_common = min(len(n1_lines), len(n2_lines), len(n3_lines), len(n4_lines))

        # Start: alles unsichtbar
        for mob in [*n1_lines, *n2_lines, *n3_lines, *n4_lines]:
            mob.set_opacity(0)

        self.add(notes_1, notes_2, notes_3, notes_4)

        for i in range(max_common):
            self.play(
                n1_lines[i].animate.set_opacity(1),
                n2_lines[i].animate.set_opacity(1),
                n3_lines[i].animate.set_opacity(1),
                n4_lines[i].animate.set_opacity(1),
                run_time=0.6
            )
            self.wait(1)
        self.play(n2_lines[2].animate.set_opacity(1),
                  n3_lines[2].animate.set_opacity(1),
                  n4_lines[2].animate.set_opacity(1))

        self.wait(2)

        take_home = Group(k1, k2, k3, k4, notes_1, notes_2, notes_3, notes_4)
        schluss_titel = Tex(
            r"\textbf{Sprachbildender Mathematikunterricht –}",
            color=BLACK
        ).scale(0.9)

        schluss_untertitel = Tex(
            r"Die vier Prinzipien verknüpft betrachten und kontinuierlich einsetzen!",
            color=BLACK
        ).scale(0.9)
        schluss_titel_group = Group(schluss_titel, schluss_untertitel).arrange(DOWN, buff=0.3).shift(UP * 3)

        self.play(
            FadeOut(Group(v_line, h_line)),
            run_time=1.0
        )

        take_home_box = SurroundingRectangle(
            take_home,
            buff=0.25,
            corner_radius=0.3,
            stroke_color=BLACK,
            stroke_width=2,
            fill_color=WHITE,
            fill_opacity=0,
        ).scale(0.8).shift(DOWN * 0.9 + RIGHT * 0.15)
        self.play(take_home.animate.scale(0.8).shift(DOWN * 0.9 + RIGHT * 0.15),
                  FadeIn(take_home_box), FadeIn(schluss_titel_group),
                  run_time=1)

        self.wait(5)
        self.play(FadeOut(take_home_box, take_home), FadeOut(schluss_titel_group), run_time=1)
