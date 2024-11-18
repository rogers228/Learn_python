def test82():
    '''
    讀取系統變數，可將敏感資料儲存於系統變數,避免資安風險
    前置作業
    windows 系統內容>環境變數>新增系統變數
    '''
    result = os.environ.get('ROG_TEST') #讀取不到時返回None
    print(result)

    result = os.environ.get('ROG_TEST2', False ) #讀取不到時返回指定值
    print(result)
    
if __name__ == '__main__':
    test82()
    print('ok')