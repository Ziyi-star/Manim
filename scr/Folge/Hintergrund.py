from manim import *

class ImageBackgroundAnimation(Scene):
    def construct(self):
        # Laden Sie das Bild als Hintergrund
        background = ImageMobject("Hintergrundbild.jpg")
        background.scale_to_fit_height(config.frame_height)
        background.scale_to_fit_width(config.frame_width)
        self.add(background)

        # Erstellen Sie die Animationen wie gewohnt
        numbers = [1, 2, 3, 4, 5, 6, 7]
        number_mobs = [Text(str(n), color=BLACK) for n in numbers]  # Set color to BLACK
        condition = Text("n >= Fogenglao", font_size=24, color=BLACK)  # Set color to BLACK

        # Animate numbers
        for i, mob in enumerate(number_mobs):
            self.play(Write(mob))
            self.wait(0.5)
            if i < len(number_mobs) - 1:
                self.play(mob.animate.shift(UP * 1.5))

        # Show condition
        self.play(Write(condition.to_edge(DOWN)))
        self.wait(2)
