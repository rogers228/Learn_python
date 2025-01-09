import socket

def socket_client():
    HOST = '220.168.100.186' #server
    # HOST = '220.168.100.195' #vb6 server 
    PORT = 8061
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.connect((HOST, PORT)) #連線
    except:
        print('無法建立連接!')
        return

    # outdata = f"hello I\'m python client."
    outdata = """
                123456789
                5001
                4905
                測試中文
                </>
                """
    print(f'send: {outdata}')
    server.send(outdata.encode())
    serverMessage = str(server.recv(1024), encoding='utf-8')
    print(f'serverMessage: {serverMessage}')
    server.close()

if __name__ == '__main__':
    socket_client() #執行
    print('ok')