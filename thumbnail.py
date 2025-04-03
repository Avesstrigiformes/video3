from manim import *
from Scenes.brachistochrone import brachistochrone
class Thumbnail(Scene):
    def construct(self):
        def create_glow(mobject, strength, color=WHITE):
            glow_group = VGroup()
            for dx in range(1, strength + 1):
                glow = mobject.copy()
                glow.set_stroke(
                    color=color,
                    width=mobject.get_stroke_width() + 1.2*dx,
                    opacity=max(0, 1 - 0.009*(dx) ** 3)
                )
                glow.set_z_index(-dx)
                glow.scale(1 + 0.003 * dx)
                glow_group.add(glow)
            return glow_group
        a = MathTex(r"\int dt").scale(2)
        b = brachistochrone().set_color_by_gradient([PURE_RED, PURE_BLUE]).set_sheen_direction(UR)
        c = Tex(r"Minimize").scale(2).set_color(PURE_RED).shift(DL*2.7)
        d = Tex(r"Constant").scale(2).set_color(PURE_BLUE).shift(UR*2.7)
        lol = create_glow(c, 12, color=PURE_RED)
        lol2 = create_glow(d, 12, color=PURE_BLUE)
        lol3 = create_glow(a, 12)
        rect = SurroundingRectangle(VGroup(a,b), fill_color=WHITE, fill_opacity=0.1, buff=1).set_color_by_gradient([PURE_RED, PURE_BLUE]).set_sheen_direction(UR)
        self.add(a, b, c, d, rect, lol, lol2, lol3)