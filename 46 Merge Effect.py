from PIL import Image

img1 = Image.open(r"PyhtonImages\img1.jpg")
# img2 = Image.open(r"PyhtonImages\img2.jpg")
# img3 = Image.open(r"PyhtonImages\img3.jpg")
r, g, b = img1.split()
# r1, b1, g1 = img2.split()
# r2, b2, g2 = img3.split()
new_image = Image.merge("RGB", (b, g, r))
new_image.show()


#
# r.show()
# g.show()
# b.show()