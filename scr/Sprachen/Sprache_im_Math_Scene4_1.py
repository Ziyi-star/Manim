from manim import *


class Sprache_S4_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Icons
        # Define the position (same as in original file)
        zielposition = np.array([5.5, 2.75, 0])
        
        # Create k3
        ICON1_PATH = "media/images/Icon 3.png"
        k3 = ImageMobject(ICON1_PATH)
        k3.set_height(2.5).move_to(zielposition).scale(0.87)
        
        self.add(k3)

        # load images
        IMG_DIR = "media/images/Sprache_im_Math_Scene4"
        CHARTS = f"{IMG_DIR}/charts.png"
        CIRCUS = f"{IMG_DIR}/circus.png"
        BOOK = f"{IMG_DIR}/book.png"

        # Add image and put them in the right position
        circus = ImageMobject(CIRCUS).shift(LEFT * 2)
        charts = ImageMobject(CHARTS).shift(LEFT * 2 + DOWN * 1.5)

        # Add texts around circle
        label_enaktiv = Text("Enaktiv", color=BLACK, font_size=20).shift(LEFT * 6 + UP * 1)
        label_symbolisch = Text("Symbolisch", color=BLACK, font_size=20).shift(RIGHT * 2 + UP * 1)
        label_ikonisch = Text("Ikonisch", color=BLACK, font_size=20).shift(LEFT * 2 + DOWN * 3.5)


        # Add book in the middle and text "EIS-Prinzip(Bruder)?" in a rectangle around it
        book = ImageMobject(BOOK).shift(RIGHT*1.5 + DOWN*1.3)
        eis_text = Text("EIS-Prinzip (Bruner)", color=BLACK, font_size=30)
        box = SurroundingRectangle(
            eis_text,
            color="#d0d0d0",
            fill_color="#d0d0d0",
            fill_opacity=1,
            buff=0.25,
            stroke_width=0,
            corner_radius=0.1
        )
        title_group = VGroup(box, eis_text)
        title_group.move_to(RIGHT * 4 + DOWN * 2)

        # Animations
        self.play(FadeIn(book), FadeIn(title_group), run_time=1)
        self.wait(1)
        self.play(FadeIn(circus), FadeIn(charts), run_time=1)
        self.wait(1)
        self.play(Write(label_enaktiv), run_time=1)
        self.play(Write(label_symbolisch), run_time=1)
        self.play(Write(label_ikonisch), run_time=1)
        self.wait(2)


        




