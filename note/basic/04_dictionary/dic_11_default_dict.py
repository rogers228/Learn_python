from collections import defaultdict

'''
d = defaultdict(default_factory)

default_factory 是一個可以被呼叫的函式，當查詢的鍵不存在時，會用這個函式的回傳值作為預設值。

'''

def test1():
    d = defaultdict(int) # 若鍵不存在，預設值為 0
    print(d['apple'])

    d = defaultdict(lambda: 'unknown') # 若鍵不存在，預設 unknown
    print(d['apple'])

def test2():
    text = "hello world"
    char_count = defaultdict(int) # 預設值為 0，適用於計數
    for char in text:
        char_count[char] += 1
        # char_count[char] 自動補上預設值 0

    # 使用普通 dict 效能較差
    # for char in text:
    #     if char in char_count:
    #         char_count[char] += 1  # 如果字母已存在，計數 +1
    #     else:
    #         char_count[char] = 1   # 如果字母不存在，初始化為 1

    # 輸出結果
    for char, count in char_count.items():
        print(f"字母 '{char}' 出現了 {count} 次")

if __name__ == '__main__':
    test2()