from tkinter import *

def north():
    print("Went north")
def east():
    print("Went east")
def south():
    print("Went south")
def west():
    print("Went west")
def attack():
    print("Attacked")
def run():
    print("Ran")


root = Tk()
root.title("Controller")
root.geometry("300x200")
app = Frame(root)
app.pack({"side":"left"})
bttn1 = Button(app, command=north)  # <---------
bttn1["text"] = "north"
bttn2 = Button(app, command=east)  # <---------
bttn2["text"] = "east"
bttn3 = Button(app, command=south)  # <---------
bttn3["text"] = "south"
bttn4 = Button(app, command=west)  # <---------
bttn4["text"] = "west"
bttn5 = Button(app, command=attack)
bttn5["text"] = "attack"
bttn6 = Button(app, command=run)
bttn6["text"] = "run"
bttn2.pack({"side":"right"})

bttn5.pack({"side":"left"})
bttn6.pack({"side":"left"})
bttn5.pack({"padx":"15"})
bttn6.pack({"padx":"15"})

bttn4.pack({"side":"left"})
bttn1.pack({"side":"top"})
bttn3.pack({"side":"bottom"})

root.mainloop()
