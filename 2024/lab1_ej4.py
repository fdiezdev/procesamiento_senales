# Digitalice y grafique la señal
# $x(t)=5*sen(6 \pi t)$ con 1000 muestras en el intervalo $[0,1)$

import matplotlib.pyplot as plt
import numpy as np 

M = 1000 # cant. de muestras
inicio = 0
fin = 1

Fm = M/1 # freq de muestreo
Pm = 1/Fm

# resolución por método linspace 
t = np.linspace(inicio, fin, M, endpoint=False)

# resolución por método arange
#t = np.arange(inicio, fin, Pm)

# definimos la función seno
x = 5 * np.sin(6*np.pi*t)

# graficamos la función
# plt.figure(figsize=(16,8))
# plt.stem(t,x)
# plt.show()


# cuántas veces oscila la función en un segundo? 
# rta -> frecuencia de muestreo
print("Freq. de muestreo: ", Fm)