## Report Topic01 - Team 03:  
# **The implementation and evaluation of Otsu thresholding**
### Data Analysis project, B.Sc.Molekulare Biotechnologie

#### **Supervisor:** PD Dr. Karl Rohr

#### **Team:** *Franka Begall, Kira Effenhauser, Selina Geiger, Anna-Lena Schulz*

#### **Tutor:** *Hannah Winter*

## Abstract
Image segmentation plays a role in many fields of research such as medicine and biology. One of the most effective ways to perform image segmentation is thresholding, in particular Otsu thresholding. This report mainly focuses on the optimization of Otsu thresholding using different preprocessing methods such as the mean, median and Gaussian filter, as well as histogram stretching. Additionally, Otsu thresholding was compared to more sophisticated versions like two-level-Otsu thresholding and local adaptive thresholding. All algorithms were applied to three different datasets displaying images of cell nuclei (N2DH-GOWT1, N2DL-HeLa, NIH3T3) and evaluated by using the Dice Score. Each dataset challenged and therefore tested the algorithm in a different way. As a result this report presents that Otsu thresholding is a reliable and fast method of image segmentation. 

## Description of the Datasets
For this project the data consists of three different, publicly available datasets, each showing cell nuclei. All of the datasets consist of the original images, as well as the ground truth images, which can be used to evaluate the implemented segmentation algorithm. 
### 2.1. N2DH-GOWT1
The first set of data contains six images of N2DH-GOWT1 mouse embryonic stem cells, which were stained by using a green flourescent protein targeted against the transcription facor Oct4. These images were captured using timelapse confocal microscopy and have a size of 1024x1024 pixels. The low contrast to the background and image noise are the main challlenges this datasets presents.
### 2.2. N2DL-HeLa
Dataset 2 contains four images of human N2DL-HeLa cells of cervical cancer with a size of 1100x700 pixels. The staining of these nuclei was also executed by using a green fluorescent protein, but targeted against H2b. The images were captured by an Olympus lx81 microscope used for live imaging of fluorescently labeled chromosomes. The main challenge this dataset presents is the low contrast.
### 2.3. NIH3T3
The last dataset consists of 18 images of mouse embryonic fibroblast cells which were visualized via Hoechst staining and captured with a fluorescence microscope. The size of these images is 1344x1024 pixels. A challenge this dataset embodies is the varying brigntness of the cell nuclei, as well as reflections, appearing as bright spots in the images.

## Folder structure

1. [Applications]()