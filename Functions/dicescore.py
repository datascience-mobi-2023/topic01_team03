def dice(img1, img2):
    """
    This function takes two binary images as parameters and returns the Dice coefficient between them. It converts the input 
    images into boolean arrays and compares the element-wise similarity between the two images. It then calculates the number 
    of common elements between the images, the total number of elements in each image and finally computes the Dice score.
   

    Args:
        img1 (_type_): Input image 1
        img2 (_type_): Input image 2

    Returns:
        _type_: dice score
    """
    import numpy as np
    #convert images into boolean arrays
    img1 = np.asarray(img1).astype(bool)
    img2 = np.asarray(img2).astype(bool)

    #calculate number of common elements bgetween the two images
    commonelements = np.equal(img1, img2)
    
    #calculate total number of elements in each image
    elements1 = img1.shape[0]*img1.shape[1]
    elements2 = img2.shape[0]*img2.shape[1]
    
    #compute dice score
    d = 2* commonelements.sum()/(elements1 + elements2)
    return d