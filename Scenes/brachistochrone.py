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
arcf = ParametricFunction(
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

b00 = Tex(r"We want to minimize: $T$").to_edge(UP)
b01 = Tex(r"Notice that this integral doesn't depend on the x explicitly").shift(DOWN*1.2)
b02 = Tex(r"Therefore, we should use an another version of the\\ Euler-Lagrange equation, i.e., the Beltrami identity").next_to(b01, DOWN)
b03 = MathTex(r"\overbrace{\qquad\qquad}^{F(y,y')}").shift(UP*1.1+RIGHT*0.5).scale(1.2)
b04 = Tex(r"Don't worry about the boundary conditions for now*").to_corner(DR).scale(0.4)

j1 = MathTex(r"\text{Recall: }F=(1+y'^{2})^{1/2}(2gy)^{-1/2}")
j2 = MathTex(r"\frac{\partial F}{\partial y'}=(2gy)^{-1/2}(1+y'^{2})^{-1/2}y'")
j3 = MathTex(r"\sqrt{\frac{1+y'^{2}}{2gy}}-y'\frac{y'}{\sqrt{2gy}\sqrt{1+y'^{2}}}=C")
j4 = MathTex(r"\frac{1+y'^2-y'^2}{\sqrt{2gy}\sqrt{1+y'^{2}}}=C")
j5 = MathTex(r"\frac{1}{\sqrt{y(1+y'^{2})}}=\sqrt{2g}C")
j6 = MathTex(r"\frac{1}{2gC^2}=y(1+y'^2)")
j7 = MathTex(r"C_0=\frac{1}{2gC^2}").to_corner(UL).set_color(GREEN)
j8 = MathTex(r"C_0=y(1+y'^2)")
j9 = MathTex(r"\sqrt{\frac{C_0-y}{y}}=y'")
j10 = MathTex(r"\sqrt{\frac{y}{C_0-y}}dy=dx")
j11 = MathTex(r"\int\sqrt{\frac{y}{C_0-y}}dy=\int dx")
j12 = MathTex(r"\int\sqrt{\frac{y}{C_0-y}}dy=x+C_1")
j13 = Tex(r"We can solve this integral using the trig substitution").to_edge(DOWN).set_color(RED)
j14 = MathTex(r"\int\sqrt{\frac{y}{C_0-y}}dy")
j15 = MathTex(r"y = C_0\sin^2(t)").set_color(BLUE)
j16 = MathTex(r"dy = 2C_0\sin(t)\cos(t)dt").next_to(j15, DOWN).set_color(BLUE)
j17 = MathTex(r"0<t<\frac{\pi}{2}*").to_corner(DR).scale(0.8)
j18 = MathTex(r"\int\sqrt{\frac{C_0\sin^2(t)}{C_0-C_0\sin^2(t)}}dy").to_corner(UL).set_color(PURE_RED)
j19 = MathTex(r"\int\sqrt{\frac{C_0\sin^2(t)}{C_0-C_0\sin^2(t)}}2C_0\sin(t)\cos(t)dt").to_corner(UL).set_color(PURE_RED)
j20 = MathTex(r"\int\sqrt{\frac{C_0\sin^2(t)}{C_0\cos^2(t)}}2C_0\sin(t)\cos(t)dt")
j21 = MathTex(r"\int\tan(t)2C_0\sin(t)\cos(t)dt")
j22 = MathTex(r"2C_0\int\sin^2(t)dt")
j23 = MathTex(r"\int\sin^2(t)dt=\int\frac{1-\cos(2t)}{2}dt").shift(DOWN*2)
j24 = MathTex(r"\int\sin^2(t)dt=\frac{t}{2}-\frac{\sin(2t)}{4}+C_2").shift(DOWN*2)
j25 = MathTex(r"2C_0\left(\frac{t}{2}-\frac{\sin(2t)}{4}\right)+C_3")
j26 = MathTex(r"C_0t-\frac{C_0\sin(2t)}{2}+C_3")
j27 = MathTex(r"x(t)=C_0t-\frac{C_0\sin(2t)}{2}+D").set_color(BLUE)
j28 = MathTex(r"\text{Recall: }y(t)=C_0\sin^2(t)").set_color(BLUE).next_to(j27, DOWN)
j29 = MathTex(r"\text{Assume: }x(0)=y(0)=0\Rightarrow D=0\\\textit{ (the particle starts at the origin)}").shift(UP*2)
j30 = MathTex(r"x(t)=C_0t-\frac{C_0\sin(2t)}{2}").set_color(BLUE)
j31 = MathTex(r"\sin^2(t)=\frac{1-\cos(2t)}{2}").next_to(j28, DOWN)
j32 = MathTex(r"y(t)=\frac{C_0}{2}(1-\cos(2t))").set_color(BLUE).next_to(j27, DOWN)
j33 = Tex(r"If we set $t=\frac{x}{2}$, we get the equation of cycloid!").shift(UP*2)
j34 = MathTex(r"x(t)=C_0\frac{x}{2}-\frac{C_0\sin(x)}{2}").set_color(BLUE)
j35 = MathTex(r"y(t)=\frac{C_0}{2}(1-\cos(x))").set_color(BLUE).next_to(j34, DOWN)
j36 = MathTex(r"x(t)=A(t-\sin(t))").set_color(BLUE)
j37 = MathTex(r"y(t)=A(1-\cos(t))").set_color(BLUE).next_to(j36, DOWN)
j38 = Tex(r"We will derive the cycloid equation at the end of the video").shift(DOWN*3).set_color(PURE_BLUE)

endrect = SurroundingRectangle(VGroup(j36, j37), buff=0.1, color=PURE_BLUE)
endrect.set_z_index(-1)