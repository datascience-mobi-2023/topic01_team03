import os
from skimage import io
from dicescore import dice
from local_thresholding_vectorized import local_thresholding_vek
from local_thresholding_vectorized import local_thresholding_vek2
def apply(function,input_path,result_path):
    """
    This function applies a function to a whole folder of images and stores the results in a different folder. It iterates 
    over all images in the folder and for each image creates a path to the input image and the result image. It then applies 
    the function on the input image and stores the result in the result folder. 
    Note: only works if the image is the only argument required for the function.

    Args:
        function (callable): The function to be applied to each image
        input_path (str): The path to the folder containing the input images
        result_path (str): The path to the folder where the results will be saved
    """
    #create a list of all images in the folder
    images = os.listdir(input_path)
    
    #iterate over all images in the folder
    for image in images:
        
        #create the path to the specific image
        file_path = os.path.join(input_path,image)
        
        #create the path to the result image
        result_file_path = os.path.join(result_path,image)
        
        #apply the function to the image
        result = function(io.imread(file_path))
        
        #save the result in the result folder
        io.imsave(result_file_path,result)
        
def applydice(input_path1,input_path2,dice_list):
    """
    This function applies the function "dice" to two folders of images and stores the results in a list. It iterates over 
    all images in the two folders and for each pair of images the dice score is computed. The results are stored in the given list.

    Args:
        input_path1 (str): The path to the first folder containing images.
        input_path2 (str): The path to the second folder containing images.
        dice_list (list): The list to store the dice scores.
    """
    
    #create lists of the images in both input folders
    images1 = os.listdir(input_path1)
    images2 = os.listdir(input_path2)
    
    #iterate over the files in the folders
    for o in range(len(images1)):
        
        #create the file paths for the corresponding images in both folders
        file_path1 = os.path.join(input_path1,images1[o])
        file_path2 = os.path.join(input_path2,images2[o])
        
        #calculate the dice score for the pair of images and append it to the list
        d = dice(io.imread(file_path1),io.imread(file_path2))
        dice_list.append(d)
        
def applylocal(input_path,result_path,S):
    """
    This function applies local thresholding (setting intensity values to 0 and 255) for a given window size S to a whole 
    folder of images and stores the results in a different folder. It iterates over all images in the folder and for each 
    image creates a path to the input image and the result image. It then applies local thresholding on the input image and 
    stores the result in the result folder. 
    
    Args:
        input_path (str): The path to the folder containing the input images
        result_path (str): The path to the folder where the results will be saved
        S (int): window size for the local thresholding algorithm
    """
    
    #create a list of all images in the folder
    images = os.listdir(input_path)
    
    #iterate over all images in the folder
    for image in images:
        
        #create the path to the specific image
        file_path = os.path.join(input_path,image)
        
        #create the path to the result image
        result_file_path = os.path.join(result_path,image)
        
        #apply local thresholding with the given window size to the image
        result = local_thresholding_vek(io.imread(file_path),window_size=S)
        
        #save the result in the result folder
        io.imsave(result_file_path,result)
        
def applylocal2(input_path,result_path,S):
    """
    This function applies local thresholding (setting intensity values to 0 and 65535) for a given window size S to a whole 
    folder of images and stores the results in a different folder. It iterates over all images in the folder and for each 
    image creates a path to the input image and the result image. It then applies local thresholding on the input image and 
    stores the result in the result folder. 

    Args:
        input_path (str): The path to the folder containing the input images
        result_path (str): The path to the folder where the results will be saved
        S (int): window size for the local thresholding algorithm
    """
    
    #create a list of all images in the folder
    images = os.listdir(input_path)
    
    #iterate over all images in the folder
    for image in images:
        
        #create the path to the specific image
        file_path = os.path.join(input_path,image)
        
        #create the path to the result image
        result_file_path = os.path.join(result_path,image)
        
        #apply local thresholding with the given window size to the image
        result = local_thresholding_vek2(io.imread(file_path),window_size=S)
        
        #save the result in the result folder
        io.imsave(result_file_path,result)
        
def applyfilter(filter,input_path,result_path,S):
    """
    This function applies a filter for a given size of the filter mask S to a whole folder of images and stores the results in 
    a different folder. It iterates over all images in the folder and for each image creates a path to the input image and the 
    result image. It then applies the filter on the input image and stores the result in the result folder. 

    Args:
        filter (callable): The filter to be applied to each image
        input_path (str): The path to the folder containing the input images
        result_path (str): The path to the folder where the results will be saved
        S (int): size of the filter mask
    """
    
    #create a list of all images in the folder
    images = os.listdir(input_path)
    
    #iterate over all images in the folder
    for image in images:
        
        #create the path to the specific image
        file_path = os.path.join(input_path,image)
        
        #create the path to the result image
        result_file_path = os.path.join(result_path,image)
        
        #apply the filter to the image with the given filter size
        result = filter(io.imread(file_path),size = S)
        
        #save the result in the result folder
        io.imsave(result_file_path,result)
        
def applygauss(filter,input_path,result_path,S):
    """
    This function applies the gaussian filter for a given sigma value S to a whole folder of images and stores the results in 
    a different folder. It iterates over all images in the folder and for each image creates a path to the input image and the 
    result image. It then applies the filter on the input image and stores the result in the result folder.

    Args:
        filter (callable): The filter to be applied to each image (gaussian filter)
        input_path (str): The path to the folder containing the input images
        result_path (str): The path to the folder where the results will be saved
        S (int): sigma value
    """
    
    #create a list of all images in the folder
    images = os.listdir(input_path)
    
    #iterate over all images in the folder
    for image in images:
        
        #create the path to the specific image
        file_path = os.path.join(input_path,image)
        
        #create the path to the result image
        result_file_path = os.path.join(result_path,image)
        
        #apply the filter to the image with the given sigma value
        result = filter(io.imread(file_path),sigma = S)
        
        #save the result in the result folder
        io.imsave(result_file_path,result)