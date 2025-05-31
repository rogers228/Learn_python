try:
    raise ValueError("格式錯誤")  # <---錯誤標示
except ValueError as e:
    print("處理了一些事情...")
    raise  # 繼續往外丟出例外

# | 例外類型                | 說明         |
# | ------------------- | ---------- |
# | `ValueError`        | 傳入不合法的數值   |
# | `TypeError`         | 資料型別錯誤     |
# | `IndexError`        | 索引超出範圍     |
# | `KeyError`          | 字典中找不到 key |
# | `FileNotFoundError` | 找不到檔案      |
# | `RuntimeError`      | 一般執行時錯誤    |
