import click

@click.command() # 命令行入口
@click.option("--count", default=1, help="Number of greetings.") # 參數名稱 預設值 說明
@click.option("--name", prompt="Your name", help="The person to greet.")  # 參數名稱 預設值 說明
def hello(count=1, name=''):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo(f"Hello, {name}!")

if __name__ == '__main__':
    hello()
    # hello(10, 'Allen')


# CMD
# 顯示所有說明
# python click01_test.py --help

# 可靈活的使用參數 比 sys.argv 好用太多了
# python click01_test.py --name Rogers
# python click01_test.py --name Rogers --count 3
# python click01_test.py --count 3 --name Julia