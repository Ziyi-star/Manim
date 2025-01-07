from manim import *

class CosineWithCircle(Scene):
    def construct(self):
        # Create the unit circle
        circle = Circle(radius=2, color=BLUE).to_edge(LEFT, buff=1)
        center = circle.get_center()

        # Value Tracker for the angle
        angle = ValueTracker(0)
        
        # Create an arrow for the angle
        arrow = always_redraw(lambda: Arrow(
            start=center, 
            # end point in an numpy array (x=cos(angle), 𝑦=sin(angle)) * radius 2
            end=center + 2 * np.array([np.cos(np.radians(angle.get_value())), np.sin(np.radians(angle.get_value())), 0]), 
            buff=0, 
            color=GREEN
        ))

        # Create the horizontal Dashline for the cosine graph
        horizontal_line = always_redraw(lambda: Line(
            start=center, 
            end=center + 2 * np.array([np.cos(np.radians(angle.get_value())), 0, 0]),
            color=YELLOW
        ))

        #Create the vertical Dashline for the cosine graph
        vertical_line = always_redraw(lambda: DashedLine(
            start=center + 2 * np.array([np.cos(np.radians(angle.get_value())), 0, 0]),
            end=center + 2 * np.array([np.cos(np.radians(angle.get_value())), np.sin(np.radians(angle.get_value())), 0]),
            color=WHITE
        ))

        # Create the Axes for the sine graph
        ax = Axes(
            x_range=[0, 360, 90],  # Corresponds to 0° to 450°
            y_range=[-1.0, 1.0, 1],  # Range for the sine graph
            x_length=7.5,
            y_length=4,
            axis_config={"color": WHITE},
            tips=True,
        ).next_to(circle, RIGHT, buff=1)


        # # Labels for the sine graph
        x_label = ax.get_x_axis_label(Tex("x (°)")).to_edge(RIGHT, buff=0.5)
        degree_labels = ax.get_x_axis().add_labels({
            0: Tex("0°"),
            90: Tex("90°"),
            180: Tex("180°"),
            270: Tex("270°"),
            360: Tex("360°")
        })

         # Cosine graph
        sine_graph_tracker = always_redraw(lambda: ax.plot(
            lambda x: np.cos(np.radians(x)),  # Convert x (degrees) to radians
            x_range=[0, angle.get_value()],  # Range from 0 to the current angle
            color=GREEN,
        ))


        # Add all elements to the scene
        self.add(circle, arrow, ax, sine_graph_tracker, degree_labels, sine_graph_tracker, x_label, horizontal_line, vertical_line)
        

        # Animate the arrow and sine graph
        self.play(angle.animate.set_value(360), run_time=20, rate_func=linear)
        self.wait()
