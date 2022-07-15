import socket

def socket_server():
    # socket server
    HOST = '220.168.100.186' #server地址
    PORT = 8061
    # socket.AF_INET 網路通訊
    # socket.SOCK_STREAM TCP協定
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT)) #綁定
    server.listen(4) #監聽數量
    print(f'Socker server start at: {HOST}:{PORT}')
    print('wait for connection...')

    echo_time = 1
    while True: #等待連線
        conn, addr = server.accept() #成功回傳連接資訊
        print(f'Connected by {conn}, {addr}') #顯示連接資訊
        print(f'Connected by {addr}') #顯示連接資訊
        clientMessage = str(conn.recv(1024), encoding='utf-8')
        print(f'clientMessage:{clientMessage}')
        serverMessage = f'I\'m server here! {echo_time}'
        conn.sendall(serverMessage.encode()) #傳送回應
        conn.close() #回應後即關閉連線
        echo_time += 1
        
if __name__ == '__main__':
    socket_server() #執行
    print('ok')