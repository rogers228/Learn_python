# cmd 進入ssh
ssh rogers@192.168.0.135
fc4r5g36

# 使用 vpn 連線 linux
ssh rogers@100.87.21.116

# 動態儀錶板
htop
Ctrl + C 關閉

# 查看硬碟
df -h

# 查看CPU溫度
cat /sys/class/thermal/thermal_zone0/temp | awk '{print $1/1000 "°C"}'

# 以編輯器開啟文字檔
nano ~/projects/test/test.txt


# windows + linux 開發架構

1. 在windows環境建立專案(開發區)，使用Sublime Text開發編程
2. 在windows環境，專案使用github desktop 版本控制
3. 使用 Tailscale VPN 建立私人連線，可多台裝置使用，多處開發，並加入linux
4. 在linux環境，使用Samba 串接 windows，提供windows同步的橋樑
5. 在windows環境，建立網路磁碟 \\100.87.21.116\projects > P:，可更輕鬆查看server的檔案狀態
6. 在linux環境，建立專案(發布區) 建立虛擬python環境，避免汙染全域
7. 在windows環境，使用cmd介面ssh執行linux，開發測試查看返回結果
8. 在windows環境，專案裡裡用 python dirsync 進行精細控制同步，將專案(開發區)發布至linux(發布區)

## 建立 ssh金鑰

ssh-keygen -t rsa -b 4096 -f %userprofile%\.ssh\id_rsa_nopass -N ""               建立

type %userprofile%\.ssh\id_rsa.pub              輸出後複製


ssh rogers@100.87.21.116          登入

echo "貼上你剛剛複製的新 ssh-rsa 亂碼" > ~/.ssh/authorized_keys   寫入金鑰
