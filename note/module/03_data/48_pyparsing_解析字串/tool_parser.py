import re
import csv
from io import StringIO
import pandas as pd
import json

class LineParser:
    def __init__(self, lines, columns):
        self.lines = lines
        self.columns = columns
        self.data = self.parse_lines()  # 初始化時就直接解析

        # 型別檢查
        is_error, details = self.is_error_types(self.data)
        if is_error:
            print(details)
            raise TypeError("欄位型別錯誤!")
        else:
            pass
            # print("✅ 型別檢查通過")

    @staticmethod
    def parse_list(raw):
        """處理中括號包裹的 list，去除空白，並自動轉換"""
        if not (raw.startswith("[") and raw.endswith("]")):
            return raw

        content = raw[1:-1].strip()
        if not content:
            return []

        items = [x.strip(" '\"") for x in content.split(",")]

        def auto_cast(val):
            try:
                if "." in val:
                    return float(val)
                return int(val)
            except ValueError:
                return val

        return [auto_cast(x) for x in items]

    @staticmethod
    def auto_cast_value(key, value):
        """根據 key 嘗試自動轉換型別"""
        if value.lower() in {"true", "yes", "1"}:
            return True
        if value.lower() in {"false", "no", "0"}:
            return False
        try:
            if "." in value:
                return float(value)
            return int(value)
        except ValueError:
            return value

    @staticmethod
    def is_error_types(data, check_all=True):
        """檢查 list[dict] 每個欄位的型別"""
        field_types = {}
        rows = data if check_all else data[:1]

        for record in rows:
            for key, value in record.items():
                field_types.setdefault(key, set()).add(type(value).__name__)

        is_error = any(len(types) > 1 for types in field_types.values())
        details = {
            field: {"types": sorted(list(types)), "is_error": len(types) > 1}
            for field, types in field_types.items()
        }

        details_format = ""
        for field, info in details.items():
            types = ", ".join(info["types"])
            flag = "⚠️" if info["is_error"] else "✅"
            details_format += f"{flag} {field:<10} → {types}\n"

        return is_error, details_format

    @staticmethod
    def preprocess_line(line):
        """將 line 中的 [list] 預先處理，去掉內部空白"""
        def replacer(match):
            return re.sub(r"\s+", "", match.group(0))
        return re.sub(r"\[.*?\]", replacer, line)

    def parse_lines(self):
        """解析多行文字，根據 schema 輸出 dict 列表"""
        data = []
        for raw in self.lines.strip().split("\n"):
            line = self.preprocess_line(raw)
            reader = csv.reader(
                StringIO(line),
                delimiter=" ",
                skipinitialspace=True, # 忽略多餘空白
                quotechar="'"          # 處理 '單引號字串'
            )
            row = next(reader)

            record = {}
            for key, value in zip(self.columns, row):
                if value.startswith("[") and value.endswith("]"):
                    record[key] = self.parse_list(value)
                else:
                    record[key] = self.auto_cast_value(key, value)
            data.append(record)
        return data

    def to_dicts(self):
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
        return json.dumps(self.data, indent=4, ensure_ascii=False, **kwargs)

def test1():
    # 測試
    columns = [
        "id", "name", "age", "score", "active", "friends", "food", "hobbies", "regex", "username" ]
    lines = '''
        awwww allen   18    95.5      true  [joe,andy]                'Curry Rice' ['singing','music']      ^.{18}(028|045).+  al_123
        byy   roger   20    88.0      false [jay]                      Steak       ['movies','drinking']    ^.{18}(063|071).+  roger_01
        ccc   andy    25    72.5      yes   [amy,bob, tom, 100, 88.5] 'Salad Bowl' [reading, 'coding']      ^.{18}(085|100).+  kateX
    '''
    parser = LineParser(lines, columns)

    print("\n📌 JSON 格式：")
    print(parser.to_json())

    print("\n📌 DataFrame：")
    df = parser.to_dataframe(index="id")
    print(df)

if __name__ == "__main__":
    test1()