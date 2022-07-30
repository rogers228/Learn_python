def func_print():
    print('this is func')

def user_func_with_string():
    # 以字串來操作函數
    dic = {'func_print': func_print}
    func = dic['func_print'] 
    func()

#--------------
dic_func = {'3': db.ger_ptd_kd, '5': db.ger_tad_kd}
df_w = df.loc[(df['品號'] != '') & (df['單別'] != '')] # 篩選
lis_data = []
for i, r in df_w.iterrows():
    func = dic_func[str(r['單別'])[:1]]
    print(func.__name__)
    cancel_no = func(r['單別'], r['單號'], r['品號'])  # 結案碼
    print(r['單別'], r['單號'], r['品號'], f'結案碼:{cancel_no}')