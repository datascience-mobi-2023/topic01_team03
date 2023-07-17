import numpy as np
def local_thresholding(img, window_size):
    """
    This function performs local thresholding on an input image using a sliding window scheme for a given window
    size. It first expands the image by mirroring the boundary rows and columns to handle edge cases.
    Then, it iterates over each pixel in the image and extracts a local window centered around that pixel.
    Within each window, the function calculates the optimal threshold value using Otsu's thresholding algorithm.
    Based on the threshold, the pixel value is set to either 0 or 255 in the output image.
    This process is repeated for each pixel and the locally thresholded image is returned.

    Args:
        img (np.ndarray): Input image
        window_size (int): size of an edge of the sliding window

    Returns:
        np.ndarray: locally thresholded image
    """
    
    #define top and bottom rows of the image
    half_window = window_size // 2
    top_rows = img[:half_window, :][::-1, :]
    bottom_rows = img[-half_window:, :][::-1, :]
    
    #expand the image by mirroring the top and bottom rows
    imgM = np.concatenate((top_rows, img, bottom_rows), axis=0)
    
    #define left and right columns of the image
    left_cols = imgM[:, :half_window][:, ::-1]
    right_cols = imgM[:, -half_window:][:, ::-1]
    
    #expand the image by mirroring the left and right columns
    imgM = np.concatenate((left_cols, imgM, right_cols), axis=1)
    imgT = imgM.copy()
    
    #define height and width of the mirrored image
    height, width = imgM.shape[:2]

    #iterate over each pixel in the image
    for y in range(half_window, height - half_window):
        for x in range(half_window, width - half_window):
            
            #extract a local window around the pixel
            window = imgM[y - half_window : y + half_window + 1, x - half_window : x + half_window + 1]
            rvl = window.ravel()
            
            #define range of intensity values and numerical values of the histogram
            ran = round(max(rvl) - min(rvl))
            counts, bins = np.histogram(rvl, bins=ran)
            
            #create a list for within class variance values for each threshold
            variance_list = list()
            
            #iterate over each possible threshold
            for T in range(1, len(counts)):
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
                within_class_varianz = w0 * var_back + w1 * var_obj
                
                #append within class variance to the list
                variance_list.append(within_class_varianz)
 
            #define optimal threshold value by selecting minimal within class variance value 
            THRESH = bins[np.argmin(variance_list)]
                 
            #assign new intensity value based on the threshold
            if imgM[y, x] < THRESH:
                imgT[y, x] = 0
            else:
                imgT[y, x] = 255
           
    #remove the mirrored border to obtain the original image dimensions
    imgT = imgT[half_window:height-half_window, half_window:width-half_window]

    return imgT

def local_thresholding2(img, window_size):
    """
    This function performs local thresholding on an input image using a sliding window scheme for a given window
    size. It first expands the image by mirroring the boundary rows and columns to handle edge cases.
    Then, it iterates over each pixel in the image and extracts a local window centered around that pixel.
    Within each window, the function calculates the optimal threshold value using Otsu's thresholding algorithm.
    Based on the threshold, the pixel value is set to either 0 or 65535 in the output image.
    This process is repeated for each pixel and the locally thresholded image is returned.

    Args:
        img (np.ndarray): Input image
        window_size (int): size of an edge of the sliding window

    Returns:
        np.ndarray: locally thresholded image
    """
    
    #define top and bottom rows of the image
    half_window = window_size // 2
    top_rows = img[:half_window, :][::-1, :]
    bottom_rows = img[-half_window:, :][::-1, :]
    
    #expand the image by mirroring the top and bottom rows
    imgM = np.concatenate((top_rows, img, bottom_rows), axis=0)
    
    #define left and right columns of the image
    left_cols = imgM[:, :half_window][:, ::-1]
    right_cols = imgM[:, -half_window:][:, ::-1]
    
    #expand the image by mirroring the left and right columns
    imgM = np.concatenate((left_cols, imgM, right_cols), axis=1)
    imgT = imgM.copy()
    
    #define height and width of the mirrored image
    height, width = imgM.shape[:2]

    #iterate over each pixel in the image
    for y in range(half_window, height - half_window):
        for x in range(half_window, width - half_window):
            
            #extract a local window around the pixel
            window = imgM[y - half_window : y + half_window + 1, x - half_window : x + half_window + 1]
            rvl = window.ravel()
            
            #define range of intensity values and numerical values of the histogram
            ran = round(max(rvl) - min(rvl))
            counts, bins = np.histogram(rvl, bins=ran)
            
            #create a list for within class variance values for each threshold
            variance_list = list()
            
            #iterate over each possible threshold
            for T in range(1, len(counts)):
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
                within_class_varianz = w0 * var_back + w1 * var_obj
                
                #append within class variance to the list
                variance_list.append(within_class_varianz)
 
            #define optimal threshold value by selecting minimal within class variance value 
            THRESH = bins[np.argmin(variance_list)]
                 
            #assign new intensity value based on the threshold
            if imgM[y, x] < THRESH:
                imgT[y, x] = 0
            else:
                imgT[y, x] = 65535
           
    #remove the mirrored border to obtain the original image dimensions
    imgT = imgT[half_window:height-half_window, half_window:width-half_window]

    return imgT