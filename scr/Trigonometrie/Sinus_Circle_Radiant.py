from manim import *

class SinusCircleRadiant(Scene):
    def construct(self):
        # Background grid without the central cross
        grid = NumberPlane(
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.6,
            },
            axis_config={
                "stroke_color": BLUE_D,  # Same color as grid lines
                "stroke_width": 1,       # Same width as grid lines
                "stroke_opacity": 0.6,   # Same opacity as grid lines
            },
        )

        # All things in Circle
        circle = Circle(radius=2, color=BLUE)
        # Set the center of the circle at (-4, 0)
        circle.move_to(grid.c2p(-5, 0))
          # Value Tracker for the angle in degrees
        angle = ValueTracker(0)
        center = circle.get_center()
        
        # Create an arrow for the angle
        arrow = always_redraw(lambda: Arrow(
            start=center, 
            # end point in an numpy array (x=cos(angle), 𝑦=sin(angle)) * radius 2
            end=center + 2 * np.array([np.cos(angle.get_value()), np.sin(angle.get_value()), 0]), 
            buff=0, 
            color=GREEN
        ))
         # Arc to display the angle on the circle
        angle_arc = always_redraw(lambda: Arc(
            radius=2,
            start_angle=0,
            angle=angle.get_value(),
            arc_center=circle.get_center(),
            color=GOLD
        ))
        # Horizontal line 
        horizontal_line = always_redraw(lambda: DashedLine(
            start=center, 
            end=center + 2 * np.array([
                np.cos(angle.get_value()),  # x
                0,  # y
                0
            ]),
            color=WHITE
        ))
        # Vertical dashed line
        vertical_line = always_redraw(lambda: Line(
            start=center + 2 * np.array([
                np.cos(angle.get_value()), 0, 0
            ]),
            end=center + 2 * np.array([
                np.cos(angle.get_value()), 
                np.sin(angle.get_value()), 
                0
            ]),
            color=YELLOW
        ))
        #Dot at Circle
        moving_dot_circle = always_redraw(lambda: Dot(
            center + 2 * np.array([np.cos(angle.get_value()), np.sin(angle.get_value()), 0]),
            color=YELLOW
        ))
        #Dot at X-Axis
        moving_dot_x_axis = always_redraw(lambda: Dot(
            center + 2 * np.array([np.cos(angle.get_value()), 0, 0]),
            color=YELLOW
        ))

        #All things in Graph
        ax = Axes(
            x_range=[0, TAU, TAU / 4],  # 0 to 2π with steps of π/2
            y_range=[-1.5, 1.5, 1],  # Range for the cosine graph
            x_length=10,
            y_length=6,
            axis_config={"color": WHITE},
            tips=True,
        )

        # Set the origin of the Axes at (-2, 0)
        ax.shift(grid.c2p(-3, 0) - ax.get_origin())

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
           # Line at the x-axis in gold
        x_axis_line = always_redraw(lambda: Line(
            start=ax.get_origin(),  # Start at (0, 0) on the graph
            end=ax.c2p(angle.get_value(), 0),  # End at the current x-value on the x-axis
            color=GOLD
        ))
        sine_line_axis = always_redraw(lambda: Line(
            start=ax.c2p(angle.get_value(), 0),  # Start at the current x-value on the x-axis
            end=ax.c2p(angle.get_value(), np.sin(angle.get_value())),  # End at the current x-value on the cosine graph
            color=YELLOW
        ))
        #Dot at X-Axis
        moving_dot_x_axis_graph = always_redraw(lambda: Dot(
            ax.c2p(angle.get_value(), 0),
            color=YELLOW
        ))
        #Dot at cosine Line
        moving_dot_graph = always_redraw(lambda: Dot(
            ax.c2p(angle.get_value(), np.sin(angle.get_value())),
            color=YELLOW
        ))


        # Add all elements to the scene
        self.add(grid)
        self.add(
            circle, arrow, ax, sine_graph_tracker, x_radian_labels, 
            y_labels, horizontal_line, vertical_line, 
            angle_arc, moving_dot_circle, moving_dot_x_axis,
            x_axis_line,sine_line_axis, moving_dot_x_axis_graph, moving_dot_graph)
        self.wait(1)

        # Animate the arrow and sine graph
        self.play(angle.animate.set_value(2*np.pi), run_time=20, rate_func=linear)
        self.wait()
