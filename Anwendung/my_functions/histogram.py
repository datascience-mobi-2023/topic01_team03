import numpy as np
def histogrammstretching(img):
    a=0
    b=255
    c = min(img.ravel())
    d = max(img.ravel())
    img_copy = img.copy()
    for p in np.ndindex(img_copy.shape):
        img_copy[p] = (img[p]-c) * ((b-a)/(d-c))+a
    return img_copy