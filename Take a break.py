import random
from tkinter import Tk, Button, Label
from tkinter.messagebox import showinfo
import time
import webbrowser

#timerLabel = Label(root, text="Timer started.")

def generate():
    dict1 = {
            "Pinterest, 5 minutes":5,
            "Pinterest, 3 minutes":3,
            "YouTube, 5 minutes":5,
            "YouTube, 3 minutes":3,
            "Watch 1 cat video, 3 minutes":3}
    
    dict2 = {
            "Lay down, 5 minutes":5,
            "Lay down, 3 minutes":3,
            "Put your head down, 3 minutes":3,
            "Sit on the sofa, 5 minutes":5,
            "Sit on the sofa, 3 minutes":3,
            "Make a drink, unlimited":None,
            "Close your eyes and reflect on your emotions, unlimited":None}
    
    dict3 = {
            "Work on a drawing, 20 minutes":20,
            "Work on a story, 20 minutes":20,
            "Doodle in your sketchbook, 7 minutes":7,
            "Work on a knitting project, 30 minutes":30,
            "Watch an art tutorial, 10 minutes":10}
    
    dictPick = random.choice([dict1, dict2, dict3])
    itemPick = random.choice(list(dictPick))
    showinfo(title="Break", message="You picked: {}".format(itemPick))
    breakTimer(dictPick.get(itemPick))

def breakTimer(minutes):
    url = "https://www.google.com/search?client=safari&rls=en&q={}+minute+timer&ie=UTF-8&oe=UTF-8".format(minutes)
    webbrowser.open_new(url)
             
root = Tk()

label = Label(root, text="Take a break!")
button = Button(root, text="Generate", command=generate)

label.pack()
button.pack()

root.mainloop()
