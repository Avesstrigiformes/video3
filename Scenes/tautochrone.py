from manim import *
from numpy import pi, array
from Scenes.brachistochrone import brachistochrone

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

#Tautochrone Graph 2

cyc = ParametricFunction(
    lambda t: np.array([
        -2*(t - np.sin(t)),
        -2*(1 - np.cos(t)),
        0
    ]),
    t_range = np.array([-4, 0]),
    color = BLUE
)

ax = Axes(
    x_range=[0, 5, 1],
    y_range=[-2, 0, 1],
    axis_config={"color": WHITE, "include_numbers": True},
    tips=False
)

cyc.shift(ax.c2p(0, 0))
end_point = Dot(cyc.get_start(), color=PURE_GREEN)

dotlabelcyc = MathTex(r"(r(t_f-\sin(t_f)), r(1-\cos(t_f))").next_to(end_point, UP).set_color(PURE_GREEN)
dot2cyc = Dot(color = PURE_GREEN)
dot2labelcyc = MathTex(r"(x_0(t_0), y_0(t_0))").set_color(PURE_GREEN).next_to(dot2cyc, DOWN)

def update_cycloid_and_dot(mob, alpha):
    new_t_range = [(4 - pi) * alpha - 4, 0]
    new_cycloid = ParametricFunction(
        lambda t: np.array([
            -2*(t - np.sin(t)),
            -2*(1 - np.cos(t)),
            0
        ]),
        t_range=np.array(new_t_range),
        color=BLUE
    )
    new_cycloid.shift(ax.c2p(0, 0))
    mob.become(new_cycloid)
    if new_cycloid.has_points():
        end_point.move_to(new_cycloid.get_start())

#Tautochrone

t1 = MathTex(r"t = \frac{s}{v}")
t2 = MathTex(r"dt = \frac{ds}{v}")
t3 = MathTex(r"mgy = \frac{1}{2}mv^2")
t310 = MathTex(r"E_{i} = E_{f}")
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
    self.play(Write(t310))
    self.play(TransformMatchingShapes(t310, t3))
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
    self.play(FadeTransform(t61, t62))
t7 = Tex(r"We want to make $T$ a constant").to_edge(UP)
t8 = MathTex(r"\text{Let's set: }x &= A(t-\sin(t))\\ y &= A(1-\cos(t));\\ dx &= A(1-\cos(t))dt\\ dy &= A\sin(t)dt").shift(DOWN*2.4).set_color(YELLOW)
t9 = MathTex(r"T = \int \frac{\sqrt{(dx)^2+(dy)^2}}{\sqrt{2gy}}").shift(UP)
t10 = MathTex(r"T = \int \frac{\sqrt{A^2(1-\cos(t))^2+A^2\sin^2(t)}}{\sqrt{2gA(1-\cos(t))}}dt").shift(UP)
t11 = MathTex(r"T = \int \frac{A\sqrt{1-2\cos(t)+\cos^2(t)+\sin^2(t)}}{\sqrt{2gA(1-\cos(t))}}dt").shift(UP)
t12 = MathTex(r"T = \int \frac{A\sqrt{2-2\cos(t)}}{\sqrt{2gA(1-\cos(t))}}dt").shift(UP)
t13 = MathTex(r"T = \int \frac{A\sqrt{2(1-\cos(t))}}{\sqrt{2gA(1-\cos(t))}}dt").shift(UP)
t14 = MathTex(r"T = \int \frac{\sqrt{A}\sqrt{2}}{\sqrt{2g}}dt").shift(UP)
t15 = MathTex(r"T = \int \frac{\sqrt{A}}{\sqrt{g}}dt").shift(UP)
t16 = MathTex(r"\sqrt{\frac{A}{g}}\int dt").shift(UP)
t17 = Tex(r"We found that the time taken from the top to the bottom\\ of the curve is $\sqrt{\frac{A}{g}}t$")
t18 = Tex(r"We need to show that this is independent of the\\ starting point on the curve").shift(DOWN*0.5)
t19 = MathTex(r"\text{Recall: }v = \sqrt{2gy}")
t20 = MathTex(r"\text{In this case: }v = \sqrt{2g(y-y_0)}")
t21 = MathTex(r"T = \int \frac{\sqrt{(x')^2+(y')^2}}{\sqrt{2g(y-y_0)}}")
t211 = MathTex(r"T = \int_{t_0}^{t_f} \frac{\sqrt{(x')^2+(y')^2}}{\sqrt{2g(y-y_0)}}")
t22 = MathTex(r"T = \int_{t_0}^{t_f} \frac{\sqrt{2A^2(1-\cos(t))}}{\sqrt{2gA(\cos(t_0)-\cos(t))}}dt")
t23 = MathTex(r"T = \sqrt{\frac{A}{g}}\int_{t_0}^{t_f} \frac{\sqrt{(1-\cos(t))}}{\sqrt{(\cos(t_0)-\cos(t))}}dt")
t24 = MathTex(r"\text{Half Angle Formulas :}\\ \cos(\frac{1}{2}t) = \pm\sqrt{\frac{1+\cos(x)}{2}}\\ \sin(\frac{1}{2}t) = \pm\sqrt{\frac{1-\cos(x)}{2}}").set_color(BLUE)
t25 = MathTex(r"\text{Half Angle Formulas :}\\ \cos(t) = 2\cos^2(\frac{1}{2}t)-1\\ \sin(\frac{1}{2}t) = \pm\sqrt{\frac{1-\cos(x)}{2}}").set_color(BLUE)
t26 = MathTex(r"T = \sqrt{\frac{A}{g}}\int_{t_0}^{t_f} \frac{\sqrt{2\sin^2(\frac{1}{2}t)}}{\sqrt{2}\sqrt{(\cos^2(\frac{1}{2}t_0)-\cos^2(\frac{1}{2}t))}}dt")
t27 = MathTex(r"T = \sqrt{\frac{A}{g}}\int_{t_0}^{t_f} \frac{\sin(\frac{1}{2}t)}{\sqrt{(\cos^2(\frac{1}{2}t_0)-\cos^2(\frac{1}{2}t))}}dt")
integralinfo = Tex(r"We can solve this integral using U-Substitution").to_edge(UP).set_color(RED)
integralsub = MathTex(r"u = \frac{\cos(\frac{1}{2}t)}{\cos(\frac{1}{2}t_0)}").shift(DOWN*2 + LEFT*2).set_color(RED)
integralsub2 = MathTex(r"du = -\frac{\frac{1}{2}\sin(t)}{2\cos(\frac{1}{2}t_0)}dt").shift(DOWN*2 + RIGHT*2).set_color(RED)
integralsub3 = MathTex(r"t = t_0 \Rightarrow u = 1\\ t = t_f \Rightarrow u = \frac{\cos(\frac{1}{2}t_f)}{\cos(\frac{1}{2}t_0)}").shift(UP*2.5).set_color(RED)
t28 = MathTex(r"T = -2\sqrt{\frac{A}{g}}\int_{t_0}^{t_f} -\frac{\sin(\frac{1}{2}t)}{2\cos(\frac{1}{2}t_0)\sqrt{1-\frac{\cos^2(\frac{1}{2}t))}{\cos^2(\frac{1}{2}t_0)}}}dt")
t29 = MathTex(r"T = -2\sqrt{\frac{A}{g}}\int_{1}^{\frac{\cos(\frac{1}{2}t_f)}{\cos(\frac{1}{2}t_0)}} \frac{du}{\sqrt{1-u^2}}").set_color(GREEN)
t30 = MathTex(r"\text{Recall: }\int \frac{du}{\sqrt{1-u^2}} = \sin^{-1}(u)").shift(DOWN*2)
t31 = MathTex(r"T = 2\sqrt{\frac{A}{g}}\int^{1}_{\frac{\cos(\frac{1}{2}t_f)}{\cos(\frac{1}{2}t_0)}} \frac{du}{\sqrt{1-u^2}}").set_color(GREEN)
t32 = MathTex(r"T = 2\sqrt{\frac{A}{g}}\sin^{-1}(u)\biggr\rvert_{\frac{\cos(\frac{1}{2}t_f)}{\cos(\frac{1}{2}t_0)}}^1")
t33 = MathTex(r"\text{Recall: }\sin^{-1}(1) = \frac{\pi}{2}").shift(DOWN*2).set_color(RED)
t34 = MathTex(r"T = \sqrt{\frac{A}{g}}\left(\pi - 2\sin^{-1}\left(\frac{\cos(\frac{1}{2}t_f)}{\cos(\frac{1}{2}t_0)}\right)\right)")
t35 = MathTex(r"\text{If we set }t_f = \pi").shift(UP*2)
t36 = MathTex(r"T = \sqrt{\frac{A}{g}}\pi").set_color_by_gradient(RED, GREEN).to_edge(DOWN)
t37 = Tex(r"We can see that the time taken is independent\\ of the starting point on the curve", font_size = 40).shift(UP*1.7)
addendum = MathTex(r"\sin^{-1}(\cos(\frac{\pi}{2})) = 0").to_corner(DR).scale(0.5)
helpmeout = Tex(r"Let's derive the cycloid equation").scale(1.5).set_color(PURPLE_C)