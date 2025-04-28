from manim import *

class gleichmassigUnstetigkeit(ZoomedScene):
    # draw the graph of the function f(x) 1/x in x range (0,9)
    def construct(self):
         # Background grid
        grid = NumberPlane(
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.6,
            },
            axis_config={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.6,
            },
        )

        axes = Axes(
            x_range=[0, 9, 1],
            y_range=[0, 6, 1],
            axis_config={"color": WHITE},
            tips=True
        ).add_coordinates()

        def func(x):
            return 1/x

        # Create the graph of f(x) = 1/x
        graph = axes.plot(
            func,
            x_range=[0.2, 8],  # Avoid x=0 since function is undefined there
            color=BLUE
        )

        # Create a ValueTracker for the x coordinate
        epsilon = 0.5
        delta_tracker = ValueTracker(0.5)
        x_tracker = ValueTracker(1)
       
        moving_epsilon_box = always_redraw(
            lambda: Rectangle(
                width=3 * axes.x_axis.unit_size,
                height=epsilon * axes.y_axis.unit_size,
                color=ORANGE,
                fill_opacity=0.4,
                stroke_width=2
            ).move_to(axes.coords_to_point(x_tracker.get_value(), func(x_tracker.get_value())))
        )
        moving_delta_box = always_redraw(
            lambda: Rectangle(
                width=delta_tracker.get_value() * axes.x_axis.unit_size,
                height=3 * axes.y_axis.unit_size,
                color=PURPLE,
                fill_opacity=0.4,
                stroke_width=2
            ).move_to(axes.coords_to_point(x_tracker.get_value(), func(x_tracker.get_value())))
        )
         # Add highlighted portion of graph between boxes
        # Add highlighted portion of graph between boxes with better visibility
        graph_piece = always_redraw(
            lambda: VGroup(                
                # Add dots at endpoints for emphasis
                Dot(
                    point=axes.coords_to_point(
                        x_tracker.get_value() - delta_tracker.get_value()/2,
                        func(x_tracker.get_value() - delta_tracker.get_value()/2)
                    ),
                    color=RED,
                    radius=0.1
                ),
                Dot(
                    point=axes.coords_to_point(
                        x_tracker.get_value() + delta_tracker.get_value()/2,
                        func(x_tracker.get_value() + delta_tracker.get_value()/2)
                    ),
                    color=GREEN,
                    radius=0.1
                )
            )
        )
        

      
        # Make sure to add graph_piece AFTER the main graph
        self.add(grid, axes, graph)
        self.add(moving_epsilon_box, moving_delta_box)
        self.add(graph_piece)  # Add this last to ensure it's on top

       
        #Label epsilon and delta = 1/2 at top right corner
        math_text_epsilon = MathTex(r"\epsilon = 0.5").set_color(ORANGE)
        math_text_epsilon.to_corner(UR)
        math_text_delta = MathTex(r"\delta = 0.5")
        math_text_delta.next_to(math_text_epsilon, DOWN).set_color(PURPLE)
        self.add(moving_epsilon_box, moving_delta_box)
        self.add(graph_piece)

        # Add elements to the scene
        self.add(grid, axes, graph)
        self.add(math_text_epsilon, math_text_delta)
        self.wait(1)

        # Activate zooming
        self.activate_zooming()

        # Animate the movement
        self.play(
            x_tracker.animate.set_value(0.5),
            delta_tracker.animate.set_value(0.1),
            run_time=3,
            rate_func=linear
        )
        self.wait(1)

        