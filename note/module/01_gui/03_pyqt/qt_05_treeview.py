import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QTreeWidget, QTreeWidgetItem, \
                            QHBoxLayout, QVBoxLayout, QItemDelegate
from PyQt6.QtCore import Qt, QRegularExpression #QRegExp
from PyQt6.QtGui import QRegularExpressionValidator

class TreeWidgetDelegate(QItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent=parent)
        pattern = '[A-z0-9]+'
        reg = QRegularExpression(pattern)
        reg_validator = QRegularExpressionValidator(reg)
        editor.setValidator(reg_validator)
        return editor


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 700, 500
        self.resize(self.window_width, self.window_height)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.tree = QTreeWidget()
        self.tree.itemDoubleClicked.connect(self.rename_value)
        #self.tree.itemChanged.connect(self.checkName, Qt.QueuedConnection) # <-- for PyQt5
        self.tree.itemChanged.connect(self.checkName, Qt.ConnectionType.QueuedConnection)
        self.layout.addWidget(self.tree)

        for i in range(5):
            item = QTreeWidgetItem([str(i)*3])
            self.tree.addTopLevelItem(item)

        delegate = TreeWidgetDelegate()
        self.tree.setItemDelegate(delegate)

    def checkName(self, item, column):
        item_text = item.data(0, 0)
        siblings = self.getSiblings(item)

        if item_text in siblings:
            print('Duplicate Item')
            item.setData(0, 0, 'Please enter a new value')
            self.tree.editItem(item)

    def getSiblings(self, item):
        siblings = [self.tree.topLevelItem(i).data(0, 0) for i in range(self.tree.topLevelItemCount())]
        item_text = item.data(0, 0)

        if item_text in siblings:
            siblings.remove(item_text)
        return siblings

    def rename_value(self):
        item = self.tree.selectedItems()
        if item:
            item = item[0]
            item.setFlags(item.flags() | Qt.ItemFlags.ItemIsEditable)


if __name__ == '__main__':
    # don't auto scale when drag app to a different monitor.
    # QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 12px;
        }
    ''')
    
    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')