from tkinter import *
from tkinter import messagebox
skillpoints = 20
intelligence = 2
luck = 2
charisma = 2
strength = 2
def skillslide(skill):
    def confirm(): #necissary to have this defined in here, stupid but it works
        global strength,intelligence,charisma,luck
        if(skill == "strength"):
            strength = strength + w.get()
            skillslider.quit()
        elif(skill == "intelligence"):
            intelligence = intelligence + w.get()
            skillslider.quit()
        elif(skill == "charisma"):
            charisma = charisma + w.get()
        elif(skill == "luck"):
            luck = luck + w.get()
    def on_closing():
        messagebox.showwarning("Can't Close", "Closing this window will break the game. Please input something and press confirm. The window will close itself")
    val=0
    skillslider = Tk()
    skillslider.title("Slider")
    skillslider.geometry("200x75")
    skillslider.protocol("WM_DELETE_WINDOW",on_closing)
    w = Scale(skillslider, from_=0, to=skillpoints, orient=HORIZONTAL, command=val)
    x = Button(skillslider,command=confirm)
    w.pack()
    x["text"] = "confirm"
    x.pack({"side":"bottom"})
    skillslider.mainloop()
skillslide("strength") #always make a string
