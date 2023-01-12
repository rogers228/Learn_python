# 同步資料夾及檔案
import dirsync

def main():
    source_path = r'C:\Users\USER\Documents\learn-front-end\test_code\20230121_react\11_template'
    target_path = r'C:\Users\USER\Documents\learn-front-end\test_code\20230121_react\46_web\template'

    args = {
        'purge': True,   # 同步清除
        'create' : True, # 資料夾不存在時則建立
        'ignore' : ['\.git', '\.gitignore', 'config.py', 'test.*'] # 忽略
    }
    dirsync.sync(source_path, target_path, 'sync', **args)
    print('sync template is finish')

if __name__ == '__main__':
    main()