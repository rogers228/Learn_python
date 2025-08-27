from deepmerge import Merger
import copy

# 合併規則：list 用 append，dict 用 merge，其他型別用 override
merger = Merger(
    [(list, ["append"]), (dict, ["merge"])], # (type, [strategy_name]) 列表
    ["override"], # 當沒有匹配 type 時使用的策略
    ["override"]  # 當 type 不是 list/dict 時的策略
)

dic_main = {
    'id': 'key',
    'name': 'pump',
    'other': {
        'model': [],
        'len': 0,
    },
    'intercourse':{
        'friends': []
    },
    'seals': ''
}

dic_a = {
    'id': 'key',
    'other': {
        'model': ['a', 'b'],
    }
}

dic_b = {
    'id': 'key',
    'intercourse':{
        'friends': ['allen', 'bill'],
    }
}

combined_data = copy.deepcopy(dic_main)

merger.merge(combined_data, dic_a)
merger.merge(combined_data, dic_b)

combined_data['other']['len'] = len(combined_data['other']['model'])

print(combined_data)
