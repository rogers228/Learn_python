import io, sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #強制編碼
s_sort_gk = ['評估中','暫緩','執行中','暫停','完成轉採','完成']
print('暫緩 的index: {0}'.format(s_sort_gk.index('暫緩')))