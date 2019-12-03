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

LB = measure.label(sobel)

for prop in measure.regionprops(LB):
    if prop.area < 200 or prop.perimeter < 1000:
        sobel[prop.coords[:,0], prop.coords[:,1]]
    else:
        print(prop.perimeter)

plt.subplot(111)
plt.imshow(sobel)
plt.show()
