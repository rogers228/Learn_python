# 同步資料夾及檔案
import dirsync

def main():
    source_path = r'C:\Users\user\Documents\GitHub\Learn_python\note\module\32_dirsync_檔案同步\dirsync01_test\sourcedir'
    target_path = r'C:\Users\user\Documents\Rogers\Temp\sync_test'

    args = {
        'purge': True,   # 同步清除
        'create' : True, # 資料夾不存在時則建立
        'ignore' : ['\.git', '\.gitignore', 'config.py', 'test.*'] # 忽略
    }
    dirsync.sync(source_path, target_path, 'sync', **args)
    print('finish')

if __name__ == '__main__':
    main()