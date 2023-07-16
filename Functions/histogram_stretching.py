
def histogram_stretching(img):
    """
    This function takes an input image as a parameter and performs histogram stretching. The intensity values of the image are
    stretched, so that the lowest intensity value is 0 and the highest intensity value is 255. The stretched image is returned.

    Args:
        img (_type_): _Input image
    

    Returns:
        _type_: stretched image
    """
    
    import numpy as np
    
    #define highest and lowest intensity values of the returned image as 0 and 255
    a = 0
    b = 255
    
    #select highest and lowest intensity value of the image
    c = min(img.ravel())
    d = max(img.ravel())
    
    #make a copy of the input image
    img_copy = img.copy()
    
    #assign every pixel of the image to it's new intensity value 
    for p in np.ndindex(img_copy.shape):
        img_copy[p] = (img[p]-c) * ((b-a)/(d-c))+a
    return img_copy


def histogram_stretching2(img):
    """
    This function takes an input image as a parameter and performs histogram stretching. The intensity values of the image are
    stretched, so that the lowest intensity value is 0 and the highest intensity value is  65535. The stretched image is returned.

    Args:
        img (_type_): _Input image
    

    Returns:
        _type_: stretched image
    """
    
    import numpy as np
    
    #define highest and lowest intensity values of the returned image as 0 and  65535
    a = 0
    b =  65535
    
    #select highest and lowest intensity value of the image
    c = min(img.ravel())
    d = max(img.ravel())
    
    #make a copy of the input image
    img_copy = img.copy()
    
    #assign every pixel of the image to it's new intensity value 
    for p in np.ndindex(img_copy.shape):
        img_copy[p] = (img[p]-c) * ((b-a)/(d-c))+a
    return img_copy