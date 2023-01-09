from PIL import Image
img = Image.open('miku.png')
width, height = img.size
pim = img.load()
pim2 = img.copy().load()
for h in range(0, width):
    for w in range(0, height):
        i = (w + h) % width
        j = (w + 2 * h) % width
        pim[w, h] = pim2[i, j]
img.show()

pim2 = img.copy().load()
for h in range(0, width):
    for w in range(0, height):
        i = (2 * w - h) % width
        j = (- w + 1 * h) % width
        pim[w, h] = pim2[i, j]
img.show()
