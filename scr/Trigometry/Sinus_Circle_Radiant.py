from manim import *

class SinusCircleRadiant(Scene):
    def construct(self):
        # Create the unit circle
        circle = Circle(radius=2, color=BLUE).to_edge(LEFT, buff=1)
        center = circle.get_center()

        # Line at 0 (horizontal line to the right)
        line_at_0 = DashedLine(
            start=center, 
            end=center + 2 * RIGHT,  # RIGHT is a predefined numpy array [1, 0, 0]
            color=WHITE
        )


        # Value Tracker for the angle
        angle = ValueTracker(0)
        
        # Create an arrow for the angle
        arrow = always_redraw(lambda: Arrow(
            start=center, 
            # end point in an numpy array (x=cos(angle), 𝑦=sin(angle)) * radius 2
            end=center + 2 * np.array([np.cos(angle.get_value()), np.sin(angle.get_value()), 0]), 
            buff=0, 
            color=GREEN
        ))


        # Create the Axes for the sine graph
        ax = Axes(
            x_range=[0, 2*np.pi, 0.5*np.pi],  # Corresponds to 0° to 450°
            y_range=[-1.0, 1.0, 1],  # Range for the sine graph
            x_length=7.5,
            y_length=5,
            axis_config={"color": WHITE},
            tips=True,
        ).next_to(circle, RIGHT, buff=1)

        #Labels for the sine graph
        x_radian_labels = ax.get_x_axis().add_labels({
            0: Tex("0"),
            (1 / 2) * np.pi: MathTex(r"\frac{\pi}{2}"),  
            np.pi: MathTex(r"\pi"),
            (3 / 2) * np.pi: MathTex(r"\frac{3\pi}{2}"),   
            2 * np.pi: MathTex(r"2\pi")
        })

        y_labels = ax.get_y_axis().add_labels({
            1: Tex("1"),
            -1: Tex("-1")
        })

         # Sine graph
        sine_graph_tracker = always_redraw(lambda: ax.plot(
            lambda x: np.sin(x),  # Convert x (degrees) to radians
            x_range=[0, angle.get_value()],  # Range from 0 to the current angle
            color=GREEN,
        ))


        # Add all elements to the scene
        self.add(circle, arrow, ax, sine_graph_tracker, x_radian_labels, sine_graph_tracker, line_at_0, y_labels)
        self.wait(1)

        # Animate the arrow and sine graph
        self.play(angle.animate.set_value(2*np.pi), run_time=20, rate_func=linear)
        self.wait()
