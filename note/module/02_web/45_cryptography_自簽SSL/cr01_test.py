import datetime
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes

def generate():
    # 生成 RSA 密钥对
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
        )
    # print(key)

    # 创建 X.509 证书主体
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, u"TW"), # 國家
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"Taichung"), # 洲或省
        x509.NameAttribute(NameOID.LOCALITY_NAME, u"Wufeng"), # 地名
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Yeoshe"), # 機構名稱
        x509.NameAttribute(NameOID.COMMON_NAME, u"Yeoshe"),    # 通用名稱
    ])
    # print(subject)

    # 创建 X.509 证书
    cert = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        issuer
    ).public_key(
        key.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.datetime.utcnow() # 生效日期
    ).not_valid_after(
        datetime.datetime.utcnow() + datetime.timedelta(days=10950) # 到期日期
    ).add_extension(
        x509.SubjectAlternativeName([x509.DNSName(u"localhost")]),
        critical=False
    ).sign(key, hashes.SHA256(), default_backend())
    # print(cert)

    # 将证书和私钥序列化为 PEM 格式
    cert_pem = cert.public_bytes(encoding=serialization.Encoding.PEM)
    key_pem = key.private_bytes(encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption())
    # print(cert_pem)
    # print(key_pem)

    # 将证书和私钥写入文件
    with open("certificate.pem", "wb") as cert_file:
        cert_file.write(cert_pem)

    with open("key.pem", "wb") as key_file:
        key_file.write(key_pem)

    print('ok')

if __name__ == '__main__':
    generate()