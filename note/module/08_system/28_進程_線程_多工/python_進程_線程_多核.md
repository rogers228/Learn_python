進程 process 是一個獨立的執行個體，底下可以多個線，
子進程 subprocess 用於開啟新進程，完全獨立，不受主程式影響。
多線程 threading 用於在 python 內部運行，可共享變數，適合 I/O 密集任務。
同步運算 multiprocessing 用於在 python 內部運行，，預設不共享變數，可用在多核。
