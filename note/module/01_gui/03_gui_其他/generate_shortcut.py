# 建立捷徑 使用 pythonw.exe 來開啟 gui 不會出現 cmd視窗
# 直接使用 bat命令 因為會開啟cmd視窗，再執行命令，故一定會有cmd視窗

import os
import win32com.client

def create_shortcut(
    target_exe: str,
    work_dir: str,
    arguments: str,
    description: str,
    icon_path: str,
    shortcut_path: str = None
):
    """
    建立 Windows 桌面捷徑 (.lnk) 的專用函數

    :param target_exe: 執行檔路徑 (例如 pythonw.exe)
    :param work_dir: 應用程式的工作目錄 (main.py 所在的資料夾)
    :param arguments: 傳入的參數 (例如 main.py)
    :param description: 捷徑說明
    :param icon_path: .ico 圖示的完整路徑
    :param shortcut_path: 捷徑建立的位置（可傳入資料夾路徑或完整的 .lnk 檔案路徑；若為 None 則預設建在桌面）
    """
    try:
        # 處理捷徑預設路徑
        if shortcut_path is None:
            desktop_dir = os.path.join(os.path.expanduser("~"), "Desktop")
            shortcut_path = os.path.join(desktop_dir, "yeoshe_portal.lnk")
        elif os.path.isdir(shortcut_path):
            # 如果傳入的是資料夾，自動補上預設的捷徑檔名
            shortcut_path = os.path.join(shortcut_path, "yeoshe_portal.lnk")

        shell = win32com.client.Dispatch('WScript.Shell')
        shortcut = shell.CreateShortcut(shortcut_path)

        shortcut.TargetPath = target_exe
        shortcut.WorkingDirectory = work_dir
        shortcut.Arguments = arguments
        shortcut.Description = description
        shortcut.IconLocation = icon_path  # 設定 .ico 圖示

        shortcut.Save()
        print(f"[成功] 捷徑已建立至: {shortcut_path}")
    except Exception as e:
        print(f"[失敗] 建立捷徑發生錯誤: {e}")

def dev_shortcut():
    target_exe = r"C:\Users\user\Documents\Rogers\python_deploy\python_environment\python-3.12.7-embed-amd64\pythonw.exe"
    work_dir = r"C:\Users\user\Documents\Rogers\python_deploy\generate_shortcut\test_app"
    script_args = "main.py"
    description = "公司內部數據處理系統"
    icon_path = r"C:\Users\user\Documents\Rogers\python_deploy\generate_shortcut\test_app\assets\logo.ico"
    shortcut_path = os.path.dirname(__file__)

    create_shortcut(
        target_exe=target_exe,
        work_dir=work_dir,
        arguments=script_args,
        description=description,
        icon_path=icon_path,
        shortcut_path=shortcut_path
    )



if __name__ == "__main__":
    dev_shortcut()