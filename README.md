# ISRO_Team25

# Stitches.py 
This file contains 3 functions that are useful for finding overlapping images and stitching them.

1. The *make_coorarr(shape,coor)* function takes an imgarray shape as first arg and a list of corner coordinates as second argument. It computes the selenographic coordinates for each pixel of the imgarray and returns it as a numpy array. 
*This function requires geographiclib library*

2. The *calc_intersect(arr,lat,lon)* function takes an imgarray and a coordinate point. It returns the pixel coordinates in the image array for the input selenographic coordinates[lat,lon]

3. The *cropimg(filename,ul,ur,ll,lr)* function returns a masked image from the input image and also takes the corner coordinates of the image as input.
*This function requires cv2 library*

# Orthographic_Plot.ipynb
This file is useful for ploting an image either NAC images or TMC2 images on the *basemap generated orthographic projection of moon*.

This file requires following libraries to be pre installed:-
(1) geographiclib
(2) basemap from mpl_toolkits

1. Above file uses function *make_coorarr()* from stitches.py to get the pixel coordinates of each pixel of image.

2. Using basemap module we are able to plot each pixel on the orthogrophic projection.

3. Using each pixel value we have ploted it based on *grayscale*. 

For instance we have provided the orthographic_tmc_plot.png 
