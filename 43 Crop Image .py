from PIL import Image

img = Image.open(r'PyhtonImages\img1.jpg')
area = (100, 100, 200, 300)
cropped_img = img.crop(area)

cropped_img.show()
