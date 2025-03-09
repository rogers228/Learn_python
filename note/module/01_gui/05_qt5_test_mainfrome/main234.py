import sys, os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox,
    QTableWidget, QTableWidgetItem,
    QPushButton, QVBoxLayout, QWidget, QMenuBar, QMenu, QAction)

from PyQt5.QtCore import Qt, QPoint
from PyQt5 import uic  # 用於直接載入 .ui 文件
from PyQt5.QtWebEngineWidgets import QWebEngineView
import markdown
from main234_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow();
        self.ui.setupUi(self) # 載入ui
        self.setWindowTitle(f'main')
        self.resize(487, 373)  # 設定視窗大小
        self.menu_bar()

        self.ui.web_view: QWebEngineView 
        self.load_notice()

    def resizeEvent(self, event):
        """當視窗大小變更時，調整 webView 大小"""
        self.ui.web_view.setGeometry(0, 0, self.width(), self.height())  # 設定大小
        event.accept()
        
    def menu_bar(self):
        menubar = self.menuBar()
        menu_config = {
            '文件': [
                ('開啟', self.open_file), 
                ('儲存', self.save_file),
                ('檢視方式', [
                    ('全螢幕', self.full_screen), 
                    ('還原', self.restore_screen) 
                ]),
                None,  # 分隔線
                ('退出', self.close)
            ],
            'Help': [ 
                ('檢查更新', self.check_update),
                ('設定', self.open_settings)
            ]
        }

        for menu_name, actions in menu_config.items():
            menu = menubar.addMenu(menu_name)
            menu.setStyleSheet("min-width: 150px;") 
            for action in actions:
                if action is None:
                    menu.addSeparator()
                elif isinstance(action[1], list):  # 子選單
                    sub_menu = menu.addMenu(action[0])
                    for sub_action_name, sub_action_method in action[1]:
                        sub_act = QAction(sub_action_name, self)
                        sub_act.triggered.connect(sub_action_method)
                        sub_menu.addAction(sub_act)
                else:
                    action_name, action_method  = action
                    act = QAction(action_name, self)
                    act.triggered.connect(action_method)
                    menu.addAction(act)

    def load_notice(self):
        with open('info.md', "r", encoding="utf-8") as f:
            md_content = f.read()
            html_content = markdown.markdown(md_content) # markdown to html
        print(html_content)
        html_template = f"""
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                h1 {{ color: #2c3e50; }}
                pre {{ background: #f4f4f4; padding: 10px; border-radius: 5px; }}
                code {{ color: #e74c3c; }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """
        self.ui.web_view.setHtml(html_template)
        # self.ui.web_view.setUrl("公告的 HTML 頁面") 來讀取網頁上的公告。
    def open_file(self):
        print("開啟文件功能")

    def full_screen(self):
        print("全螢幕模式")
        self.showFullScreen()

    def restore_screen(self):
        print("還原視窗")
        self.showNormal()

    def save_file(self):
        print("儲存文件功能")

    def check_update(self):
        print("檢查更新功能")
        
    def open_settings(self):
        print("開啟設定功能")

def main():
    app = QApplication(sys.argv)
    argv1 = sys.argv[1] if len(sys.argv) > 1 else "no argv"
    print('argv1:', argv1)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()