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


# linux 建立虛擬環境
在windows開發打字，透過sm同步至linux，但是使用ssh執行linux，
使用ssh 記得要在 linux 專案建立專屬的虛擬python環境
