from tkinter import *

window = Tk()

window.title('TEST')
window.geometry('200x160')

label = Label(
  text = 'Hello!',
  width = 30,
  height = 5,
  underline = 0,
  background='maroon1'
)

button = Button(
  text = 'Click',
  width = 30,
  height = 5,
  activebackground = 'cyan2',
  background='dark violet'
)

label.pack()
button.pack()

window.mainloop()