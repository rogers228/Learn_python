## 進程 process 是一個獨立的執行個體，底下可以多個線，

子進程 subprocess 用於開啟新進程，完全獨立，不受主程式影響。
多線程 threading 用於在 python 內部運行，可共享變數，適合 I/O 密集任務。
同步運算 multiprocessing.Process() 用於在 python 內部運行，，可共享變數，使用CPU多核心，單核心也行。


## 獨立運作的子進程
如果需要共享變數，又要獨立運作，不阻塞主程序，應該使用multiprocessing.Process()，不應使用subprocess.Popen() 