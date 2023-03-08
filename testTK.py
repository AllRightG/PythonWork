""" from turtle import *
joe = Turtle()
def sq(a):
     for i in range(4):
          joe.forward(a)
          joe.left(90)
colors = ['gold', 'cyan','magenta','firebrick','green']
joe.speed(1000)
dlina = 80
for i in range(100):
     joe.color(colors[i%5])
     joe.circle(dlina)
     joe.right(10)
     dlina=dlina+1
"""
""" #Task 3. Напишите программу, которая на вход принимает число и выдает его квадрат
x=int(input('Введите число: '))

print((lambda x: x**2)(x)) """


"""  #Task 4. Задача №1. Напишите программу, которая на вход принимает два числа и проверяет, является ли первое число квадратом второго.
first = int(input())
second = int(input())
if first == second**2:
     print(f'Число {first} является квадратом числа {second}')
else:
     print(f'Число {first} не является квадратом числа {second}')  """



""" #Task 5. Задача №3. Напишите программу, которая будет выдавать название дня недели по заданному номеру.
day = int(input('Введите номер дня недели: '))
match day:
	case(1):
		print('Понедельник')
	case(2):
		print('Вторник')
	case(3):
		print('Среда')
	case(4):
		print('Четверг')
	case(5):
		print('Пятница')
	case(6):
		print('Суббота')
	case(7):
		print('Воскресенье')
	case _:
		print('Нет такого дня недели') """

#Рандомазейр на ткинтере
""" from tkinter import *
import random as ran
def rand():
	num = ran.randint(0, 10000)
	lbl['text'] = f'Сгенерировалось число: {num}'


window = Tk()
window.geometry('400x300')
window.resizable(0,0)
window.title('Генератор рандомных чисел')

lbl = Label(
	window,
	height=5, width=75,
	bg='aquamarine2',
	text = 'Здесь будет рандомное число после нажатия на кнопку'
)
lbl.pack(side=TOP)

btn = Button(window,
	height=2, width=20,
	text='Генерация числа',
	bg='OliveDrab2',
	command=rand
)
btn.pack(side=BOTTOM)

window.mainloop() """

""" #Задача №5. Напишите программу, которая на вход принимает одно число (N), а на выходе показывает все целые числа в промежутке от -N до N.
N = int(input('Введите число: '))
n= -N
for i in range(n, N+1):
	print(i) """

""" #Task 1. Задача №9. Напишите программу, которая выводит случайное число из отрезка [10, 99] и показывает наибольшую цифру числа.
import random as rand
begin = 10
end = 99
print(rand.randint(begin, end)) """

#Task 4. Задача №14. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно одновременно 7 и 23
num = int(input('Введите число: '))
if num % 23 ==0 and num % 7==0:
     print('Да, оно кратно числам 23 и 7')
else:
     print('Не кратно')

#Task 6. Задача №1. Напишите программу, которая выводит все четные числа от 2 до 100
""" begin = 2
end = 100
for i in range(begin, end):
     if i%2==0:
          print(i) """
