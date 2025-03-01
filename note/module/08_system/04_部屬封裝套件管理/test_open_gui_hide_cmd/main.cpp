#include <windows.h>

int main() {
    STARTUPINFO si = { sizeof(STARTUPINFO) };
    PROCESS_INFORMATION pi;

    // 執行 Python 腳本 (使用 pythonw.exe)
    if (CreateProcess(
        NULL,
        (LPSTR)"pythonw C:\\Users\\USER\\Documents\\Learn_python\\note\\module\\01_gui\\03_pyqt\\test1.py", // 指定要執行的命令
        NULL, NULL, FALSE,
        0, // 移除 CREATE_NO_WINDOW
        NULL, NULL, &si, &pi)) {
        // 如果需要等待執行完畢，可使用 WaitForSingleObject(pi.hProcess, INFINITE);
        CloseHandle(pi.hProcess);
        CloseHandle(pi.hThread);
    }
    return 0;
}
