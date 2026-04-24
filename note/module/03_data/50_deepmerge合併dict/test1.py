from deepmerge import Merger, StrategyRequest
import copy

# Strategy策略 list

# 1. 策略如下
# dict
# merge         遞迴合併字典內部的 Key-Value。
# use_existing  保留舊字典，忽略新字典。
# override      覆蓋

# lsit
# append          將新列表元素加在舊列表後方。
# prepend         將新列表元素加在舊列表前方。
# append_unique   只加入舊列表中不存在的元素（去除重複）

# 通用 type
# override        後者覆蓋前者（最常用）。
# use_existing    保留前者，捨棄後者


# 2.Strategy策略 list 裡面可以多個，失敗將嘗試下一個
# 3.Strategy策略 可以是自訂函數

def test1():
    merger = Merger(
        # 類型策略列表 由元組組成的列表 [(Type, ["Strategy"]), ...]
        type_strategies = [(list, ["append"]), (dict, ["merge"])], # 預到 list 使用append, 預到dict使用 merge
        fallback_strategies = ["override"],      # 當遇到type未定義在 type_strategies 時使用的策略
        type_conflict_strategies = ["override"]  # 當遇到型別不同時，直接覆蓋
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

def test2():

    # 策略是自訂函數
    def merge_if_same_len(config, path, base, nxt):
        if len(base) == len(nxt):
            return base + nxt
        # 如果條件不符，拋出此異常，Merger 會自動跳到下一個策略
        raise StrategyRequest.NAME_NOT_FOUND

    merger = Merger(
        [(list, [merge_if_same_len, "override"])], # 先試自定義，失敗就 override
        ["override"],
        ["override"]
    )

def test2():

    # 1. 自定義策略函數  固定4個參數
    # config  環境變數    指向目前的 Merger 實例。你可以透過它取得合併時的配置，或是呼叫 config.value_strategy 來手動觸發其他型別的合併邏輯。
    # path    地圖導航    一個 List，記錄從根節點到目前位置的所有 Key。它是你撰寫「條件式合併」最重要的依據。
    # base    舊資料 (左方)    目前存在於目標物件（你正在修改的那個 dict）中的值。
    # nxt    新資料 (右方)    準備要合併進去的值（來自 merger.merge(base, nxt) 的第二個參數）。

    def smart_strategy(config, path, base, nxt):
        # 根據 path 判定邏輯
        if path and path[-1] == "admin_users":
            print(f"-> 偵測到關鍵路徑 {path}，執行去重合併")
            return list(set(base + nxt))

        if path and path[-1] == "priority":
            print(f"-> 偵測到優先級 {path}，保留較大值")
            return max(base, nxt)

        # 告訴 Merger：這個我不處理，請交給策略鏈中的下一個（例如內建的 append 或 override）
        raise StrategyRequest.NAME_NOT_FOUND

    # 2. 初始化 Merger
    # 針對 list：先跑 smart_strategy，不行再跑 append
    # 針對 int：先跑 smart_strategy，不行再跑 override
    merger = Merger(
        [
            (list, [smart_strategy, "append"]),
            (int, [smart_strategy, "override"])
        ],
        ["override"], # fallback
        ["override"]  # type conflict
    )

    # 3. 準備資料
    default_config = {
        "server_name": "Generic_Server",
        "priority": 10,
        "settings": {
            "admin_users": ["alice", "bob"],
            "tags": ["production"]
        }
    }

    custom_config = {
        "priority": 50,  # 觸發 smart_strategy (保留大值)
        "settings": {
            "admin_users": ["alice", "charlie"], # 觸發 smart_strategy (去重)
            "tags": ["east-asia"] # 觸發內建 append
        }
    }

    # 4. 執行合併
    # 使用 deepcopy 確保原始資料不被污染
    final_config = copy.deepcopy(default_config)
    merger.merge(final_config, custom_config)

    # 5. 印出結果
    import json
    print("\n--- 合併後的最終設定 ---")
    print(json.dumps(final_config, indent=4))

if __name__ == '__main__':
    test1()