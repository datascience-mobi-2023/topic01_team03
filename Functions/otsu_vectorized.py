def otsu_thresholding_vek(img1):
    """
    This function takes an input image as a parameter and returns a binary image where pixels are either set to 0 or 255.
    It calculates the class propabilities, mean levels and variances for foreground and background for every possible threshold. 
    Then the within class variance is computed and the optimal threshold is defined as the value with the lowest within class variance. 
    The image is clipped based on the optimal threshold value and the binarized image is returned.

    Args:
        img1 (_type_): Input image

    Returns:
        _type_: Thresholded image
    """
    
    import numpy as np
    
    #create copy of the input image and flatten image
    imgT = img1.copy()
    rvl = img1.ravel()

    #define range of intensity values and numerical values of the histogram
    ran = round(max(rvl) - min(rvl))
    counts, bins = np.histogram(rvl,bins = ran)
    
    #calculate sum of the pixels in the foreground and background for each threshold
    sum_back = np.cumsum(counts)[:-1]
    sum_obj = sum(counts)-sum_back
    
    #calculate mean levels of foreground and background for each threshold 
    mean_back = np.cumsum(bins[:-2]*counts[:-1])/sum_back
    mean_obj = (sum(bins[:-2]*counts[:-1])-np.cumsum(bins[:-2]*counts[:-1]))/sum_obj
    
    #calculate class propabilities of foreground and background for each threshold
    w0_list = sum_back/sum(counts)
    w1_list = 1 - w0_list

    #crteate empty lists for foreground and background variances
    var_back_list = list()
    var_obj_list = list()
    
    #calculate background and foreground variances for each threshold and store them in lists
    for i in range (0,len(mean_back)):
        var_back = sum(counts[:i]*(bins[:i]-mean_back[i])**2)/sum_back[i]
        var_back_list.append(var_back)
        var_obj = sum(counts[i:]*(bins[i:-1]-mean_obj[i])**2)/sum_obj[i]
        var_obj_list.append(var_obj)
    
    #calculate within class variance for each threshold 
    wcv_list = (w0_list * var_back_list) + (w1_list * var_obj_list)
    
    #define optimal threshold value by selecting minimal within class variance value 
    THRESH = bins[np.argmin(wcv_list)]

    #clip intensities based on the optimal threshold
    for p in np.ndindex(imgT.shape):
        if img1[p] < THRESH:
            imgT[p] = 0
        else:
            imgT[p] = 255
    return imgT

def otsu_thresholding_vek2(img1):
    """
    This function takes an input image as a parameter and returns a binary image where pixels are either set to 0 or 65535.
    It calculates the class propabilities, mean levels and variances for foreground and background for every possible threshold. 
    Then the within class variance is computed and the optimal threshold is defined as the value with the lowest within class variance. 
    The image is clipped based on the optimal threshold value and the binarized image is returned.

    Args:
        img1 (_type_): Input image

    Returns:
        _type_: Thresholded image
    """
    
    import numpy as np
    
    #create copy of the input image and flatten image
    imgT = img1.copy()
    rvl = img1.ravel()

    #define range of intensity values and numerical values of the histogram
    ran = round(max(rvl) - min(rvl))
    counts, bins = np.histogram(rvl,bins = ran)
    
    #calculate sum of the pixels in the foreground and background for each threshold
    sum_back = np.cumsum(counts)[:-1]
    sum_obj = sum(counts)-sum_back
    
    #calculate mean levels of foreground and background for each threshold 
    mean_back = np.cumsum(bins[:-2]*counts[:-1])/sum_back
    mean_obj = (sum(bins[:-2]*counts[:-1])-np.cumsum(bins[:-2]*counts[:-1]))/sum_obj
    
    #calculate class propabilities of foreground and background for each threshold
    w0_list = sum_back/sum(counts)
    w1_list = 1 - w0_list

    #crteate empty lists for foreground and background variances
    var_back_list = list()
    var_obj_list = list()
    
    #calculate background and foreground variances for each threshold and store them in lists
    for i in range (0,len(mean_back)):
        var_back = sum(counts[:i]*(bins[:i]-mean_back[i])**2)/sum_back[i]
        var_back_list.append(var_back)
        var_obj = sum(counts[i:]*(bins[i:-1]-mean_obj[i])**2)/sum_obj[i]
        var_obj_list.append(var_obj)
    
    #calculate within class variance for each threshold 
    wcv_list = (w0_list * var_back_list) + (w1_list * var_obj_list)
    
    #define optimal threshold value by selecting minimal within class variance value 
    THRESH = bins[np.argmin(wcv_list)]

    #clip intensities based on the optimal threshold
    for p in np.ndindex(imgT.shape):
        if img1[p] < THRESH:
            imgT[p] = 0
        else:
            imgT[p] = 65535
    return imgT
