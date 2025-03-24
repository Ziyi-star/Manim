from manim import *

class CircleFlip(Scene):
    def construct(self):
        # Create a white circle
        circle = Circle(radius=1.0, color=WHITE)
        
        # Add a small dot to make rotation visible
        #dot = Dot(color=RED).move_to(circle.point_at_angle(0))
        
        # Group circle and dot together
        group = VGroup(circle)
        
        # Show the circle and dot
        self.play(Create(group), run_time=1)
        self.wait(0.5)
        
        # Flip animation - rotate around y-axis
        self.play(
            ApplyMatrix(
                [[1, 0, 0],
                 [0, np.cos(PI), -np.sin(PI)],
                 [0, np.sin(PI), np.cos(PI)]],
                group
            ),
            run_time=2,
        )
        self.wait(1)