import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import argrelmin
ResF = []
ResF2 = []
B1 = []
B2 = []
B = [0.11, 0.24, 0.16, 0.20, 0.38, 0.25, 0.29, 0.45, 0.38, 0.58, 0.47, 0.71, 0.55, 0.83, 0.64, 0.96, 0.73, 1.09, 0.82, 1.21, 1.22]
for i in range(2,23):
    df = pd.read_csv("NewFile" + str(i) + ".csv", delimiter=',')
    Int = df['CH1'].tolist()
    Intensity = np.array(Int)
    if i < 4:
        x = np.linspace(1, 2, len(Intensity))
    elif i > 3 and i < 7:
        x = np.linspace(2, 3, len(Intensity))
    elif i<20: 
        x = np.linspace(np.floor((i-2)/2.0), np.floor((i-2)/2.0)+1, len(Intensity))
    else:
        x = np.linspace(9, 10, len(Intensity))
    mini = np.argmin(Intensity)
    #plt.vlines(x[mini], min(Intensity), max(Intensity))
    #plt.plot(x,Intensity, color= 'red', label='Vergleichsspektrum')
    #plt.legend(loc='upper right')
    #plt.title("Spectrum number " + str(i))
    #plt.show()
    if i % 2:
        ResF.append(x[mini])
        B1.append(B[i-2])
    else:
        ResF2.append(x[mini])
        B2.append(B[i-2])


a = 23
B = [0.11, 0.24, 0.16, 0.20, 0.38, 0.25, 0.29, 0.45, 0.38, 0.58, 0.47, 0.71, 0.55, 0.83, 0.64, 0.96, 0.73, 1.09, 0.82, 1.21]
ResF = [1.060884070058382,2.084236864053378, 3.5562969140950793, 4.537114261884904, 5.52627189324437, 6.472060050041701, 7.546288573811509, 8.490408673894912, 9.432860717264386]
ResF2 = [1.4678899082568808, 2.939949958298582,2.5287739783152627, 2.939115929941618, 3.537948290241868, 4.531276063386155, 5.510425354462051, 6.497080900750626, 7.482902418682235, 8.492910758965804, 9.50208507089241]
B1 = [0.24,0.38, 0.45, 0.58, 0.71, 0.83, 0.96, 1.09, 1.21]
B2 = [ 0.11, 0.16,0.2, 0.25, 0.29, 0.38, 0.47, 0.55, 0.64, 0.73, 0.82]
coef = np.polyfit(B1, ResF,1)
plt.scatter(B1, ResF, marker = 'o')
plt.plot(B1, np.poly1d(coef)(B1))
coef = np.polyfit(B2, ResF2,1)
plt.plot(B2, np.poly1d(coef)(B2))
plt.scatter(B2, ResF2, marker = 'o')
plt.xlabel('Magnetfeldstärke')
plt.ylabel('Resonanfrequenz')
plt.show()
print(ResF)

print(ResF2)

print(B1)
print(B2)