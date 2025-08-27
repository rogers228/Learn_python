from pyparsing import Word, alphas, alphanums, nums, Suppress, delimitedList, QuotedString, Combine, oneOf, Group
import pandas as pd
import json

def build_row_parser(schema):
    parsers = []

    float_number = Combine(Word(nums) + "." + Word(nums))
    bool_value = oneOf("true false yes no", caseless=True)
    alphanum_word = Word(alphanums)
    any_word = Word(alphanums + "_-.")

    for field, ftype in schema:
        if ftype == "str":
            p = Word(alphas)(field)
        elif ftype == "regex_pattern":
            p = Word(alphanums + "^$.*+?()[]{}|\\")(field)
        elif ftype == "alphanum":
            p = alphanum_word(field)
        elif ftype == "anystr":
            p = any_word(field)
        elif ftype == "int":
            p = Word(nums)(field)
        elif ftype == "float":
            p = float_number(field)
        elif ftype == "bool":
            p = bool_value(field)
        # 修正後的 list 規則
        elif ftype == "list":
            p = Group(Suppress("[") + delimitedList(Word(alphas), delim=',') + Suppress("]"))(field)
        # 修正後的 list_q 規則
        elif ftype == "list_q":
            p = Group(Suppress("[") + delimitedList(QuotedString("'") | Word(alphas), delim=',') + Suppress("]"))(field)
        elif ftype == "str_q":
            p = (QuotedString("'") | Word(alphas))(field)
        else:
            raise ValueError(f"未知型別: {ftype}")
        parsers.append(p)

    # 用空白符號拼接
    row = parsers[0]
    for p in parsers[1:]:
        row += p.suppress().leaveWhitespace() | p

    return row

def parse_lines(text, schema):
    row_parser = build_row_parser(schema)
    result = {}

    for line in text.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        tokens = row_parser.parseString(line)
        # 使用 tokens.asDict() 轉換為字典
        parsed_tokens = tokens.asDict()

        key = parsed_tokens.pop(schema[0][0])
        record = {}
        for field, ftype in schema[1:]:
            value = parsed_tokens[field]
            if ftype == "int":
                record[field] = int(value)
            elif ftype == "float":
                record[field] = float(value)
            elif ftype == "bool":
                record[field] = str(value).lower() in ["true","yes"]
            # 正確處理列表值，無需額外轉換
            elif ftype in ["list","list_q"]:
                record[field] = list(value)
            else:
                record[field] = value
        result[key] = record

    return result

def test1():
    # 原始資料
    lines = '''
        awwww allen 18  95.5 true  [joe,andy]    'Curry Rice'  ['singing','music']   ^.{18}(028|045).+  al_123
        byy   roger 20  88.0 false [jay]         Steak         ['movies','drinking'] ^.{18}(063|071).+  roger_01
        ccc   kate  25  72.5 yes   [amy,bob,tom] 'Salad Bowl' [reading, 'coding']   ^.{18}(085|100).+  kateX
    '''

    # 定義資料格式
    schema = [
        ("id", "str"),
        ("name", "str"),
        ("age", "int"),
        ("score", "float"),
        ("active", "bool"),
        ("friend", "list"),
        ("lunch", "str_q"),
        ("hobbies", "list_q"),
        ("pattern", "regex_pattern"),
        ("nickname", "anystr")
    ]

    dic = parse_lines(lines, schema)
    print(json.dumps(dic, indent=4, ensure_ascii=False))



    df = pd.DataFrame.from_dict(dic, orient='index')
    df.index.name = 'id'
    pd.set_option('display.max_rows', df.shape[0]+1) # 顯示最多列
    pd.set_option('display.max_columns', None) #顯示最多欄位
    print(df)

if __name__ == "__main__":
    test1()
