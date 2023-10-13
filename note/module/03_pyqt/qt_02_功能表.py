import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenuBar
from PyQt6.QtGui import QAction, QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 設定主視窗標題
        self.setWindowTitle("Menu Example")

        # 創建功能表列
        menu_bar = self.menuBar()

        # 創建文件功能表
        file_menu = menu_bar.addMenu("File")

        # 創建動作（選項）
        new_action = QAction("New", self)
        open_action = QAction("Open", self)
        save_action = QAction("Save", self)
        exit_action = QAction("Exit", self)

        # 將動作添加到文件功能表
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)

        # 添加分隔線
        file_menu.addSeparator()

        # 將退出動作添加到文件功能表
        file_menu.addAction(exit_action)

        # 連接退出動作到關閉應用程式的函數
        exit_action.triggered.connect(self.close)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # sys.exit(app.exec())
    app.exec()

if __name__ == '__main__':
    main()
