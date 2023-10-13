import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tab Example")
        self.resize(800, 600)
        # 創建一個主窗口的 widget
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # 創建一個 QVBoxLayout 來放置 Tab
        layout = QVBoxLayout(main_widget)

        # 創建一個 TabWidget
        tabs = QTabWidget()
        layout.addWidget(tabs)

        # 創建三個標籤
        tab1 = QLabel("This is Tab 1")
        tab2 = QLabel("This is Tab 2")
        tab3 = QLabel("This is Tab 3")

        # 在 TabWidget 中添加標籤
        tabs.addTab(tab1, "Tab 1")
        tabs.addTab(tab2, "Tab 2")
        tabs.addTab(tab3, "Tab 3")

        tabs.setStyleSheet("QTabBar::tab { font-size: 16px; width: 80px; height: 28px;}")  # 調整字體大小為16px，寬度為100px

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()