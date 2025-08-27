from pyparsing import Word, alphas, alphanums, nums, Suppress, delimitedList, QuotedString, Combine, oneOf, Group
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
        elif ftype == "list":
            p = Suppress("[") + delimitedList(Word(alphas), delim=',') + Suppress("]")(field)
        elif ftype == "list_q":
            p = Suppress("[") + delimitedList(QuotedString("'") | Word(alphas), delim=',') + Suppress("]")(field)
        elif ftype == "str_q":
            p = QuotedString("'") | Word(alphas)
            p = p(field)
        else:
            raise ValueError(f"未知型別: {ftype}")
        parsers.append(p)

    # 用空白拼接
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
        tokens = list(tokens)

        key = tokens[0]
        record = {}
        for i, (field, ftype) in enumerate(schema[1:], start=1):
            value = tokens[i]
            if ftype == "int":
                record[field] = int(value)
            elif ftype == "float":
                record[field] = float(value)
            elif ftype == "bool":
                record[field] = str(value).lower() in ["true","yes"]
            elif ftype in ["list","list_q"]:
                record[field] = value if isinstance(value, list) else [value]
            else:
                record[field] = value
        result[key] = record

    return result

# =========================
# 測試
# =========================
def test1():
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

    lines = '''
    awwww allen 18  95.5 true  [joe,andy]    'Curry Rice'  ['singing','music']   ^.{18}(028|045).+  al_123
    byy   roger 20  88.0 false [jay]          Steak        ['movies','drinking'] ^.{18}(063|071).+  roger_01
    ccc   kate  25  72.5 yes   [amy,bob,tom]  'Salad Bowl' ['reading', coding]  ^.{18}(085|100).+  kateX
'''

    result = parse_lines(lines, schema)
    print(json.dumps(result, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    test1()
