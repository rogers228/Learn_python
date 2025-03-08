import os
import time
import tempfile
import subprocess

def find_subl():
    """嘗試尋找 subl 位置"""
    result = None
    subl_paths = [
        r"C:\Program Files\Sublime Text\sublime_text.exe",
        r"C:\Program Files (x86)\Sublime Text\sublime_text.exe",
    ]
    for path in subl_paths:
        if os.path.exists(path):
            return path

    if result is None:
        print('sublime text 找不到')

    return resule

def delete_file_later(filename, delay=5):
    """延遲刪除檔案"""
    print('delete_file_later')
    time.sleep(delay)
    if os.path.exists(filename):
        # print('ready delete')
        os.remove(filename)
        print(f"暫存檔 {filename} 已刪除")
    else:
        print(f'{filename} 不存在!')

def test1():
    subl = find_subl()
    if subl is None:
        return

    file = os.path.join(os.path.dirname(__file__), 'file_19_獲取檔案列表.py')
    # print(file)
    with open(file, 'r', encoding ='utf-8') as f:
        content = f.read()
    # print(content)

    # create temp
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w", encoding="utf-8") as t:
        t.write(content)
        temp_filename = t.name  # 獲取檔案名稱
    print(temp_filename)

    subprocess.run([subl, temp_filename])
    delete_file_later(temp_filename, delay=2) # 在 2 秒後刪除檔案

if __name__ == '__main__':
    test1()