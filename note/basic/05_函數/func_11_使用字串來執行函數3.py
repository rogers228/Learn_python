import gui_sav07

def main(name):
    dic = {'sav07': sav07} 
    func = dic.get(name, None)
    if func is not None:
        func()

def sav07():
    gui_sav07.Gui_sav07()

if __name__ == '__main__':
    main('sav07')