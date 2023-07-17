import numpy as np 
def binarize(img):
    """
    This function takes an input image as a parameter and returns a binarized image. 
    It sets all intensity values above 0 to 255.

    Args:
        img (np.ndarray): Input image

    Returns:
        np.ndarray: binarized image
    """
    #create copy of the image
    img1 = img.copy()
    
    #iterate over all pixels and assign new intrensities
    for p in np.ndindex(img1.shape):
        if img[p] > 0: 
           img1[p] = 255
        else:
            img1[p] = 0
    
    return img1

def binarize2(img):
    """
    This function takes an input image as a parameter and returns a binarized image. 
    It sets all intensity values above 0 to 65535.

    Args:
        img (np.ndarray): Input image

    Returns:
        np.ndarray: binarized image
    """
    #create copy of the image
    img1 = img.copy()
    
    #iterate over all pixels and assign new intrensities
    for p in np.ndindex(img1.shape):
        if img[p] > 0: 
           img1[p] = 65535
        else:
            img1[p] = 0
    
    return img1