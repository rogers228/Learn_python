dataframe_to_recoeds(list fo jinja2)


print(df)

'''
   wk01   wk02                    wk03   wk04  wk05
0     1   液壓機械    Hydraulic Mechanical   液壓机械    10
1     2    液壓站              Power unit    液壓箱    20
2     7  工具機選配  Machine tool equipment  工具机選配    25
3     3   油壓泵浦          Hydraulic Pump     泵浦    30
4     6   油壓馬達         Reversible pump   油壓馬達    32
5     5   泵浦零件              Pump Parts   泵浦零件    35
6     4   液壓閥類         Hydraulic Valve   液壓閥類    40
7     9   液壓配件    Hydraulic Components   液壓配件    45
8     8   工程機械       Construction pump   工程机械   100
'''


lis = df.to_dict('records')
print(lis)

'''
[{'wk01': 1, 'wk02': '液壓機械', 'wk03': 'Hydraulic Mechanical', 'wk04': '液壓机械', 'wk05': 10}, {'wk01': 2, 'wk02': '液壓站', 'wk03': 'Power unit', 'wk04': '液壓箱', 'wk05': 20}, {'wk01': 7, 'wk02': '工具機選配', 'wk03': 'Machine tool equipment', 'wk04': '工具机選配', 'wk05': 25}, {'wk01': 3, 'wk02': '油壓泵浦', 'wk03': 'Hydraulic Pump', 'wk04': '泵浦', 'wk05': 30}, {'wk01': 6, 'wk02': '油壓馬達', 'wk03': 'Reversible pump', 'wk04': '油壓馬達', 'wk05': 32}, {'wk01': 5, 'wk02': '泵浦零件', 'wk03': 'Pump Parts', 'wk04': '泵浦零件', 'wk05': 35}, {'wk01': 4, 'wk02': '液壓閥類', 'wk03': 'Hydraulic Valve', 'wk04': '液壓閥類', 'wk05': 40}, {'wk01': 9, 'wk02': '液壓配件', 'wk03': 'Hydraulic Components', 'wk04': '液壓配件', 'wk05': 45}, {'wk01': 8, 'wk02': '工程機械', 'wk03': 'Construction pump', 'wk04': '工程机械', 'wk05': 100}]

''''