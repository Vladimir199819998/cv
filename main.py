# to count all balls, we have to 
# count how many balls belong to 
# a certain color
import matplotlib.pyplot as plt 
import numpy as np 
from skimage import filters, measure

image = plt.imread("./circ1.png")[:,:,:]

result = []
for i in range(image.shape[-1]):
    lb = measure.label(image[:, :, i])
    result.append(np.max(lb))

print(result)
print(np.sum(result[:-1]))
plt.figure(figsize=(8,8))
plt.imshow(image)
plt.show()
