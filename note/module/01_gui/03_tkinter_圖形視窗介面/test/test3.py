import tkinter as tk
root = tk.Tk()

canvas = tk.Canvas(root, width = 500, height = 500)
canvas.pack()
radius = 10
bbox = (-radius, -radius, radius, radius)
oval = canvas.create_oval(*bbox)

def move_oval():
    canvas.move(oval, 1, 1)
    canvas.after(10, move_oval)  # after 多久後再執行一次func

# Start moving!
move_oval()

root.mainloop()