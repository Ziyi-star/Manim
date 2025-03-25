from manim import *

class FolgenStueckParabel(Scene):
    def construct(self):
        # Load the background image
        background = ImageMobject("Hintergrundbild.jpg")
        background.scale_to_fit_height(config.frame_height)
        background.scale_to_fit_width(config.frame_width)
        self.add(background)

        #