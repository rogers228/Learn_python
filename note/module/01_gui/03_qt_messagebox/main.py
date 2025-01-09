# 引用模組 -----
import os, sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox, QPushButton)

# from PyQt5.QtCore import Qt, QPoint

# 引用內部模組 -----
from form1 import Ui_MainWindow

# 載入 UI 文件
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow();
        self.ui.setupUi(self) # 載入ui
        self.setWindowTitle(f'{os.path.basename(__file__)}')


        self.ui.pushButton_1.clicked.connect(self.pushButton_1_chick)
        self.ui.pushButton_2.clicked.connect(self.pushButton_2_chick)
        self.ui.pushButton_3.clicked.connect(self.pushButton_3_chick)
        self.ui.pushButton_4.clicked.connect(self.pushButton_4_chick)
    def pushButton_1_chick(self):
        QMessageBox.critical(None, 'Error', '這是錯誤訊息', QMessageBox.Ok)

    def pushButton_2_chick(self):
        QMessageBox.information(None, 'Information', '這是資訊訊息', QMessageBox.Ok)

    def pushButton_3_chick(self):
        QMessageBox.warning(None, 'Warning', '這是警告訊息', QMessageBox.Ok)

    def pushButton_4_chick(self):
        result = QMessageBox.question(None, 'Question', '你確定要繼續嗎？',
                              QMessageBox.Yes | QMessageBox.No, QMessageBox.No)  # 預設按鈕設為 No
        if result == QMessageBox.Yes:
            print("用戶選擇 Yes")
        else:
            print("用戶選擇 No")

def main():
    print('test')
    app = QApplication(sys.argv)
    argv1 = sys.argv[1] if len(sys.argv) > 1 else "no argv"
    print('argv1:', argv1)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()