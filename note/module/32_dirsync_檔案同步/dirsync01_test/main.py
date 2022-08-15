# 同步資料夾及檔案
import dirsync

def main():
    source_path = r'C:\Users\user\Documents\GitHub\Learn_python\note\module\32_dirsync_檔案同步\dirsync01_test\sourcedir'
    target_path = r'C:\Users\user\Documents\Rogers\Temp\sync_test'
    dirsync.sync(source_path, target_path, action='sync')
    print('finish')

if __name__ == '__main__':
    main()