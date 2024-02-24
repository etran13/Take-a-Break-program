import random
from tkinter import Tk, Button, Label
from tkinter.messagebox import showinfo
import time
import webbrowser

#Library
list3min = ["Pinterest, 3 minutes",
            "YouTube, 3 minutes",
            "Watch 1 cat video, 3 minutes",
            "Lay down, 3 minutes",
            "Sit on the sofa, 3 minutes"]

list5min = ["Pinterest, 5 minutes",
            "YouTube, 5 minutes",
            "Lay down, 5 minutes"]

list10min = ["Work on a drawing, 10 minutes",
             "Read a book, 10 minutes",
             "Work on a drawing, 10 minutes",
             "Watch an art tutorial, 10 minutes",
             "Work on a knitting project, 10 minutes"]

list20min = ["Work on a drawing, 20 minutes",
             "Read a book, 20 minutes",
             "Work on a drawing, 20 minutes",
             "Watch an art tutorial, 20 minutes",
             "Work on a knitting project, 20 minutes",
             "Work on a story, 20 minutes"]

#Functions

def timer1():
    generate(list3min)
    breakTimer("3")

def timer2():
    generate(list5min)
    breakTimer("5")

def timer3():
    generate(list10min)
    breakTimer("10")

def timer4():
    generate(list20min)
    breakTimer("20")
    
def generate(lst):
    itemPick = random.choice(lst)
    showinfo(title="Break", message="You picked: {}".format(itemPick))

def breakTimer(minutes):
    "Opens up a browser window with a timer according to amount of minutes passed in"
    url = "https://www.google.com/search?client=safari&rls=en&q={}+minute+timer&ie=UTF-8&oe=UTF-8".format(minutes)
    webbrowser.open_new(url)
             
root = Tk()

label = Label(root, text="Take a break!")
button1 = Button(root, text="3 minutes", command=timer1)
button2 = Button(root, text="5 minutes", command=timer2)
button3 = Button(root, text="10 minutes", command=timer3)
button4 = Button(root, text="20 minutes", command=timer4)

label.pack()
button1.pack()
button2.pack()
button3.pack()
button4.pack()

root.mainloop()
