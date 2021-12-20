import cv2
import numpy as np


output = 0 # printen ?
path = r'p/graustufe2.png' # graustufenbild

grauskalabild = cv2.imread(path, cv2.COLOR_BGR2GRAY)

grauskalabild = grauskalabild[50:, :]

#-----------------------------------------------------------------------------
#unterbilder 
#Unterbild1
unterbild1 = grauskalabild[10:430,0:50] # abschnitte definieren

cv2.imwrite('p/unterbilder/unterbild1.png', unterbild1) # bild speichern
print(np.mean(unterbild1), np.std(unterbild1))

#Unterbild2
unterbild2 = grauskalabild[10:430,100:150]

cv2.imwrite('p/unterbilder/unterbild2.png', unterbild2)
print(np.mean(unterbild2), np.std(unterbild2))
#Unterbild3
unterbild3 = grauskalabild[10:430,250:300]

cv2.imwrite('p/unterbilder/unterbild3.png', unterbild3)
print(np.mean(unterbild3), np.std(unterbild3))
#Unterbild4
unterbild4 = grauskalabild[10:430,420:470]

cv2.imwrite('p/unterbilder/unterbild4.png', unterbild4)
print(np.mean(unterbild4), np.std(unterbild4))
#Unterbild5
unterbild5 = grauskalabild[10:430,570:620]

cv2.imwrite('p/unterbilder/unterbild5.png', unterbild5)
print(np.mean(unterbild5), np.std(unterbild5))
#-----------------------------------------------------------------------------

# falls erwünscht ouput auf 1 um die graustufen zu printen
if (output == 1):
   cv2.imshow('test',unterbild1) 
   cv2.imshow('test2',unterbild2)
   cv2.imshow('test3',unterbild3)
   cv2.imshow('test4',unterbild4)
   cv2.imshow('test5',unterbild5)
    
cv2.waitKey(0)

#-----------------------------------------------------------------------------
# einlesen der dunkelbilder    
dunkelbilder = np.zeros((10, 430, 640,))
for i in range(1, 10):
    pic = cv2.imread("P/dunkelbilder/dunkelbild%i.png" % (i), cv2.COLOR_BGR2GRAY)
    dunkelbilder[i] = pic[50:,:]
dunkelbild = np.mean(dunkelbilder, axis=0)
#print(dunkelbild)
cv2.imwrite("p/ergebnisse/meandunkelbild.png", dunkelbild)
#-----------------------------------------------------------------------------
dunkelbildkontrastmaximiert = cv2.equalizeHist(dunkelbild.astype('uint8')) # dunkelbild kontrastmaximieren
cv2.imwrite("p/ergebnisse/dunkelbildkontrast.png", dunkelbildkontrastmaximiert)  # das kontrastmaximierte dunkelbild speichern
#-----------------------------------------------------------------------------
#weissbilder einlesen
weissbilder = np.empty((10, 430, 640))
for i in range(1, 10):
    weissbild = cv2.imread("p/weissbilder/weisbild%i.png" % (i), cv2.COLOR_BGR2GRAY)
    weissbilder[i] = weissbild[50:,:,1]
    
#-----------------------------------------------------------------------------
weissbild = np.mean(weissbilder, axis=0) # Mittelwert des weissbilds berechnen
cv2.imwrite("p/ergebnisse/meanweissbild.png", weissbild) # Das berechnete bild speichern
weissbildkontrastmaximiert = cv2.equalizeHist(weissbild.astype('uint8')) # weisbild kontrastmaximieren
cv2.imwrite("P/ergebnisse/weissbildkontrast.png", weissbildkontrastmaximiert)
#-----------------------------------------------------------------------------
#weissbild mittel
weisbild = np.mean(weissbild, axis = 0)
## Weissbild - Dunkelbild
subweissbild = weissbild - dunkelbild
cv2.imwrite("p/ergebnisse/subweissbild.png", subweissbild)
#-----------------------------------------------------------------------------
#weissbild norm
weissbildnorm = weissbild / np.mean(weissbild)
#-----------------------------------------------------------------------------
## Grauswertkeil - dunkelbild
grauskalaK = (grauskalabild[:,:,1] - dunkelbildkontrastmaximiert[:,:])
cv2.imwrite("p/ergebnisse/grauskalaK.png", grauskalaK)

## subgrauskalabild / weissbildnorm
korregiert = grauskalaK / weissbildnorm
cv2.imwrite("p/ergebnisse/korregiert.png", korregiert)
#-----------------------------------------------------------------------------
# werte von oben korregieren
print("Korrergierte Wertet")
unterbild1 = korregiert[10:430,0:50] # abschnitte definieren
print(np.mean(unterbild1), np.std(unterbild1))
#Unterbild2
unterbild2 = korregiert[10:430,100:150]
print(np.mean(unterbild2), np.std(unterbild2))
#Unterbild3
unterbild3 = korregiert[10:430,250:300]
print(np.mean(unterbild3), np.std(unterbild3))
#Unterbild4
unterbild4 = korregiert[10:430,420:470]
print(np.mean(unterbild4), np.std(unterbild4))
#Unterbild5
unterbild5 = korregiert[10:430,570:620]
print(np.mean(unterbild5), np.std(unterbild5))
#-----------------------------------------------------------------------------
## Positionen der dead/stuckpixel in Koordinaten
deadpixel = np.argwhere(weissbildkontrastmaximiert[:, :] == 0)
stuckpixel = np.argwhere(dunkelbildkontrastmaximiert[:, :] == 255)
#-----------------------------------------------------------------------------

stuckpixelbild = cv2.cvtColor(grauskalabild, cv2.COLOR_BGR2GRAY)

# cv2 drawfunktion die die pixel aufmalt
for (x, y) in stuckpixel:
    stuckpixelbild = cv2.circle(img=stuckpixelbild, center=(y, x), radius=1, color=(255, 0, 0))

cv2.imwrite("p/ergebnisse/stuckpixelbild.png", stuckpixelbild)

# cv2 drawfunktion die die pixel aufmalt
deadpixelbild = cv2.cvtColor(grauskalabild, cv2.COLOR_BGR2GRAY)
for (x, y) in deadpixel:
    deadpixelbild = cv2.circle(img=deadpixelbild , center=(y, x), radius=1, color=(0, 0, 255))
cv2.imwrite("p/ergebnisse/deadpixelbild.png", deadpixelbild)


    


    
