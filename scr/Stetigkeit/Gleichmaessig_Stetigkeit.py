from manim import *

class gleichmassigStetigkeit(Scene):
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

        # Labels
        #function_label = MathTex("f(x)=\\frac{1}{x}").next_to(graph, UP)

        #Label epsilon and delta = 1/2 at top right corner
        math_text_epsilon = MathTex(r"\epsilon = 0.5").set_color(ORANGE)
        math_text_epsilon.to_corner(UR)
        math_text_delta = MathTex(r"\delta = 0.5")
        math_text_delta.next_to(math_text_epsilon, DOWN).set_color(PURPLE)

        # Create me 2 boxes with epsilon and delta in the point (1,1)
        epsilon = 1
        delta = 1
        point = axes.coords_to_point(1.5, func(1.5))
        dot = Dot(point, color=YELLOW)


        # Epsilon box (vertical)
        epsilon_box = Rectangle(
            width=3 * axes.x_axis.unit_size, 
            height=epsilon * axes.y_axis.unit_size,
            color=ORANGE,
            fill_opacity=0.4,
            stroke_width=2
        ).move_to(point)
        delta_box = Rectangle(
            width=delta * axes.x_axis.unit_size,
            height=3 * axes.y_axis.unit_size,
            color=PURPLE,
            fill_opacity=0.4,
            stroke_width=2
        ).move_to(point)



        # Add all elements to the scene
        self.add(grid, axes, graph)
        #self.wait(1)
        self.add(math_text_epsilon, math_text_delta)
        #self.wait(1)
        self.add(dot, epsilon_box, delta_box)
        self.wait(1)

