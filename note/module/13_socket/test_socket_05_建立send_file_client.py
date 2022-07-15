import socket
# import tqdm
import os

def socket_file_client():
    SEPARATOR = "<SEPARATOR>"
    BUFFER_SIZE = 4096 # send 4096 bytes each time step
    HOST = '220.168.100.186' #vb6 server 
    PORT = 8061

    filename = r"U:\dsprog\py_excel\test\test.txt"
    filesize = os.path.getsize(filename)

    s = socket.socket()
    try:
        print(f"[+] Connecting to {HOST}:{PORT}")
        s.connect((HOST, PORT)) #連線
    except:
        print('無法建立連接!')
        return

    # print("[+] Connected.")
    print(f'[+] File sending... {filename}')
    s.send(f"{filename}{SEPARATOR}{filesize}".encode()) # send the filename and filesize
    # progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    
    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE) # read the bytes from the file
            if not bytes_read:
                break
            s.sendall(bytes_read)
    print(f'[+] Finished')
    s.close() # close the socket

if __name__ == '__main__':
    socket_file_client() #執行
    print('ok')