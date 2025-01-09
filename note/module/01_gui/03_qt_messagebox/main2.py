import os, sys
from PyQt5.QtWidgets import QApplication , QMessageBox

def show_message():
    app = QApplication([])
    QMessageBox.critical(None, 'Error', '這是錯誤訊息', QMessageBox.Ok)

    result = QMessageBox.question(None, 'Question', '你確定要繼續嗎？',
                          QMessageBox.Yes | QMessageBox.No, QMessageBox.No)  # 預設按鈕設為 No
    if result == QMessageBox.Yes:
        print("用戶選擇 Yes")
    else:
        print("用戶選擇 No")
def test1():
    show_message()

if __name__ == '__main__':
    test1()
