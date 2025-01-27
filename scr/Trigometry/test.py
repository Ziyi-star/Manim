from manim import *

class Test(Scene):
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
        ).add_coordinates()

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
            end=center + 2 * np.array([
                np.cos(angle.get_value()),  # x = cos(angle in radians)
                np.sin(angle.get_value()),  # y = sin(angle in radians)
                0
            ]), 
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
        horizontal_line = always_redraw(lambda: Line(
            start=center, 
            end=center + 2 * np.array([
                np.cos(angle.get_value()),  # x
                0,  # y
                0
            ]),
            color=YELLOW
        ))
        # Vertical dashed line
        vertical_line = always_redraw(lambda: DashedLine(
            start=center + 2 * np.array([
                np.cos(angle.get_value()), 0, 0
            ]),
            end=center + 2 * np.array([
                np.cos(angle.get_value()), 
                np.sin(angle.get_value()), 
                0
            ]),
            color=WHITE
        ))
        #todo: Dots at Circle
        

        #todo: Dot at Radius



        # All things in Axes
        ax = Axes(
            x_range=[0, TAU, TAU / 4],  # 0 to 2π with steps of π/2
            y_range=[-1.0, 1.0, 1],  # Range for the cosine graph
            x_length=10,
            y_length=4,
            axis_config={"color": WHITE},
            tips=True,
        )

        # Set the origin of the Axes at (-2, 0)
        ax.shift(grid.c2p(-3, 0) - ax.get_origin())


        # Add labels to the Axes
        x_radian_labels = ax.get_x_axis().add_labels({
            0: MathTex("0"),
            PI / 2: MathTex("\\frac{\\pi}{2}"),
            PI: MathTex("\\pi"),
            3 * PI / 2: MathTex("\\frac{3\\pi}{2}"),
            TAU: MathTex("2\\pi")
        })

        y_degree_labels = ax.get_y_axis().add_labels({
            1: MathTex("1"),
            -1: MathTex("-1")
        })

        # Cosine graph
        cosine_graph_tracker = always_redraw(lambda: ax.plot(
            lambda x: np.cos(x),  # x is already in radians
            x_range=[0, angle.get_value()],  # Range from 0 to the current angle
            color=GREEN,
        ))
        # Line at the x-axis in gold
        x_axis_line = always_redraw(lambda: Line(
            start=ax.get_origin(),  # Start at (0, 0) on the graph
            end=ax.c2p(angle.get_value(), 0),  # End at the current x-value on the x-axis
            color=GOLD
        ))
        cosine_line_axis = always_redraw(lambda: Line(
            start=ax.c2p(angle.get_value(), 0),  # Start at the current x-value on the x-axis
            end=ax.c2p(angle.get_value(), np.cos(angle.get_value())),  # End at the current x-value on the cosine graph
            color=YELLOW
        ))

        # Add all elements to the scene
        self.add(grid)
        self.add(
            circle, arrow, ax, cosine_graph_tracker, x_radian_labels, 
            y_degree_labels, horizontal_line, vertical_line, 
            angle_arc,x_axis_line,cosine_line_axis)
        
        # Animate the arrow and cosine graph
        #self.play(angle.animate.set_value(TAU), run_time=20, rate_func=linear)  # TAU = 2π
        self.play(angle.animate.set_value(TAU), run_time=5, rate_func=linear)  # TAU = 2π
        self.wait()



