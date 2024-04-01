import numpy as np
import matplotlib.pyplot as plt

edad_luna = 22 # variable normal

                    #  0   1  2  3
edad_grupo = np.array([12,22,23,65]) # array -> vector

print("Edad luna: " + str(edad_luna))

print("Edades del grupo: " + str(edad_grupo))

print("Cantidad de gente en el grupo: " + str(len(edad_grupo)))

# valor = indice - 1 
print("Edad persona 2: " + str( edad_grupo[1] ))
print(np.amin(edad_grupo))

x = np.arange(0,20,2)
print(x)

xp = np.linspace(0,20,12)
print(xp)

# print(x+xp)

zeros = np.ones(12)
print(zeros)

plt.plot(xp)