import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist 
coord_data = [(25.056, -75.7226),
          (25.7411, -79.1197),
          (25.2897, -79.2294),
          (25.6716, -79.3378)]  
print('The Euclidean Matrix Transformation is:')
X=cdist(coord_data,coord_data,'euclidean') 
print(X)
print('The Manhattan Matrix Transformation is:')
Y = cdist(coord_data, coord_data, 'cityblock')
print(Y)   
print('The Chessboard Matrix Transformation is:')
Z = cdist(coord_data, coord_data, 'chebyshev') 
print(Z)