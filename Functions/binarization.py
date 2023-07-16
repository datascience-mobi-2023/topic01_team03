def binarize(img):
    import numpy as np
    img1 = img.copy()

    for p in np.ndindex(img1.shape):
        if img[p] > 0: 
           img1[p] = 255
        else:
            img1[p] = 0
    
    return img1
def binarize2(img):
    import numpy as np
    img1 = img.copy()

    for p in np.ndindex(img1.shape):
        if img[p] > 0: 
           img1[p] = 65535
        else:
            img1[p] = 0
    
    return img1