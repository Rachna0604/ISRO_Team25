import cv2 
import numpy as np
from geographiclib.geodesic import Geodesic
import matplotlib.pyplot as plt


def make_coorarr(shape,coor):
    '''Creates a coordinate list[Lat,Lon] corrosponding to each pixel of the passed image array.
    Given the corner coordinates of the image passed in z format as a list'''
    h,w = shape
    
    coor1 = {'ult': coor[0],
             'ulg': coor[1],
             'urt': coor[2],
             'urg': coor[3],
             'llt': coor[4],
             'llg': coor[5],
             'lrt': coor[6],
             'lrg': coor[7]}

    coorarr = np.zeros((h,w,2))
    coorarr[0,0,0] = coor1['ult']
    coorarr[0,0,1] = coor1['ulg']
    coorarr[0,-1,0] = coor1['urt']
    coorarr[0,-1,1] = coor1['urg']
    coorarr[-1,0,0] = coor1['llt']
    coorarr[-1,0,1] = coor1['llg']
    coorarr[-1,-1,0] = coor1['lrt']
    coorarr[-1,-1,1] = coor1['lrg']
    
    l = Geodesic.WGS84.InverseLine(coor1['ult'],coor1['ulg'],coor1['urt'],coor1['urg'])
    r = Geodesic.WGS84.InverseLine(coor1['llt'],coor1['llg'],coor1['lrt'],coor1['lrg'])
    
    for i in range(1,w-1,4):
        m1 = l.Position((i/(w-1))*l.s13)
        coorarr[0,i,0]= m1['lat2']
        coorarr[0,i,1]= m1['lon2']
        m2 = r.Position((i/(w-1))*r.s13)
        coorarr[-1,i,0]= m2['lat2']
        coorarr[-1,i,1]= m2['lon2']
        
    for i in range(1,w,4):
        if i%5==0:
            print(f"Ending stage {i}")
        l = Geodesic.WGS84.InverseLine(coorarr[0,i,0],coorarr[0,i,1],coorarr[-1,i,0],coorarr[-1,i,1])
        for j in range(1,h-1):
            m1 = l.Position((j/(h-1))*l.s13)
            coorarr[j,i,0]= m1['lat2']
            coorarr[j,i,1]= m1['lon2']
        
    l1 = np.arange(0,w,1)
    l2 = np.arange(1,w,4)
    np.append([0],l2)
    emp = []
    for i in l1:
        if i not in l2:
            emp.append(i)

    for i in range(0,h):
        coorarr[i,emp,0] = np.interp(emp,l2,coorarr[i,l2,0])
        coorarr[i,emp,1] = np.interp(emp,l2,coorarr[i,l2,1])
        
    return coorarr 

def calc_intersect(arr,ult,ulg):
    '''Calculates the pixel coordinate in the image array
    from the given selenographic coordinates[ult,ulg]'''
    r,co,u=arr.shape
    q,p= (-1,-1)
    minm=99999
    for i in range(0,r):
        for j in range(0,co):
            c=arr[i,j,:]
            e=((c[0]-ult)**2+(c[1]-ulg)**2)*(1/2)
            if(e<minm):
                q=i
                p=j
                minm = e
    return [q,p]
    
def cropimg(filename, ul,ur,ll,lr):
    '''creates a mask of an image  given 4 corner pixel coordinates[ul,ur,ll,lr]'''
    photo = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    plt.figure(figsize=(15,15))
    p4=cv2.cvtColor(photo,cv2.COLOR_BGR2RGB)
    
    minh = min(ul[0],ur[0],ll[0],lr[0])
    maxh = max(ul[0],ur[0],ll[0],lr[0])
    minw = min(ul[1],ur[1],ll[1],lr[1])
    maxw = max(ul[1],ur[1],ll[1],lr[1])
    
    ul = [ul[1]-minw, ul[0]-minh]
    ur = [ur[1]-minw,ur[0]-minh]
    ll = [ll[1]-minw,ll[0]-minh]
    lr = [lr[1]-minw,lr[0]-minh]
    print('generated crop')
    mask = np.zeros(((maxh-minh),(maxw-minw)),dtype=np.uint8)
    pts = np.array([ul,ur,lr,ll], np.int32).reshape(-1,1,2)
    finalpts = cv2.fillPoly(mask,[pts],255)
    plt.imshow(cv2.fillPoly(mask,[pts],255), cmap='gray')
    plt.show()
    p3 = p4[minh:maxh,minw:maxw,:]
    # compute the bitwise AND using the mask
    masked_img = cv2.bitwise_and(p3,p3,mask = finalpts)
    plt.figure(figsize=(15,15))
    plt.imshow(masked_img)
    return masked_img