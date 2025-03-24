from manim import *
import numpy as np

class GrowingCircles(Scene):
    def construct(self):
        circles = VGroup()
        num_circles = 32
        
        for i in range(num_circles):
            t = (num_circles - i - 1) * 0.3  # Reverse order
            radius = 0.05 + (num_circles - i - 1) * 0.01  # Decrease size gradually
            x = (1 + 0.5 * t) * np.cos(t)
            
            # Add +2 as an offset to move circles upward
            y = -(1 + 0.5 * t) * np.sin(t) + 1
            
            circle = Circle(radius=radius, color=WHITE)
            circle.move_to([x, y, 0])
            circles.add(circle)
        
        self.play(Create(circles), run_time=4)
        self.wait(2)

