import numpy as np
import matplotlib.pyplot as plt
import skimage.io

lily = skimage.io.imread('farm.jpeg')

#White Patch
def white_patch(image, percentile=100):
    """
    White balance image using White patch algorithm
    Parameters
    ----------
    image : numpy array
            Image to white balance
    percentile : integer, optional
                  Percentile value to consider as channel maximum
    Returns
    -------
    image_wb : numpy array
               White-balanced image
    """
    white_patch_image = skimage.img_as_ubyte((image*1.0 /
                                   np.percentile(image,percentile,
                                   axis=(0, 1))).clip(0, 1))
    return white_patch_image
#call the function to implement white patch algorithm
skimage.io.imshow(white_patch(lily, 85))

