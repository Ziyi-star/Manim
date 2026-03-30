from manim import *


class Sprache_S3(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Icons
        # Define the position (same as in original file)
        zielposition = np.array([5.5, 2.75, 0])
        
        # Create k2
        ICON1_PATH = "media/images/Icon 2.png"
        k2 = ImageMobject(ICON1_PATH)
        k2.set_height(2.5).move_to(zielposition).scale(0.87)
        
        self.add(k2)

        # book
        BOOK_ICON = "media/images/book.png"
        book = ImageMobject(BOOK_ICON)
        book.move_to(LEFT * 5)

        # Text
        TEXT = "media/images/aktives_formulieren.png"
        text = ImageMobject(TEXT)
        text.move_to(DOWN * 1)
        self.play(FadeIn(book), FadeIn(text), run_time=1)
        self.wait(2)


       