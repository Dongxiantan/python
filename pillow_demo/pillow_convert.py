from PIL import Image
# pil_im = Image.open('QQ图片20171023201929.jpg')
pil_im = Image.open('QQ图片20171023201929.jpg').convert('L')
pil_im.save('convert.jpg', 'jpeg')
