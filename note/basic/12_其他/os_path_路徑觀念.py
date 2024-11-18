import os


def test1():
    path_work = os.getcwd() # 回傳工作目錄 的絕對位置
    #  會因為啟動位置不同而改變  雖然是絕對位置， (它會改變 所不是絕對)
    print('path_work:', path_work)

    file_path = os.path.dirname(__file__) # 回傳檔案所在位置 的絕對位置
    #  不會因為啟動位置不同而改變
    #  在不同的電腦環境 (使用git push pull) 也會改變
    print('file_path:', file_path)

    # 以上兩者都不是萬全的寫法
    # 真正好的寫法 要先考慮執行的電腦環境，可以使用電腦名稱

def test2():
    # 路徑引用的萬全方法 (可適用不同系統，不同電腦)
    if os.name == 'posix':
        # linux
        username = 'vqpcm2y2n0qr'
        pj_base = os.path.join('/home', username)

    else:
        # windows
        dic_base = {
            'VM-TESTER': r'C:\Users\user\Documents\Rogers',
        }
        computer = os.environ['COMPUTERNAME']
        pj_base = dic_base.get(computer, '') # 依電腦名稱尋找 project_base
        if pj_base == '':
            raise TypeError('project base is not found!')
        # print('pj_base:', pj_base)
        PROJECT = os.path.join(pj_base, 'project_name') # 依實際情況修改
        print('PROJECT:', PROJECT)







if __name__ == '__main__':
    test2()