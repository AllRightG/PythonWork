#игра "угадай число"
'''from tkinter import *
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

window.mainloop()'''

#Прога по спросу имени у пользователя и выведения в окошко
'''from tkinter import *
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

wind.mainloop()'''