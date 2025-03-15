# pyqt5 + multiprocessing.Process

如果需要共享變數，又要獨立運作，不阻塞主程序，應該使用multiprocessing.Process()，不應使用subprocess.Popen()


pyqt5與multiprocessing.Process()才是真正的絕妙組合，執行工作起來體感順暢。