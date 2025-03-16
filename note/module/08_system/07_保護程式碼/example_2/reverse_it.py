
def main():
    with open('func.py', 'r', encoding='utf-8') as f:
        content = f.read()
    print(content)

    with open('func_reversed.py', 'w', encoding='utf-8') as f:
        f.write(content[::-1])

    print('created reversed.')

if __name__ == '__main__':
    main()