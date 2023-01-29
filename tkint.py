from tkinter import *

from random import *


def change():
    list = ['white','black','orange','green','yellow']
    a = choice(list)

    x = randint(1,300)
    y = randint(1,300)
    z = randint(1,300)
    q = randint(1,300)
    c = randint(1,300)
    m = randint(1,300)

    t = randint(1, 3)
    if t == 1:
        square = canvas.create_polygon(x,y,z,q, c,m, fill=a)
    elif t == 2:
        square = canvas.create_rectangle(x,y,z,q, fill=a)
    elif t == 3:
        square = canvas.create_oval(x,y,z,q, fill=a)

root=Tk()
root.geometry('500x500')

canvas=Canvas(root, width=300, height=300, bg='white')
canvas.pack()




Button(text='фигура', command=change).pack()

root.mainloop()