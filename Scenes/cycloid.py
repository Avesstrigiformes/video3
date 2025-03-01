from manim import *
from numpy import pi, array
r = 2
circle = Circle(radius=r, color=YELLOW).shift(LEFT*5.9)
groundpoint = array([circle.get_center()[0], -2, 0])
dot = Dot(circle.point_at_angle(-PI / 2), color=RED)
path = TracedPath(dot.get_center, stroke_color=RED, stroke_width=4)
radius = Arrow(circle.get_center(), dot.get_center(), color=GREEN)
centerline = Line(groundpoint, circle.get_center())
groundline = Line(groundpoint, groundpoint, color=GREEN, buff=2)
centerr = MathTex(r"r").next_to(centerline)
perpendicularline = Line(color=GREEN)
info = Tex(r"Let $t = \theta$").to_edge(DOWN)
info2 = Tex(r"Coordinates of the red dot:").to_corner(UL)
minus = MathTex(r"-")
minus2 = MathTex(r"-")
xc = MathTex(r"=r(\theta-\cos\theta)")
yc = MathTex(r"=r(1-\sin\theta)")
final = MathTex(r"(x,y)=(r(\theta-\cos\theta),r(1-\sin\theta))", color=PURE_RED).to_edge(UP)
diagonallines = VGroup()
for x in range(-7, 8, 1):
    diagonal_line = Line(   
        start = array([x + 0.1, -2, 0]),
        end = array([x - 0.5 + 0.1, -2.5, 0]),
        color = WHITE,
        stroke_width = 2
    )
    diagonallines.add(diagonal_line)
axes = Axes(
    x_range = [-13, 13, 1],
    y_range = [-4, 4, 1],
    axis_config = {"include_numbers": True, "color": WHITE},
    x_length = 26,
    y_length = 8,
    tips=False
).move_to(array([circle.get_center()[0] - 0.1, -2, 0]))
angle = Arc()

def update_circle(mob, dt): 
    mob.shift(RIGHT*r*dt) 
    mob.rotate(-dt, about_point=mob.get_center())

def update_dot(mob, dt):
    mob.shift(RIGHT*r*dt)
    mob.rotate(-dt, about_point=circle.get_center())

def update_radius(mob):
    mob.put_start_and_end_on(circle.get_center(), dot.get_center())

def update_centerline(mob):
    mob.put_start_and_end_on(array([circle.get_center()[0], -2, 0]), circle.get_center())

def update_centerr(mob):
    mob.next_to(centerline)

def update_groundline(mob):
    mob.put_start_and_end_on(groundpoint, array([circle.get_center()[0] + 0.001, -2, 0])) #Bug???

def update_perpendicularline(mob):
    mob.put_start_and_end_on(dot.get_center(), array([circle.get_center()[0] + 0.001, dot.get_center()[1], 0])) #Bug???

def trueangle(angle):
    if angle <= pi / -2:
        return angle + pi / 2
    else:
        return angle - 3*pi / 2

def update_angle(mob):
    mob.become(
        Arc(
            radius = 0.5,
            start_angle = - pi / 2,
            angle = trueangle(radius.get_angle()),
            color = BLUE  
        ).move_arc_center_to(circle.get_center())
    )

def update_all():
    circle.add_updater(update_circle)
    dot.add_updater(update_dot)
    radius.add_updater(update_radius)
    centerline.add_updater(update_centerline)
    groundline.add_updater(update_groundline)
    perpendicularline.add_updater(update_perpendicularline)
    angle.add_updater(update_angle)

def remove_all():
    circle.remove_updater(update_circle)
    dot.remove_updater(update_dot)
    radius.remove_updater(update_radius)
    centerline.remove_updater(update_centerline)
    groundline.remove_updater(update_groundline)
    perpendicularline.remove_updater(update_perpendicularline)
    angle.remove_updater(update_angle)

#Outro

end = Tex(r"I hope you found this video useful! You can check out\\ these for similar problems:\\ $\bullet\text{Catenary Problem}$\\ $\bullet\text{Optimal Shape of a Rotating Fluid}$\\ $\bullet\text{Ideal Rocket Equation}$\\ $\bullet\text{Path of a Particle in a Central Force Field}$\\ $\bullet\text{Bubble Equation}$")
end2 = MathTex(r"\boxed{\frac{1}{k}\cosh(kx+A)+B}").to_corner(UL)
end3 = MathTex(r"\boxed{\text{Paraboloid}}").next_to(end2)
end4 = MathTex(r"\boxed{\Delta v=v_{e}+\ln\left(\frac{m_{0}}{m_{f}}\right)}").next_to(end3)
end5 = MathTex(r"---").to_corner(DL)
end6 = MathTex(r"\boxed{\int^{x_2}_{x_1}2\pi f(x)\sqrt{1+(f'(x))^2}dx}").to_corner(DR)
arrow2 = Arrow(end[0][67:83].get_center(), end2.get_center(), color=RED, stroke_width=2, tip_length=0.2)
arrow3 = Arrow(end[0][83:112].get_center(), end3.get_center(), color=RED, stroke_width=2, tip_length=0.2)
arrow4 = Arrow(end[0][112:132].get_center(), end4.get_center(), color=RED, stroke_width=2, tip_length=0.2)
arrow5 = Arrow(end[0][132:168].get_center(), end5.get_center(), color=RED, stroke_width=2, tip_length=0.2)
arrow6 = Arrow(end[0][168::].get_center(), end6.get_center(), color=RED, stroke_width=2, tip_length=0.2)
endgroup = VGroup(end2, end3, end4, end5, end6, arrow2, arrow3, arrow4, arrow5, arrow6)
tfw = Union(*Tex(r"Thanks for Watching").scale(2).copy()[0]).set_color_by_gradient([PURE_RED, PURE_BLUE]).set_sheen_direction(UR)