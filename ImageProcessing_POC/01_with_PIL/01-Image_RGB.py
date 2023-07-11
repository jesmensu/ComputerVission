import numpy as np
from matplotlib import pyplot, image
from PIL import Image
img = Image.open("./ImageProcessing_POC/data/IMG_01.jpg")

pyplot.imshow(img)
pyplot.show()

img = np.array(img)
img1 = img.copy()
img2 = img.copy()
img3 = img.copy()

img1[:, :, 0] = 0
pyplot.imshow(img1)
pyplot.title("Without Red Color")
pyplot.show()

img2[:, :, 1] = 0
pyplot.imshow(img2)
pyplot.title("Without Green Color")
pyplot.show()

img3[:, :, 2] = 0
pyplot.imshow(img3)
pyplot.title("Without Blue Color")
pyplot.show()
