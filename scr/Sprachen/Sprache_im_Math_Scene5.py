from manim import *


class Sprache_S5(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Icons
        # Define the position (same as in original file)
        zielposition = np.array([5.5, 2.75, 0])
        
        # Create k4
        ICON1_PATH = "media/images/Icon 4.png"
        k4 = ImageMobject(ICON1_PATH)
        k4.set_height(2.5).move_to(zielposition).scale(0.8)
        
        self.add(k4)

        # book
        BOOK_ICON = "media/images/book.png"
        book = ImageMobject(BOOK_ICON)
        book.move_to(LEFT * 5)

        # Text
        TEXT = "media/images/variationsprinzip.png"
        text = ImageMobject(TEXT)
        text.move_to(DOWN * 1)
        self.play(FadeIn(book), FadeIn(text), run_time=1)
        self.wait(2)


       