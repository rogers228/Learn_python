import py7zr

def test1():
    # 建立壓縮檔 保留資料夾架構

    print('建立壓縮檔...')
    file_7z = r'python-embed-environment.7z' # 建立壓縮檔的名稱
    source_folder = 'python-3.12.9-embed-amd64_202503_1' # 壓縮來源資料夾
    target_folder = 'python-3.12.9-embed-amd64_202503_1' # 建立壓縮檔後的資料夾名稱

    if os.path.exists(file_7z):
        print(f"{file_7z} 已存在! 建立失敗")
    else:
        with py7zr.SevenZipFile(file_7z, mode='w') as archive:
            archive.writeall(source_folder, arcname=target_folder)
        print('完成')

def test2(): # 列出檔案內容
    file_7z = r'C:\Users\USER\Documents\cpgn\python-3.12.9-embed-amd64_202503_1.7z'
    print(file_7z)
    with py7zr.SevenZipFile(file_7z, mode='r') as archive:
        file_list = archive.getnames()
        print(file_list)

def test3():
    # 解壓縮到指定資料夾
    with py7zr.SevenZipFile('example.7z', mode='r') as archive:
        archive.extractall(path='output_directory')
        
        
if __name__ == '__main__':
    test1()