from PIL import Image

img = Image.open(r"PyhtonImages\img1.jpg")
print(img.size)
print(img.format)

img.show()
