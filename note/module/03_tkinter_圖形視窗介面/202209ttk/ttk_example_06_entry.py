import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def test1():
    def clicked():
        print(pdno.get())

    # root window
    root = tk.Tk()
    root.geometry("300x150")
    root.resizable(False, False)
    root.title('Sign In')

    label = ttk.Label(root, text='請輸入品號:', font=("新細明體", 12)).place(x=10, y=20)
    pdno = tk.StringVar()
    entry_name = ttk.Entry(root, textvariable=pdno, width=22, font=("新細明體", 12)).place(x=105, y=20)
    # https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/ttk-Entry.html

    button = ttk.Button(root, text="ok", command=clicked).place(x=60, y=50)

    root.mainloop()


def test2():
    def clicked():
        print(pdno.get())
        print(agreement.get())
    # root window
    root = tk.Tk()
    root.geometry("300x150")
    root.resizable(False, False)
    root.title('Sign In')

    ttk.Style().configure('.', font=('新細明體', 12))


    pdno = tk.StringVar()
    agreement = tk.StringVar()

    ttk.Label(root, text='請輸入品號:').place(x=10, y=20)
    ttk.Entry(root, textvariable=pdno, width=22, font=('新細明體', 12)).place(x=105, y=20)
    ttk.Checkbutton(root, text='選型', variable=agreement,onvalue=True,offvalue=False).place(x=10, y=50)


    ttk.Button(root, text="ok", command=clicked).place(x=60, y=100)

    root.mainloop()

if __name__ == '__main__':
    test2()