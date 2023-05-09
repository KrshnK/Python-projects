import pyttsx3
from tkinter import *
engine = pyttsx3.init()
root=Tk()
root.title("Robo Speaker")
root.geometry("350x200")
lbl=Label(root,text="**Welcome to Robo speaker**")
txt = Entry(root,width=10)
txt.grid(column=1,row=0)
def clicked():
    engine.say(txt)
    engine.runAndWait()
    engine.stop()
btn=Button(root,text="say",fg="red",command=clicked())
btn.grid(column=1,row=1)
root.mainloop()