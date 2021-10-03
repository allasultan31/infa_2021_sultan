from graph import *

windowSize(600, 800)
canvasSize(550, 760)

penColor(95, 188, 211)
brushColor(95, 188, 211)
rectangle(0, 0, 550, 200)


def budka():
    penSize(1.5)
    penColor("black")
    brushColor(200, 171, 55)
    polygon([(323, 535), (426, 587), (426, 450), (323, 398), (323, 535)])
    penSize(1)
    polygon([(426, 587), (460, 522), (460, 383), (426, 450), (426, 587)])
    brushColor(212, 170, 0)
    polygon([(323, 398), (385, 335), (426, 450), (323, 398)])
    polygon([(460, 383), (424, 315), (385, 335), (426, 450), (460, 383)])

    brushColor("black")
    oval(340, 530, 400, 450)

    brushColor(200, 171, 55)
    penSize(1)
    oval(339, 530, 355, 520)
    brushColor(55, 200, 113)
    oval(325, 550, 340, 540)
    brushColor(108, 103, 83)
    oval(328, 543, 345, 527)
    brushColor(55, 200, 113)
    oval(310, 555, 330, 546)
    oval(302, 560, 312, 550)
    oval(280, 564, 306, 555)
    oval(270, 567, 283, 560)
    oval(257, 564, 273, 560)
    oval(250, 565, 260, 555)
    oval(240, 565, 253, 560)
    oval(228, 568, 242, 560)


penColor("black")
brushColor(200, 171, 55)
x1 = 100;
y1 = 10
x2 = 570;
y2 = 390
n = 9
rectangle(x1, y1, x2, y2)
h = (x2 - x1) / (n + 1)
x = x1 + h
for i in range(n):
    line(x, y1, x, y2)
    x += h
penSize(1)
line(100, 389, 570, 389)
penSize(1)
penColor("gray")
line(100, 10, 100, 390)
line(100, 10, 570, 10)

penColor(55, 200, 113)
brushColor(55, 200, 113)
rectangle(0, 390, 550, 760)

penColor("black")
brushColor(200, 171, 55)
x1 = 0;
y1 = 150
x2 = 340;
y2 = 400
n = 13
rectangle(x1, y1, x2, y2)
h = (x2 - x1) / (n + 1)
x = x1 + h
for i in range(n):
    line(x, y1, x, y2)
    x += h
penSize(1)
line(0, 400, 340, 400)
penColor("gray")
line(0, 150, 0, 400)
line(0, 150, 340, 150)

penColor("black")
brushColor(200, 171, 55)
x1 = 300;
y1 = 250
x2 = 580;
y2 = 450
n = 9
rectangle(x1, y1, x2, y2)
h = (x2 - x1) / (n + 1)
x = x1 + h
for i in range(n):
    line(x, y1, x, y2)
    x += h
penColor("gray")
line(300, 250, 300, 450)
line(300, 250, 580, 250)
line(340, 150, 340, 250)

penColor("black")
brushColor(200, 171, 55)
x1 = -10;
y1 = 270
x2 = 240;
y2 = 470
n = 10
rectangle(x1, y1, x2, y2)
h = (x2 - x1) / (n + 1)
x = x1 + h
for i in range(n):
    line(x, y1, x, y2)
    x += h
penColor("gray")
line(-10, 270, 240, 270)
line(240, 270, 240, 470)


def sobaka1():
    penColor(108, 103, 83)
    brushColor(108, 103, 83)
    oval(13, 570, 67, 460)
    oval(10, 585, 63, 567)
    oval(80, 590, 134, 480)
    oval(73, 606, 120, 588)
    oval(25, 520, 170, 455)
    oval(100, 500, 200, 440)
    oval(150, 520, 210, 460)
    oval(190, 577, 211, 505)
    oval(170, 592, 208, 575)
    oval(110, 490, 170, 430)
    oval(140, 550, 157, 500)
    oval(117, 565, 155, 550)

    penColor("black")
    penSize(1)
    brushColor(108, 103, 83)
    rectangle(25, 400, 120, 500)

    penSize(1)
    penColor("black")
    oval(15, 423, 35, 401)
    oval(110, 423, 130, 401)

    brushColor("white")
    oval(40, 438, 60, 432)
    oval(75, 438, 95, 432)
    brushColor("black")
    circle(50, 435, 3)
    circle(85, 435, 3)

    arc(42, 470, 95, 500, start=0, end=190, style=ARC)
    brushColor("white")
    polygon([(46, 476), (50, 461), (53, 472), (46, 476)])
    polygon([(90, 476), (86, 461), (83, 472), (90, 476)])


sobaka1()


def sobaka2():
    penColor(108, 103, 83)
    brushColor(108, 103, 83)
    oval(430, 500, 546, 435)
    oval(520, 537, 554, 470)
    oval(521, 542, 555, 529)
    oval(465, 547, 500, 480)
    oval(469, 559, 503, 545)
    oval(430, 490, 480, 420)
    oval(440, 515, 464, 500)

    penColor("black")
    penSize(1)
    brushColor(108, 103, 83)
    rectangle(486, 410, 551, 480)

    penSize(1)
    penColor("black")
    oval(476, 431, 496, 410)
    oval(541, 431, 561, 410)

    brushColor("white")
    oval(498, 439, 510, 434)
    oval(529, 439, 541, 434)
    brushColor("black")
    circle(504, 436, 2)
    circle(535, 436, 2)

    arc(500, 460, 540, 480, start=0, end=190, style=ARC)
    brushColor("white")
    polygon([(504, 463), (508, 453), (511, 460), (504, 463)])
    polygon([(535, 463), (531, 453), (528, 460), (535, 463)])


sobaka2()
budka()

def sobaka3():
    penColor(108, 103, 83)
    brushColor(108, 103, 83)
    oval(108, 690, 250, 622)
    oval(212, 735, 255, 635)
    oval(218, 746, 260, 728)
    oval(153, 746, 195, 655)
    oval(160, 762, 200, 745)
    oval(80, 672, 160, 620)
    oval(125, 650, 160, 617)
    oval(60, 695, 111, 640)
    oval(55, 737, 73, 680)
    oval(60, 751, 95, 735)
    oval(115, 719, 134, 630)
    oval(118, 730, 160, 715)


    penColor("black")
    penSize(1)
    brushColor(108, 103, 83)
    rectangle(170, 590, 250, 670)

    penSize(1)
    penColor("black")
    oval(160, 615, 180, 590)
    oval(240, 615, 260, 590)

    brushColor("white")
    oval(185, 625, 204, 618)
    oval(219, 625, 238, 618)
    brushColor("black")
    circle(195, 621, 3)
    circle(229, 621, 3)

    arc(184, 647, 230, 670, start=0, end=190, style=ARC)
    brushColor("white")
    polygon([(190, 650), (193, 640), (196, 648), (190, 650)])
    polygon([(226, 652), (223, 640), (220, 648), (226, 650)])

sobaka3()

def sobaka4():
    penColor(108, 103, 83)
    brushColor(108, 103, 83)
    oval(290, 1000, 650, 590)

    penColor("black")
    penSize(3)
    brushColor(108, 103, 83)
    rectangle(310, 510, 535, 740)

    penSize(3)
    penColor("black")
    oval(280, 590, 350, 510)
    oval(505, 590, 575, 510)

    brushColor("white")
    penSize(3)
    oval(345, 610, 390, 595)
    oval(455, 610, 500, 595)
    brushColor("black")
    circle(368, 602, 6)
    circle(478, 602, 6)

    penSize(1.5)
    arc(356, 676, 480, 750, start=0, end=190, style=ARC)
    brushColor("white")
    polygon([(367, 692), (375, 653), (386, 681), (367, 692)])
    polygon([(472, 693), (464, 653), (453, 681), (472, 692)])




sobaka4()

run()