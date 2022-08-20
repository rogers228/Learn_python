from tkinter import *

#functions

def pop_menu(event):
    menu.tk_popup(event.x_root, event.y_root)

def copy():
    text.event_generate("<<Copy>>")

def cut():
    text.event_generate("<<Cut>>")

def paste():
    text.event_generate("<<Paste>>")

def select_all():
    text.event_generate("<<SelectAll>>")

#master window
root = Tk()
root.geometry("500x300")
root.title("NCG - Right Click Menu")

#text widget
text = Text(root, font = ("Fira Code", 35))
text.insert(1.0, "NCG")
text.pack()

#Right Click Menu
menu = Menu(text, tearoff=0, bg="black", fg="white")
#options
menu.add_command(label="Copy", command=copy)
menu.add_command(label="Cut", command=cut)
menu.add_separator()
menu.add_command(label="Paste", command=paste)
menu.add_separator()
menu.add_command(label="Select All", command=select_all)

#Make the menu pop up
text.bind("<Button - 3>", pop_menu)

root.mainloop()

"""

tk menu options and methods:

https://www.tutorialspoint.com/python/tk_menu.htm



other virtual events for the event_generate method:

https://www.tcl.tk/man/tcl8.6/TkCmd/event.htm

"""