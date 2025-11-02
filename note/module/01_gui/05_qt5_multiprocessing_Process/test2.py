import sys
import time
import multiprocessing
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
# 引入 QThread, QObject, pyqtSignal
from PyQt5.QtCore import pyqtSignal, QObject, QThread, QTimer

# ----------------------------------------------------
# 1. PyQt5 信號物件
class WorkerSignals(QObject):
    finished = pyqtSignal(dict)
    # 也可以新增一個 error 或 progress 信號

# ----------------------------------------------------
# 2. 耗時任務 (子進程執行)
def long_running_task(queue):
    print('long_running_task')
    # 子進程中執行 sleep 不會阻塞 UI
    time.sleep(2)
    result = {'is_finished' : True, 'data': 'Result from Process'}
    queue.put(result)
    print('long_running_task finished')
# ----------------------------------------------------

# 3. Queue 監聽器 Worker (在 QThread 中執行)
class QueueListener(QObject):
    """將監聽邏輯封裝在這個 Worker 裡，它將運行在 QThread 中"""
    finished = pyqtSignal(dict) # 任務完成時發出結果訊號

    def __init__(self, queue: multiprocessing.Queue, parent=None):
        super().__init__(parent)
        self.queue = queue
        self._running = True # 控制迴圈的開關

    def stop(self):
        self._running = False

    def run(self):
        """這是 Worker 真正運行的地方，將由 QThread.started 呼叫"""
        print("QueueListener 啟動監聽...")
        while self._running:
            if not self.queue.empty():
                result = self.queue.get()
                self.finished.emit(result)  # 透過信號發送結果
                self.stop() # 收到結果後停止監聽迴圈

            # 使用 QThread.msleep 代替 time.sleep，更符合 Qt 標準
            QThread.msleep(100)

        print("QueueListener 停止。")


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        # 追蹤 QThread 和 Process 實例
        self.process = None
        self.listener_thread = None
        self.queue = None
        self.initUI()
        self.button.setEnabled(True)

    def initUI(self):
        self.setWindowTitle("PyQt5 + multiprocessing")
        self.setGeometry(100, 100, 400, 200)

        self.label = QLabel("按下按鈕開始任務...", self)
        self.button = QPushButton("開始耗時任務", self)
        self.button.clicked.connect(self.start_process)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def start_process(self):
        self.label.setText("執行中，請稍候...")
        self.button.setEnabled(False) # 鎖住按鈕，防止重複啟動

        # 1. 創建 IPC Queue
        self.queue = multiprocessing.Queue()

        # 2. 啟動子進程
        self.process = multiprocessing.Process(target=long_running_task, args=(self.queue,))
        self.process.daemon = True # 讓子進程隨主程序結束
        self.process.start()

        # 3. 啟動監聽線程 (QThread 標準模式)
        self.listener_thread = QThread()
        self.listener_worker = QueueListener(self.queue)

        # 將 Worker 移動到新線程中
        self.listener_worker.moveToThread(self.listener_thread)

        # 連接：線程啟動 -> Worker.run
        self.listener_thread.started.connect(self.listener_worker.run)

        # 連接：Worker 完成 -> 更新 UI (cross-thread signal)
        self.listener_worker.finished.connect(self.update_label)

        # 連接：Worker 完成 -> 清理線程
        self.listener_worker.finished.connect(self.stop_and_cleanup)

        self.listener_thread.start()

    def stop_and_cleanup(self):
        """在 Worker 完成後安全地停止並清理線程和行程"""
        self.listener_thread.quit()
        self.listener_thread.wait() # 等待線程安全退出
        self.listener_thread.deleteLater()
        self.listener_worker.deleteLater()

        # 清理子行程
        if self.process and self.process.is_alive():
            self.process.terminate() # 確保子進程結束
            self.process.join()

    def update_label(self, result):
        """在主線程中被 Signal 呼叫，安全更新 UI"""
        print('update_label called in main thread.')
        print("Result:", result)

        if result['is_finished']:
            self.label.setText(f'任務完成！收到數據: {result.get("data")}')
        else:
            self.label.setText('任務異常結束。')

        self.button.setEnabled(True) # 恢復按鈕

if __name__ == "__main__":
    multiprocessing.freeze_support()
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())