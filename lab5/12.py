from tkinter import *
from random import randrange as rnd, choice
from math import *
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
    
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'cyan', 'aqua', 'indigo', 'lime', 'maroon', 'violet', 'fuchsia']


class Ball(object):
	def __init__  (self, x, y, r, color, vx, vy):
		self.x = x
		self.y = y
		self.r = r
		self.color = color
		self.vx = vx
		self.vy = vy
		
balls = []
for i in range(10):
	balls.append(Ball(rnd(100, 700), rnd(100,500), rnd(30,50), choice(colors), rnd(5,30), rnd(2,10)))
	

def new_ball():
	#cоздаём функцию для нового шара
	#задаём такие х, у, r, что их значения сохраняюся и после завершения работы функции, т.е переменные будут глобальными
	#через метод delete устанавливаем удаление шарика после выполнения функции
	#переменная х - координата оси абцисс - принимает рандомные значения в интервале (100,700)
	#переменная у - координата оси ординат - принимает рандомные значения в интервале (100,500)
	#переменная r - радиус шара - принимает рандомные значения в интервале (30,50)
	#методом create_oval создаём овал в указанных координатах
	#fill - заполнения шара рандомным цветом
	#width - ширина обводки шара
	#метод after: задаём время=1000 мс, через которое функция начинает выполняться
	canv.delete(ALL)
	for i in range (10):
		canv.create_oval(balls[i].x-balls[i].r, balls[i].y-balls[i].r, balls[i].x+balls[i].r, balls[i].y+balls[i].r, fill=balls[i].color, width=0)
	canv.delete(ALL)
	for i in range (3):
		canv.create_rectangle(rec[i].x, rec[i].y, rec[i].x+rec[i].h, rec[i].y+rec[i].h, fill=rec[i].color, width=0)
	root.after(1000, dvij)
	
	
def dvij():
	canv.delete(ALL)
	for i in range (10):
		balls[i].x = balls[i].x + balls[i].vx
		balls[i].y = balls[i].y + balls[i].vy
		if balls[i].x>800 or balls[i].x<0:
			balls[i].vx = -balls[i].vx		
		if balls[i].y>600 or balls[i].y<0:
			balls[i].vy = -balls[i].vy	
		canv.create_oval(balls[i].x-balls[i].r, balls[i].y-balls[i].r, balls[i].x+balls[i].r, balls[i].y+balls[i].r, fill=balls[i].color, width=0)
	for i in range (3):
		rec[i].x = rec[i].x + rec[i].vx*rnd(-1,1)
		rec[i].y = rec[i].y + rec[i].vy*rnd(-1,1)
		if rec[i].x>800 or rec[i].x<0:
			rec[i].vx = -rec[i].vx		
		if rec[i].y>600 or rec[i].y<0:
			rec[i].vy = -rec[i].vy	
		canv.create_rectangle(rec[i].x, rec[i].y, rec[i].x+rec[i].h, rec[i].y+rec[i].h, fill=rec[i].color, width=0)
	root.after(10, dvij)


        
    
def click(event):
	global point
	print(balls[i].x, balls[i].y, balls[i].r)
	if balls[i].r>sqrt((balls[i].x-event.x)**2+(balls[i].y-event.y)**2):
		point+=1
		print(point)
	else:
    		print('no')
    		
    		
class Rect(object):
	def __init__  (self, x, y, h, color, vx, vy):
		self.x = x
		self.y = y
		self.h = h
		self.color = color
		self.vx = vx
		self.vy = vy   		

rec = []
for i in range(3):
	rec.append(Rect(rnd(5, 1000), rnd(60,500), rnd(15,40), choice(colors), rnd(3,5), rnd(2,5)))   
	
	
	
	
	
    
point = 0       
new_ball()
canv.bind('<Button-1>', click)
mainloop()
