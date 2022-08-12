import click

@click.command() # 命令行入口
@click.option('-name', help='your name', required=True) # required 必要的
def test1(name):
    click.echo(f"Hello, {name}!")

if __name__ == '__main__':
    test1()

# cmd
# python click02_必要參數.py --help
# python click02_必要參數.py -name Andy