import matplotlib.pyplot as plt
import numpy as np
from skimage import filters, measure
from skimage.measure import label

# воходное изображение нужно избавить от 
# рамки, это связано с расчетом производной
img = plt.imread("./lama_on_moon.png")
gray = np.average(img, 2)[50:-50, 50:-50]

sobel = filters.sobel(gray)
thresh = filters.threshold_otsu(sobel)
sobel[sobel < thresh] = 0
sobel[sobel >= thresh] = 1

max_area = 0
index = -1
LB = measure.label(sobel)
props = measure.regionprops(LB)

for prop in enumerate(props):
    if prop.convex_area > max_area:
        index = i
        max_area = prop.convex_area

bb = props[index].bbox
lama = img[bb[0]::bb[2], bb[1]::bb[3]]

plt.subplot(111)
plt.imshow(sobel)
plt.show()
