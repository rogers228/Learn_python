from unittest import TestCase

# 創建一個單例，用於調用比較方法
comparator = TestCase('__init__')

def compare_nested_dicts(dict_a, dict_b):
    """
    比較兩個巢狀字典的內容是否相同，忽略 key 順序。
    """
    try:
        # assertDictEqual 會進行遞迴比較：
        # 1. 檢查所有鍵值對是否都相同。
        # 2. 如果值本身是字典，它會遞迴呼叫比較。
        # 3. 如果值是列表，它會檢查列表內容是否相同 (但列表內部元素順序會被檢查)。
        comparator.assertDictEqual(dict_a, dict_b)
        return True
    except AssertionError:
        # 如果內容不匹配，assertDictEqual 會拋出 AssertionError
        return False

def test1():
    dict1 = {
        "id": 1001,
        "user": "Alice",
        "details": {
            "score": 95,
            "active": True
        }
    }

    # 巢狀字典的鍵順序不同
    dict2 = {
        "details": {
            "active": True,  # 內部順序也不同
            "score": 95
        },
        "user": "Alice",
        "id": 1001
    }
    # 內容相同，只是順序不同
    is_same = compare_nested_dicts(dict1, dict2)
    print(f"dict1, dict2 is_same: {is_same}")


    # 內容不同
    dict3 = {
        "id": 1001,
        "user": "Alice",
        "details": {
            "score": 95,
            "active": False # 值不同
        }
    }
    is_same = compare_nested_dicts(dict1, dict3)
    print(f"dict1, dict3 is_same: {is_same}")

if __name__ == '__main__':
    test1()