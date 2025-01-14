import subprocess
import os
import tempfile

def open_in_sublime(content, sublime_path="subl"):
    try:
        # 建立臨時檔案
        with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode="w", encoding="utf-8") as temp_file:
            temp_file.write(content)
            temp_file_path = temp_file.name

        # 使用 subprocess 呼叫 Sublime Text 開啟檔案
        subprocess.run([sublime_path, temp_file_path])

        # 事後刪除檔案
        # os.remove(temp_file_path)
    finally:
        # 注意：檔案不會自動刪除，視需求自行清理
        print(f"臨時檔案路徑：{temp_file_path}")

# 使用範例
my_string = "這是我要顯示的內容！"
open_in_sublime(my_string)


