from tkinter import *

press = 0

def Clicks():
	global press
	press += 1
	label['text'] = f'Clicks {press}'

window = Tk()

window.title('TEST')
window.geometry('200x500')

label = Label(
  text = 'Hello!',
  width = 30,
  height = 5,
  underline = 0,
  background='maroon1',
  font= ('impact', 15)
)

button = Button(
  text = 'Click',
  width = 30,
  height = 5,
  activebackground = 'cyan2',
  background='dark violet',
  command = Clicks
)

label.pack()
button.pack()

window.mainloop()