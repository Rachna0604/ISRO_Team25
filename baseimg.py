import numpy as np
import cv2
import pandas as pd
import time

nac = pd.read_csv('Nac_coords.csv')
#%%
base = np.zeros((25000,25000), dtype=np.uint16)
# lats = np.linspace(-20,-21,25000)
# lons = lats
# x_1, y_1 = np.meshgrid(lats, lons)
# base[:,:,0]= x_1
# base[:,:,1]= y_1

filename =['M1108418696LE.png', 'M1155535992RE.png', 'M1317866853RE.png', 'M1387140621RE.png', 'M1108418696RE.png', 'M1175538221LE.png', 'M1322563400RE.png', 'M1422330896LE.png', 'M1129625059LE.png', 'M1243793205LE.png', 'M1336660583LE.png', 'M1422330896RE.png', 'M1131978825RE.png', 'M1247328164LE.png', 'M1336667665RE.png', 'M165978955LE.png', 'M1146112778RE.png', 'M1269660582RE.png', 'M1350761945RE.png', 'M165978955RE.png', 'M1151993612LE.png', 'M1272008542LE.png', 'M1374246998RE.png', 'M178942582RE.png', 'M1151993612RE.png', 'M1313163693LE.png', 'M1385982865RE.png', 'M1155535992LE.png', 'M1317866853LE.png', 'M1387140621LE.png']
start=time.time()
for i in range(0,2):
    parsename = filename[i]
    img = cv2.imread(parsename)
    imgarray = img[:,:,1]
    h,w = imgarray.shape
    coorarr = np.zeros((h,w,2))
    j=0
    for j in range(len(nac)):
        if nac.iloc[j,1][:-5] + 'E.png' == filename[i]:
            break
    print(time.time()-start)
    coor1 = {'ult': nac['ult'][j],
             'ulg': nac['ulg'][j],
             'urt': nac['urt'][j],
             'urg': nac['urg'][j],
             'llt': nac['llt'][j],
             'llg': nac['llg'][j],
             'lrt': nac['lrt'][j],
             'lrg': nac['lrg'][j]}
    llatitudes = np.linspace(coor1['ult'],coor1['llt'], h)
    llongitudes = np.linspace(coor1['ulg'],coor1['llg'], h)
    rlatitudes = np.linspace(coor1['urt'],coor1['lrt'], h)
    rlongitudes = np.linspace(coor1['urg'],coor1['lrg'], h)

    lcoors = list(zip(llatitudes,llongitudes))
    rcoors = list(zip(rlatitudes,rlongitudes))

    c = 0
    for l,r in zip(lcoors,rcoors):
        llat,llon = l
        rlat,rlon = r
        lats = np.linspace(llat,rlat,w)
        lons = np.linspace(llon,rlon,w)
        coors = zip(lats,lons)
        coorarr[c,:] = list(map(list,coors))
        c+=1
    print(time.time()-start)
    for k in range(h):
        for j in range(w):
            lat = coorarr[k,j,0]
            lon = coorarr[k,j,1]
            py = int(((-20) - lat) * 25000) 
            px = int(((-20) - lon) * 25000)
            if (px<25000 and px>=0) and (py<25000 and py>=0) :
                base[px,py]= imgarray[k,j]
    print(time.time()-start)

            
            

