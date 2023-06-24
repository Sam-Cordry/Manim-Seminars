from manim import *
from math import *

class IntroScene(Scene):
    def construct(self):
        top_text = Tex("Welcome to", font_size=72).shift(UP)
        middle_text = Tex("Calculus I", font_size=72).next_to(top_text, DOWN)
        bottom_text = Tex("with Sam Cordry (@samc)", font_size=32).next_to(middle_text, 4 * DOWN)

        limit_text = Tex("\\[ \\lim_{h\\to 0} \\frac{f(x + h) - f(x)}{h} \\]").shift(4.5 * LEFT).shift(2.5 * UP)

        derivative1_text = Tex("\( f(x) = x^2 \)", font_size=48).shift(4.5 * RIGHT).shift(2 * DOWN)
        derivative1_text_copy = Tex("\( f(x) = x^2 \)", font_size=48).shift(4.5 * RIGHT).shift(2 * DOWN)

        derivative2_text = Tex("\( df = 2x\ dx \)", font_size=48).next_to(derivative1_text, DOWN)

        right_axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 6, 2],
            axis_config={"include_numbers": True},
            x_length=3,
            y_length=2,
            tips=False
        ).shift(5 * RIGHT, 2 * UP)
        right_graph = right_axes.plot(lambda x: x ** 2, x_range=[-sqrt(6), sqrt(6)])
        
        left_axes = Axes(
            x_range=[-2, 2, 1],
            y_range=[-4, 4, 2],
            axis_config={"include_numbers": True},
            x_length=3,
            y_length=3,
            tips=False
        ).shift(5 * LEFT, 2 * DOWN)
        left_graph = left_axes.plot(lambda x: 2 * x, x_range=[-2, 2])

        self.play(Write(top_text))
        self.play(Write(middle_text))
        self.play(Write(bottom_text))

        self.play(Write(limit_text))

        self.play(Create(right_axes))
        self.play(Create(right_graph))

        self.play(Create(left_axes))
        self.play(Create(left_graph))

        self.play(Write(derivative1_text), Write(derivative1_text_copy))
        self.play(Transform(derivative1_text_copy, derivative2_text))


class OverwhelmingScene(Scene):
    def construct(self):
        constant_text = Tex("\( \\frac{d}{dx}(a) = 0 \)", font_size=32).shift(3.5 * UP, 5 * LEFT)
        linear_text = Tex("\( \\frac{d}{dx}(x) = 1 \)", font_size=32).next_to(constant_text, DOWN)
        sine_text = Tex("\( \\frac{d}{dx}(\\sin(x)) = \\cos(x) \)", font_size=32).next_to(linear_text, DOWN)
        cosine_text = Tex("\( \\frac{d}{dx}(\\cos(x)) = -\\sin(x) \)", font_size=32).next_to(sine_text, DOWN)
        tangent_text = Tex("\( \\frac{d}{dx}(\\tan(x)) = \\sec^2(x) \)", font_size=32).next_to(cosine_text, DOWN)
        secant_text = Tex("\( \\frac{d}{dx}(\\sec(x)) = \\sec(x)\\tan(x) \)", font_size=32).next_to(tangent_text, DOWN)
        cosecant_text = Tex("\( \\frac{d}{dx}(\\csc(x)) = -\\csc(x)\\cot(x) \)", font_size=32).next_to(secant_text, DOWN)
        cotangent_text = Tex("\( \\frac{d}{dx}(\\cot(x)) = -\\csc^2(x) \)", font_size=32).next_to(cosecant_text, DOWN)

        arcsine_text = Tex("\( \\frac{d}{dx}(sin^{-1}(x)) = \\frac{1}{\\sqrt{1 - x^2}} \)", font_size=32).next_to(constant_text, 7.5 * RIGHT)
        arccosine_text = Tex("\( \\frac{d}{dx}(cos^{-1}(x)) = -\\frac{1}{\\sqrt{1 - x^2}} \)", font_size=32).next_to(arcsine_text, DOWN)
        arctangent_text = Tex("\( \\frac{d}{dx}(tan^{-1}(x)) = \\frac{1}{1 + x^2} \)", font_size=32).next_to(arccosine_text, DOWN)
        e_text = Tex("\( \\frac{d}{dx}(e^x) = e^x \)", font_size=32).next_to(arctangent_text, DOWN)
        exponential_text = Tex("\( \\frac{d}{dx}(a^x) = a^x\\ln(a) \)", font_size=32).next_to(e_text, DOWN)
        ln_text = Tex("\( \\frac{d}{dx}(\\ln(x)) = \\frac{1}{x} \)", font_size=32).next_to(exponential_text, DOWN)
        logarithm_text = Tex("\( \\frac{d}{dx}(\\log_a(x)) = \\frac{1}{x\\ln(a)} \)", font_size=32).next_to(ln_text, DOWN)

        const_mult_text = Tex("\( \\frac{d}{dx}(af(x)) = af'(x) \)", font_size=32).next_to(arcsine_text, 8 * RIGHT)
        add_sub_text = Tex("\( \\frac{d}{dx}(f(x) \\pm g(x)) = f'(x) \\pm g'(x) \)", font_size=32).next_to(const_mult_text, DOWN)
        product_text = Tex("\( \\frac{d}{dx}(f(x)g(x)) = f(x)g'(x) + g(x)f'(x) \)", font_size=32).next_to(add_sub_text, DOWN)
        quotient_text = Tex("\( \\frac{d}{dx}(\\frac{f(x)}{g(x)}) = \\frac{g(x)f'(x) - f(x)g'(x)}{(g(x))^2} \)", font_size=32).next_to(product_text, DOWN)
        chain_text = Tex("\( \\frac{d}{dx}(f(g(x))) = f'(g(x))g'(x) \)", font_size=32).next_to(quotient_text, DOWN)

        self.add(constant_text, linear_text, sine_text, cosine_text, tangent_text, secant_text, cosecant_text, cotangent_text, arcsine_text, arccosine_text, arctangent_text)
        self.add(e_text, exponential_text, ln_text, logarithm_text, const_mult_text, add_sub_text, product_text, quotient_text, chain_text)


class ContentsScene(Scene):
    def construct(self):
        title_text = Tex("Content To Cover").shift(3 * UP)

        chapters = []

        chapters.append(Tex("1. What is Calculus?").next_to(title_text, 5 * DOWN))
        chapters.append(Tex("2. Derivatives"))
        chapters.append(Tex("3. Limits"))
        chapters.append(Tex("4. L'Hopital's Rule"))
        chapters.append(Tex("5. Applications of Derivatives"))
        chapters.append(Tex("6. Integrals"))
        chapters.append(Tex("7. Applications of Integrals"))

        for i in range(1, 7):
            chapters[i].next_to(chapters[i - 1], DOWN)

        self.play(Write(title_text))
        
        for i in range(7):
            self.play(Write(chapters[i]))


class Chapter1Scene(Scene):
    def construct(self):
        chapter = Tex("\\underline{Chapter 1}").shift(UP)
        title = Tex("What is Calculus?")
        self.play(Write(chapter))
        self.play(Write(title))

        self.wait(1)
        self.play(Homotopy(MoveUp3Munits, title, run_time=1.5), FadeOut(chapter), run_time=.5)
        self.wait(10)
        
        numberLine = NumberLine(
            x_range=[0, 5, 1],
            length=10,
            include_numbers=True
        ).shift(DOWN)
        car = SVGMobject(file_name="car.svg", height=1, fill_color=WHITE, stroke_color=BLACK).align_to(numberLine, LEFT).shift(LEFT)

        self.play(Create(numberLine))

        self.play(Create(car))
        self.play(Homotopy(MoveCar, car, run_time=3))

        time = Tex("3 seconds").shift(2 * DOWN)
        self.play(Write(time))

        group = VGroup(numberLine, car, time)
        group.generate_target()
        group.target.scale(.5)
        group.target.shift(3.5 * LEFT + 2 * UP)

        self.play(MoveToTarget(group))

        can_do = Tex("What you know how to do:", font_size=12).next_to(group).shift(UP + RIGHT)

        self.play(Write(can_do))

        average_velocity = Tex("Average Velocity:").next_to(group).shift(RIGHT)
        avg_velocity = Tex("\( \\frac{\\Delta x}{\\Delta t} \)").next_to(average_velocity).shift(RIGHT)
        answer = Tex("\( = \\frac{5}{3} \\frac{\\text{meters}}{\\text{seconds}} \)").next_to(avg_velocity, RIGHT)

        self.play(Write(average_velocity))
        self.play(Write(avg_velocity))
        self.play(Write(answer))

        question1 = Tex("How fast is the car moving at t = 2 seconds?").shift(DOWN)
        question2 = Tex("Is the car ever moving faster than 5/3 m/s?").shift(2 * DOWN)

        self.play(Write(question1, run_time=3))
        self.play(Write(question2, run_time=3))

        self.play(FadeOut(group), FadeOut(avg_velocity), FadeOut(answer), FadeOut(question1), FadeOut(question2), run_time=2)

        self.wait(3)

class Chapter2Scene(Scene):
    def construct(self):
        title = Tex("Derivatives")
        self.play(Write(title))
        self.wait(1)
        self.play(Homotopy(MoveUp3Munits, title, run_time=1))
        self.wait(1)

class Chapter3Scene(Scene):
    def construct(self):
        title = Tex("Limits")
        self.play(Write(title))
        self.wait(1)
        self.play(Homotopy(MoveUp3Munits, title, run_time=1))
        self.wait(1)

class Chapter4Scene(Scene):
    def construct(self):
        title = Tex("l'Hopital's Rule")
        self.play(Write(title))
        self.wait(1)
        self.play(Homotopy(MoveUp3Munits, title, run_time=1))
        self.wait(1)

class Chapter5Scene(Scene):
    def construct(self):
        title = Tex("Applications of Derivatives")
        self.play(Write(title))
        self.wait(1)
        self.play(Homotopy(MoveUp3Munits, title, run_time=1))
        self.wait(1)

class Chapter6Scene(Scene):
    def construct(self):
        title = Tex("Integrals")
        self.play(Write(title))
        self.wait(1)
        self.play(Homotopy(MoveUp3Munits, title, run_time=1))
        self.wait(1)

class Chapter7Scene(Scene):
    def construct(self):
        title = Tex("Applications of Integrals")
        self.play(Write(title))
        self.wait(1)
        self.play(Homotopy(MoveUp3Munits, title, run_time=1))
        self.wait(1)

def MoveUp3Munits(x, y, z, t):
    return [x, 3 * t + y, z]

def MoveCar(x, y, z, t):
    return [(t ** 2) * 10 + x, y, z]
