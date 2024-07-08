# s(t)=3.cos(5.2 \pi t)+ 2.cos(13.2\pi t)

import numpy as np
import matplotlib.pyplot as plt 

M = 1000 # cant. de muestras
inicio = 0
fin = 1

Fm = M/1 # freq de muestreo
Pm = 1/Fm

# resolución por método linspace 
t = np.linspace(inicio, fin, M, endpoint=False)

s = 3*np.cos(10*np.pi*t)+2*np.cos(26*np.pi*t)

plt.figure(figsize=(16,8))
plt.plot(t,s)
plt.show()

