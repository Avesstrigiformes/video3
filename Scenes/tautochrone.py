from manim import *
from numpy import pi, array
from brachistochrone import acceleration2, brachistochrone, brachistochrone1, dot1, dot2, dot3, start_label, end_label

#Intro 

placeholder = Dot([0,3,0])
PROBLEM = Tex(r"In this video we will derive the tautochrone\\ and the brachistochrone equations.").shift(UP)
t = Tex(r"Derivation:").shift(DOWN)
PROBLEM.next_to(placeholder, DOWN)
rect = SurroundingRectangle(PROBLEM, fill_color=WHITE, fill_opacity=0.2, buff=0.1, color=GREEN)
rect.set_z_index(-1)
tauto = Text(r"ταὐτόχρόνος", font="Arial", font_size=100).set_color_by_gradient(RED, GREEN)
tauto0 = MathTex(r"\underbrace{\qquad\qquad}_{\text{same time}}", font_size=100).set_color_by_gradient(RED, GREEN)
t1 = Tex(r"We want to fix: $\int dt$").shift(UP*2).scale(2)

#Tautochrone

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