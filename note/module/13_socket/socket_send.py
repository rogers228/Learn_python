import sys, socket

def socket_client_send(argv1, argv2):
    # argv1 傳送的String
    # argv2 通訊ip及接口 220.168.100.186:8061

    HOST = argv2.split(':')[0]
    PORT = int(argv2.split(':')[1])

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.connect((HOST, PORT)) #連線
    except:
        print('無法建立連接!')
        sys.exit()

    server.send(argv1.encode())
    server.close()

if __name__ == '__main__':
    # sys.argv[0] 是執行程式
    # print('sys.argv', sys.argv)
    if len(sys.argv) == 3:
        socket_client_send(sys.argv[1], sys.argv[2])
    else:
        print('無效的引數!')
        sys.exit()