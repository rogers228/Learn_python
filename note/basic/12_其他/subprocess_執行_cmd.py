import subprocess
try:
    # 新進程
    subprocess.run([self.pyapp, script, argv], check=True)
except:
    sg.popup('執行錯誤!')



import os
os.system()