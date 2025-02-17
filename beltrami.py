from manim import *

#Label indices with index_labels(mathtex[0])
#Cancel out a part of a math expression with cancel(mathtex[0][start:end])
#This code is a bit primitive, but it gets the job done

def cancel(mob):
    return Line(mob.get_corner(UR), mob.get_corner(DL), color=RED)

#Expressions

b1 = MathTex(r"\frac{dF}{dx}=\frac{\partial F}{\partial x}\frac{dx}{dx}+\frac{\partial F}{\partial y}\frac{dy}{dx}+\frac{\partial F}{\partial y'}\frac{dy'}{dx}")
b10 = cancel(b1[0][6:15])
b11 = MathTex(r"\frac{\partial F}{\partial x}=0", color=RED)
b2 = MathTex(r"\frac{dF}{dx}=\frac{\partial F}{\partial y}y'+\frac{\partial F}{\partial y'}y''")
b20 = MathTex(r"\frac{dF}{dx}-\frac{\partial F}{\partial y'}y''=\frac{\partial F}{\partial y}y'", color=GREEN).to_corner(UL)
b3 = MathTex(r"\frac{d}{dx}\left(\frac{\partial F}{\partial y'}\right)=\frac{\partial F}{\partial y}", color=RED)
b4 = MathTex(r"y'\frac{d}{dx}\left(\frac{\partial F}{\partial y'}\right)=y'\frac{\partial F}{\partial y}")
b204 = VGroup(b20[0][:15], b4[0][:15])
b5 = MathTex(r"\frac{d}{dx}\left(y'\frac{\partial F}{\partial y'}\right)=y''\frac{\partial F}{\partial y'}+y'\frac{d}{dx}\left(\frac{\partial F}{\partial y'}\right)", color=RED)
b50 = MathTex(r"-", color = RED)
b51 = MathTex(r"0", color=RED)
b6 = MathTex(r"\frac{d}{dx}\left[y'\frac{\partial F}{\partial y'}-F\right]=0")
b7 = MathTex(r"y'\frac{\partial F}{\partial y'}-F=C")