def test1():
    # filter 迭代取出 為True者 為新的list
    lis = [1,2,2,2,3]
    lis2 = list(filter(lambda e: e != 2,lis))
    print(lis2)




def test2():
    dic = {'rd02': 1, 'rd06': 0.78, 'rd10':2, 'rd21': 4}
    # print(dic)
    dic_rd = {
    'rd06': '出', # 實際出勤(天)
    'rd07': '缺', # 實際缺勤(天)
    'rd08': '遲', # 核定遲到(分鐘)
    'rd10': '加', # 加班分段
    'rd14': '公休', # 公休天數
    'rd15': '周休', # 周休天數
    'rd16': '國定假日', # 國定假日天數
    'rd17': '無薪公休', # 無薪公休天數
    'rd18': '不計天數', # 不計天數
    'rd21': '特休', # 特休假天數
    'rd22': '公假', # 公假天數
    'rd23': '婚假', # 婚假天數
    'rd24': '喪假', # 喪假天數
    'rd25': '產假', # 產假天數
    'rd26': '病假', # 病假天數
    'rd27': '事假', # 事假天數
    'rd28': '陪產假', # 陪產假天數
    'rd29': '產檢假', # 產檢假天數
    'rd30': '育嬰假', # 育嬰假天數
    'rd31': '留職停薪', # 留職停薪天數
    'rd33': '補刷卡次數', # 補刷卡次數
    'rd34': '防疫照顧假', # 防疫照顧假
    'rd35': '疫苗接種假' # 疫苗接種假
    }
    # print(dic_rd)
    lis = list(filter(lambda e: e in list(dic_rd.keys()), list(dic.keys()))) # a list in b list
    t = ' '.join([f'{dic_rd[e]}{dic[e]}' for e in lis])
    print(t)

def test3():
    dic = {'rd02': 100, 
            'rd03': '20220728000000', 
            'rd04': 1, 
            'rd06': 0.0, 
            'rd07': 0.0, 
            'rd08': 0.0, 
            'rd10': '', 
            'rd11': '', 
            'rd12': '特休假:07280800~07291730', 
            'rd14': 0.0, 
            'rd15': 0.0, 
            'rd16': 0.0, 
            'rd17': 0.0, 
            'rd18': 0.0, 
            'rd19': 0.0, 
            'rd21': 1.0, 
            'rd22': 0.0, 
            'rd23': 0.0, 
            'rd24': 0.0, 
            'rd25': 0.0, 
            'rd26': 0.0, 
            'rd27': 0.0, 
            'rd28': 0.0, 
            'rd29': 0.0, 
            'rd30': 0.0, 
            'rd31': 0.0, 
            'rd33': 0, 
            'rd34': 0.0, 
            'rd35': 0.0}
    print(dic)
    lis_key = list(filter(lambda e: all([dic[e]!= 0, dic[e]!='']) ,list(dic.keys()))) # 篩選出不為0 不為''的key
    print(lis_key)
    lis_value = [dic[e] for e in lis_key]
    print(lis_value)
    dic2 = dict(zip(lis_key, lis_value))
    print(dic2)


if __name__ == '__main__':
    test3()