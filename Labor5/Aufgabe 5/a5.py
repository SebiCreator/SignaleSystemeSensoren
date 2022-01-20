import redlab as rl
import matplotlib.pyplot as plt

frequenz = 6660
nyquist_frequemz = 3330
n1 = 1665
n2 = 2498
n3 = 3330
n4 = 4163
n5 = 4995
n6 = 5828
n7 = 6660
diff = 832,5

messung = rl.cbVInScan(0,0,0,1000,frequenz, 1)
plt.plot(messung)
plt.xlabel("Abtastpunkt (1000/s)")
plt.ylabel("Spannung in Volt")
plt.savefig('6660.png')
#plt.save(f"{testfrequenz}.png")