def local_thresholding(img, window_size):
    """
    This function performs local thresholding on an input image using a sliding window scheme for a given window
    size. It first expands the image by mirroring the boundary rows and columns to handle edge cases.
    Then, it iterates over each pixel in the image and extracts a local window centered around that pixel.
    Within each window, the function calculates the optimal threshold value using Otsu's thresholding algorithm.
    Based on the threshold, the pixel value is set to either 0 or 255 in the output image.
    This process is repeated for each pixel and the locally thresholded image is returned.

    Args:
        img (_type_): Input image
        window_size (_type_): size of an edge of the sliding window

    Returns:
        _type_: locally thresholded image
    """
    import numpy as np
    
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

    
    for y in range(half_window, height - half_window):
        for x in range(half_window, width - half_window):
            window = imgM[y - half_window : y + half_window + 1, x - half_window : x + half_window + 1]
             
            rvl = window.ravel()
            ran = round(max(rvl) - min(rvl))
            counts, bins = np.histogram(rvl, bins=ran)
            
 
            variance_list = []
 
            for T in range(1, len(counts)):
                sum_back = 0 
                mean_sum_back = 0
                for i in range(0, T):
                    sum_back += counts[i]
                    mean_sum_back += counts[i] * bins[i]
 
                w0 = sum_back / sum(counts)
                mean_back = mean_sum_back / sum_back
 
                sum_obj = 0
                mean_sum_obj = 0
                for j in range(T, len(counts)):
                    sum_obj += counts[j]
                    mean_sum_obj += counts[j] * bins[j]
 
                w1 = sum_obj / sum(counts)
                mean_obj = mean_sum_obj / sum_obj
 
                var_sum_back = 0
                for k in range(0, T):
                    var_sum_back += counts[k] * (bins[k] - mean_back)**2 
 
                var_back = var_sum_back / sum_back
 
                var_sum_obj = 0
                for l in range(T, len(counts)):
                    var_sum_obj += counts[l] * (bins[l] - mean_obj)**2 
 
                var_obj = var_sum_obj / sum_obj
 
                within_class_varianz = w0 * var_back + w1 * var_obj
                variance_list.append(within_class_varianz)
 
            minvar = min(variance_list)
            THRESH = round(bins[variance_list.index(minvar)])
 
            if imgM[y, x] < THRESH:
                imgT[y, x] = 0
            else:
                imgT[y, x] = 255

    return imgT