import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStatusBar, QLabel, QWidget, QHBoxLayout
from PyQt6.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Status Bar Example")
        self.setGeometry(100, 100, 400, 300)
        self.resize(800, 600)
        # 創建一個狀態列並將其設置為視窗的狀態列
        status_bar = self.statusBar()

        # 創建三個不同的訊息
        message1 = "This is message 1"
        message2 = "This is message 2"
        message3 = "This is message 3"

        # 在狀態列中添加三個標籤小部件來顯示這些訊息
        label1 = QLabel(message1, self)
        label2 = QLabel(message2, self)
        label3 = QLabel(message3, self)
        label4 = QLabel('', self)

        label3.setToolTip("This is message 3 tooltip")  # 添加工具提示

        # 添加圖標到第三個標籤
        icon = QIcon("python_icon.ico")  # 替換 "icon.png" 為你自己的圖標路徑
        label4.setPixmap(icon.pixmap(16, 16))  # 設置圖標大小

        # 創建一個容器小部件來容納右側的小部件
        right_container = QWidget()
        right_layout = QHBoxLayout()
        right_container.setLayout(right_layout)

        # 添加一個 spacer 將第三個小部件推到右側
        right_layout.addStretch(1)
        right_layout.addWidget(label4)
        right_layout.addWidget(label3)
        
        # 在狀態列中添加左側的小部件
        status_bar.addWidget(label1)
        status_bar.addWidget(label2)

        # 在狀態列中添加容器小部件，包含右側的小部件
        status_bar.addPermanentWidget(right_container)

        # 使用樣式表來調整狀態列文字的大小
        status_bar.setStyleSheet("QLabel { font-size: 12pt; }")  # 調整文字大小為12pt
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
