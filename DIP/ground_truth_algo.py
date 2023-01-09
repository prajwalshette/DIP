import numpy as np
import matplotlib.pyplot as plt
import skimage
# from skimage.io import imread, imshow

# lily = img = imread('lily.jpg')
lily = skimage.io.imread('lily.jpg')

from matplotlib.patches import Rectangle
fig, ax = plt.subplots()
ax.imshow(lily)
ax.add_patch(Rectangle((650, 550), 100, 100, edgecolor='b', facecolor='none'));
