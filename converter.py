s={'M1422330896LE.IMG', 'M1108418696RE.IMG', 'M1374246998RE.IMG', 'M1387140621LE.IMG', 'M165978955LE.IMG', 'M1269660582RE.IMG', 'M1394179616RE.IMG', 'M1129625059LE.IMG', 'M1155535992RE.IMG', 'M1394179616LE.IMG', 'M1151993612RE.IMG', 'M1317866853LE.IMG', 'M1151993612LE.IMG', 'M1336660583LE.IMG', 'M1317866853RE.IMG', 'M1108418696LE.IMG', 'M1350761945RE.IMG', 'M1243793205LE.IMG', 'M178942582RE.IMG', 'M1322563400RE.IMG', 'M1129625059RE.IMG', 'M1175538221LE.IMG', 'M1155535992LE.IMG', 'M1385982865RE.IMG', 'M1272008542LE.IMG', 'M1422330896RE.IMG', 'M1402413883RE.IMG', 'M1336667665RE.IMG', 'M1131978825RE.IMG', 'M1146112778LE.IMG', 'M1146112778RE.IMG', 'M1313163693LE.IMG', 'M1374246998LE.IMG', 'M1247328164LE.IMG', 'M1243786180RE.IMG', 'M165978955RE.IMG', 'M1387140621RE.IMG'}
print(len(s))
import subprocess
import cv2
from planetaryimage import PDS3Image
for i in s:

    image = PDS3Image.open(i)
    cv2.imwrite('/wd/users/b21082/nac_png/'+i[:-4]+'.png',image.image)