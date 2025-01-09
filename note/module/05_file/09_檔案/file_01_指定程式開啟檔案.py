#使用指定程式開啟檔案
import subprocess
uApp = r'C:\Program Files (x86)\Notepad++\notepad++.exe'
myfile = r'\\220.168.100.104\油聖油昇共用資料庫-1\0-部門間資料分享平台使用完應刪除\1-設計課\給小陸\20170603\129.txt'
subprocess.Popen('%s %s' % (uApp, myfile))
