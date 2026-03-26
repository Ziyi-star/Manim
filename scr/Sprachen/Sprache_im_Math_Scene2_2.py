from manim import *


class Sprache_S2_2(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Icons
        # Define the position (same as in original file)
        zielposition = np.array([5.5, 2.75, 0])
        
        # Create k1
        ICON1_PATH = "media/images/Icon 1.png"
        k1 = ImageMobject(ICON1_PATH)
        k1.set_height(2.5).move_to(zielposition).scale(0.8)
        
        self.add(k1)

        # Image folder (relative to scr/Sprachen when running manim there)
        IMG_DIR = "media/images/Sprache_im_Math_Scene2_2"
        BOOK_ICON = f"{IMG_DIR}/book_icon.png"
        FLAG = f"{IMG_DIR}/flag.png"
        ROUTE = f"{IMG_DIR}/route.png"
        CLOUD_LEFT = f"{IMG_DIR}/sprech_blasen_left.png"
        CLOUD_RIGHT = f"{IMG_DIR}/sprech_blasen_right.png"
        START_ICON = f"{IMG_DIR}/start_icon.png"

        # Base images
        route = (
            ImageMobject(ROUTE).shift(LEFT * 2.5 + DOWN * 0.5)
        )
        start_icon = (
            ImageMobject(START_ICON).scale(1.5).shift(LEFT * 6 + DOWN * 3)
        )

        # Task icons
        book1 = (
            ImageMobject(BOOK_ICON)
            .scale(1.5)
            .move_to(LEFT * 4.5 + UP * 0.3)
        )
        book2 = (
            ImageMobject(BOOK_ICON)
            .scale(1.5)
            .move_to(LEFT * 1.8 + DOWN * 3)
            .set_z_index(2)
        )
        book3 = (
            ImageMobject(BOOK_ICON)
            .scale(1.5)
            .move_to(LEFT * 1.3 + UP * 0.5)
        )

        flag = (
            ImageMobject(FLAG)
            .scale(1.5)
            .move_to(RIGHT * 0.5 + UP * 2.5)
        )

        # Clouds
        cloud_left = (
            ImageMobject(CLOUD_LEFT)
            .move_to(LEFT * 4 + UP * 2)
        )
        left_cloud_txt = (
            Text("Sprachliche\nHilfsmittel?", color=WHITE, font_size=20)
            .move_to(cloud_left.get_center()+ LEFT* 0.7 + UP*0.2)
        )
        cloud_right = (
            ImageMobject(CLOUD_RIGHT)
            .move_to(RIGHT * 0.8 + DOWN * 2)
        )
        right_cloud_txt = (
            Text("Fachtypische\nSprachhandlungen?", color=WHITE, font_size=20)
            .move_to(cloud_right.get_center() + RIGHT*0.1 + UP * 0.2)  # inside cloud near top

        )

        # Text
        title = Text("Unterrichtsplanung", color=BLACK, font_size=20).move_to(
            UP * 3 + LEFT * 1.5
        )
        a1 = (
            Text("Aufgabe 1", color=BLACK, font_size=20)
            .next_to(book1, UP, buff=0.1)
        )
        a2 = (
            Text("Aufgabe 2", color=BLACK, font_size=20)
            .next_to(book2, DOWN, buff=0.1)
        )
        a3 = (
            Text("Aufgabe 3", color=BLACK, font_size=20)
            .next_to(book3, UP, buff=0.1)
        )


        right_top = (
            Text("Mathematische Inhalte", color=BLACK, font_size=20)
            .move_to(RIGHT * 5 + DOWN * 0.5)
        )
        right_mid = Text("↓↑", color=BLACK, font_size=50).move_to(
            RIGHT * 5 + DOWN * 1.3
        )
        right_bottom = (
            Text("Sprachliche Anforderungen", color=BLACK, font_size=20)
            .move_to(RIGHT * 5 + DOWN * 2)
        )

        # Animation
        self.play(FadeIn(route), run_time=1)

        self.play(FadeIn(start_icon), run_time=1)

        self.play(FadeIn(title), run_time=1)

        self.play(FadeIn(book1), FadeIn(a1), run_time=1)
        self.play(FadeIn(book2), FadeIn(a2), run_time=1)
        self.play(FadeIn(book3), FadeIn(a3), run_time=1)

        self.play(FadeIn(flag), run_time=1)

        self.play(FadeIn(right_top), run_time=1)

        self.play(FadeIn(right_bottom), run_time=1)

        self.play(FadeIn(right_mid), run_time =1)

        self.play(FadeIn(cloud_right), FadeIn(right_cloud_txt), run_time=1)

        self.play(FadeIn(cloud_left), FadeIn(left_cloud_txt), run_time=1)

        self.wait(2)
