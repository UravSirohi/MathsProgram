from tkinter import *

root = Tk()


def hi(event):
    print('greetings')


button1 = Button(root, text='Click me')
button1.bind("<Button-1>", hi)
button1.pack()
quit()
root.mainloop()
