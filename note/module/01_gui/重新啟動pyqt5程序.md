# 重新啟動pyqt5程序

重新啟動，就是開啟一個新實例，結束舊的程序。

```py
import sys
import os
import subprocess

def restart_app():
    subprocess.Popen([sys.executable] + sys.argv)
    sys.exit()
```