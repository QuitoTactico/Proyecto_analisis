"""
Supongamos que alguien de M  ́unich (Alemania) planea unas
vacaciones en Bangkok (Tailandia) durante el mes de diciembre
y quiere obtener informaci  ́on sobre el clima para preparar su
viaje. Supongamos que las temperaturas m  ́aximas diurnas (en
grados Celsius) del a  ̃no pasado para el per ́ıodo del 1 al 31 de
diciembre fueron las siguientes:
22, 24, 21, 22, 25, 26, 25, 24, 23, 25, 25, 26, 27, 25, 26,
25, 26, 27, 27, 28, 29, 29, 29, 28, 30, 29, 30, 31, 30, 28, 29.
Determine la mediana de los datos
"""
import numpy as np
import wdb
# wdb.set_trace()
# Datos
datos = [22, 24, 21, 22, 25, 26, 25, 24, 23, 25, 25, 26, 27, 25, 26,
         25, 26, 27, 27, 28, 29, 29, 29, 28, 30, 29, 30, 31, 30, 28, 29]
# Ordenar los datos
datos.sort()
print(datos)

# Calcular la mediana
n = len(datos)
print(n)
if n % 2 == 0:
    mediana = (datos[n//2-1] + datos[n//2])/2
else:
    mediana = datos[n//2]
print(mediana)

#Determine los cuantiles de los datos
q1 = np.percentile(datos, 25)
q2 = np.percentile(datos, 50)
q3 = np.percentile(datos, 75)
print(q1, q2, q3)
# Determine el rango intercuartil
rango_intercuartil = q3 - q1
print(rango_intercuartil)