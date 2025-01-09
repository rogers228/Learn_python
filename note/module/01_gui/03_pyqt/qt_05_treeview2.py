import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTreeView, QVBoxLayout, QWidget
from PyQt6.QtGui import QStandardItemModel, QStandardItem

class TreeViewWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tree View Example")

        # 創建主佈局
        layout = QVBoxLayout()

        # 創建 TreeView
        tree_view = QTreeView()

        # 創建 ItemModel
        model = QStandardItemModel()

        # 添加數據
        root = model.invisibleRootItem()

        # root
        item1 = QStandardItem("root")
        item2 = QStandardItem("")
        item3 = QStandardItem("")
        root.appendRow([item1, item2, item3])
        # root.appendRow([item1])


        # 第二層
        item11 = QStandardItem("Item 1-1")
        item12 = QStandardItem("Item 1-2")
        item1.appendRow([item11])
        item1.appendRow([item12])
        # 第三層
        item111 = QStandardItem("Item 1-1-1")
        item112 = QStandardItem("Item 1-1-2")
        item12.appendRow([item111, item112])

        # 設置 TreeView 的模型
        tree_view.setModel(model)

        # 添加 TreeView 到佈局
        layout.addWidget(tree_view)

        # 創建一個 widget 並將佈局設置為它的佈局
        widget = QWidget()
        widget.setLayout(layout)

        # 設置 QMainWindow 的中央 widget
        self.setCentralWidget(widget)

def main():
    app = QApplication(sys.argv)
    window = TreeViewWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()






