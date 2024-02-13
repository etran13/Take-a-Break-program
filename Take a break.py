import random
from tkinter import Tk, Button, Label
from tkinter.messagebox import showinfo

def generate():
    list1 = ["Pinterest, 5 minutes", "Pinterest, 3 minutes",
             "YouTube, 5 minutes", "YouTube, 3 minutes",
             "Snapchat, send a snap to somebody"
             "Watch 1 cat video"]
    list2 = ["Lay down, 5 minutes", "Lay down, 3 minutes",
             "Put your head down, 3 minutes",
             "Sit on the sofa, 5 minutes", "Sit on the sofa, 3 minutes",
             "Make a drink",
             "Close your eyes and reflect on your emotions, unlimited"]
    list3 = ["Work on a drawing, 20 minutes", "Work on a story, 20 minutes",
             "Doodle in your sketchbook, 7 minutes",
             "Work on a knitting project, 30 minutes",
             "Watch an art tutorial, 10 minutes"]
    listPick = random.choice([list1, list2, list3])
    itemPick = random.choice(listPick)
    showinfo(title="Break", message="You picked: {}".format(itemPick))
             
root = Tk()

label = Label(root, text="Take a break!")
button = Button(root, text="Generate", command=generate)

label.pack()
button.pack()

root.mainloop()
