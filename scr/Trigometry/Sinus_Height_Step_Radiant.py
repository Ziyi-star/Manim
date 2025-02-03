from manim import *

class SineHeightStepsRadiant(Scene):
    def construct(self):
        text = Text("Sinusfunktion im Bogenmaß", font="Arial", font_size=36, color=YELLOW)

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

        # Create the unit circle with radius = 2 (matching max y-axis value)
        circle_radius = 2.5
        circle = Circle(circle_radius, color=BLUE)
        circle.move_to(grid.c2p(-3, 0))
        center = circle.get_center()
        dot_center = Dot(center, color=YELLOW)
        center_label = Tex("M").next_to(dot_center, DOWN)

        # Axes for the cosine graph
        ax = Axes(
            x_range=[0, np.pi*7/12, np.pi/12],  # x-axis in radians (π/12 = 15° intervals)
            y_range=[0, 1.5, 1],  # y-axis for sine values (max value = 2)
            # Adjust number for better view to align with circle
            x_length=5,  
            y_length=1.5*circle_radius,  # Matches the circle's radius
            axis_config={"color": WHITE},
            tips=True,
        )
        # Set the origin of the Axes at (-5, 0)
        ax.shift(grid.c2p(-0.5, 0) - ax.get_origin())

        # Add labels to the x-axis
        x_radian_labels = ax.get_x_axis().add_labels({
            0: MathTex("0"),
            (1 / 12) * np.pi: MathTex(r"\frac{\pi}{12}"),  # Simplify \frac{1\pi}{12} to \frac{\pi}{12}
            (2 / 12) * np.pi: MathTex(r"\frac{\pi}{6}"),   # Simplify \frac{1\pi}{6} to \frac{\pi}{6}
            (3 / 12) * np.pi: MathTex(r"\frac{\pi}{4}"),   # Simplify \frac{1\pi}{4} to \frac{\pi}{4}
            (4 / 12) * np.pi: MathTex(r"\frac{\pi}{3}"),   # Simplify \frac{1\pi}{3} to \frac{\pi}{3}
            (5 / 12) * np.pi: MathTex(r"\frac{5\pi}{12}"), # Keep \frac{5\pi}{12} as-is
            (6 / 12) * np.pi: MathTex(r"\frac{\pi}{2}"),   # Simplify \frac{1\pi}{2} to \frac{\pi}{2}
        })

        y_labels = ax.get_y_axis().add_labels({
            1: Tex("1"),
            2: Tex("2"),
        })

        # Dashed line between the circle's center and the axes' origin
        dashed_line = DashedLine(
            start=center,
            end=ax.get_origin(),
            dash_length=0.1,
            color=WHITE
        )

        ##############################
        # self.play(Write(text))
        # self.wait(1)
        # self.play(FadeOut(text))
        self.add(
            grid, circle, dot_center, center_label, ax, dashed_line,
            x_radian_labels, y_labels
        )
        self.wait(1)

        # Animation logic
        for angle in range(0, 91, 15):  # Loop through 0° to 90° in 15° steps
            # Current angle in radians
            angle_rad = np.radians(angle)

            # In the circle: dot, arrow, vertical line
            arrow = Arrow(
                start=center,
                end=center + circle_radius * np.array([np.cos(angle_rad), np.sin(angle_rad), 0]),
                buff=0,
                color=GREEN
            )
            moving_dot = Dot(
                center + circle_radius * np.array([np.cos(angle_rad), np.sin(angle_rad), 0]),
                color=YELLOW
            )

            # Horizontal line from endpoint to the x-axis
            horizontal_line_from_end = DashedLine(
                end=center,
                start=center + circle_radius * np.array([np.cos(angle_rad), 0, 0]),  # Projected down to x-axis
                color=WHITE
            )
            horizontal_line_from_end_dot = Dot(
                center + circle_radius * np.array([np.cos(angle_rad), 0, 0]),
                color=YELLOW
            )
            # Vertical line from endpoint to the y-axis
            vertical_line_from_end = Line(
                start=center + circle_radius * np.array([np.cos(angle_rad), np.sin(angle_rad), 0]),  # Endpoint projected to y-axis
                end=center + circle_radius * np.array([np.cos(angle_rad), 0, 0]),  # Endpoint projected to x-axis
                color=GREEN
            )
            #Kreisbogen
            angle_arc = Arc(
                radius=circle_radius,
                start_angle=0,
                angle=angle_rad,
                arc_center=center,
                color=GOLD
            )

            # In Graph: Dot and line
            graph_line = Line(
                start=ax.coords_to_point(angle_rad, 0),
                end=ax.coords_to_point(angle_rad, np.sin(angle_rad)),
                color=GREEN
            )
            graph_dot = Dot(
                ax.coords_to_point(angle_rad, np.sin(angle_rad)),
                color=YELLOW
            )
            #Winkel wachsen in x axis
            x_axis_line = Line(
            start=ax.get_origin(),  
            end=ax.c2p(angle_rad, 0),  # End at the current x-value on the x-axis
            color=GOLD
            )
            x_axis_line_dot=Dot(
            ax.c2p(angle_rad, 0),
            color=YELLOW
            )

            # Add circle arrow and radius line
            self.play(Create(angle_arc,run_time = 2))
            self.play(FadeIn(moving_dot))
            self.play(GrowArrow(arrow,run_time=2))
            self.wait(0.5)
            self.play(Create(vertical_line_from_end, run_time =1))
            self.play(Create(horizontal_line_from_end, run_time =1))
            self.play(FadeIn(horizontal_line_from_end_dot))
            self.wait(0.5)

            # Move radius line to graph
            self.play(Transform(angle_arc, x_axis_line))
            self.play(FadeIn(x_axis_line, x_axis_line_dot))
            self.wait(0.5)
            self.play(Transform(vertical_line_from_end, graph_line))
            self.play(FadeIn(graph_line, graph_dot))
            self.wait(0.5)

            # Remove the arrow, moving dot, and radius line
            self.remove(
                arrow, moving_dot, horizontal_line_from_end,  horizontal_line_from_end_dot,vertical_line_from_end, 
                angle_arc, x_axis_line, x_axis_line_dot)

        # Add sine graph
        sine_graph = ax.plot(lambda x: np.sin(x), color=GREEN, x_range=[0, np.pi / 2])
        self.play(Create(sine_graph), run_time=2)
        self.wait(2)
