import numpy as np
from PIL import Image


arr = np.arange(0, 1024*720, 1, np.uint8)
print(type(arr))

print(arr.shape)
arr = np.reshape(arr, (1024, 720))
print(arr.shape)
print(arr)

img = Image.fromarray(arr)
img.save('image_from_array.png')