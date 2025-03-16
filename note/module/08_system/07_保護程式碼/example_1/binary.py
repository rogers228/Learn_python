def save_script_as_binary(input_file, output_file):
    """讀取 script.py 轉換為二進位字串，存入 script.txt"""
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 將文件內容轉換為無空格的二進位表示
    binary_content = ''.join(format(ord(char), '08b') for char in content)

    # 將二進位字串寫入 script.txt
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(binary_content)
    print(f"✅ 已將 {input_file} 轉換為二進位並存入 {output_file}")


def main():
    save_script_as_binary("tool_module.py", "tool_module_b.py")

if __name__ == '__main__':
    main()