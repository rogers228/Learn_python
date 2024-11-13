import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox,
    QTableWidget, QTableWidgetItem,
    QPushButton, QVBoxLayout, QWidget, QMenu)

from PyQt5.QtCore import Qt, QPoint
from PyQt5 import uic  # 用於直接載入 .ui 文件

# 載入 UI 文件
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('test.ui', self)  # 載入 .ui 文件

        # 直接訪問已經存在的 QTableWidget
        # self.tableWidget.setAlternatingRowColors(True) # 啟用隔行顏色
        self.tableWidget.setStyleSheet("""
            QTableWidget {
                alternate-background-color: lightgray; /* 隔行背景顏色 */
                selection-background-color: blue;  /* 選擇背景顏色 */
            }
            QHeaderView::section {
                background-color: #f0f0f0; /* 表頭背景顏色 */
            }
        """)
        self.tableWidget.horizontalHeader().setDefaultAlignment(Qt.AlignLeft) # 標題靠左
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)  # 啟用自訂右鍵選單
        self.tableWidget.customContextMenuRequested.connect(self.on_right_click)  # 連接右鍵點擊事件

        # 設置表頭
        # self.tableWidget.setHorizontalHeaderLabels(["列1", "列2", "列3"])
        self.tableWidget.cellClicked.connect(self.on_cell_clicked)

        # 找到按鈕並連接功能
        self.button = self.findChild(QPushButton, 'pushButton')  # 'pushButton' 是按鈕在 .ui 文件中的名稱
        self.button.clicked.connect(self.on_button_clicked)  # 連接按鈕功能

    def on_button_clicked(self):
        # 按鈕的點擊事件功能
        input_text = self.lineEdit.text()
        QMessageBox.information(self, "訊息", f"您輸入的是{input_text}")
        data = [
            ["資料1", "資料2", "資料3"],
            ["資料4", "資料5", "資料6"],
            ["資料7", "資料8", "資料9"],
        ]
        self.update_table(data)

    def on_cell_clicked(self, row, column):
        print(f"Clicked cell at row {row}, column {column}")

    def update_table(self, data):
        tb = self.tableWidget
        tb.setRowCount(0) # clear
        tb.setColumnCount(3)  # 設定列數
        tb.setHorizontalHeaderLabels(["列1", "列2", "列3"])
        # 更新 QTableWidget 的資料
        for row_data in data:
            row_position = tb.rowCount()  # 獲取目前行數
            print('row_position:', row_position)
            tb.insertRow(row_position)  # 插入新行
            for column_index, item in enumerate(row_data):
                # print('row_data:', row_data)
                tb.setItem(row_position, column_index, QTableWidgetItem(item))  # 設定單元格內容

    def on_right_click(self, pos: QPoint):
        # 獲取右鍵點擊位置的行與列
        row = self.tableWidget.rowAt(pos.y())
        column = self.tableWidget.columnAt(pos.x())
        print(f"Right-clicked cell at row {row}, column {column}")

        # 建立右鍵選單
        menu = QMenu(self)
        action1 = menu.addAction("操作 1")
        menu.addSeparator() # 分隔線
        action2 = menu.addAction("操作 2")

        # 顯示選單，並獲取使用者選擇的選項
        action = menu.exec_(self.tableWidget.viewport().mapToGlobal(pos))

        # 根據選項執行不同動作
        if action == action1:
            QMessageBox.information(self, "訊息", f"在行 {row}, 列 {column} 執行操作 1")
        elif action == action2:
            QMessageBox.information(self, "訊息", f"在行 {row}, 列 {column} 執行操作 2")

def main():
    app = QApplication(sys.argv)
    argv1 = sys.argv[1] if len(sys.argv) > 1 else "no argv"
    print('argv1:', argv1)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()