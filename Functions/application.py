
def apply(function,input_path,result_path):
    import os
    from skimage import io
    files = os.listdir(input_path)
    for file in files:
        file_path = os.path.join(input_path,file)
        result_file_path = os.path.join(result_path,file)
        result = function(io.imread(file_path))
        io.imsave(result_file_path,result)
        
def applydice(input_path1,input_path2,dice_list):
    import os
    from skimage import io
    from dicescore import dice
    files1 = os.listdir(input_path1)
    files2 = os.listdir(input_path2)
    for o in range(len(files1)):
        file_path1 = os.path.join(input_path1,files1[o])
        file_path2 = os.path.join(input_path2,files2[o])
        d = dice(io.imread(file_path1),io.imread(file_path2))
        dice_list.append(d)
        
def applylocal(input_path,result_path,S):
    import os
    from skimage import io
    from local_thresholding_vectorized import local_thresholding_vek
    files = os.listdir(input_path)
    for file in files:
        file_path = os.path.join(input_path,file)
        result_file_path = os.path.join(result_path,file)
        result = local_thresholding_vek(io.imread(file_path),window_size=S)
        io.imsave(result_file_path,result)
        
def applylocal2(input_path,result_path,S):
    import os
    from skimage import io
    from local_thresholding_vectorized import local_thresholding_vek2
    files = os.listdir(input_path)
    for file in files:
        file_path = os.path.join(input_path,file)
        result_file_path = os.path.join(result_path,file)
        result = local_thresholding_vek2(io.imread(file_path),window_size=S)
        io.imsave(result_file_path,result)
        
def applyfilter(filter,input_path,result_path,S):
    import os
    from skimage import io
    files = os.listdir(input_path)
    for file in files:
        file_path = os.path.join(input_path,file)
        result_file_path = os.path.join(result_path,file)
        result = filter(io.imread(file_path),size = S)
        io.imsave(result_file_path,result)
        
def anwendunggauss(function,input_path,result_path,S):
    import os
    from skimage import io
    files = os.listdir(input_path)
    for file in files:
        file_path = os.path.join(input_path,file)
        result_file_path = os.path.join(result_path,file)
        result = function(io.imread(file_path),sigma = S)
        io.imsave(result_file_path,result)