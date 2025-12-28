from pathlib import Path # 不用安裝

def get_folder_list(target_path=".", ignore = []):
    # 獲取 target_path 底下的資料夾列表
    # target_path 目標路徑
    # ignore 忽略清單
    p = Path(target_path)
    return [f.name for f in p.iterdir() if f.is_dir() and f.name not in ignore]

def test1():
    target_path = r'C:\Users\USER\Documents\ispc_svelte\ssg\website'
    ignore = ['.git', 'node_modules', '.svelte-kit', '__pycache__']
    lis_folder = get_folder_list(target_path, ignore)
    print(lis_folder)

if __name__ == '__main__':
    test1()