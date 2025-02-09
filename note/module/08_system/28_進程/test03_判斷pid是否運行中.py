import ctypes
from ctypes.wintypes import HANDLE, DWORD, BOOL

def is_pid_running(pid):
    """使用 Windows API 判斷 PID 是否存在"""
    PROCESS_QUERY_INFORMATION = 0x0400
    process = ctypes.windll.kernel32.OpenProcess(PROCESS_QUERY_INFORMATION, False, pid)
    if process:
        ctypes.windll.kernel32.CloseHandle(process)
        return True
    return False

def test1():
    # 測試 PID 是否運行
    pdi = 6688
    if is_pid_running(pdi):
        print(f"PID {pdi} 正在運行")
    else:
        print(f"PID {pdi} 不存在或未運行")

if __name__ == '__main__':
    test1()