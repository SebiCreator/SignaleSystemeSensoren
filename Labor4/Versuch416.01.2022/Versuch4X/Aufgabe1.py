import numpy as np
import pyaudio
import scipy.signal as sgl
import math

import matplotlib.pyplot as plt

def zerteilen(array):
    gauss_fenster = np.array(sgl.gaussian(512, 512 / 4))
    for i in range(0, len(array) - 512 + 1, 256):
        yield np.concatenate([[0] * i, list(gauss_fenster * array[i:i + 512]), [0] * (len(array) - (i + 512))])

def windowing_func(array):
    fenster = np.array(list(zerteilen(array)))
    return np.fft.fft(fenster).mean(0)


path = "Testdatensatz/trigger/"
filename = "test123"
ending = ".npy"
file = path + filename + ending
data = np.load(file)
fig2, ax2 = plt.subplots()
ax2.plot(data)

data_trans = windowing_func(data)

fouriertransformierte = np.fft.fft(data)

zeit = 1 #1 Sekunde




print("fft :" +   str(np.max(fouriertransformierte)))

frequencys = []
for i in range(len(fouriertransformierte)):
    frequencys.append(i / zeit)


fig2, ax2 = plt.subplots()
ax2.plot(frequencys, np.abs(data_trans))
ax2.set_xlabel('Frequenz (Hz)')
ax2.set_ylabel('Amplitude')
ax2.set_title("Amplitudenspektrum " + file)
plt.show()
