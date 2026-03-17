from manim import *


class Sprache_S4_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # load images
        IMG_DIR = "media/images/Sprache_im_Math_Scene4"
        CHARTS = f"{IMG_DIR}/charts.png"
        CIRCUS = f"{IMG_DIR}/circus.png"
        BOOK = f"{IMG_DIR}/book.png"

        # Add image and put them in the right position
        circus = ImageMobject(CIRCUS).shift(LEFT * 2)
        charts = ImageMobject(CHARTS).shift(LEFT * 2 + DOWN * 1.5)

        self.add(circus, charts)

        # todo: add texts around circle
        label_enaktiv = Text("Enaktiv", color=BLACK, font_size=20).shift(LEFT * 6 + UP * 1)
        label_symbolisch = Text("Symbolisch", color=BLACK, font_size=20).shift(RIGHT * 2 + UP * 1)
        label_ikonisch = Text("Ikonisch", color=BLACK, font_size=20).shift(LEFT * 2 + DOWN * 3.5)

        self.add(label_enaktiv, label_ikonisch, label_symbolisch)
        




