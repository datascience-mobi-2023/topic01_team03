import numpy as np
def otsu_thresholding(img1):
    """
    This function takes an input image as a parameter and returns a binary image where pixels are either set to 0 or 255.
    It calculates the class propabilities, mean levels and variances for foreground and background for every possible threshold. 
    Then the within class variance is computed and the optimal threshold is defined as the value with the lowest within class variance. 
    The image is clipped based on the optimal threshold value and the binarized image is returned.

    Args:
        img1 (np.ndarray): Input image

    Returns:
        np.ndarray: Thresholded image
    """
 
    #create copy of the input image and flatten image
    imgT = img1.copy()
    rvl = img1.ravel()

    #define range of intensity values and numerical values of the histogram
    ran = round(max(rvl) - min(rvl))
    counts, bins = np.histogram(rvl,bins = ran)
 
    #create a list for within class variance values for each threshold
    variance_list = list()
    

    #iterate over each possible threshold
    for T in range(1,len(counts)):
        
        #background
        
        #calculate mean levels and class propabilities
        sum_back = 0 
        mean_sum_back = 0
        for i in range(0,T):
            sum_back += counts[i]
            mean_sum_back += counts[i] * bins[i]

        w0 = sum_back / sum(counts)
        mean_back = mean_sum_back / sum_back
        
        #calculate variance
        var_sum_back = 0
        for k in range(0, T):
            var_sum_back += counts[k] * (bins[k] - mean_back)**2 

        var_back = var_sum_back / sum_back

        #foreground
        
        #calculate mean levels and class propabilities
        sum_obj = 0
        mean_sum_obj = 0

        for j in range(T,len(counts)):
            sum_obj += counts[j]
            mean_sum_obj += counts[j] * bins[j]

        w1 = sum_obj / sum(counts)
        mean_obj = mean_sum_obj / sum_obj

        
        #calculate variance
        var_sum_obj = 0
        for l in range(T, len(counts)):
            var_sum_obj += counts[l] * (bins[l] - mean_obj)**2 

        var_obj = var_sum_obj / sum_obj

        #calculate within class variance
        within_class_variance = w0 * var_back + w1 * var_obj
        
        #append within class variance to the list
        variance_list.append(within_class_variance)
    
    #define optimal threshold value by selecting minimal within class variance value 
    THRESH = bins[np.argmin(variance_list)]

    
    #clip intensities based on the optimal threshold
    for p in np.ndindex(imgT.shape):
        if img1[p] < THRESH:
            imgT[p] = 0
        else:
            imgT[p] = 255
    return imgT


def otsu_thresholding2(img1):
    """
    This function takes an input image as a parameter and returns a binary image where pixels are either set to 0 or 65535.
    It calculates the class propabilities, mean levels and variances for foreground and background for every possible threshold. 
    Then the within class variance is computed and the optimal threshold is defined as the value with the lowest within class variance. 
    The image is clipped based on the optimal threshold value and the binarized image is returned.

    Args:
        img1 (np.ndarray): Input image

    Returns:
        np.ndarray: Thresholded image
    """
 
    #create copy of the input image and flatten image
    imgT = img1.copy()
    rvl = img1.ravel()

    #define range of intensity values and numerical values of the histogram
    ran = round(max(rvl) - min(rvl))
    counts, bins = np.histogram(rvl,bins = ran)
 
    #create a list for within class variance values for each threshold
    variance_list = list()
    

    #iterate over each possible threshold
    for T in range(1,len(counts)):
        
        #background
        
        #calculate mean levels and class propabilities
        sum_back = 0 
        mean_sum_back = 0
        for i in range(0,T):
            sum_back += counts[i]
            mean_sum_back += counts[i] * bins[i]

        w0 = sum_back / sum(counts)
        mean_back = mean_sum_back / sum_back
        
        #calculate variance
        var_sum_back = 0
        for k in range(0, T):
            var_sum_back += counts[k] * (bins[k] - mean_back)**2 

        var_back = var_sum_back / sum_back

        #foreground
        
        #calculate mean levels and class propabilities
        sum_obj = 0
        mean_sum_obj = 0

        for j in range(T,len(counts)):
            sum_obj += counts[j]
            mean_sum_obj += counts[j] * bins[j]

        w1 = sum_obj / sum(counts)
        mean_obj = mean_sum_obj / sum_obj

        
        #calculate variance
        var_sum_obj = 0
        for l in range(T, len(counts)):
            var_sum_obj += counts[l] * (bins[l] - mean_obj)**2 

        var_obj = var_sum_obj / sum_obj

        #calculate within class variance
        within_class_variance = w0 * var_back + w1 * var_obj
        
        #append within class variance to the list
        variance_list.append(within_class_variance)
    
    #define optimal threshold value by selecting minimal within class variance value 
    THRESH = bins[np.argmin(variance_list)]

    
    #clip intensities based on the optimal threshold
    for p in np.ndindex(imgT.shape):
        if img1[p] < THRESH:
            imgT[p] = 0
        else:
            imgT[p] = 65535
    return imgT