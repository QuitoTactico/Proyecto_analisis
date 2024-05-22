# Necesito hacer la serie de taylor de sen(x) alrededor de 0, con un error de 0.5E-3

import pandas as pd
import numpy as np
import math
import wdb
#wdb.set_trace()
x = 7.5 # -> Valor de x alrededor del cual se quiere aproximar la función

Tol = 0.5E-5 # -> Decimales correctos a los que se quiere iterar la función

n=0 # -> Contador de iteraciones
#N=[]
fm=[] # -> Lista de valores de la función
fx=((-1)**n)*(x**(2*n+1))/math.factorial(2*n+1) # -> Valor inicial de la función sen(x) alrededor de 0
E=[] # -> Lista de errores
E.append(100) # -> Valor inicial del error
fm.append(fx) # -> Valor inicial de la función
#N.append(n)
while E[n]>Tol:
     n+=1
     #N.append(n)
     fx+=((-1)**n)*(x**(2*n+1))/math.factorial(2*n+1)
     fm.append(fx)
     error=abs(fm[n]-fm[n-1])
     E.append(error)

Tabla=[E,fm]
Tabla=np.transpose(Tabla)
df=pd.DataFrame(Tabla, columns=["Error", "senx"])
print(df)

#Como puedo verificar que el valor de sen(7.5) es correcto?
#Puedo comparar el valor obtenido con el valor real de sen(7.5) que es 0.9379999767747389

