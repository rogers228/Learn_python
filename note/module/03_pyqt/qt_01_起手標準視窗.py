import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setWindowIcon(QIcon("python_icon.ico"))
        self.resize(800, 600)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()

if __name__ == '__main__':
    main()

