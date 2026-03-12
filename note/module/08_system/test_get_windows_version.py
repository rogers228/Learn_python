# 啟動時
# 檢測 windows 版本是否可用，太新未驗證 阻止使用
# 檢查使用期限 是否超過使用限制

import winreg
from datetime import date, timedelta
import sys

# -------------------------------
# 配置（人工填寫）
# -------------------------------
# 例如人工測試通過後填寫：
MAX_SUPPORTED_BUILD = 22631 # Windows 11 23H2

SUPPORT_YEARS = 2
SOFTWARE_RELEASE_DATE = date(2025, 3, 12)
# -------------------------------

def get_windows_build():
    """取得當前 Windows Build + UBR"""
    key_path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion"
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
        build = int(winreg.QueryValueEx(key, "CurrentBuildNumber")[0])
        ubr = int(winreg.QueryValueEx(key, "UBR")[0])
        return build, ubr

def check_windows_support():
    """檢查 Windows build 是否支援"""
    build, ubr = get_windows_build()
    build_version = f"{build}.{ubr}"
    print(f"Detected Windows build: {build_version}")
    print(f"Configured MAX_SUPPORTED_BUILD: {MAX_SUPPORTED_BUILD}")

    if build > MAX_SUPPORTED_BUILD:
        sys.exit(
            f"Windows build {build_version} exceeds MAX_SUPPORTED_BUILD "
            f"({MAX_SUPPORTED_BUILD}). Program cannot run."
        )
    else:
        print(f"Windows build {build_version} is supported.")

def check_software_support():
    """檢查軟體支援期限"""
    support_end_date = SOFTWARE_RELEASE_DATE + timedelta(days=SUPPORT_YEARS*365)
    today = date.today()
    if today > support_end_date:
        sys.exit(f"Software support expired on {support_end_date}. Please update.")
    print(f"Software is within support period (until {support_end_date}).")

if __name__ == "__main__":
    # 1️⃣ 顯示當前環境的 Windows build，供人工確認
    current_build, current_ubr = get_windows_build()
    print(f"Current Windows build detected: {current_build}.{current_ubr}")

    # 2️⃣ 檢查是否符合已填寫的 MAX_SUPPORTED_BUILD
    check_windows_support()
    check_software_support()

    print("Environment OK. Program can start.")