#剔除空白行
# lis_b = [] 
# for e in lis_a:
#     if e.strip(): #非空白
#         lis_b.append(e.strip())



同上
lis_b =[e.strip() for e in lis_a if e.strip()]