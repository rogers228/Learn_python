from cerberus import Validator

# 自定義驗證函式
def check_length_sum(field, value, error):
    """檢查字串長度是否大於 10。"""
    if len(value) <= 10:
        # 使用傳入的 error 函式來報告錯誤
        error(field, '字串長度總和必須大於 10')

def unique_list(field, value, error):
    if len(value) != len(set(value)):
        error(field, '列表項目重複: 確保列表中的每個元素都是唯一的。')

# 使用方法
schema = {
    'comment': {
        'type': 'string',
        # 【關鍵】使用 check_with 並傳入函式名稱
        'check_with': check_length_sum
    },
    'key_lis':{
        'type': 'list',
        'check_with': unique_list,
        'schema': {
            'type': 'string',
            'allowed': ['a', 'b', 'c', 'd']
        }
    },
}

data = {
    'comment': 'Too short yes',
    'key_lis': ['a', 'b', 'c', 'b']
}
v = Validator(schema)
if not v.validate(data):
    print("檢查失敗：", v.errors)
else:
    print("檢查通過")
    print(v.document) # 驗證通過後的數據（包含預設值）。
# v.validate({'comment': 'Too short'}) # 9個字
# print(v.errors)
# 輸出: {'comment': ['字串長度總和必須大於 10']}