import os
import subprocess
import shutil

def find_7z_exe():
    """嘗試尋找 7z.exe 位置"""
    possible_paths = [
        r"C:\Program Files\7-Zip\7z.exe",
        r"C:\Program Files (x86)\7-Zip\7z.exe",
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    return shutil.which("7z")  # 嘗試從系統 PATH 找 7z.exe

def extract_7z(archive_path, output_dir):
    """使用 7z.exe 解壓縮 7z 檔案"""
    seven_zip = find_7z_exe()
    if not seven_zip:
        print("找不到 7z.exe，請安裝 7-Zip 或設定環境變數。")
        return False

    if not os.path.exists(archive_path):
        print(f"找不到壓縮檔: {archive_path}")
        return False

    os.makedirs(output_dir, exist_ok=True) # 建立輸入資料夾，若存在則繼續

    cmd = [seven_zip, "x", archive_path, f"-o{output_dir}", "-y"]
        # x：解壓縮檔案
        # -o目標目錄：指定解壓縮目標資料夾
        # -y：自動確認所有提示（避免手動確認覆蓋檔案）
    try:
        subprocess.run(cmd, check=True)
        print(f"解壓縮完成: {output_dir}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"解壓縮失敗: {e}")
        return False

def test1():
    archive_file = r"C:\Users\USER\Desktop\test2\test.7z"
    extract_to = r"C:\Users\USER\Documents\Learn_python\note\module\08_system\04_部屬封裝套件管理\example_extract\output"
    extract_7z(archive_file, extract_to)

if __name__ == '__main__':
    test1()