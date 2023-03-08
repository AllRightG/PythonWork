#['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',1,2,3,4,5,6,7,8,9,0]
#игра "угадай число"
from tkinter import *
def sravn():
    first = ent1.get()
    second = ent2.get()
    if int(first) > int(second):
        rs['text'] = f'Число {first} больше {second}'
    else:
        rs['text'] = f'Число {first} меньше {second}'


window = Tk()
window.geometry('600x300')

ent1 = Entry(window, bg = 'gray64')
ent1.place(x=0,y=250)

ent2 = Entry(window, bg='gray64')
ent2.place(x=477,y=250)

btn = Button(window, bg='lime green', text='Сравнить 2 числа', command=sravn)
btn.pack(side=BOTTOM)

lbl = Label(window, bg='magenta2', text='Итог сравнения ниже', height=2,width=65)
lbl.pack(side=TOP)

rs = Label(window, bg='dodger blue', fg='white', text='', height=2,width=60)
rs.place(x= 90,y=150)

window.mainloop() 

#Прога по спросу имени у пользователя и выведения в окошко
""" from tkinter import *
def hello():
    name=ent.get()
    lbl['text'] = f'Здравствуйте, {name}'

wind = Tk()
wind.geometry('400x300')

lbl = Label(wind, bg='sea green', text='Введите ваше имя', height=2, width=35)
lbl.pack(side=TOP)

btn = Button(wind, text='Поприветствовать пользователя', 
             bg='firebrick1',
             width=30,
             height=3, command=hello)
btn.pack(side=BOTTOM)

ent = Entry(wind, width=35, bg='gold')
ent.pack()

wind.mainloop()
 """

#Программа по генерации рандомного пароля   dodger blue, cyan, magenta, tomato, gold, steel blue
""" from tkinter import *
import random as rand
def password():
	Verh=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
	pas = rand.sample(Verh, 6)
	pl['text'] = f'{pas}'



root = Tk()
root.geometry('500x300')
root.title('Генератор паролей')
root.resizable(0, 0)

Label(root, bg='coral', height=3,width=22, text='Ваш пароль:').pack(side=TOP)

Button(root, bg='spring green', fg='black', height=2,width=40, text='Сгенерировать пароль', command=password).pack(side=BOTTOM)

pl = Label(root, bg='dodger blue', width=35, height=3, text='Тут будет ваш пароль после генерации')
pl.place(x=130,y=130)

root.mainloop() """

# 7
# Напишите программу, в которой определенный символ в тексте будет заменять 
# с одного на другой. Текст пользователь пишет в виджете Text, так же у пользователя
# должна быть возможность выбрать с какого на какой символ он хочет поменять.
# Символы должны заменять по нажатию на кнопку.
# 2 entry, 1 text, 1 button
#1 entry - символ который хотим поменять, 2 entry - символ на который мы поменяем символ из 1 entry
 
""" from tkinter import *
global txet
def change():
	it = txet.get()



wind = Tk()
wind.geometry('500x300')
wind['bg'] = 'RoyalBlue1'
wind.resizable(0,0)

txet = Text(
    wind,
    width=40,
    height=5,
    bg='salmon',
    font='calibri 15',
    
)
txet.pack()

btn = Button(
    wind,
    width=30,
    height=2,
    bg='lawngreen',
    text='Нажмите чтобы изменить символы'
)
btn.pack(side=BOTTOM)

ent = Entry(
    wind,
    width=10,
    bg = 'darkslategray',
    fg='white'
)
ent.place(x= 0, y=124)

ent2 = Entry(
wind,
width=10,
bg = 'darkslategray',
fg='white'
)
ent2.place(x=436,y=124)

wind.mainloop() """
print(23*7)