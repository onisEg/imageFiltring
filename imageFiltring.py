
from PIL import Image, ImageFilter
# open image
befor = Image.open("1.jpg")

# make blur on photo
after = befor.filter(ImageFilter.BoxBlur(5))
after.save("new1.png")
