import socket
# import tqdm
import os

def socket_file_server():
    # socket server
    SERVER_HOST  = '220.168.100.186' #server地址
    SERVER_PORT  = 8061

    # receive 4096 bytes each time
    BUFFER_SIZE = 4096
    SEPARATOR = "<SEPARATOR>"

    s = socket.socket()
    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen(5)
    print(f'[*] Listening as {SERVER_HOST}:{SERVER_PORT}')
    print('wait for connection...')

    while True: #等待連線
        client_socket, address = s.accept()
        print(f"[+] {address} is connected.")
        received = client_socket.recv(BUFFER_SIZE).decode()
        filename, filesize = received.split(SEPARATOR)
        filename = os.path.basename(filename) #檔案名稱
        filesize = int(filesize)              #檔案大小
        print(f'[+] File geting... {filename}')
        # progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(filename, "wb") as f:
            while True:
                # read 1024 bytes from the socket (receive)
                bytes_read = client_socket.recv(BUFFER_SIZE)
                if not bytes_read:
                    break
                f.write(bytes_read)
                # progress.update(len(bytes_read)) # update the progress bar
        client_socket.close()  # close the client socket
        print(f'[+] Finished')
        # s.close()              # close the server socket

if __name__ == '__main__':
    socket_file_server() #執行
    print('ok')