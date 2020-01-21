import os
from PIL import Image
from PIL import ImageOps

img = Image.open('original2.tif').convert('L')
size = 720 , 320
im_resized = img.resize(size, Image.ANTIALIAS)
binary = im_resized.point(lambda x: 0 if x<225 else 255, '1')  #binarization || x<225 is threshold value for binarization
inverted_image = ImageOps.invert( binary.convert('RGB') )
# inverted_image.save('output.png')
inverted_image.save('inverted.jpg')




# img = Image.open('original2.tif').convert('L')
# size = 720 , 320
# im_resized = img.resize(size, Image.ANTIALIAS)
# binary = im_resized.point(lambda x: 0 if x<225 else 255, '1')  #binarization || x<225 is threshold value for binarization
# inverted_image = ImageOps.invert( binary.convert('RGB') )
# inverted_image.save('output2.png')