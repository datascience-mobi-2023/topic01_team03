import numpy as np
def local_thresholding_vek(img, window_size):
    half_window = window_size // 2
    top_rows = img[:half_window, :][::-1, :]
    bottom_rows = img[-half_window:, :][::-1, :]
    imgM = np.concatenate((top_rows, img, bottom_rows), axis=0)
    
    left_cols = imgM[:, :half_window][:, ::-1]
    right_cols = imgM[:, -half_window:][:, ::-1]
    imgM = np.concatenate((left_cols, imgM, right_cols), axis=1)
    imgT = imgM.copy()
    start_index = (half_window, half_window)
    end_index = (imgM.shape[0]-half_window,imgM.shape[1]-half_window)

    for p in np.ndindex(imgM.shape):
        if end_index[0] > p[0] >= start_index[0] and end_index[1] > p[1] >= start_index[1]:
            
            window = imgM[p[0] - half_window : p[0] + half_window + 1, p[1] - half_window : p[1] + half_window + 1]
             
            rvl = window.ravel()
            ran = round(max(rvl) - min(rvl))
            counts, bins = np.histogram(rvl, bins=ran)
            
            sum_back = np.cumsum(counts)[:-1]
            sum_obj = sum(counts)-sum_back
            mean_back = np.cumsum(bins[:-2]*counts[:-1])/sum_back
            mean_obj = (sum(bins[:-2]*counts[:-1])-np.cumsum(bins[:-2]*counts[:-1]))/sum_obj
            w0_list = sum_back/sum(counts)
            w1_list = 1 - w0_list

            #calculate background and foreground variance
            var_back_list = list()
            var_obj_list = list()
            for i in range (0,len(mean_back)):
                var_back = sum(counts[:i]*(bins[:i]-mean_back[i])**2)/sum_back[i]
                var_back_list.append(var_back)
                var_obj = sum(counts[i:]*(bins[i:-1]-mean_obj[i])**2)/sum_obj[i]
                var_obj_list.append(var_obj)
        
   
        
            wcv_list = (w0_list * var_back_list) + (w1_list * var_obj_list)
            THRESH = bins[np.argmin(wcv_list)]
            
 
            if imgM[p] < THRESH:
                imgT[p] = 0
            else:
                imgT[p] = 255

    return imgT

def local_thresholding_vek2(img, window_size):
    half_window = window_size // 2
    top_rows = img[:half_window, :][::-1, :]
    bottom_rows = img[-half_window:, :][::-1, :]
    imgM = np.concatenate((top_rows, img, bottom_rows), axis=0)
    
    left_cols = imgM[:, :half_window][:, ::-1]
    right_cols = imgM[:, -half_window:][:, ::-1]
    imgM = np.concatenate((left_cols, imgM, right_cols), axis=1)
    imgT = imgM.copy()
    start_index = (half_window, half_window)
    end_index = (imgM.shape[0]-half_window,imgM.shape[1]-half_window)

    for p in np.ndindex(imgM.shape):
        if end_index[0] > p[0] >= start_index[0] and end_index[1] > p[1] >= start_index[1]:
            
            window = imgM[p[0] - half_window : p[0] + half_window + 1, p[1] - half_window : p[1] + half_window + 1]
             
            rvl = window.ravel()
            ran = round(max(rvl) - min(rvl))
            counts, bins = np.histogram(rvl, bins=ran)
            
            sum_back = np.cumsum(counts)[:-1]
            sum_obj = sum(counts)-sum_back
            mean_back = np.cumsum(bins[:-2]*counts[:-1])/sum_back
            mean_obj = (sum(bins[:-2]*counts[:-1])-np.cumsum(bins[:-2]*counts[:-1]))/sum_obj
            w0_list = sum_back/sum(counts)
            w1_list = 1 - w0_list

            #calculate background and foreground variance
            var_back_list = list()
            var_obj_list = list()
            for i in range (0,len(mean_back)):
                var_back = sum(counts[:i]*(bins[:i]-mean_back[i])**2)/sum_back[i]
                var_back_list.append(var_back)
                var_obj = sum(counts[i:]*(bins[i:-1]-mean_obj[i])**2)/sum_obj[i]
                var_obj_list.append(var_obj)
        
   
        
            wcv_list = (w0_list * var_back_list) + (w1_list * var_obj_list)
            THRESH = bins[np.argmin(wcv_list)]
            
 
            if imgM[p] < THRESH:
                imgT[p] = 0
            else:
                imgT[p] = 65535

    return imgT