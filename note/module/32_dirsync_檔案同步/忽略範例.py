
import dirsync

def main():
    # print(config.get('develop_path'))
    # print(config.get('production_path'))
    args = {
        'purge': True,   # 同步清除
        'create' : True, # 資料夾不存在時則建立

        # 在windows平台下 使用 r'' 來避免轉義
        # r'正則表達式'
        # r'.*'   .代表任何字元  *代表0或多次
        # r'/'    資料夾路徑使用  左斜 /
        # r'\'    正則表達式的轉義符 為右斜 \
        # r'.*/*' 代表任何資料夾 或 無資料夾 root
        # r'\.'   代表.   \為正則表達式的轉義符

        'ignore' : [
            r'.git', r'\.gitattributes', 'r\.gitignore', # 忽略 git 相關
            r'update_to_pdm\.py', r'sublime_hide\.py',   # 忽略特定檔案
            r'.*/*readme\.md',                           # 忽略任何資料夾中的 readme.md
            r'.*/01_ui2py\.bat', r'.*/02_dev\.bat', r'.*\.ui',
            # system
            r'system/user_permissions\.json5', r'system/encode_permissions\.py',
            # rphc
            r'rphc/form\.ico', r'rphc/readme\.md', r'rphc/run_pyqt_and_hide_cmd\.ahk',
        ] # 忽略
    }

    dirsync.sync(config.get('develop_path'), config.get('production_path'), 'sync', **args)
    print('update is finished')

if __name__ == '__main__':
    main()