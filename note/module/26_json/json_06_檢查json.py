import re
import json

# 包含 \n 控制字符的 json
json_string = '''{
  "name": "John Doe",
  "age": 30,
  "address": "123 Main St
New York, NY"
}'''

def clean_json_string(json_string):
    # 仅替换非法的控制字符
    clean_string = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', lambda x: '\\u{:04x}'.format(ord(x.group())), json_string)
    # 将换行符替换为合法的 \n
    clean_string = clean_string.replace('\n', '\\n')
    return clean_string

def test1():
    cleaned_json_string = clean_json_string(json_string)
    print("Cleaned JSON String:")
    print(cleaned_json_string)

    try:
        data = json.loads(cleaned_json_string)
        print("JSON parsed successfully!")
        print(data)
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")

if __name__ == '__main__':
    test1()
