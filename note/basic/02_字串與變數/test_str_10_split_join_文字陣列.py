# 文字陣列 轉lis
# lis 合併為字串
data = 'PVS08-012__%__PVS10-012__%__PVS10-012-2__%__PVS12-012__%__PVS13-012__%__PVS08-013__%__PVS08-015-1__%__PVS08-015-2__%__PVS10-016-2__%__PVS13-016__%__PVS08-017__%__PVS08-018__%__PVS10-018__%__PVS08-021'
draws = data.split('__%__') # 分解為陣列
print(draws)

lis = ','.join(str(d) for d in draws) # 合併相加為字串
print(lis)


#效率比 + 高