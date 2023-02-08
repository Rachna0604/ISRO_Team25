# ISRO_Team25

# Stitches.py 
This file contains 3 functions that are useful for finding overlapping images and stitching them.
The *make_coorarr(shape,coor)* function takes an imgarray shape as first arg and a list of corner coordinates as second argument. It computes the selenographic coordinates for each pixel of the imgarray and returns it as a numpy array. 
*This function requires geographiclib library*
The *calc_intersect(arr,lat,lon)* function takes an imgarray and a coordinate point. It returns the pixel coordinates in the image array for the input selenographic coordinates[lat,lon]
The *cropimg(filename,ul,ur,ll,lr)* function returns a masked image from the input image and also takes the corner coordinates of the image as input.
*This function requires cv2 library*
