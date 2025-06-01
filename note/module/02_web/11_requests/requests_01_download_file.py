import os
import requests

def download_7z_file(url, save_path):
    # url: 下載網址
    # save_path: 儲存路徑
    # 下載成功回傳 True
    print(f"正在從 {url} 下載檔案...")
    response = requests.get(url, stream=True) # 適合檔案
    
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192): # 一次讀取 8KB
                if chunk:
                    f.write(chunk)
        print(f"下載完成，儲存於 {save_path}")
        return True
    else:
        print(f"下載失敗，狀態碼: {response.status_code}")
        return False

def test1():
    # print('test1')
    server = 'https://pythongreen.netlify.app/'
    file_name = 'python-3.12.9-embed-amd64_202504_1.7z'
    # file_name = 'index.html'
    url = f'{server}{file_name}'
    print(url)

    save2folder = os.path.dirname(__file__)
    save_path = os.path.join(save2folder, file_name)
    print(save_path)
    
    is_finished = download_7z_file(url, save_path)
    if is_finished:
        print(f"下載完成，儲存於 {save_path}")
    else:
        print(f"下載失敗")

if __name__ == '__main__':
    test1()