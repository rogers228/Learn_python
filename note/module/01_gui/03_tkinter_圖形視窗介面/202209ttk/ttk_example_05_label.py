# https://www.pythontutorial.net/tkinter/tkinter-label/
import tkinter as tk
from tkinter import ttk

# label = ttk.Label(container, **options)
def test1():
    root = tk.Tk()
    root.geometry('300x200')
    root.resizable(False, False)
    root.title('Label Widget Demo')

    label = ttk.Label(root, text='This is a label', background='red', font=("Helvetica", 14))
    label.pack(ipadx=10, ipady=10)

    root.mainloop()

def test2():
    root = tk.Tk()
    root.geometry('300x200')
    # 使用字典 程式碼更簡潔明確
    label_a = {
        'text': 'This is a label',
        'font': ("Helvetica", 14),
        'background': 'red',
    }

    label = ttk.Label()
    for a, v in label_a.items():
        label[a] = v
    label.pack()
    root.mainloop()


# Displaying an image
# photo = tk.PhotoImage(file='./assets/python.png')

    
if __name__ == '__main__':
    test2()