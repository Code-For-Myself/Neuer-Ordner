import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import argrelmin


df = pd.read_csv("NewFile2.csv", delimiter=',')
Int = df['CH1'].tolist()
Intensity = np.array(Int)
    #if i < 4:
x = np.linspace(1, 2, len(Intensity))
    #elif i > 3 and i < 7:
    #    x = np.linspace(2, 3, len(Intensity))
    #else: 
    #    x = x = np.linspace(np.floor((i-2)/2.0), np.floor((i-2)/2.0)+1, len(Intensity))
mini = np.argmin(Intensity)
plt.vlines(x[mini], min(Intensity), max(Intensity))
plt.plot(x,Intensity, color= 'red', label='Vergleichsspektrum')
plt.legend(loc='upper right')
plt.show()
print("Frequency is: " +  str(x[mini]))
