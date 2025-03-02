#include <windows.h>

int main() {
    // 取得當前執行檔的完整路徑
    char exePath[MAX_PATH];
    GetModuleFileName(NULL, exePath, MAX_PATH);

    // 從完整路徑中剔除檔案名稱，只保留資料夾路徑
    char *lastSlash = strrchr(exePath, '\\');
    if (lastSlash != NULL) {
        *lastSlash = '\0'; // 將最後一個反斜線替換為字串結束符號
    }

    // 將工作目錄設為 exe 所在的資料夾
    SetCurrentDirectory(exePath);

    STARTUPINFO si = { sizeof(STARTUPINFO) };
    PROCESS_INFORMATION pi;

    // 執行 Python 腳本 (使用 pythonw.exe)
    if (CreateProcess(
        NULL,
        (LPSTR)"pythonw test\\test1.py", // 執行命令
        NULL, NULL, FALSE,
        0, // 移除 CREATE_NO_WINDOW
        NULL, NULL, &si, &pi)) {
        // 如果需要等待執行完畢，可使用 WaitForSingleObject(pi.hProcess, INFINITE);
        CloseHandle(pi.hProcess);
        CloseHandle(pi.hThread);
    }
    return 0;
}

// 命令說明
// pythonw 專為開啟 windows gui
// 使用相對路徑 路徑應使用兩個右斜 \\ 