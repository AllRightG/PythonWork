from tkinter import *

from random import *

t = randint(1, 3)
def change():
    t = [1,2,3]
    figura = choice(t)

    x = randint(1,300)
    y = randint(1,300)
    z = randint(1,300)
    q = randint(1,300)
    c = randint(1,300)
    m = randint(1,300)


    if figura == 1:
        square = canvas.create_polygon(x,y,z,q, c,m, fill='black')
    elif figura == 2:
        square = canvas.create_rectangle(x,y,z,q, fill='black')
    elif figura == 3:
        square = canvas.create_oval(x,y,z,q, fill='black')

root=Tk()
root.geometry('500x500')

canvas=Canvas(root, width=300, height=300, bg='white')
canvas.pack()




Button(text='фигура', command=change).pack()

root.mainloop()