from manim import *


class Sprache_S4_2(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Icons
        # Define the position (same as in original file)
        zielposition = np.array([5.5, 2.75, 0])
        
        # Create k3
        ICON1_PATH = "media/images/Icon 3.png"
        k3 = ImageMobject(ICON1_PATH)
        k3.set_height(2.5).move_to(zielposition).scale(0.8)
        
        self.add(k3)

        # load images
        IMG_DIR = "media/images/Sprache_im_Math_Scene4"
        RIGHT_ETAGE = f"{IMG_DIR}/right_etage.png"
        PEOPLE = f"{IMG_DIR}/people.png"
        RIGHT_ARROW = f"{IMG_DIR}/right_arrow.png"
        LEFT_ETAGE = f"{IMG_DIR}/left_etage.png"
        DOUBLE_ARROW = f"{IMG_DIR}/double_arrow.png"
        SPRECHBLASE = f"{IMG_DIR}/sprechblase.png"


        # Add image and put them in the right position
        right_etage = ImageMobject(RIGHT_ETAGE).shift(RIGHT * 4)
        people = ImageMobject(PEOPLE)
        right_arrow = ImageMobject(RIGHT_ARROW).shift(RIGHT * 2.3 + DOWN * 1)
        left_arrow = ImageMobject(RIGHT_ARROW).shift(LEFT * 2.5 + DOWN * 1)
        left_etage = ImageMobject(LEFT_ETAGE).shift(LEFT * 4)
        double_arrow = ImageMobject(DOUBLE_ARROW).shift(DOWN * 0.5)
        sprechblase = ImageMobject(SPRECHBLASE).shift(UP * 2).scale(0.8)

        self.play(FadeIn(right_etage, right_arrow))

        # #debug, um Positionen zu testen
        # self.add(right_etage, left_arrow, right_arrow, left_etage, double_arrow, sprechblase)

        # Startposition = symbolische Darstellung
        pos_enaktiv = RIGHT * 5 + UP * 1.5
        pos_ikonisch = RIGHT * 5 
        pos_symbolisch = RIGHT * 5 + DOWN * 1.5

        # animations
        people.move_to(pos_symbolisch)
        self.play(FadeIn(people))
        self.wait(1)
        self.remove(people)

        people.move_to(pos_enaktiv)
        self.play(FadeIn(people))
        self.wait(1)
        self.remove(people)

        people.move_to(pos_ikonisch)
        self.play(FadeIn(people))
        self.wait(1)
        self.remove(people)

        # add pfeile
        self.play(FadeIn(left_etage))
        self.wait(1)
        self.play(FadeIn(left_arrow))
        self.wait(1)
        self.play(FadeIn(double_arrow))

        # blink 3x
        for i in range(3):
            self.play(FadeOut(double_arrow,left_arrow,right_arrow), run_time=0.3)
            self.play(FadeIn(double_arrow,left_arrow,right_arrow), run_time=0.3)
        self.wait(1)
        self.play(FadeIn(sprechblase))
        self.wait(2)








        




