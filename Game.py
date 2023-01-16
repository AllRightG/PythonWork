''' 
Игра - угадай число. 
 В программе задано число, пользователь должен его угадать
 Если введенное число > чем загаданное, то просим уменьшить введеное число
 Если введенное число < чем загаданное, то просим увеличить введеное число
 -Entry
 -Button
 -Label
 '''
from tkinter import *

from random import randint
rand = randint(0, 100) # Загадали число от 0 до 100

def button_1():
    global rand
    guess = a.get()
    if(int(guess) > rand):
        l.config(text='Уменьшите число!')
    elif(int(guess) < rand):
        l.config(text='Увеличьте число!')
    elif(int(guess) == rand):
        l.config(text='Угадали!')

root = Tk()
root.title('Угадай число')
root.geometry('500x300')

a = Entry(root, width=15, bg='gray', fg='cyan', font='consolas')
a.pack()

Button(root, text='Угадал?', width=15, height=2, bg='white', command=button_1).pack()

l = Label(root, width=30, bg='gray', fg='cyan', font='consolas')
l.pack()

root.mainloop()