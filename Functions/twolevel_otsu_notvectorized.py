import numpy as np
def twolevel_thresholding(img1):
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
    
    #create copy of the input image and flatten image
    imgT = img1.copy()
    rvl = img1.ravel()

    #define range of intensity values and numerical values of the histogram
    ran = round(max(rvl) - min(rvl))
    counts, bins = np.histogram(rvl,bins = ran)
 
    #create lists for within class variance values and thresholds
    variance_list = list()
    threshold_list = list()

    #iterate over each possible threshold combination
    for T in range(1,len(counts)):
        for T2 in range(T+1,len(counts)):
            
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

            #middle class
            
            #calculate mean levels and class propabilities
            sum_mid = 0
            mean_sum_mid = 0
            for j in range(T,T2):
                sum_mid += counts[j]
                mean_sum_mid += counts[j] * bins[j]

            w1 = sum_mid / sum(counts)
            if sum_mid != 0 :
                mean_mid = mean_sum_mid / sum_mid
            
            #calculate variance
            var_sum_mid = 0
            if sum_mid != 0:
                for m in range(T,T2):
                    var_sum_mid += counts[m] * (bins[m] - mean_mid)**2 
                if sum_mid != 0:
                    var_mid = var_sum_mid / sum_mid
            
            #foreground
        
            #calculate mean levels and class propabilities
            sum_obj = 0
            mean_sum_obj = 0

            for j in range(T2,len(counts)):
                sum_obj += counts[j]
                mean_sum_obj += counts[j] * bins[j]

            w2 = sum_obj / sum(counts)
            mean_obj = mean_sum_obj / sum_obj
            
            #calculate variance
            var_sum_obj = 0
            for l in range(T2, len(counts)):
                var_sum_obj += counts[l] * (bins[l] - mean_obj)**2 

            var_obj = var_sum_obj / sum_obj
            
            #calculate within class variance
            if sum_mid !=0:
                within_class_varianz = w0 * var_back + w1 * var_mid + w2 * var_obj
        
            #within class variance zu Liste hinzufügen
            if sum_mid != 0:
                variance_list.append(within_class_varianz)
            
            #append within class variance to the list
            if sum_mid != 0:
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

def twolevel_thresholding2(img1):
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
    
    #create copy of the input image and flatten image
    imgT = img1.copy()
    rvl = img1.ravel()

    #define range of intensity values and numerical values of the histogram
    ran = round(max(rvl) - min(rvl))
    counts, bins = np.histogram(rvl,bins = ran)
 
    #create lists for within class variance values and thresholds
    variance_list = list()
    threshold_list = list()

    #iterate over each possible threshold combination
    for T in range(1,len(counts)):
        for T2 in range(T+1,len(counts)):
            
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

            #middle class
            
            #calculate mean levels and class propabilities
            sum_mid = 0
            mean_sum_mid = 0
            for j in range(T,T2):
                sum_mid += counts[j]
                mean_sum_mid += counts[j] * bins[j]

            w1 = sum_mid / sum(counts)
            if sum_mid != 0 :
                mean_mid = mean_sum_mid / sum_mid
            
            #calculate variance
            var_sum_mid = 0
            if sum_mid != 0:
                for m in range(T,T2):
                    var_sum_mid += counts[m] * (bins[m] - mean_mid)**2 
                if sum_mid != 0:
                    var_mid = var_sum_mid / sum_mid
            
            #foreground
        
            #calculate mean levels and class propabilities
            sum_obj = 0
            mean_sum_obj = 0

            for j in range(T2,len(counts)):
                sum_obj += counts[j]
                mean_sum_obj += counts[j] * bins[j]

            w2 = sum_obj / sum(counts)
            mean_obj = mean_sum_obj / sum_obj
            
            #calculate variance
            var_sum_obj = 0
            for l in range(T2, len(counts)):
                var_sum_obj += counts[l] * (bins[l] - mean_obj)**2 

            var_obj = var_sum_obj / sum_obj
            
            #calculate within class variance
            if sum_mid !=0:
                within_class_varianz = w0 * var_back + w1 * var_mid + w2 * var_obj
        
            #within class variance zu Liste hinzufügen
            if sum_mid != 0:
                variance_list.append(within_class_varianz)
            
            #append within class variance to the list
            if sum_mid != 0:
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

