import os
from livereload import Server, shell

server = Server()
def main():
    port=5500
    print(f'run local_server\npid:{os.getpid()}')
    print('exit: Ctrl + C')

    # 每當 'README.md' 改變，就執行 `make html` 再刷新畫面
    # server.watch('README.md', shell('make html'))

    # 當 temp_data.js 有變動，就執行 generate_index.py，重新產生 index.html
    # server.watch('temp_data.js', shell('python generate_index.py'))

    # 支援多命令
    # shell('python step1.py && python step2.py')

    server.watch('index.html') # 監測 index.html 檔案
    # server.watch('*.html')
    # server.watch('static/*.js')
    # server.watch('static/*.css')
    server.serve(root='.', port=port) # http://127.0.0.1:5500

    # ctrl + C 關閉

if __name__ == '__main__':
    main()