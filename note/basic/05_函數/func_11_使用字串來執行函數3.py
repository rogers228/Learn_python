
def main(name):
    argv1 = 'allen'
    dic = {
        'sav07': sav07,
        'sav08': sav08(argv1),
        }
    func = dic.get(name, None)
    if func is not None:
        func()

def sav07():
    print('hi')

def sav08(name):
    print(f'hi {name}')

if __name__ == '__main__':
    main('sav08')