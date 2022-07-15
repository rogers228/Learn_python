import socket

def get_read_ip(url):
    if 'http://' in url:
        name = url.replace('http://', '')
    else:
        name = url.replace('https://', '')

    try:
        info = socket.getaddrinfo(name, 80, 0, 0, socket.SOL_TCP)
        return info[0][4][0]
    except socket.gaierror as err:
        print(err)

if __name__ == '__main__':
    print(get_read_ip('yshr.asuscomm.com'))