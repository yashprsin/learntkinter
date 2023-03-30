# Create button
from tkinter import *

root = Tk()

#
def my_click():
    myLabel = Label(root, text="Look! I clicked a Button")
    myLabel.pack()


myButton = Button(root, text="Click Me!", command=my_click, fg="blue", bg="black")
# myButton2 = Button(root, text="Click Me!", state=DISABLED)
# myButton3 = Button(root, text="Click Me!", padx=50)
# myButton4 = Button(root, text="Click Me!", padx=50, pady=50)

myButton.pack()
# myButton2.pack()
# myButton3.pack()
# myButton4.pack()




root.mainloop()