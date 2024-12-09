from manim import *

class SineHeightSteps(Scene):
    def construct(self):
        #Background grid
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
        }
        )

        # Create the unit circle
        circle = Circle(radius=1, color=BLUE).to_edge(LEFT, buff=1).move_to(LEFT * 3 + UP * 2)  # Adjust position
        center = circle.get_center()
        dot_center = Dot(center, color=YELLOW)
        center_label = Tex("M").next_to(dot_center, DOWN)

        # Axes for the sine graph
        ax = Axes(
            x_range=[0, 90, 15],  # x-axis in degrees with 15-degree intervals
            y_range=[0, 1.0, 0.5],  # y-axis for sine values
            x_length=4,
            y_length=2,
            axis_config={"color": WHITE},
            tips=True,
        ).next_to(circle,RIGHT, buff=1).align_to(dot_center, DOWN)

        # Add labels to the axes
        x_label = ax.get_x_axis_label(Tex("Drehwinkel").scale(0.7))
        y_label = ax.get_y_axis_label(Tex("Höhe").scale(0.7))
        degree_labels = ax.get_x_axis().add_labels({
            0: Tex("0°"),
            15: Tex("15°"),
            30: Tex("30°"),
            45: Tex("45°"),
            60: Tex("60°"),
            75: Tex("75°"),
            90: Tex("90°"),
        })

        # Add elements to the scene
        self.add(grid, circle, dot_center, center_label, ax, degree_labels, x_label, y_label)

        # Animation logic
        for angle in range(0, 91, 15):  # Loop through 0° to 90° in 15° steps
            # Current angle in radians
            angle_rad = np.radians(angle)

            # In the circle: dot, arrow, vertikel line 
            arrow = Arrow(
                start=center,
                end=center + 1 * np.array([np.cos(angle_rad), np.sin(angle_rad), 0]),
                buff=0,
                color=GREEN
            )
            moving_dot = Dot(
                center + 1 * np.array([np.cos(angle_rad), np.sin(angle_rad), 0]),
                color=GREEN
            )
            # Vertical line from endpoint to the x-axis
            vertical_line_from_end = Line(
                start=center + 1 * np.array([np.cos(angle_rad), np.sin(angle_rad), 0]),  # Endpoint on the circle
                end=center + 1 * np.array([np.cos(angle_rad), 0, 0]),  # Projected down to x-axis
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
            self.play(GrowArrow(arrow), FadeIn(moving_dot))
            self.wait(0.5)
            self.play(Create(vertical_line_from_end))
            self.wait(0.5)

            # Move radius line to graph
            self.play(Transform(vertical_line_from_end, graph_line))
            self.play(FadeIn(graph_line,graph_dot))
            self.wait(0.5)

            # Remove the arrow, moving dot, and radius line
            self.remove(arrow, moving_dot, vertical_line_from_end)

        self.wait()

