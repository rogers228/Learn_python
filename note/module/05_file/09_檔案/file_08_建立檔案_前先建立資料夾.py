# 找到變數 PRIVATE_JSON 所指檔案的父目錄路徑
# 然後創建這個目錄（包括所有必要的上層目錄），如果目錄已經存在，則不要報錯。
os.makedirs(os.path.dirname(PRIVATE_JSON), exist_ok=True)
with open(PRIVATE_JSON, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)