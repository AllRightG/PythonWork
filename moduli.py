#Random
#import random

# # a=  random.random()   генерация рандомных числел от 0 до 1, рациональные
#a= random.uniform(1,3)  генерация рандомных числел от 1 до 3, рациональные
# # a= random.randint(1,7) генерация рандомных чисел от 1 до 7 (включ.), целые
# # a= random.randrange(10) рандомные числа от 0 до 10
# # a= random.gauss(0,3.5)  рандом по гаусу
# lst = [1,6,3,87,2,78,8,231,546] 
# # a= random.choice(lst)  выбор из списка случ. число
# # random.shuffle(lst) перемешать список
# # print(lst)
# # a= random.sample(lst, 3)  выбрать из списка 3 случайных числа
# random.seed(23)  зерно списка
# a = [random.randint(0,10) for i in range(20)]
#print(a)

from tkinter import *

window = Tk()
window.geometry('250x200')

text = Text(
    font = 'Calibri',
    wrap = WORD
)
text.pack()


window.mainloop()