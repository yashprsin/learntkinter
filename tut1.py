from tkinter import *
root = Tk()

# Create a Label widget
myLabel = Label(root, text="Hello world").grid(row=0, column=0)
myLabel0 = Label(root, text="My name is Code.").grid(row=1, column=5)
myLabel1 = Label(root, text=" ")
myLabel2 = Label(root, text="My age is 20")


# Showing it into the screen
# myLabel.pack()

# myLabel.grid(row=0, column=0)
# myLabel0.grid(row=1, column=5)
# myLabel1.grid(row=1, column=3)
# myLabel2.grid(row=1, column=3)

# Loop
root.mainloop()
