#include <windows.h>

int main() {
    STARTUPINFO si = { sizeof(STARTUPINFO) };
    PROCESS_INFORMATION pi;

    // ���� Python �}�� (�ϥ� pythonw.exe)
    if (CreateProcess(
        NULL,
        (LPSTR)"pythonw C:\\Users\\USER\\Documents\\Learn_python\\note\\module\\01_gui\\03_pyqt\\test1.py", // ���w�n���檺�R�O
        NULL, NULL, FALSE,
        0, // ���� CREATE_NO_WINDOW
        NULL, NULL, &si, &pi)) {
        // �p�G�ݭn���ݰ��槹���A�i�ϥ� WaitForSingleObject(pi.hProcess, INFINITE);
        CloseHandle(pi.hProcess);
        CloseHandle(pi.hThread);
    }
    return 0;
}
