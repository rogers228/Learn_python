import sys, os
import click

def computer_name():
    click.echo(f"電腦名稱 (COMPUTERNAME): {os.getenv('COMPUTERNAME')}")

def display_os():
    click.echo(f"作業系統平台: {sys.platform}")

FUNCTION_MAP = {
    'cn': computer_name,
    'os': display_os,
}

@click.command() # 命令行入口
@click.option('-name', help='your name', required=True) # required 必要的
def main(name):
    target_func = FUNCTION_MAP.get(name)
    if target_func:
        target_func()
    else:
        error_msg = f"錯誤：找不到對應的操作 '{name}'。"
        click.echo(error_msg, err=True)
        click.echo(f"請使用以下任一選項: {', '.join(FUNCTION_MAP.keys())}", err=True)
        sys.exit(1) # 設置返回碼，讓 shell 知道程式執行失敗

if __name__ == '__main__':
    main()

# cmd
# python click03_computer_name.py -name cn