from collections import deque

'''
# 創建 deque
dq = deque(iterable, maxlen)
iterable  可選，任何可迭代對象（如列表、字串）
maxlen  可選，設定最大長度，超過時會自動移除舊元素
'''

def test1():
    dq = deque([1, 2, 3, 4])

    dq.pop() # 從右側移除元素
    print(dq)  # ➜ deque([1, 2, 3])

    # 從左側移除元素
    dq.popleft()
    print(dq)  # ➜ deque([2, 3])

def test2():
    dq = deque([1, 2, 3], maxlen=3)

    # 新增元素會自動移除舊元素
    dq.append(4)
    print(dq)  # ➜ deque([2, 3, 4])
    print(dq[0])

    dq.appendleft(0)
    print(dq)  # ➜ deque([0, 2, 3])  (右邊的 4 被移除)

if __name__ == '__main__':
    test2()