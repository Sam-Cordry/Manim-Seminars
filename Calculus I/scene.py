from manim import *
from math import *

class Intro(Scene):
    def construct(self):
        top_text = Tex("Welcome to", font_size=72).shift(UP)
        middle_text = Tex("Calculus I", font_size=72).next_to(top_text, DOWN)
        bottom_text = Tex("with Sam Cordry (@samc)", font_size=32).next_to(middle_text, 4 * DOWN)

        limit1_text = Tex("\\[ \\lim_{x\\to\\infty} f(x) \\]").shift(5 * LEFT).shift(3 * UP)

        derivative1_text = Tex("\( f(x) = x^2 \)", font_size=48).shift(5 * RIGHT).shift(2 * DOWN)
        derivative2_text = Tex("\( f^\prime(x) = 2x \)", font_size=48).next_to(derivative1_text, DOWN)

        left_axes = Axes(
            x_range=[-4, 4, 2],
            y_range=[0, 6, 2],
            axis_config={"include_numbers": True, "tip_shape": StealthTip},
            x_length = 3,
            y_length = 2,
            tips=False
        ).shift(5 * LEFT).shift(2 * DOWN)
        left_graph = left_axes.plot(lambda x: x ** 2, x_range=[-sqrt(6), sqrt(6)], use_smoothing=True)

        # right_axes = Axes()

        self.play(Write(top_text))
        self.play(Write(middle_text))
        self.play(Write(bottom_text))

        self.play(Write(limit1_text))

        self.play(Write(derivative1_text))
        self.play(Write(derivative2_text))

        self.play(Create(left_axes))
        self.play(Create(left_graph))
        # self.play(Create(right_graph))

        self.wait(1)
