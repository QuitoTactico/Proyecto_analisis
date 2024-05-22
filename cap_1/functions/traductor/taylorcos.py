import pandas as pd
import numpy as np
import math
import wdb
#wdb.set_trace()
x = np.pi/4 # -> Valor de x alrededor del cual se quiere aproximar la función

Tol = 0.5E-3 # -> Decimales correctos a los que se quiere iterar la función

n=0
#N=[]
fm=[] # -> Lista de valores de la función
fx=((-1)**n)*(x**(2*n))/math.factorial(2*n) # -> Valor inicial de la función cos(x) alrededor de 0
E=[] # -> Lista de errores
E.append(100) # -> Valor inicial del error
fm.append(fx) # -> Valor inicial de la función
#N.append(n)
while E[n]>Tol:
     n+=1
     #N.append(n)
     fx+=((-1)**n)*(x**(2*n))/math.factorial(2*n)
     fm.append(fx)
     error=abs(fm[n]-fm[n-1])
     E.append(error)

Tabla=[E,fm]
Tabla=np.transpose(Tabla)
df=pd.DataFrame(Tabla, columns=["Error", "cosx"])
print(df)  

