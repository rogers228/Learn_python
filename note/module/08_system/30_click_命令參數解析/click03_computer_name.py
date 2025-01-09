import sys, os
sys.path.append(os.getcwd())

import click

@click.command() # 命令行入口
@click.option('-name', help='your name', required=True) # required 必要的
def main(name):
    dic = {'cn': computer_name}
    func = dic.get(name, None)
    if func is not None:
        func()

def computer_name():
    click.echo(os.getenv('COMPUTERNAME'))

if __name__ == '__main__':
    main()

    # cmd
    # python click03_computer_name.py -name cn