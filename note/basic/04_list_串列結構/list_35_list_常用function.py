import itertools

def list_duplicates(seq): # 回傳 重複的list
    seen = set()
    seen_add = seen.add
    seen_twice = set( x for x in seq if x in seen or seen_add(x) )
    return list( seen_twice )

def list_only(seq): # 回傳 不重複的list
    return sorted(set(seq), key = seq.index)

def list_remove_b(lis): # 移除空白 及 None
    return list(filter(None, lis))

def list_fgm(lis): #將list中元素展平
    # ['70', '140,210', '250'] -> ['70', '140', '210', '250']
    if lis is None:
        return
    t = ''
    for e in lis:
        t += '{0},'.format(e) # 合併
    t = t.rstrip(',') #去除字尾
    lis_a = t.split(',') #分解
    lis_b = [e.strip().upper() for e in lis_a] # 去除空白 轉大寫
    return lis_b

def list_stack(lis): #堆疊
    # [['CTR'], ['PVS'], ['A'], ['70', '140', '210', '250']]
    # return
    # ['CTR-PVS-A-70', 'CTR-PVS-A-140', 'CTR-PVS-A-210', 'CTR-PVS-A-250']
    if lis is None:
        return    
    return ["-".join(t) for t in itertools.product(*lis)]

def list_duplicates_id(lis): # 回傳 重複的 index
    lis_dup = list_duplicates(lis)
    lis_a = []
    for index, e in enumerate(lis):
        if e in lis_dup:
            lis_a.append(index)
    return lis_a

def list_index_all(lis, element): # 回傳元素的所有index
    lis_a = []
    for index, e in enumerate(lis):
        if e  == element:
            lis_a.append(index)
    return lis_a

def list_reversed(lis): # 回傳 反序的list
    return list(reversed(lis))
