import os
import signal

def kill_pid(pid):
    try:
        # 終止指定的 PID
        os.kill(pid, signal.SIGTERM)  # 或使用 signal.SIGKILL（強制結束）
        print(f"成功終止 PID {pid}")
    except ProcessLookupError:
        print(f"PID {pid} 不存在或已終止")
    except PermissionError:
        print(f"沒有權限終止 PID {pid}")
    except Exception as e:
        print(f"無法終止 PID {pid}：{e}")

def test1():
    # 測試殺死進程
    pid_to_kill = 6688  # 替換為你要終止的 PID
    kill_pid(pid_to_kill)

if __name__ == '__main__':
    test1()