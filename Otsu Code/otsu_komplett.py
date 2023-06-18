from skimage import io
from matplotlib import pyplot as plt
import numpy as np
import matplotlib as mpl
def otsu_thresholding(img1):
    
    #Kopie des Bildes machen und glätten
    imgT = img1.copy()
    rvl = img1.ravel()
    

    #range und numerische Werte des Histogramms definieren
    ran = round(max(rvl) - min(rvl))
    counts, bins = np.histogram(rvl,bins = ran)
 
    
    
    #leere Liste für alle within class variances erstellen
    variance_list = list()

    # optimalen threshhold herausfinden
    for T in range(1,len(counts)):
        
        #within class variance herausfinden
        
        #definieren von w0 und Hintergrund Mittelwert
        sum_back = 0 
        mean_sum_back = 0
        for i in range(0,T):
            sum_back += counts[i]
            mean_sum_back += counts[i] * bins[i]

        w0 = sum_back / sum(counts)
        mean_back = mean_sum_back / sum_back


        #definieren von w1 und Vordergrund Mittelwert
        sum_obj = 0
        mean_sum_obj = 0

        for j in range(T,len(counts)):
            sum_obj += counts[j]
            mean_sum_obj += counts[j] * bins[j]

        w1 = sum_obj / sum(counts)
        mean_obj = mean_sum_obj / sum_obj

        #Varianz Hintergrund
        var_sum_back = 0
        for k in range(0, T):
            var_sum_back += counts[k] * (bins[k] - mean_back)**2 

        var_back = var_sum_back / sum_back

        #Varianz Vordergrund
        var_sum_obj = 0
        for l in range(T, len(counts)):
            var_sum_obj += counts[l] * (bins[l] - mean_obj)**2 

        var_obj = var_sum_obj / sum_obj

        # Within Class Varianz berechnen
        within_class_varianz = w0 * var_back + w1 * var_obj
        
        #within class variance zu Liste hinzufügen
        variance_list.append(within_class_varianz)
   
    #minimalen Wert für T aussuchen 
    minvar = min(variance_list)
    for m in range(0,len(variance_list)):
        if variance_list[m] == minvar: 
            THRESH = round(bins[m])

    
    #intensitätswerte anpassen
    for p in np.ndindex(imgT.shape):
        if img1[p] < THRESH:
            imgT[p] = 0
        else:
            imgT[p] = 255
    return imgT