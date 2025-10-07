import subprocess

result = subprocess.run(["git", "--version"], capture_output=True, text=True)

# 檢查是否有安裝git
print(result.stdout) # git version 2.51.0.windows.2