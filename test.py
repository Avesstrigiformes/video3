from manim import *
class Test(Scene):
    def construct(self):
        a = MathTex("a").to_edge(DOWN).shift(LEFT)
        self.play(Write(a))
        '''        
        def create_glow(mobject, strength, color=WHITE):
            glow_group = VGroup()
            for dx in range(strength):
                new_line = Line(mobject.get_edge_center(LEFT) + 0.01*dx*LEFT, mobject.get_edge_center(RIGHT) + 0.01*dx*RIGHT, stroke_width=8*dx, color=color, stroke_opacity=(1-0.09*dx)**3)
                new_line.set_z_index(-1*dx)
                glow_group.add(new_line)
            return glow_group'''
        self.wait(4)