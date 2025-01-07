from manim import *

class SineHeightSteps(Scene):
    def construct(self):
        text = Text("Sinusfunktion", font="Arial", font_size=36, color=YELLOW)

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
        circle_radius = 2  # Same as the y-axis range in axes
        circle = Circle(radius=circle_radius, color=BLUE).to_edge(LEFT, buff=1)
        center = circle.get_center()
        dot_center = Dot(center, color=YELLOW)
        center_label = Tex("M").next_to(dot_center, DOWN)

        # Axes for the sine graph
        ax = Axes(
            x_range=[0, 100, 15],  # x-axis in degrees with 15-degree intervals
            y_range=[0, 2.0, 1],  # y-axis for sine values (max value = 2)
            x_length=7.5,  # Adjusted for clarity
            y_length=4,  # Matches the circle's radius
            axis_config={"color": WHITE},
            tips=True,
        )

        # Add labels to the axes
        x_degree_labels = ax.get_x_axis().add_labels({
            0: Tex("0°"),
            15: Tex("15°"),
            30: Tex("30°"),
            45: Tex("45°"),
            60: Tex("60°"),
            75: Tex("75°"),
            90: Tex("90°"),
        })

        y_degree_labels = ax.get_y_axis().add_labels({
            1: Tex("1"),
            2: Tex("2"),
        })


        # Align the axes origin with the circle's center
        ax_y_offset = center[1] - ax.get_origin()[1]  # Calculate vertical offset
        ax.shift(UP * ax_y_offset)  # Align the origin of the axes with the circle's center

        # Move the axes slightly to the right
        ax.shift(RIGHT * 2)  # Shift the axes to the right

        # Dashed line between the circle's center and the axes' origin
        dashed_line = DashedLine(
            start=center,
            end=ax.get_origin(),
            dash_length=0.1,
            color=WHITE
        )

        # Dashed line between the circle's center and the axes' origin
        dashed_line = DashedLine(
            start=center,
            end=ax.get_origin(),
            dash_length=0.1,
            color=WHITE
        )

        ##############################
        self.play(Write(text))
        self.wait(1)
        self.play(FadeOut(text))
        self.add(
            grid, circle, dot_center, center_label, ax, dashed_line,
            x_degree_labels, y_degree_labels
        )
        self.wait(1)

        # Animation logic
        for angle in range(0, 91, 15):  # Loop through 0° to 90° in 15° steps
            # Current angle in radians
            angle_rad = np.radians(angle)

            # In the circle: dot, arrow, vertical line
            arrow = Arrow(
                start=center,
                end=center + 2 * np.array([np.cos(angle_rad), np.sin(angle_rad), 0]),
                buff=0,
                color=GREEN
            )
            moving_dot = Dot(
                center + 2 * np.array([np.cos(angle_rad), np.sin(angle_rad), 0]),
                color=YELLOW
            )

            # Angle label
            angle_label = MathTex(f"{angle}^\circ").scale(0.7).move_to(
                center + 1.5 * np.array([np.cos(angle_rad / 2), np.sin(angle_rad / 2), 0])
            )


            # Vertical line from endpoint to the x-axis
            vertical_line_from_end = Line(
                start=center + 2 * np.array([np.cos(angle_rad), np.sin(angle_rad), 0]),  # Endpoint on the circle
                end=center + 2 * np.array([np.cos(angle_rad), 0, 0]),  # Projected down to x-axis
                color=GREEN
            )

            # In Graph: Dot and line
            graph_line = Line(
                start=ax.coords_to_point(angle, 0),
                end=ax.coords_to_point(angle, np.sin(angle_rad)),
                color=GREEN
            )
            graph_dot = Dot(
                ax.coords_to_point(angle, np.sin(angle_rad)),
                color=YELLOW
            )

            # Add circle arrow and radius line
            self.play(GrowArrow(arrow), FadeIn(moving_dot), Create(angle_label))
            self.wait(0.5)
            self.play(Create(vertical_line_from_end))
            self.wait(0.5)

            # Move radius line to graph
            self.play(Transform(vertical_line_from_end, graph_line))
            self.play(FadeIn(graph_line, graph_dot))
            self.wait(0.5)

            # Remove the arrow, moving dot, and radius line
            self.remove(arrow, moving_dot, vertical_line_from_end, angle_label)

        # add sine graph
        sine_graph = ax.plot(lambda x: np.sin(np.radians(x)), color=GREEN, x_range=[0, 90])
        self.play(Create(sine_graph), run_time=2)
        self.wait(2)
