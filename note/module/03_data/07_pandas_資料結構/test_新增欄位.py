df.insert(1, "sort", alis, True) #插在最前

df.insert(len(df.columns), "sort", alis, True) #插在最後

df.insert(df.columns.tolist().index('pdf'), "inst", alis, True) #插在特定欄位之前


#插入內容為空白欄位
df.insert(len(df.columns), '檢查結果', ['']*len(df.index), True) #插在最後

#使用插入欄位
插入第幾位
欄位名稱
值  可為list
是否允許重複值


# 以欄位計算結果 增加欄位
df_all['hday'] = (df_all['ps23'] - df_all['SUM_sw06'])