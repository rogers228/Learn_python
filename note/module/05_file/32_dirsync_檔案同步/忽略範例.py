
import dirsync

def main():
    # print(config.get('develop_path'))
    # print(config.get('production_path'))
    args = {
        'purge': True,   # 同步清除
        'create' : True, # 資料夾不存在時則建立

        # dirsync的 ignore 是使用正則表達式
        # git 的 .gitignore 非正則表達式  不要混淆

        # 在windows平台下使用python  r'' 來避免轉義符\ 與windows路徑\的混亂
        # r'正則表達式'  使用r 可以讓正則表達式的轉義符 維持 原意 即正則

        # r'.'    任何字元
        # r'*'  # 任意次 0次或多次
        # r'?'  # 任意次 0次或1次
        # r'+'  # 任意次 1次獲多次

        # r'.*'   .代表任何字元  *代表0或多次
        # r'/'    資料夾路徑使用  左斜 /  來避免 \同時為正則轉義符 與windows路徑符 的問題
        # r'folder($|/|\\)' 資料夾使用結尾$ 或左斜(Linux環境) / 或右斜(\\) 更正確
        # r'.*/*' 代表任何資料夾 或 無資料夾 root
        # r'\'    正則表達式的轉義符 為右斜 \   使用 r 才會正確
        # r'\.'   代表.   \為正則表達式的轉義符

        'ignore' : [
            r'^\.git', r'^\.gitattributes', r'^\.gitignore', # 忽略 git 相關
            r'update_to_pdm\.py', r'sublime_hide\.py',   # 忽略特定檔案
            r'.*/*readme\.md',                           # 忽略任何資料夾中的 readme.md
            r'.*/01_ui2py\.bat', r'.*/02_dev\.bat', r'.*\.ui',  # 忽略任何資料夾中的 ui

            # system/
            r'system/database_structure\.md',

            # system/permissions
            r'system/permissions/encode_permissions\.py',
            r'system/permissions/easy_per\.py',

            # rphc
            r'rphc/form\.ico', r'rphc/readme\.md', r'rphc/run_pyqt_and_hide_cmd\.ahk',
        ] # 忽略
    }

    dirsync.sync(config.get('develop_path'), config.get('production_path'), 'sync', **args)
    print('update is finished')

if __name__ == '__main__':
    main()