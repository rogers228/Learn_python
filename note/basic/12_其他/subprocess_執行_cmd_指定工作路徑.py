import subprocess

# 指定要運行的命令和工作路徑
command = 'dir'
cwd = 'C:/Users/your-username/Documents'

# 使用 subprocess.run 函數運行命令
result = subprocess.run(command, cwd=cwd, shell=True, capture_output=True, text=True)

# 輸出命令的結果
print(result.stdout)


'''
在這個例子中，我們運行了一個名為 dir 的命令，
並指定工作路徑為 C:/Users/your-username/Documents。
我們使用了 subprocess.run 函數來運行命令，
並將 cwd 參數設置為指定的工作路徑。

需要注意的是，在 Windows 中，我們需要將 shell 參數設置為 True，
以便運行命令解析器 (cmd.exe)。在 Linux 或 macOS 中，可以將 shell 參數設置為 False，
以避免運行命令解析器。另外，capture_output 參數可以將命令的輸出捕獲到 result.stdout 屬性中，
而 text 參數則可以指定命令的輸入和輸出應該使用文本模式處理。
''''