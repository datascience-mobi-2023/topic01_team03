import numpy as np
def multi_otsu_thresholding2(img1):
    
    #Kopie des Bildes machen und glätten
    imgT = img1.copy()
    rvl = img1.ravel()

    #range und numerische Werte des Histogramms definieren
    ran = round(max(rvl) - min(rvl))
    counts, bins = np.histogram(rvl,bins = ran)
 
    #leere Liste für alle within class variances erstellen
    variance_list = list()
    threshold_list = list()
    
    sum_counts_list = np.cumsum(counts)
    mean_sum_list = np.cumsum(counts*bins[:-1])
    w0_list = sum_counts_list/sum(counts)
    mean_back_list = mean_sum_list/sum_counts_list
    print(len(counts))
    
    
    for T in range(1,len(counts)-1):
        var_back = sum(counts[:T]*(bins[:T]-mean_back_list[T])**2)/sum_counts_list[T]
        w0 = w0_list[T]
        
        for T2 in range(T+1,len(counts)):
        
            sum_mid = sum_counts_list[T2]-sum_counts_list[T]
            mean_sum_mid = mean_sum_list[T2]-mean_sum_list[T]
            
            w1 = sum_mid / sum(counts)
            mean_mid = mean_sum_mid / sum_mid
            
            sum_obj = sum_counts_list[len(counts)-1]-sum_counts_list[T2]
            mean_sum_obj = mean_sum_list[len(counts)-1]-mean_sum_list[T]

            w2 = sum_obj / sum(counts)
            mean_obj = mean_sum_obj / sum_obj

            
            
            #Varianz Mitte
            var_sum_mid = 0
            
            for m in range(T,T2):
                var_sum_mid += counts[m] * (bins[m] - mean_mid)**2 
            var_mid = var_sum_mid / sum_mid
            
            
            #Varianz Vordergrund
            var_sum_obj = 0
            for n in range(T2, len(counts)):
                var_sum_obj += counts[n] * (bins[n] - mean_obj)**2 
            var_obj = var_sum_obj / sum_obj

            # Within Class Varianz berechnen
            
            within_class_varianz = w0 * var_back + w1 * var_mid + w2 * var_obj
        
            #within class variance zu Liste hinzufügen
            
            variance_list.append(within_class_varianz)
            
            #thresholds zur Liste hinzufügen
            
            threshold_list.append((T,T2))
    
    #minimalen Wert für T aussuchen 
    
    thresh1, thresh2 = threshold_list[np.argmin(variance_list)]
    
    
    #intensitätswerte anpassen
    for p in np.ndindex(imgT.shape):
        if img1[p] < thresh1:
            imgT[p] = 0
        elif img1[p] < thresh2:
            imgT[p] = 65535
        else:
            imgT[p] = 0
    return imgT