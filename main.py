import matplotlib.pyplot as plt 
import numpy as np 
from skimage import filters, measure

image = plt.imread("./circ1.png")[:,:,:]

LB = measure.label(image)
props = measure.regionprops(LB)
length = len(props)
print(length)


plt.figure(figsize=(8,8))
plt.imshow(image)
plt.show()
