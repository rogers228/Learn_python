from types import SimpleNamespace

data = {'key': 'value', 'another_key': 42}
dic = SimpleNamespace(**data)

print(dic.key)  # 輸出: value
print(dic.another_key)  # 輸出: 42

# SimpleNamespace 適合靜態結構的資料，新增鍵值需要重新建立對象。