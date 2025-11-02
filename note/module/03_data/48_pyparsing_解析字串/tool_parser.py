import re
import csv
from io import StringIO
import pandas as pd
import json

class LineParser:
    def __init__(self, lines, columns, text_fields = None):
        # text_fields 強制指定為 text 的欄位

        self.lines = lines
        self.columns = columns
        self.text_fields = text_fields if text_fields is not None else set()
        self.data = self._parse_lines()  # 初始化時就直接解析

        # 型別檢查
        is_error, details = self._is_error_types(self.data)
        if is_error:
            print(details)
            raise TypeError("欄位型別錯誤!")
        else:
            pass
            # print("✅ 型別檢查通過")

    def _parse_list(self, raw):
        """處理中括號包裹的 list，去除空白，並自動轉換"""
        if not (raw.startswith("[") and raw.endswith("]")):
            return raw

        content = raw[1:-1].strip()
        if not content:
            return []

        # 處理引號和空白
        items = [x.strip(" '\"") for x in content.split(",")]

        def auto_cast(val):
            """內部自動轉換，支援 int, float, str"""
            try:
                # 優先判斷是否為浮點數
                if "." in val and val.replace(".", "", 1).isdigit():
                    return float(val)
                # 接著判斷是否為整數
                if val.isdigit() or (val.startswith('-') and val[1:].isdigit()):
                    return int(val)
                return val # 預設回傳字串
            except ValueError:
                return val

        return [auto_cast(x) for x in items]

    def _auto_cast_value(self, key, value):
        """根據 key 嘗試自動轉換型別 (布林, 數字, 字串)"""

        # 如果欄位名稱在 text_fields 集合中，則直接回傳字串，不進行數字轉換
        if key in self.text_fields:
            return value

        # 1. 處理布林值
        if value.lower() in {"true", "yes", "1"}:
            return True
        if value.lower() in {"false", "no", "0"}:
            return False

        # 2. 處理數字
        try:
            if "." in value:
                return float(value)
            return int(value)
        except ValueError:
            # 3. 預設回傳字串
            return value

    def _is_error_types(self, data, check_all=True):
        """檢查 list[dict] 每個欄位的型別 (內部方法)"""
        field_types = {}
        # 僅檢查第一筆資料以判斷型別，除非 check_all=True
        rows = data if check_all else data[:1]

        for record in rows:
            for key, value in record.items():
                field_types.setdefault(key, set()).add(type(value).__name__)

        # 判斷是否有欄位包含超過一種型別
        is_error = any(len(types) > 1 for types in field_types.values())
        details = {
            field: {"types": sorted(list(types)), "is_error": len(types) > 1}
            for field, types in field_types.items()
        }

        details_format = "⚠️ 欄位型別不一致檢查結果：\n"
        for field, info in details.items():
            types = ", ".join(info["types"])
            flag = "⚠️" if info["is_error"] else "✅"
            details_format += f"{flag} {field:<10} → {types}\n"

        return is_error, details_format

    def _preprocess_line(self, line):
        """將 line 中的 [list] 預先處理，去掉內部空白 (內部方法)"""
        # 找到所有 [list] 結構
        def replacer(match):
            # 對匹配到的 [list] 內容，去掉內部所有空白
            # 這樣 csv.reader 就不會誤判 list 內部的元素間隔
            return re.sub(r"\s+", "", match.group(0))

        # 應用替換，只針對中括號內容進行
        return re.sub(r"\[.*?\]", replacer, line)

    def _parse_lines(self):
        """解析多行文字，根據 schema 輸出 dict 列表 (內部方法)"""
        data = []
        for raw in self.lines.strip().split("\n"):
            # 1. 預先處理 list 內容，防止 csv.reader 錯誤分割
            line = self._preprocess_line(raw)

            # 2. 使用 csv.reader 解析，以空格為分隔符，並處理單引號
            reader = csv.reader(
                StringIO(line),
                delimiter=" ",
                skipinitialspace=True, # 忽略多餘空白
                quotechar="'"          # 處理 '單引號字串'
            )
            try:
                row = next(reader)
            except StopIteration:
                # 處理空行
                continue

            record = {}
            # 3. 根據欄位名稱和值進行自動轉換
            for key, value in zip(self.columns, row):
                if value.startswith("[") and value.endswith("]"):
                    # 這是 list 欄位，呼叫專門的 list 解析器
                    record[key] = self._parse_list(value)
                else:
                    # 這是普通欄位，呼叫自動轉換器
                    record[key] = self._auto_cast_value(key, value)
            data.append(record)
        return data

    def to_dict(self):
        """回傳 list of dict"""
        return self.data

    def to_dataframe(self, index=None):
        """轉換成 DataFrame"""
        df = pd.DataFrame(self.data)
        if index and index in df.columns:
            df.set_index(index, inplace=True)
        return df

    def to_json(self, **kwargs):
        """轉換成 JSON"""
        # 確保中文不會變成 \uXXXX
        return json.dumps(self.data, indent=4, ensure_ascii=False, **kwargs)

def test1():
    # 測試

    # columns = [
    #     "id", "name", "age", "score", "active", "friends", "food", "hobbies", "regex", "username" ]
    # lines = '''
    #     awwww allen   18    95.5      true  [joe,andy]                'Curry Rice' ['singing','music']      ^.{18}(028|045).+  al_123
    #     byy   roger   20    88.0      false [jay]                      Steak       ['movies','drinking']    ^.{18}(063|071).+  roger_01
    #     ccc   andy    25    72.5      yes   [amy,bob, tom, 100, 88.5] 'Salad Bowl' [reading, 'coding']      ^.{18}(085|100).+  kateX
    # '''
    # data = LineParser(lines, columns)


    columns = [
        "model", "item", "alias"]
    lines = '''
        03dp   010   10
    '''
    data = LineParser(lines, columns, text_fields=("item", "alias")) # 強制數字轉文字

    print("\n📌 DICT 格式：")
    print(data.to_dict())

    print("\n📌 JSON 格式：")
    print(data.to_json())

    print("\n📌 DataFrame：")
    df = data.to_dataframe(index="id")
    print(df)

if __name__ == "__main__":
    test1()