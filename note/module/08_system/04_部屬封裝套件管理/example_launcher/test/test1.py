# https://hackmd.io/@kaneyxx/HJdX8DXCr#13-WebView

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

# 建構第一個視窗

def buttonClick():
    print(123)

app = QApplication(sys.argv) # app變數將用sys來控制我們程式離開
w = QWidget() # 建構我們的視窗
w.setWindowTitle("open") # 設定視窗標題

# button
button = QPushButton("Fist Button", w) #("按鍵名稱", 放置的widget)
button.setToolTip("This will display message when I take mouse on button")
button.move(100,100)  #視窗左上=(0, 0)  向右為+x, 向下為+y
button.clicked.connect(buttonClick) #connect(函數名稱不用括號)
w.show() # 讓視窗顯現出來
sys.exit(app.exec_()) #sys.exit()當我們關閉程式時可以幫助我們離開