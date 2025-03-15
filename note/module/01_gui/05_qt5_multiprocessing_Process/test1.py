import sys
import time
import multiprocessing
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import pyqtSignal, QObject, QThread

# PyQt5 信號物件
class WorkerSignals(QObject):
    finished = pyqtSignal(str)

# 耗時任務（子進程執行）
def long_running_task(queue):
    time.sleep(5)  # 模擬耗時 5 秒
    queue.put("任務完成！")  # 把結果放入 multiprocessing.Queue()

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PyQt5 + multiprocessing")
        self.setGeometry(100, 100, 300, 200)

        self.label = QLabel("按下按鈕開始任務...", self)
        self.button = QPushButton("開始耗時任務", self)
        self.button.clicked.connect(self.start_process)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

        # 創建 PyQt5 信號
        self.worker_signals = WorkerSignals()
        self.worker_signals.finished.connect(self.update_label)  # 當收到信號時更新 UI

    def start_process(self):
        self.label.setText("執行中，請稍候...")

        # 創建 Queue 來傳遞訊息
        self.queue = multiprocessing.Queue()

        # 啟動子進程
        self.process = multiprocessing.Process(target=long_running_task, args=(self.queue,))
        # daemon=True 子進程隨著主程序結束

        
        self.process.start()

        # 使用 QThread 監聽 Queue 是否有結果
        self.listener_thread = QThread()
        self.listener_thread.run = self.check_queue
        self.listener_thread.start()

    def check_queue(self):
        """在 QThread 中監聽 Queue，當有結果時通知 UI"""
        while True:
            if not self.queue.empty():
                message = self.queue.get()
                self.worker_signals.finished.emit(message)  # 透過信號更新 UI
                break
            time.sleep(0.1)  # 避免高 CPU 負載

    def update_label(self, message):
        self.label.setText(message)

if __name__ == "__main__":
    multiprocessing.freeze_support()  # Windows 需要這行
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
