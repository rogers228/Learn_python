import sys, os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox,
    QTableWidget, QTableWidgetItem,
    QPushButton, QVBoxLayout, QWidget, QMenu)

from PyQt5.QtCore import Qt, QPoint
from PyQt5 import uic  # 用於直接載入 .ui 文件

from main234_ui import Ui_MainWindow

# 載入 UI 文件
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow();
        self.ui.setupUi(self) # 載入ui
        self.setWindowTitle(f'main')
        self.resize(487, 373)  # 設定視窗大小
def main():
    app = QApplication(sys.argv)
    argv1 = sys.argv[1] if len(sys.argv) > 1 else "no argv"
    print('argv1:', argv1)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()