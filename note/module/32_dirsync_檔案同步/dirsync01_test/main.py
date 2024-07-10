# 同步資料夾及檔案
import dirsync

def main():
    source_path = r'C:\Users\USER\Documents\learn-front-end\test_code\20230121_react\11_template'
    target_path = r'C:\Users\USER\Documents\learn-front-end\test_code\20230121_react\46_web\template'

    args = {
        'purge': True,   # 同步清除
        'create' : True, # 資料夾不存在時則建立
        'ignore' : ['\.git', '\.gitignore', 'readme.md', 'push_to_webserver.py', r'.*\.log', '__pycache__'] # 忽略
        # \. 代表 .
        # \* 代表 *
        # \\ 代表 \
        # __pycache__ 代表 資料夾__pycache__
    }

    dirsync.sync(source_path, target_path, 'sync', **args)
    print('sync template is finish')

if __name__ == '__main__':
    main()