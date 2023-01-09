from PIL import Image


def encrypt(img, key):
    u = 4
    width, height = img.size
    a = key
    x = [a]
    size = width * height
    pim = img.load()   #基本参数的获取与图像的读取

    for i in range(0, 500):
        x[0] = u * x[0] * (1 - x[0]) #迭代
    for i in range(1, size * 3 + 1):
        x.append(u * x[i - 1] * (1 - x[i - 1])) #生成密码序列
    
    i = 0
    for w in range(0, width):
        for h in range(0, height):
            tmp = (int(255 * x[i]), int(255 * x[i + 1]), int(255 * x[i + 2]))
            R, G, B = pim[w, h]
            R, G, B = R ^ tmp[0], G ^ tmp[1], B ^ tmp[2]
            pim[w, h] = (R, G, B)   #逐个像素进行加密，每个像素使用密码序列中的三位
            i += 3
    return img

def decrypt(img, key):
    u = 4
    width, height = img.size
    a = key
    x = [a]
    size = width * height
    pim = img.load()
    for i in range(0, 500):
        x[0] = u * x[0] * (1 - x[0])
    for i in range(1, size * 3 + 1):
        x.append(u * x[i - 1] * (1 - x[i - 1]))
    i = 0
    for w in range(0, width):
        for h in range(0, height):
            tmp = (int(255 * x[i]), int(255 * x[i + 1]), int(255 * x[i + 2]))
            R, G, B = pim[w, h]
            R, G, B = R ^ tmp[0], G^tmp[1], B^tmp[2]
            pim[w, h] = (R, G, B)
            i += 3
    return img

img = Image.open('plant.png')
width, height = img.size
pixel_value = img.getpixel((width // 2, height // 2))
key = 0.123
img_ency = encrypt(img, key)
img_decy = decrypt(img_ency.copy(), key)
img_ency.show()
img_decy.show()

