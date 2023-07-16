from skimage import io
import os
def anwendung(function,input_path,result_path):
    files = os.listdir(input_path)
    for file in files:
        file_path = os.path.join(input_path,file)
        result_file_path = os.path.join(result_path,file)
        result = function(io.imread(file_path))
        io.imsave(result_file_path,result)