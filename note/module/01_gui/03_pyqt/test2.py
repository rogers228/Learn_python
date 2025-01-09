from PyQt6.QtWidgets import QApplication, QMenu
from PyQt6.QtGui import QAction, QIcon, QSystemTrayIcon

# 定義點擊事件
def on_tray_icon_activated(reason):
    print(f'Tray icon activated, reason: {reason}')

# 創建應用程序
app = QApplication([])

# 創建系統托盤圖示
tray_icon = QSystemTrayIcon(QIcon('python_icon.ico'), parent=None)

# 創建功能表
menu = QMenu()
open_action = QAction("Open", triggered=lambda: print('Open'))
save_action = QAction("Save", triggered=lambda: print('Save'))
exit_action = QAction("Exit", triggered=app.quit)
menu.addAction(open_action)
menu.addAction(save_action)
menu.addAction(exit_action)

tray_icon.setContextMenu(menu)
tray_icon.show()

# 監聽系統托盤圖示的事件
tray_icon.activated.connect(on_tray_icon_activated)

app.exec()
