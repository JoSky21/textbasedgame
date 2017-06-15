from tkinter import *
#different buttons for each of the choices in game. choices should change based on what room/area the player is in.
def button1(option):
    choice = str(option)
def button2(option):
    choice = str(option)
def button3(option):
    choice = str(option)
def button4(option):
    choice = str(option)
def button5(option):
    choice = str(option)
def button6(option):
    choice = str(option)

#the variables for changing the choices of each button
c1 = str("1")
c2 = str("2")
c3 = str("3")
c4 = str("4")
c5 = str("5")
c6 = str("6")

root = Tk()
root.title("Controller")
root.geometry("300x200")
app = Frame(root)
app.pack({"side":"left"})
bttn1 = Button(app, command=button1(c1))
bttn1["text"] = c1
bttn2 = Button(app, command=button2(c2))
bttn2["text"] = c2
bttn3 = Button(app, command=button3(c3))
bttn3["text"] = c3
bttn4 = Button(app, command=button4(c4))
bttn4["text"] = c4
bttn5 = Button(app, command=button5(c5))
bttn5["text"] = c5
bttn6 = Button(app, command=button6(c6))
bttn6["text"] = c6
bttn2.pack({"side":"right"})
bttn5.pack({"side":"left"})
bttn6.pack({"side":"left"})
bttn5.pack({"padx":"15"})
bttn6.pack({"padx":"15"})
bttn4.pack({"side":"left"})
bttn1.pack({"side":"top"})
bttn3.pack({"side":"bottom"})

root.mainloop()
