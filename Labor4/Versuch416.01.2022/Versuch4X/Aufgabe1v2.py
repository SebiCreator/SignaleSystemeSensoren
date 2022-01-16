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

#Aufgabe1 c)
path = "audiodateien/trigger/"
filename = "HochL1"
ending = ".npy"
file = path + filename + ending
data = np.load(file)
fig2, ax2 = plt.subplots()
ax2.plot(data)

data_trans = windowing_func(data)

fouriertransformierte = np.fft.fft(data)
spektrum = np.abs(data_trans)
aufnehmsekunden = 1 #1 Sekunde

freq = np.zeros(44100) 
for i in range(len(fouriertransformierte)):               #Fill Frequenz Array (for y Axis)
    freq[i] = (i / aufnehmsekunden)




frequencys = []
for i in range(len(fouriertransformierte)):
    frequencys.append(i / aufnehmsekunden)


fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(data)
ax2.plot(freq, spektrum)

ax1.set_ylabel("Amplitude in mV")
ax1.set_xlabel("Zeit")
ax1.set_title("Amplitudenspektrum")
ax2.set_ylabel("Amplitude")
ax2.set_xlabel("Frequenz in Hz")