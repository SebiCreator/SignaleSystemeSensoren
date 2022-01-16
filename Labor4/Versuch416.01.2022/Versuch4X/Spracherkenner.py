import numpy as np
import scipy.signal as sgl
import scipy.stats as scsts

def zerteilen(array):
    gauss_fenster = np.array(sgl.gaussian(512, 512 / 4))
    for i in range(0, len(array) - 512 + 1, 256):
        yield np.concatenate([[0] * i, list(gauss_fenster * array[i:i + 512]), [0] * (len(array) - (i + 512))])

def windowing_func(array):
    fenster = np.array(list(zerteilen(array)))
    return np.fft.fft(fenster).mean(0)


path2 = "results/"
ending = "Result.npy"


Spektrum_tief = np.load(path2 + "Tief" + ending)
Spektrum_hoch = np.load(path2 + "Hoch" + ending )
Spektrum_rechts = np.load(path2 + "Rechts" + ending)
Spektrum_links = np.load(path2 + "Links" + ending )

Ergebnisse = ""
Zuweisung = ["Hoch" , "Tief", "Rechts", "Links"]


def spracherkenner(path):
    Spektrum_tief = np.load(path2 + "Tief" + ending)
    Spektrum_hoch = np.load(path2 + "Hoch" + ending )
    Spektrum_rechts = np.load(path2 + "Rechts" + ending)
    Spektrum_links = np.load(path2 + "Links" + ending )
    print("____________________________________________________________")
    print("Spracherkenner Datei: %s\n" % path)

    # Hier die File einfügen
    data = np.load(path)
    data2 = np.abs(windowing_func(data))
    Korrelationen = []

    Korrelationen.append(scsts.pearsonr(Spektrum_hoch, data2)[0])
    Korrelationen.append(scsts.pearsonr(Spektrum_tief, data2)[0])
    Korrelationen.append(scsts.pearsonr(Spektrum_rechts, data2)[0])
    Korrelationen.append(scsts.pearsonr(Spektrum_links, data2)[0])
    
    for i in range (4):
        print(Zuweisung[i]  + " : " + str(Korrelationen[i]))

    current = 0 
    for i in range (4):
        if Korrelationen[i] > current:
            current = Korrelationen[i] 
            Ergebnisse = Zuweisung[i]
            

    print("Erkanntes Wort: " + Ergebnisse)
    print("____________________________________________________________")
    return Ergebnisse


#sprach_erkenner("Testdatensatz/trigger/HochL1.npy")
spracherkenner("audiodateien/trigger/RechtsL5.npy")

p1 = "audiodateien/trigger/"
p2 = "Testdatensatz/trigger/"
a = []
a.append("Hoch")
a.append("Tief")
a.append("Rechts")
a.append("Links")

counterright = 0

for i in range(4):
    for j in range (5):
        t = spracherkenner(p2 + a[i] + "L" + str(j + 1 ) + ".npy")
        if t == a[i]:
           counterright = counterright + 1
           
print("Von 20 EIngeben sind" + str(counterright) + " richtig" )  
print("in Prozent : " + str(counterright / 20) )        
        

    
    