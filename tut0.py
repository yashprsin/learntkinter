from tkinter import *

root = Tk()


def my_click():
    myLabel = Label(root, text="Look! I clicked a Button")
    myLabel.pack()


myButton = Button(root, text="Click Me!", command=my_click)
myButton.pack()

root.mainloop()
