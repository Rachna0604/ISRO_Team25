## Stiches.py
- This file contains 3 functions that are useful for finding overlapping images and stitching them.

- The make_coorarr(shape,coor) function takes an imgarray shape as first arg and a list of corner coordinates as second argument. It computes the selenographic coordinates for each pixel of the imgarray and returns it as a numpy array. This function requires geographiclib library

- The calc_intersect(arr,lat,lon) function takes an imgarray and a coordinate point. It returns the pixel coordinates in the image array for the input selenographic coordinates[lat,lon]

- The cropimg(filename,ul,ur,ll,lr) function returns a masked image from the input image and also takes the corner coordinates of the image as input. This function requires cv2 library


## Orthographic_Plot.ipynb

This file is useful for ploting an image either NAC images or TMC2 images on the basemap generated orthographic projection of moon.

This file requires following libraries to be pre installed:- 
- (1) geographiclib
- (2) basemap from mpl_toolkits

Following are the things done in this:
- Above file uses function make_coorarr() from stitches.py to get the pixel coordinates of each pixel of image.

- Using basemap module we are able to plot each pixel on the orthogrophic projection.

- Using each pixel value we have ploted it based on grayscale.

- For instance we have provided the orthographic_tmc_plot.png


1. Automator.ipynb - This is the pyautogui code for getting the coordinates of the tmc files. To run this code, open the PRADAN website in brave browser with bookmarks tab ‘ON’ and the resolution of the screen should be 2560x1600. Run the code and go to Pradan website and within 5 seconds scroll down full and full right. Now let the code do the job. The data will be saved in



2.WebScraperForNac- This is the code for getting the coordinates for NAC images. In the Reader2.txt file, paste the data after copying the result after filling the corner coordinates(West,East,South,North) on https://wms.lroc.asu.edu/lroc/search and then Select EDR and NACL and NACR. After pasting in the Reader2.txt data, run the code and let the code run. Change the value of up such that 9*up is greater than the number of NAC links.It will show an error signifying that the code has run. After that run the following cells. The coordinates will be saved in Nac_coords.csv file

3. Nacmaker.ipynb - This is the code that reads the data from the above codes and returns the NAC images which are inside a TMC image

4. Converter.py - This converts the .IMG files to .png files. Change the list according to the NAC images present