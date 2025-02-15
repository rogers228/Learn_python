import subprocess

# 獨立運作新進程
# subprocess.Popen()（不阻塞主程式）
# 適合長時間運行的任務（如下載、更新）

subprocess.Popen(["python", "sub.py"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, close_fds=True)

# stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL 讓輸出不影響 main
# close_fds=True（Windows 用 creationflags=subprocess.DETACHED_PROCESS）確保 main 關閉時，sub.py 仍繼續運行。