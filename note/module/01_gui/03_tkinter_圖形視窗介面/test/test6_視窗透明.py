import tkinter as tk
window = tk.Tk()
# window.config(highlightbackground='#000000')
canvas = tk.Canvas(window, width=200, height=200, background='#ff00ff')
canvas.place(x=0, y=0)

canvas = tk.Canvas(window, width=100, height=100, bd=0, highlightthickness=0)
canvas.place(x=0, y=0)

# window.overrideredirect(True)
window.wm_attributes('-transparentcolor','#ff00ff')
# window.wm_attributes('-topmost', True)
canvas.create_window(0, 0, anchor=tk.NW)
tk.mainloop()