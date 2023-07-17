import numpy as np
def multi_otsu_thresholding_vek(img1):
    """
    This function performs two-level thresholding on an input image.
    It calculates two optimal threshold values by finding the combination of thresholds that minimizes the within class variance.
    The function iterates over pairs of threshold values and computes the within class variance for each combination.
    Based on the minimal within class variance, it determines the two optimal threshold values.
    Using these thresholds, the function assigns pixel intensities to one of the three levels: 
    every intensity value below the first threshold is assigned to 0, every intensity value in between the two thresholds is assigned 
    to 255 and every intensity value above the second threshold is assigned to 0, so that reflections are assigned to the background.

    Args:
        img1 (np.ndarray): Input image

    Returns:
        np.ndarray: twolevel-thresholded image
    """
    
    #create copy of the input image and flatten it
    imgT = img1.copy()
    rvl = img1.ravel()

    #define range of intensity values and numerical values of the histogram
    ran = round(max(rvl) - min(rvl))
    counts, bins = np.histogram(rvl,bins = ran)
 
    #create lists for within class variance values and thresholds
    variance_list = list()
    threshold_list = list()
    
    #calculate cumulative sums and means for efficiency
    sum_counts_list = np.cumsum(counts)
    mean_sum_list = np.cumsum(counts*bins[:-1])
    
    #calculate list of background class propabilities and mean levels
    w0_list = sum_counts_list/sum(counts)
    mean_back_list = mean_sum_list/sum_counts_list
    
    #iterate over each possible threshold combination
    for T in range(1,len(counts)-1):
        
        #calculate class propability and variance for the background
        var_back = sum(counts[:T]*(bins[:T]-mean_back_list[T])**2)/sum_counts_list[T]
        w0 = w0_list[T]
        
        for T2 in range(T+1,len(counts)):
            
            #middle class
            
            #calculate sum of the pixels, mean level and class propability
            sum_mid = sum_counts_list[T2]-sum_counts_list[T]
            mean_sum_mid = mean_sum_list[T2]-mean_sum_list[T]
            w1 = sum_mid / sum(counts)
            mean_mid = mean_sum_mid / sum_mid
            
            #calculate variance
            var_sum_mid = 0
            for m in range(T,T2):
                var_sum_mid += counts[m] * (bins[m] - mean_mid)**2 
            var_mid = var_sum_mid / sum_mid
            
            #foreground
            
            #calculate sum of the pixels, mean level and class propability
            
            sum_obj = sum_counts_list[len(counts)-1]-sum_counts_list[T2]
            mean_sum_obj = mean_sum_list[len(counts)-1]-mean_sum_list[T]

            w2 = sum_obj / sum(counts)
            mean_obj = mean_sum_obj / sum_obj

            #calculate variance
            var_sum_obj = 0
            for n in range(T2, len(counts)):
                var_sum_obj += counts[n] * (bins[n] - mean_obj)**2 
            var_obj = var_sum_obj / sum_obj

            #calculate within class variance
            
            within_class_variance = w0 * var_back + w1 * var_mid + w2 * var_obj
        
            #append within class variance to the list
            
            variance_list.append(within_class_variance)
            
            #append thresholds to list
            
            threshold_list.append((T,T2))
    
   #define optimal threshold values by selecting minimal within class variance value  
    thresh1, thresh2 = threshold_list[np.argmin(variance_list)]
    
    
    #clip intensities based on optimal thresholds
    for p in np.ndindex(imgT.shape):
        if img1[p] < thresh1:
            imgT[p] = 0
        elif img1[p] < thresh2:
            imgT[p] = 255
        else:
            imgT[p] = 0
    return imgT

def multi_otsu_thresholding_vek2(img1):
    """
    This function performs two-level thresholding on an input image.
    It calculates two optimal threshold values by finding the combination of thresholds that minimizes the within class variance.
    The function iterates over pairs of threshold values and computes the within class variance for each combination.
    Based on the minimal within class variance, it determines the two optimal threshold values.
    Using these thresholds, the function assigns pixel intensities to one of the three levels: 
    every intensity value below the first threshold is assigned to 0, every intensity value in between the two thresholds is assigned 
    to 65535 and every intensity value above the second threshold is assigned to 0, so that reflections are assigned to the background.

    Args:
        img1 (np.ndarray): Input image

    Returns:
        np.ndarray: twolevel-thresholded image
    """
    
    #create copy of the input image and flatten it
    imgT = img1.copy()
    rvl = img1.ravel()

    #define range of intensity values and numerical values of the histogram
    ran = round(max(rvl) - min(rvl))
    counts, bins = np.histogram(rvl,bins = ran)
 
    #create lists for within class variance values and thresholds
    variance_list = list()
    threshold_list = list()
    
    #calculate cumulative sums and means for efficiency
    sum_counts_list = np.cumsum(counts)
    mean_sum_list = np.cumsum(counts*bins[:-1])
    
    #calculate list of background class propabilities and mean levels
    w0_list = sum_counts_list/sum(counts)
    mean_back_list = mean_sum_list/sum_counts_list
    
    #iterate over each possible threshold combination
    for T in range(1,len(counts)-1):
        
        #calculate class propability and variance for the background
        var_back = sum(counts[:T]*(bins[:T]-mean_back_list[T])**2)/sum_counts_list[T]
        w0 = w0_list[T]
        
        for T2 in range(T+1,len(counts)):
            
            #middle class
            
            #calculate sum of the pixels, mean level and class propability
            sum_mid = sum_counts_list[T2]-sum_counts_list[T]
            mean_sum_mid = mean_sum_list[T2]-mean_sum_list[T]
            w1 = sum_mid / sum(counts)
            mean_mid = mean_sum_mid / sum_mid
            
            #calculate variance
            var_sum_mid = 0
            for m in range(T,T2):
                var_sum_mid += counts[m] * (bins[m] - mean_mid)**2 
            var_mid = var_sum_mid / sum_mid
            
            #foreground
            
            #calculate sum of the pixels, mean level and class propability
            
            sum_obj = sum_counts_list[len(counts)-1]-sum_counts_list[T2]
            mean_sum_obj = mean_sum_list[len(counts)-1]-mean_sum_list[T]

            w2 = sum_obj / sum(counts)
            mean_obj = mean_sum_obj / sum_obj

            #calculate variance
            var_sum_obj = 0
            for n in range(T2, len(counts)):
                var_sum_obj += counts[n] * (bins[n] - mean_obj)**2 
            var_obj = var_sum_obj / sum_obj

            #calculate within class variance
            
            within_class_variance = w0 * var_back + w1 * var_mid + w2 * var_obj
        
            #append within class variance to the list
            
            variance_list.append(within_class_variance)
            
            #append thresholds to list
            
            threshold_list.append((T,T2))
    
   #define optimal threshold values by selecting minimal within class variance value  
    thresh1, thresh2 = threshold_list[np.argmin(variance_list)]
    
    
    #clip intensities based on optimal thresholds
    for p in np.ndindex(imgT.shape):
        if img1[p] < thresh1:
            imgT[p] = 0
        elif img1[p] < thresh2:
            imgT[p] = 65535
        else:
            imgT[p] = 0
    return imgT