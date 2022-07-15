# 加密
def enctry(s): 
    k = r'Gb@e1T,</bFa<!t&8c*r7#^4s1R55*-15Sghfh!@fE6(3.d4lF$d'
    encry_str = ""
    for i,j in zip(s,k): # i為字符，j為秘鑰字符
        temp = str(ord(i)+ord(j))+'_' # 加密字符 = 字符的Unicode碼 + 秘鑰的Unicode碼
        encry_str = encry_str + temp
    return encry_str

# 解密
def dectry(p):
    k = r'Gb@e1T,</bFa<!t&8c*r7#^4s1R55*-15Sghfh!@fE6(3.d4lF$d'
    dec_str = ""
    for i,j in zip(p.split("_")[:-1],k): # i 為加密字符，j為秘鑰字符
        temp = chr(int(i) - ord(j)) # 解密字符 = (加密Unicode碼字符 - 秘鑰字符的Unicode碼)的單字節字符
        dec_str = dec_str+temp
    return dec_str

mystr = '12ddf34R$'
print(mystr)

a=enctry(mystr)
print(a)

b=dectry(a)
print(b)

