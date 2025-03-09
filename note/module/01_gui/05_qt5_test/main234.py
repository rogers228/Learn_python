import sys, os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox,
    QTableWidget, QTableWidgetItem,
    QPushButton, QVBoxLayout, QWidget, QMenuBar, QMenu, QAction)

from PyQt5.QtCore import Qt, QPoint
from PyQt5 import uic  # 用於直接載入 .ui 文件

from main234_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow();
        self.ui.setupUi(self) # 載入ui
        self.setWindowTitle(f'main')
        self.resize(487, 373)  # 設定視窗大小
        self.menu_bar()

    def menu_bar(self):
        menubar = self.menuBar()
        menu_config = {
            '文件': [
                ('&開啟', self.open_file, 'Alt+O'),  # Alt + O
                ('&儲存', self.save_file, 'Alt+S'),  # Alt + S
                ('檢視方式', [
                    ('&全螢幕', self.full_screen, 'Alt+F11'),  # Alt + F11
                    ('&還原', self.restore_screen, 'Alt+F10')  # Alt + F10
                ]),
                None,  # 分隔線
                ('&退出', self.close, 'Alt+X')  # Alt + X
            ],
            '&Help(說明)': [  # Alt + H
                ('檢查更新', self.check_update, 'Alt+U'),  # Alt + U
                ('&設定', self.open_settings, 'Alt+E')  # Alt + E
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
                    for sub_action_name, sub_action_method, sub_shortcut in action[1]:
                        sub_act = QAction(sub_action_name, self)
                        sub_act.triggered.connect(sub_action_method)
                        sub_act.setShortcut(sub_shortcut)  # 設定快捷鍵
                        sub_menu.addAction(sub_act)
                else:
                    action_name, action_method, shortcut = action
                    act = QAction(action_name, self)
                    act.triggered.connect(action_method)
                    act.setShortcut(shortcut)  # 設定快捷鍵
                    menu.addAction(act)

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