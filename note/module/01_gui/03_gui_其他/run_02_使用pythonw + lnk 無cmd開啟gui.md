# 無cmd視窗 絲滑的開啟 GUI

pythonw.exe 的底層奧秘在於，它是直接以 Windows GUI 子系統（而非 Console 子系統）編譯出來的執行檔。當你透過 .lnk 捷徑直接呼叫它時，Windows 資源管理器從一開始就「根本不會為它分配任何終端機視窗」。這就是為什麼它能做到真正意義上的零閃爍、極速、無感啟動。


# 正確使用方式

不是使用命令來執行 pythonw.exe，而是使用捷徑來執行 pythonw.exe。

因為使用命令本身就會執行命令視窗，再開始執行命令，故 一定會有cmd視窗。

請使用 generate_shortcut.py 來建立捷徑