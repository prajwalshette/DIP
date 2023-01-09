import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage.io import imread, imshow

# lily = img = imread('lily.jpg')
lily = skimage.io.imread('lily.jpg')

def gray_world(image):
    """
    White balance image using Gray-world algorithm
    Parameters
    ----------
    image : numpy array
            Image to white balance
    
    Returns
    -------
    image_wb : numpy array   
               White-balanced image
    """
    image_grayworld = ((image * (access.mean() / 
                      image.mean(axis=(0,1)))).
                      clip(0,255).astype(int))
    # for images having a transparency channel
    
    if image.shape[2] == 4:
     image_grayworld[:,:,3] = 255
    return image_grayworld
#call the function to implement gray world algorithm
skio.imshow(gray_world(lily))
 