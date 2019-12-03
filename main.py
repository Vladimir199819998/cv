import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
from scipy.ndimage import binary_dilation
from skimage.filters import threshold_otsu
from skimage import filters

image = plt.imread("./lama_on_moon.png")
gray = np.average(image, 2)[50:-50, 50:-50]

sobel = filters.sobel(gray)
thresh = filters.threshold_otsu(sobel)
sobel[sobel < thresh] = 0
sobel[sobel >= thresh] = 1

lb = label(sobel)
symbols = regionprops(lb)
areas=[]
for sym in symbols:
    areas.append(sym.area)

maxi=0
i=0

for ar in areas:
    i=i+1
    if ar>maxi:
        maxi=ar
        j=i
        x1 , y1, x2, y2 = symbols[j-1].bbox

image1 = image[x1+50:x2+50, y1+50:y2+50]

plt.figure()
plt.imshow(image1)
plt.show()
