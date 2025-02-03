from io import StringIO
import pandas as pd
import json

def test1():
    # 定義帶有空白的 CSV 字串
    csv_string = """
        index, name,  weidth,  comment
        1,    lower,       0,  test1
        2,    middle,      4,  test2
        3,    normal,     42,
        4,    buzz,       44,
        5,    high,        8,
        6,    higher,      1,
        7,    bigger,      0,
    """

    csv_data = StringIO(csv_string) # 使用 StringIO 模擬 CSV 文件
    df = pd.read_csv(csv_data, sep=",") # 讀取 CSV，清理欄位名稱的多餘空白
    df.columns = df.columns.str.strip()  # 清理欄位名稱空白
    df["index"] = df["index"].astype(int) # 確保 'index' 欄位作為整數型別的 key
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x) # 清理所有欄位值中的空白
    df['comment'] = df['comment'].fillna('') # nan 空白

    # 將資料轉為字典格式，並設定 key 為整數類型
    result_dict = df.set_index("index").T.to_dict(into=dict)
    print(result_dict)

    # 輸出為 JSON 格式並打印
    # print(json.dumps(result_dict, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    test1()
