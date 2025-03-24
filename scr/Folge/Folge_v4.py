from manim import *
import numpy as np

class GrowingCircles(Scene):
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
        self.wait(2)

