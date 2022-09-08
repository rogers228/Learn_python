def this_is_a_long_name_function(name):
    print(f'hello! {name}')

def test1():
    this_is_a_long_name_function('rogers')

    # change func name
    hello = this_is_a_long_name_function
    hello('rogers')

if __name__ == '__main__':
    test1()