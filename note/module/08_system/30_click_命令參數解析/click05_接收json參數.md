
```py
import click
import json

@click.command()
@click.option("--data", type=str, required=True, help="JSON format dictionary")
def process_dict(data):
    """接收 JSON 字串並轉換為字典"""
    try:
        parsed_data = json.loads(data)  # 解析 JSON 字串為 dict
        click.echo(f"接收到的字典: {parsed_data}")
    except json.JSONDecodeError:
        click.echo("❌ 錯誤: 無效的 JSON 格式！")

if __name__ == "__main__":
    process_dict()
```

```bash
    python script.py --data '{"name": "Alice", "age": 25, "city": "Taipei"}'
```