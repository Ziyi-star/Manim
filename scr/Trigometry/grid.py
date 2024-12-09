from manim import *

class Grid(Scene):
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

        # Create the unit circle with radius = 2 (matching max y-axis value)
        circle_radius = 2  # Same as the y-axis range in axes
        circle = Circle(radius=circle_radius, color=BLUE).to_edge(LEFT, buff=1)
        circle_center = circle.get_center()
        dot_center = Dot(circle_center, color=YELLOW)
        center_label = Tex("M").next_to(dot_center, DOWN)

        # Axes for the sine graph
        ax = Axes(
            x_range=[0, 90, 15],  # x-axis in degrees with 15-degree intervals
            y_range=[0, 2.0, 0.5],  # y-axis for sine values (max value = 2)
            x_length=5,  # Adjusted for clarity
            y_length=4,  # Matches the circle's radius
            axis_config={"color": WHITE},
            tips=True,
        )

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

        # Align the axes origin with the circle's center
        ax_y_offset = circle_center[1] - ax.get_origin()[1]  # Calculate vertical offset
        ax.shift(UP * ax_y_offset)  # Align the origin of the axes with the circle's center

        # Move the axes slightly to the right
        ax.shift(RIGHT * 2)  # Shift the axes to the right

        # Dashed line between the circle's center and the axes' origin
        dashed_line = DashedLine(
            start=circle_center,
            end=ax.get_origin(),
            dash_length=0.1,
            color=WHITE
        )

        # Add all elements to the scene
        self.add(
            grid, circle, dot_center, center_label, ax, dashed_line,
            degree_labels, x_label, y_label
        )
