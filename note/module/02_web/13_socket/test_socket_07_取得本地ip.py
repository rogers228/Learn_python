import socket

def get_ipv4():
    try:
        # 獲取本機主機名
        hostname = socket.gethostname()
        # 獲取本機IP地址
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception as e:
        return f"無法獲取本機IPv4地址：{e}"

# 使用示例
ip = get_ipv4()
print(f"本機IPv4地址是：{ip}")