import types
import os

def load_module(input_file):
    """從 script.txt 讀取二進位字串，動態建立 Python 模組"""
    with open(input_file, 'r', encoding='utf-8') as f:
        binary_content = f.read()

    # 轉換回原始 Python 代碼
    original_code = ''.join(chr(int(binary_content[i:i+8], 2)) for i in range(0, len(binary_content), 8))

    # 取檔名作為模組名稱，移除副檔名
    module_name = os.path.splitext(os.path.basename(input_file))[0]

    # 建立模組
    module = types.ModuleType(module_name)
    exec(original_code, module.__dict__)  # 在模組作用域執行代碼

    # print(f"✅ 已從 {input_file} 讀取並載入模組 {module_name}")
    return module

sp = load_module("tool_module_b.py")

def test1():
    print(sp.add(3, 5))

if __name__ == '__main__':
    test1()