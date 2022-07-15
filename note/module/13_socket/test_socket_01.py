import socket

def test2():
    # socket server
    HOST = '220.168.100.186' #server地址
    PORT = 8061    
    # socket.AF_INET 網路通訊
    # socket.SOCK_STREAM TCP協定
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT)) #綁定
    server.listen(4) #監聽數量
    print(f'server start at: {HOST}:{PORT}')
    print('wait for connection...')

    while True: #等待連線
        conn, addr = server.accept() #成功回傳連接資訊
        print(f'Connected by {conn}, {addr}') #顯示連接資訊
        while True:
            data = conn.recv(1024) #接收TCP連接的資料
            print('data:', data)
            conn.send("server received you message.")

def test1():
    #本機電腦名稱
    hostname = socket.gethostname()
    print('hostname:', hostname) #本機電腦名稱

    local_ip = socket.gethostbyname(hostname)
    print('local_ip:', local_ip)

if __name__ == '__main__':
    test1()
    print('ok')