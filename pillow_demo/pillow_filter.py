from PIL import Image, ImageFilter
im = Image.open('QQ图片20171023201929.jpg')
im2 = im.filter(ImageFilter.BLUR)
im2.save(r'D:\blur.jpg', 'jpeg')
