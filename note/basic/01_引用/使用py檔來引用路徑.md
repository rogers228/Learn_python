# custom_path.py
在 python 跟目錄建立 custom_path.py
```py custom_path.py
custom_path = {
    'hr_report_202208' : r'\\220.168.100.104\pdm\python_program\hr_report_202208',
    'pdm_202209':        r'\\220.168.100.104\pdm\python_program\pdm_202209',
    'bomcost_202301':    r'\\220.168.100.104\pdm\python_program\bomcost_202301',
    'make_202210':       r'\\220.168.100.104\pdm\python_program\make_202210',
    'rd_link':           r'\\220.168.100.104\pdm\python_program\rd_link',
    'rd_start':          r'\\220.168.100.104\pdm\python_program\rd_start',
    }
```

在專案中可直接匯入
```py
import custom_path # 讀取 虛擬環境中的 custom_path
sys.path.append(custom_path.custom_path['rd_start'])
```

# 缺點
更換環境時需重新設定