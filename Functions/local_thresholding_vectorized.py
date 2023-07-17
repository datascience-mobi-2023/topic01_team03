import numpy as np
def local_thresholding_vek(img, window_size):
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
    
    #define start and end index for the iteration over the image
    start_index = (half_window, half_window)
    end_index = (imgM.shape[0]-half_window,imgM.shape[1]-half_window)

    #iterate over each pixel of the image 
    for p in np.ndindex(imgM.shape):
        if end_index[0] > p[0] >= start_index[0] and end_index[1] > p[1] >= start_index[1]:
            
            #extract a local window around the pixel
            window = imgM[p[0] - half_window : p[0] + half_window + 1, p[1] - half_window : p[1] + half_window + 1]
            rvl = window.ravel()
            
            #define range of intensity values and numerical values of the histogram
            ran = round(max(rvl) - min(rvl))
            counts, bins = np.histogram(rvl, bins=ran)
            
            #calculate sum of the pixels in the foreground and background for each threshold
            sum_back = np.cumsum(counts)[:-1]
            sum_obj = sum(counts)-sum_back
            
            #calculate mean levels of foreground and background for each threshold 
            mean_back = np.cumsum(bins[:-2]*counts[:-1])/sum_back
            mean_obj = (sum(bins[:-2]*counts[:-1])-np.cumsum(bins[:-2]*counts[:-1]))/sum_obj
            
            #calculate class propabilities of foreground and background for each threshold
            w0_list = sum_back/sum(counts)
            w1_list = 1 - w0_list

            #calculate background and foreground variances and store them in lists
            var_back_list = list()
            var_obj_list = list()
            for i in range (0,len(mean_back)):
                var_back = sum(counts[:i]*(bins[:i]-mean_back[i])**2)/sum_back[i]
                var_back_list.append(var_back)
                var_obj = sum(counts[i:]*(bins[i:-1]-mean_obj[i])**2)/sum_obj[i]
                var_obj_list.append(var_obj)
        
            #calculate within class variance for each threshold 
            wcv_list = (w0_list * var_back_list) + (w1_list * var_obj_list)
            
            #define optimal threshold value by selecting minimal within class variance value 
            THRESH = bins[np.argmin(wcv_list)]
            
            #assign new intensity value based on the threshold
            if imgM[p] < THRESH:
                imgT[p] = 0
            else:
                imgT[p] = 255
                
    #remove the mirrored border to obtain the original image dimensions
    imgT = imgT[half_window:imgT.shape[0]-half_window, half_window:imgT.shape[1]-half_window]
    
    return imgT

def local_thresholding_vek2(img, window_size):
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
    
    #define start and end index for the iteration over the image
    start_index = (half_window, half_window)
    end_index = (imgM.shape[0]-half_window,imgM.shape[1]-half_window)

    #iterate over each pixel of the image 
    for p in np.ndindex(imgM.shape):
        if end_index[0] > p[0] >= start_index[0] and end_index[1] > p[1] >= start_index[1]:
            
            #extract a local window around the pixel
            window = imgM[p[0] - half_window : p[0] + half_window + 1, p[1] - half_window : p[1] + half_window + 1]
            rvl = window.ravel()
            
            #define range of intensity values and numerical values of the histogram
            ran = round(max(rvl) - min(rvl))
            counts, bins = np.histogram(rvl, bins=ran)
            
            #calculate sum of the pixels in the foreground and background for each threshold
            sum_back = np.cumsum(counts)[:-1]
            sum_obj = sum(counts)-sum_back
            
            #calculate mean levels of foreground and background for each threshold 
            mean_back = np.cumsum(bins[:-2]*counts[:-1])/sum_back
            mean_obj = (sum(bins[:-2]*counts[:-1])-np.cumsum(bins[:-2]*counts[:-1]))/sum_obj
            
            #calculate class propabilities of foreground and background for each threshold
            w0_list = sum_back/sum(counts)
            w1_list = 1 - w0_list

            #calculate background and foreground variances and store them in lists
            var_back_list = list()
            var_obj_list = list()
            for i in range (0,len(mean_back)):
                var_back = sum(counts[:i]*(bins[:i]-mean_back[i])**2)/sum_back[i]
                var_back_list.append(var_back)
                var_obj = sum(counts[i:]*(bins[i:-1]-mean_obj[i])**2)/sum_obj[i]
                var_obj_list.append(var_obj)
        
            #calculate within class variance for each threshold 
            wcv_list = (w0_list * var_back_list) + (w1_list * var_obj_list)
            
            #define optimal threshold value by selecting minimal within class variance value 
            THRESH = bins[np.argmin(wcv_list)]
            
            #assign new intensity value based on the threshold
            if imgM[p] < THRESH:
                imgT[p] = 0
            else:
                imgT[p] = 65535
                
    #remove the mirrored border to obtain the original image dimensions
    imgT = imgT[half_window:imgT.shape[0]-half_window, half_window:imgT.shape[1]-half_window]
    
    return imgT