from PIL import Image

img1 = Image.open(r"PyhtonImages\img1.jpg")
r, g, b= img1.split()


r.show()
g.show()
b.show()