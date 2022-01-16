
import scipy.stats as scsts
import numpy as np
import math
path = "results/"
filename = "Hoch"
ending = "Result.npy"


Spektrum = []
Spektrum.append(np.load(path + "Tief" + ending))
Spektrum.append(np.load(path + "Hoch" + ending ))
Spektrum.append(np.load(path + "Rechts" + ending))
Spektrum.append(np.load(path + "links" + ending ))
            



for i in range(4):
    for j in range(4):
        print(str(i) + "" + str(j)  + " ", scsts.pearsonr(Spektrum[j], Spektrum[i])[0])
        
 
        
 
def korr(a, b):
             print( " Korrelation", scsts.pearsonr(np.load(a), np.load(b))[0])
            
            
        

def average(x):
    assert len(x) > 0
    return float(sum(x)) / len(x)

def pearson_def(x, y):
    assert len(x) == len(y)
    n = len(x)
    assert n > 0
    avg_x = average(x)
    avg_y = average(y)
    diffprod = 0
    xdiff2 = 0
    ydiff2 = 0
    for idx in range(n):
        xdiff = x[idx] - avg_x
        ydiff = y[idx] - avg_y
        diffprod += xdiff * ydiff
        xdiff2 += xdiff * xdiff
        ydiff2 += ydiff * ydiff

    return diffprod / math.sqrt(xdiff2 * ydiff2)             

korr("results/HochResult.npy","results/TiefResult.npy" )    