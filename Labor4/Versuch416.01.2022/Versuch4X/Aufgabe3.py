import numpy as np
import matplotlib.pyplot as plt
def conv(x):
    return x.replace(',', '.').encode()


ton = np.genfromtxt((conv(x) for x in open("Töne/ton1.csv")),
                     delimiter=';', skip_header=3, usecols=())

plt.plot(ton[5010:5096:,0], ton[5010:5096:,1], 'b')
plt.grid(True)
plt.xlabel("Zeitpunkt t in ms")
plt.ylabel("Amplitude in mV")

Signaldauer = np.abs(np.max(ton[:,0])) + np.abs(np.min(ton[:,0]))
M = len(ton[:,0])
delta_t = ton[1,0] - ton[0,0]
Signaldauer_2 = (M-1) * delta_t
Abtastfrequenz = M / Signaldauer
fft = np.fft.fft(ton[:,1])
plt.plot(range(len(fft))/(M*delta_t), np.real(fft), 'b');
plt.xlabel("Frequenz in Hz")
plt.ylabel("Amplitude")

plt.plot(range(len(fft))/(M*delta_t), np.imag(fft), 'b');
plt.xlabel("Frequenz in Hz")
plt.ylabel("Amplitude")


ck = np.max(fft)
Grundfrequenz = np.argmax(fft) / (M * delta_t)
Ak = np.real(ck + np.conjugate(ck))
ak = Ak / 2
Bk = np.real((ck - np.conjugate(ck))*1j)
bk = Bk / 2
print(f"Grundfrequenz: {Grundfrequenz}Hz")
print(f"Amplitude d. Grundfrequenz: {ck}")
print(f"Ak: {Ak}")
print(f"Bk : {Bk}")