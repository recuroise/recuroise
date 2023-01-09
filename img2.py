from PIL import Image

def logistic(img, key):
    ux = uy =uz = u = 3.9 + 0.1 * (int(key[0:3]) / 1000.0)
    width, height = img.size
    a = int(key[3:6]) / 1000.0
    b = int(key[6:9]) / 1000.0
    c = int(key[9:12]) / 1000.0
    print(u, a)
    x, y, z = [a], [b], [c]
    size = width * height
    pim = img.load() #基本参数的获取与图像的读取


    def func(u, x):
        return u * x * (1 - x)

    for i in range(0, 5000):
        x[0] = func(ux, x[0])
        y[0] = func(uy, y[0])
        z[0] = func(uz, z[0])
    for i in range(1, size):
        x.append(func(ux, x[i - 1]))
        y.append(func(uy, y[i - 1]))
        z.append(func(uz, z[i - 1]))  #生成密码序列
    i = 0
    for w in range(0, width):
        for h in range(0, height):
            tmp = (int(255 * x[i]), int(255 * y[i]), int(255 * z[i])) 
            i += 1
            R, G, B = pim[w, h]
            R, G, B = R ^ tmp[0], G ^ tmp[1], B ^ tmp[2]
            pim[w, h] = (R, G, B)   #逐个像素进行加密，分别使用三个不同的加密序列
    return img

def encrypt(img, key):
    pim = img.load()
    pim2 = img.copy().load()
    for w in range(0, width):
        for h in range(0, height):
            i = (w + 7 * h) % width
            j = (w + 8 * h) % width
            pim[w, h] = pim2[i, j]          #Arnold置乱法 a=1 b=7
    img = logistic(img.copy(), key)         #先置乱，后加密
    return img

def decrypt(img, key):
    img = logistic(img.copy(), key)
    pim = img.load()
    pim2 = img.copy().load()
    for w in range(0, width):
        for h in range(0, height):
            i = (8 * w - 7 * h) % width
            j = (- w + 1 * h) % width
            pim[w, h] = pim2[i, j]      #先解密，后复位
    return img

img = Image.open('miku.png')
key1 = '999234542141'
key2 = '998234542141'
width, height = img.size
img_ency = encrypt(img.copy(), key1)
img_decy = decrypt(img_ency.copy(), key2)
img_ency.show()
img_decy.show()

