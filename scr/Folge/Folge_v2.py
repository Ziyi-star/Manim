from manim import *
import numpy as np

class CirclePackingAlongPath(Scene):
    def construct(self):
        path = ParametricFunction(
            lambda t: np.array([t, np.sin(2*t), 0]),
            t_range=[-PI, PI, 0.1], 
            color=WHITE
        )
        
        circles = VGroup()
        num_circles = 30  # Number of circles along the curve
        min_radius, max_radius = 0.05, 0.4  # Radius range
        
        for i in range(num_circles):
            alpha = i / num_circles  # Normalized position
            point = path.point_from_proportion(alpha)
            radius = max_radius * (1 - alpha) + min_radius * alpha  # Gradually decreasing size
            
            circle = Circle(radius=radius, color=WHITE)
            circle.move_to(point)
            circles.add(circle)

        self.play(Create(circles), run_time=3)
        self.wait(2)
