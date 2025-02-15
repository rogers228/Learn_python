import subprocess
try:
    # 新進程
    subprocess.run([self.pyapp, script, argv], check=True)
except:
    sg.popup('執行錯誤!')

# subprocess.run 會等待子進程執行完畢後，主程式才繼續。
# 預設 check=False，即使命令執行失敗也不會報錯（可設 check=True 來強制報錯


import os
os.system()




# 確保執行
result1 = subprocess.run(command1, capture_output=True, text=True)
result1.check_returncode()  # 確保 command1 運行成功
if result1.returncode == 0: # 確保 command1 運行成功
    print('result1 is run finished')