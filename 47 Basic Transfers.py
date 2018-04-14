from PIL import Image
from PIL import ImageFilter


img = Image.open(r'PyhtonImages\img1.jpg')
black_white = img.convert("L")

blur = img.filter(ImageFilter.BLUR)
detail = img.filter(ImageFilter.DETAIL)
edges = img.filter(ImageFilter.FIND_EDGES)


black_white.show()
blur.show()
detail.show()
edges.show()


