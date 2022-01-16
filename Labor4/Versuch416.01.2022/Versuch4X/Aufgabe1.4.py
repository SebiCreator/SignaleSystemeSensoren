import numpy as np
import scipy.signal as sgl
import matplotlib.pyplot as plt

def zerteilen(array):
    gauss_fenster = np.array(sgl.gaussian(512, 512 / 4))
    for i in range(0, len(array) - 512 + 1, 256):
        yield np.concatenate([[0] * i, list(gauss_fenster * array[i:i + 512]), [0] * (len(array) - (i + 512))])

def windowing_func(array):
    fenster = np.array(list(zerteilen(array)))
    return np.fft.fft(fenster).mean(0)

#Versuch 2 a)



def spectren(name):
    what = name
    path = "audiodateien/trigger/"
    filename = what + "L"

    ending = ".npy"
    file = path + filename

    filenameS = what +"Result"
    filepathS = "results/" + filenameS

    alle_spektren = []
    for i in range(5):
        data = np.load(file + str(i + 1) + ending)
        print(file + str(i + 1) + ending)
        alle_spektren.append(windowing_func(data))

    Spektrum_Result = np.mean(alle_spektren, 0)


    np.save(filepathS, np.real(Spektrum_Result))
    
    fouriertransformierte = np.fft.fft(Spektrum_Result)
    aufnehmsekunden = 1 #1 Sekunde

    frequencys = []
    for i in range(len(fouriertransformierte)):
        frequencys.append(i / aufnehmsekunden)

    fig2, ax2 = plt.subplots()
    ax2.plot(frequencys[:5000], np.abs(Spektrum_Result[:5000]))
    ax2.set_xlabel('Frequenz (Hz)')
    ax2.set_ylabel('Amplitude')
    ax2.set_title("Amplitudenspektrum " + filenameS)
    plt.show()

spectren("Hoch")
spectren("Tief") 
spectren("Rechts") 
spectren("Links")     