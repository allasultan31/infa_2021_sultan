# coding: utf-8
from graph import *
windowSize(600, 800)
canvasSize(550, 760)

penColor("black")
brushColor(200, 171, 55)
x1=0; y1=100
x2=600; y2=400
n=15
rectangle(x1, y1, x2, y2)
h=(x2-x1)/(n+1)
x=x1+h
for i in range(n):
	line(x, y1, x, y2)
	x+=h
penSize(2)
line(0, 400, 550, 400)

penColor(95, 188, 211)
brushColor(95, 188, 211)
rectangle(0, 0, 550, 100)

penColor(55, 200, 113)
brushColor(55, 200, 113)
rectangle(0, 401, 550, 760)

penSize(1.5)
penColor("black")
brushColor(200,171,55)
polygon([(293,535),(396,587),(396,450),(293,398),(293,535)])
penSize(1)
polygon([(396,587),(430,522),(430,383),(396,450),(396,587)])
brushColor(212,170,0)
polygon([(293,398),(355,335),(396,450),(293,398)])
polygon([(430,383),(395,315),(355,335),(396,450),(430,383)])

penColor(108,103,83)
brushColor(108,103,83)
oval(20,620,55,540)
oval(10,630,52,615)
oval(70,630,105,550)
oval(60,640,100,625)
oval(28,580,155,520)
oval(100,560,180,523)
oval(150,580,190,535)
oval(176,610,190,566)
oval(159,620,189,608)
oval(120,560,165,517)
oval(135,600,149,556)
oval(118,610,148,598)


penColor("black")
penSize(1)
brushColor(108,103,83)
rectangle(30,490,95,560)

penSize(1)
penColor("black")
oval(20,513,40,490)
oval(85,513,105,490)

brushColor("black")
oval(310,530,370,450)

brushColor(200,171,55)
penSize(1)
oval(309,530,325,520)
brushColor(55, 200, 113)
oval(295,550,310,540)
brushColor(108,103,83)
oval(298,543,315,527)
brushColor(55, 200, 113)
oval(280,555,300,546)
oval(272,560,282,550)
oval(250,564,276,555)
oval(240,567,253,560)
oval(227,564,243,560)
oval(220,565,230,555)
oval(210,565,223,560)
oval(198,568,212,560)

brushColor("white")
oval(40,520,55,514)
oval(70,520,85,514)
brushColor("black")
circle(47,517,3)
circle(77,517,3)

arc(42, 537, 80, 565, start = 0, end = 190, style = ARC )
brushColor("white")
polygon([(46,542),(50,532),(53,538),(46,542)])
polygon([(76,542),(72,532),(69,538),(76,542)])




run()