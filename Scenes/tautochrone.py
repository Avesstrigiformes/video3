from manim import *
from numpy import pi, array
from Scenes.brachistochrone import acceleration2, brachistochrone, brachistochrone1, dot1, dot2, dot3, start_label, end_label

#Intro 

placeholder = Dot([0,3,0])
PROBLEM = Tex(r"In this video we will derive the tautochrone\\ and the brachistochrone equations.").shift(UP)
t = Tex(r"Derivation:").shift(DOWN)
PROBLEM.next_to(placeholder, DOWN)
rect = SurroundingRectangle(PROBLEM, fill_color=WHITE, fill_opacity=0.2, buff=0.1, color=GREEN)
rect.set_z_index(-1)
tauto = Text(r"ταὐτόχρόνος", font="Arial", font_size=100).set_color_by_gradient(RED, GREEN)
tauto0 = MathTex(r"\underbrace{\qquad\qquad}_{\text{same time}}", font_size=100).set_color_by_gradient(RED, GREEN)
t0 = Tex(r"We want to fix: $\int dt$").shift(UP*2).scale(2)

#Tautochrone Graph

brachistochrone2 = brachistochrone(t_range = array([1.5, pi]))
brachistochrone3 = brachistochrone(t_range = array([2.5, pi]))
code0 = '''
blue = ParametricFunction(
lambda t: array([?, ?, ?]),
t_range = array([?, ?])
)'''
rendered_code0 = Code(
    code_string=code0,
    language="python",
    background="window",
    background_config={"stroke_color": "maroon"},
).scale(0.4).to_corner(UR)
tinfo = Tex(r"We want to find the equation of the curve which $''$the time taken by an\\ object sliding without friction in uniform gravity to its lowest point is\\ independent of its starting point on the curve$''$").scale(0.6).move_to(UR*2 + DOWN)
tstart = Tex(r"Let's start").scale(1.3).set_color(ORANGE)

#Tautochrone

t1 = MathTex(r"t = \frac{s}{v}")
t2 = MathTex(r"dt = \frac{ds}{v}")
t3 = MathTex(r"mgy = \frac{1}{2}mv^2")
t31 = MathTex(r"E_{i} = E_{f}")
t4 = MathTex(r"v = \sqrt{2gy}")
t5 = MathTex(r"ds = \sqrt{dx^2+dy^2}")
t51 = MathTex(r"ds = \sqrt{1+(y')^2}dx")
t6 = MathTex(r"dt = \frac{\sqrt{1+(y')^2}}{\sqrt{2gy}}dx")
t61 = MathTex(r"\int dt = \int \frac{\sqrt{1+(y')^2}}{\sqrt{2gy}}dx")
t62 = MathTex(r"T = \int \frac{\sqrt{1+(y')^2}}{\sqrt{2gy}}dx")
def start0(self):
    self.play(Write(t1))
    self.play(TransformMatchingShapes(t1, t2))
    self.play(t2.animate.to_corner(UL).set_color(RED))
    self.play(Write(t31))
    self.play(TransformMatchingShapes(t31, t3))
    self.wait(2)
    self.play(TransformMatchingShapes(t3, t4))
    self.play(t4.animate.to_corner(UR).set_color(RED))
    self.play(Write(t5))
    self.play(TransformMatchingShapes(t5, t51))
    self.play(t2.animate.move_to(ORIGIN), t51.animate.to_edge(UP).set_color(RED))
    tt = VGroup(t2, t4, t51)
    self.wait(2)
    self.play(TransformMatchingShapes(tt, t6))
    self.play(TransformMatchingShapes(t6, t61))
    self.play(ReplacementTransform(t61, t62))
t7 = Tex(r"We want to make $T$ a constant").to_edge(UP)
t8 = MathTex(r"\text{Let's set: }x &= A(t-\sin(t))\\ y &= A(1-\cos(t));\\ dx &= A(1-\cos(t))dt\\ dy &= A\sin(t)dt").shift(DOWN*2.4).set_color(YELLOW)
t9 = MathTex(r"T = \int \frac{\sqrt{(x')^2+(y')^2}}{\sqrt{2gy}}").shift(UP)
t10 = MathTex(r"T = \int \frac{\sqrt{A^2(1-\cos(t))^2+A^2\sin^2(t)}}{\sqrt{2gA(1-\cos(t))}}dt").shift(UP)
t11 = MathTex(r"T = \int \frac{A\sqrt{1-2\cos(t)+\cos^2(t)+\sin^2(t)}}{\sqrt{2gA(1-\cos(t))}}dt").shift(UP)
t12 = MathTex(r"T = \int \frac{A\sqrt{2-2\cos(t)}}{\sqrt{2gA(1-\cos(t))}}dt").shift(UP)
t13 = MathTex(r"T = \int \frac{A\sqrt{2(1-\cos(t))}}{\sqrt{2gA(1-\cos(t))}}dt").shift(UP)
t14 = MathTex(r"T = \int \frac{\sqrt{A}\sqrt{2}}{\sqrt{2g}}dt").shift(UP)
t15 = MathTex(r"T = \int \frac{\sqrt{A}}{\sqrt{g}}dt").shift(UP)
t16 = MathTex(r"\sqrt{\frac{A}{g}}\int dt").shift(UP)
t17 = Tex(r"")