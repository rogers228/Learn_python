from cerberus import Validator

def test1():
    # 定義驗證規則
    # type 類型     : string, integer, float, boolean, list, dict
    # required 必填 : True, False
    # default 預設值 : 補充預設值  {'default': 'unknown'}
    # min 最小/ max 最大: 用於數字驗證
    # minlength 最小長度/ maxlength 最大長度: 用於文字驗證
    # regex 正則驗證
    # allowed 指定允許值
    # schema 用於巢狀規則

    # 除以上驗證方式，可以自訂驗證規則

    schema = {
        'name': {'type': 'string', 'required': True}, # required 必填
        'age': {'type': 'integer', 'min': 0, 'required': True},  # integer數字 可以使用 min, max
        'email': {'type': 'string', 'regex': r'^\S+@\S+\.\S+$'}, # string文字 可以使用 regex 正則驗證
        'move': {'type': 'string', 'required': True, 'default': ''},
        'key_lis':{
            'type': 'list',  # 必須是列表
            'schema': { # 巢狀內容的規則
                'type': 'string',
                'allowed': ['a', 'b', 'c']  # 限定內容必須在 ['a', 'b', 'c'] 內
            }
        },
        'dic' :{'type': 'dict', 'required': True}
    }

    # 待檢查的字典
    data = {
        'name': 'John',
        'age': 30,
        'key_lis': ['a', 'b', 'c'],
        'dic': {
            'key_a': 'value'
        }
    }

    v = Validator(schema)
    if not v.validate(data):
        print("檢查失敗：", v.errors)
    else:
        print("檢查通過")
        print(v.document) # 驗證通過後的數據（包含預設值）。

if __name__ == '__main__':
    test1()