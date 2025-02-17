from manim import *
from tautochrone import *
from brachistochrone import *
from beltrami import *
from cycloid import *


###NOTE: Keep in mind that the video will be long, so you might want to split it into multiple classes if you want to keep track of the code. I will just put everything in one class for rendering purposes.


class Video(Scene):
    def construct(self):
        #Intro
        '''
        self.play(Create(rect), Write(PROBLEM), run_time=5)
        self.wait(5)
        self.play(Write(t))
        self.play(Flash(t, line_length=0.5, num_lines=50, color=GREEN, flash_radius=1.1, time_width=0.5, run_time=2, rate_func = rush_from))
        self.play(FadeOut(PROBLEM, t, rect))
        self.clear()
        '''
        #Tautochrone Intro
        '''
        self.play(Write(tauto))
        self.play(Write(tauto0.next_to(tauto, DOWN)))
        self.play(Write(t1))
        self.wait(2)
        self.play(FadeOut(tauto, tauto0, t1))
        self.clear()
        '''
        #Tautochrone Graph
        '''                   WE WANT TO FIND THE EQUATION OF THE CURVE THAT MAKES THE TIME TAKEN BY A BALL TO ROLL DOWN THE CURVE SAME FOR ALL POINTS ON THE CURVE UNDER THE INFLUENCE OF GRAVITY
        self.play(Create(brachistochrone1))
        self.play(Write(start_label), Write(end_label))
        self.play(Write(rendered_code0))
        self.play(MoveAlongPath(dot1, brachistochrone1), MoveAlongPath(dot2, brachistochrone2), MoveAlongPath(dot3, brachistochrone3), run_time=4, rate_func=acceleration2)
        self.wait(2)
        self.play(FadeOut(brachistochrone1, start_label, end_label, rendered_code0, dot1, dot2, dot3))
        self.clear()
        '''
        #Tautochrone
        #Brachistochrone Intro
        '''
        self.play(Write(brachisto))
        self.play(Write(brachisto0.next_to(brachisto, DOWN)))
        self.play(Write(r1))
        self.wait(2)
        self.play(FadeOut(brachisto, brachisto0, r1))
        self.clear()
        '''
        #Brachistochrone Graph
        '''                   WE WANT TO FIND THE EQUATION OF THE CURVE THAT MAKES THE TIME TAKEN BY A BALL TO ROLL DOWN THE CURVE THE LEAST UNDER THE INFLUENCE OF GRAVITY
        self.play(Create(brachistochrone1), Create(straight), Create(arc))
        self.play(Write(start_label), Write(end_label))
        self.play(Write(rendered_code1), Write(rendered_code2.next_to(rendered_code1, LEFT)), Write(rendered_code3.next_to(rendered_code1, DOWN)))
        self.play(MoveAlongPath(dot1, brachistochrone1, rate_func=acceleration2), MoveAlongPath(dot2, straight, rate_func=acceleration2), MoveAlongPath(dot3, arc, rate_func=acceleration2), run_time=2)
        self.play(Write(a0))
        self.wait(2)
        self.play(FadeOut(brachistochrone1, straight, arc, start_label, end_label, rendered_code1, rendered_code2, rendered_code3, dot1, dot2, dot3, a0))
        self.clear()
        '''
        #Brachistochrone
        #Beltrami
        '''
        self.play(Write(b1))
        self.play(Write(b10),Write(b11.next_to(b10, UP)))
        self.play(FadeOut(b10), FadeOut(b11), ReplacementTransform(b1,b2))
        self.play(ReplacementTransform(b2,b20))
        self.play(Write(b3))
        self.play(ReplacementTransform(b3,b4))
        self.play(FadeOut(b20[0][15::],b4[0][15::]), b20[0][:15].animate.move_to(b4[0][15::].get_center() + RIGHT*0.8).set_color(WHITE))
        self.play(b204.animate.to_corner(UL).set_color(GREEN))
        self.play(Write(b5))
        self.play(FadeOut(b5[0][25::], b204[1]), b204[0].animate.move_to(b5[0][25::].get_center() + RIGHT*0.1).set_color(RED))
        arc = ArcBetweenPoints(b204[0][:5].get_center(), b5[0][14].get_center() + RIGHT*0.7, angle=PI)
        self.play(FadeOut(b5[0][15:25], b204[0][5::]), MoveAlongPath(b204[0][:5], arc), b5[0][14].animate.move_to(RIGHT*0.6), Write(b50.next_to(b5[0][13], RIGHT)))
        self.play(Write(b51.next_to(b5[0][14], RIGHT)))
        self.play(ReplacementTransform(VGroup(b204[0][:5], b5[0][:15], b50, b51), b6))
        self.play(ReplacementTransform(b6, b7))
        self.clear()
        '''
        #Brachistochrone 2
        #Cycloid
        '''
        self.play(Create(axes), Create(diagonallines))
        self.play(Create(circle), Create(dot), Create(path), Write(info))
        self.add(radius, centerline, centerr, perpendicularline, groundline, angle)
        update_all()
        centerr.add_updater(update_centerr)
        self.wait(1)
        remove_all()
        r2 = MathTex(r"r").next_to(radius.get_center(), 0.8*UL + 0.2*RIGHT)
        theta = MathTex(r"\theta", font_size=36).set_color(BLUE).next_to(circle.get_center(), 2*DL + 0.65*RIGHT)
        rsint = MathTex(r"r\sin\theta", font_size=36).next_to(perpendicularline.get_center(), 0.6*DOWN)
        rcost = MathTex(r"r\cos\theta", font_size=36).next_to(circle.get_center(), DR + 0.4*DOWN + 0.1*LEFT)
        rt = MathTex(r"r\theta", font_size=36).next_to(groundline.get_center(), 2.2*DOWN)
        inal = VGroup(centerr, rsint, rcost, rt, minus, minus2, xc, yc, info2)
        rsint[0][4].set_color(BLUE)
        rcost[0][4].set_color(BLUE)
        rt[0][1].set_color(BLUE)
        self.play(Write(r2), Write(theta), Write(rsint), Write(rcost), Write(rt))
        self.play(Write(info2))
        self.play(rt.animate.next_to(info2).scale(48 / 36))
        self.play(Write(minus.next_to(rt)))
        self.play(rsint.animate.next_to(minus, 1.3*RIGHT).scale(48 / 36))
        centerr.remove_updater(update_centerr)
        self.play(centerr.animate.next_to(rt, DOWN))
        self.play(Write(minus2.next_to(centerr)))
        self.play(rcost.animate.next_to(minus2, 1.3*RIGHT).scale(48 / 36))
        self.play(Write(xc.next_to(rcost)), Write(yc.next_to(rsint)))
        self.wait(3)
        self.play(TransformMatchingShapes(inal, final))
        self.wait(2)
        self.play(Unwrite(r2), Unwrite(theta))
        update_all()
        self.wait(7)
        self.play(FadeOut(axes, diagonallines, path, info, groundline))
        self.clear()
        '''
        #End
        self.play(Write(end, run_time=8))
        self.wait(1)
        self.play(FadeOut(end), DrawBorderThenFill(tfw))
        self.wait(3)

        
        self.wait(5)