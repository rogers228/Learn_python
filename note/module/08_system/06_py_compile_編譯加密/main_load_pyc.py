import sys
import importlib.util

if True: #  import pyc
    pyc_path = '__pycache__/secure.cpython-37.pyc' # 指定 .pyc 檔案路徑
    spec = importlib.util.spec_from_file_location("secure", pyc_path)
    secure = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(secure)

def main():
    print(secure.config.get('name'))
    print(secure.secret_function(3, 5))

if __name__ == '__main__':
    main()