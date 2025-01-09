# push to godaddy webdisk

if True:
    import sys, os
    _p = os.path.dirname

    from glob import glob
    import shutil
    import hashlib

def calculate_md5(file_path):
    # 取得檔案的 hash_md5
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def is_file_modified(original_file, current_file):
    # 判斷檔案是否修改
    original_hash = calculate_md5(original_file)
    current_hash = calculate_md5(current_file)
    return original_hash != current_hash

def push_root_data():
    print('push...')
    source_path = _p(__file__)
    target_path = r'G:\public_html'
    # print(source_path)
    # print(target_path)

    # 欲更新的所有檔案
    files = glob(os.path.join(source_path, ".*")) + glob(os.path.join(source_path, "*.*"))
    # print(files)

    ignore = [
        'push_root_to_server.py',
        'readme.md',
    ]

    is_update = False
    for f in files:
        # print(f)
        # print(os.path.basename(f))
        if os.path.basename(f) not in ignore: # 未忽略
            # print(os.path.basename(f))
            target_file = os.path.join(target_path, os.path.basename(f)) # 目標檔案完整路徑
            if is_file_modified(f, target_file): # 已修改過  必須更新
                print(f'{os.path.basename(f)} is modified.')
                is_update = True
                # clear
                if os.path.exists(target_file):
                    os.remove(target_file)
                # copy2
                shutil.copy2(f, target_file)
                print(os.path.basename(f), 'updated.')

    if is_update:
        print('push root data is finish. ^_^')
    else:
        print('no file need to update.')

if __name__ == '__main__':
    push_root_data()