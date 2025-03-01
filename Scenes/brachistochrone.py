from manim import *
from numpy import sin, cos, pi, array

#Intro

brachisto = Text(r"βράχιστος χρόνος", font="Arial", font_size=100).set_color_by_gradient(RED, GREEN)
brachisto0 = MathTex(r"\underbrace{\qquad\qquad\qquad}_{\text{shortest time}}", font_size=100).set_color_by_gradient(RED, GREEN)
r1 = Tex(r"We want to minimize: $\int dt$").shift(UP*2).scale(2)
a0 = MathTex(r"?").scale(6).set_color(PURPLE_C)
binfo = Tex("We want to find the equation of the curve which $''$the time taken by an object sliding without friction in uniform gravity to its lowest point is the shortest time possible$''$").scale(0.6).to_edge(DOWN).shift(LEFT)
bstart = Tex("Let's start").scale(1.3).set_color(BLUE)

#Im not gonna write a realistic code for this, but you get the idea lol

def acceleration2(t):
    return t**2

#Create the brachistochrone curve

start = array([-4.5, 2.5, 0])
end = array([4.5, -2.5, 0])
def brachistochrone(start = start, end = end, t_range=array([0, pi])):
    return ParametricFunction(
        lambda t: array([
            start[0] + (end[0] - start[0])*(t - sin(t)) / (pi - sin(pi)),
            start[1] - (start[1] - end[1])*(1 - cos(t)) / (1 - cos(pi)),
            0
        ]),
        t_range=t_range,
        color=BLUE
    )

brachistochrone1 = brachistochrone()
code1 = '''
blue = ParametricFunction(
    lambda t: array([
        start[0] + (end[0] - start[0])*(t - sin(t)) / (pi - sin(pi)),
        start[1] + (end[1] - start[1])*(1 - cos(t)) / (1 - cos(pi)),
        0
    ]),
    t_range = array([0, pi])
)'''
code2 = '''red = Line(start, end)'''
code3 = '''
green = ParametricFunction(
    lambda t: array([
        start[0] + (end[0] - start[0])*(t**20),
        start[1] + (end[1] - start[1])*t,
        0
    ]),
    t_range = array([0, 1])
)'''
straight = Line(start, end, color=RED)
arc = ParametricFunction(
    lambda t: array([
        start[0] + (end[0] - start[0])*(t**20),
        start[1] + (end[1] - start[1])*t,
        0
    ]),
    t_range = array([0, 1]),
    color = GREEN
)
start_label = Text("Start", font_size=24).next_to(start, UP)
end_label = Text("End", font_size=24).next_to(end, DOWN)
dot1 = Dot(start, color=YELLOW, radius=0.1)
dot2 = Dot(start, color=YELLOW, radius=0.1)
dot3 = Dot(start, color=YELLOW, radius=0.1)
rendered_code1 = Code(
    code_string=code1,
    language="python",
    background="window",
    background_config={"stroke_color": "maroon"},
).scale(0.4).to_corner(UR)
rendered_code2 = Code(
    code_string=code2,
    language="python",
    background="window",
    background_config={"stroke_color":  "maroon"},
).scale(0.4)
rendered_code3 = Code(
    code_string=code3,
    language="python",
    background="window",
    background_config={"stroke_color": "maroon"},
).scale(0.4)

#Brachistochrone
