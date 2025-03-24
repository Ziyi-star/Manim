from manim import *
import numpy as np

class FolgenSpirale(Scene):
    def construct(self):
        circles = VGroup()
        num_circles = 50  # Mehr Kreise

        angle_offset = -0.8  # Radians (z.B. ~23°)

        for i in range(num_circles):
            # Kleinerer Multiplikator für eine engere Spiralbahn
            t = (num_circles - i - 1) * 0.2
            
            # Radius etwas kleiner halten, damit die Kreise weniger wachsen
            radius = 0.04 + (num_circles - i - 1) * 0.007
            
            x = (0.5 + 0.35 * t) * np.cos(t+angle_offset)
            # +1 als Offset, um die Spirale etwas anzuheben
            y = -(0.5 + 0.35 * t) * np.sin(t+angle_offset) + 1
            
            circle = Circle(radius=radius, color=WHITE)
            circle.move_to([x, y, 0])
            circles.add(circle)
        
        self.play(Create(circles), run_time=4)
        #self.wait(2)

         # Flip each circle one by one around its x-axis
        for circle in circles:
            center = circle.get_center()
            self.play(
                Rotate(
                    circle,
                    angle=PI,
                    axis=RIGHT,  # This makes it rotate around x-axis
                    about_point=center  # This makes it rotate around its own center
                ),
                run_time=0.1  # Adjust this value to control flip speed
            )
        
        self.wait(2)

       

