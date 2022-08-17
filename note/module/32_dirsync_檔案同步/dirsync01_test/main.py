# 同步資料夾及檔案
import dirsync

def main():
    source_path = r'C:\Users\user\Documents\GitHub\Learn_python\note\module\32_dirsync_檔案同步\dirsync01_test\sourcedir'
    target_path = r'C:\Users\user\Documents\Rogers\Temp\sync_test'
    dirsync.sync(source_path, target_path, action='sync')

    # dirsync.sync(config_develop_program, config_servr_program, action='sync', purge = True)
    # purge = True 同步清除不存在的檔案
    print('finish')

if __name__ == '__main__':
    main()