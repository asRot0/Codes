from PIL import Image
import numpy
img = Image.open('image_from_array.png')

print(img.format)
print(img.size)
print(img.mode)

print(numpy.asarray(img).size)
print(numpy.asarray(img).shape)
print(numpy.asarray(img))