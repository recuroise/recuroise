def encrypt(text, password):
    u = 4

    ciphertext = ''
    a = (password % 10000) * 0.0001 #通过密钥得到混沌系统的初值
    x = [a]
    for i in range(0, 500):
        x[0] = u * x[0] * (1 - x[0])  #迭代500次后达到混沌
    size = len(text)
    for i in range(1, size):
        x.append(u * x[i - 1] * (1 - x[i - 1])) #生成密码序列

    for i in range(0, size):
        x[i] = int(255 * x[i])  #将[0, 1]间的实数映射到[0, 255]间的整数
        ciphertext += chr(ord(text[i]) ^ x[i]) #通过异或得到加密后的密文
    return ciphertext


def decrypt(ciphertext, password):
    u = 4
    text = ''
    a, b = (password % 10000) * 0.0001, (password // 10000) * 0.0001
    x = [a]
    for i in range(0, 500):
        x[0] = u * x[0] * (1 - x[0])
    size = len(ciphertext)
    for i in range(1, size):
        x.append(u * x[i - 1] * (1 - x[i - 1]))

    for i in range(0, size):
        x[i] = int(255 * x[i])
        text += chr(ord(ciphertext[i]) ^ x[i])
    return text


password = int(input()) % 100000000
text = input()
ciphertext = encrypt(text, password)
text1 = decrypt(ciphertext, password)
print(ciphertext, text1)
