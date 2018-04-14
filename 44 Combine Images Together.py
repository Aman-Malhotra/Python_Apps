from PIL import Image

img_1 = Image.open(r"PyhtonImages\img1.jpg")
img_2 = Image.open(r"PyhtonImages\img3.jpg")


area= (0, 0, 296, 300)

img_2.paste(img_1, area)
img_2.show()


# (296, 300)