from manim import *

class TaylorpolynomeT1(ZoomedScene):
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
            x_range=[-2.0, 2.5, 0.5],
            y_range=[0, 8, 1],
            axis_config={"include_numbers": True}
        ).add_coordinates()

        def exp_func(x):
            return np.exp(x)
        
        point = Dot(axes.c2p(0, exp_func(0)), color=YELLOW)
        
        # Create graphs for left and right portions
        left_graph = axes.plot(
            exp_func,
            x_range=[-2.0,-0.01],
            color=BLUE
        ).reverse_points()
        right_graph = axes.plot(
            exp_func,
            x_range=[0.01, 2.0],
            color=BLUE
        )

        # Animate
        self.add(grid, axes)
        self.play(Create(point))
        self.play(Create((left_graph), run_time =2.0))
        self.play(Create((right_graph), run_time =2.0))
        self.wait(1)
