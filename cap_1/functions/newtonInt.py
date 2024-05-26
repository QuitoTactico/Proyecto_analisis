import numpy as np
from math import *
from .base import func as base_func, grafico_interactivo
#from base import func as base_func, graficar_template, grafico_interactivo


def Newtonint(x: np.array.__class__, y: np.array.__call__):
    n = len(x)
    Tabla = np.zeros((n, n + 1))
    Tabla[:, 0] = x
    Tabla[:, 1] = y

    for j in range(2, n + 1):
        for i in range(j - 1, n):
            Tabla[i, j] = (Tabla[i, j - 1] - Tabla[i - 1, j - 1]) / (Tabla[i, 0] - Tabla[i - (j - 1), 0])

    mensaje = "it worked"

    #function = f"{Tabla[0][1]} + {Tabla[1][2]}*x + {Tabla[2][3]}*x*x + {Tabla[3][4]}*x*x*x "

    print(function)

    img_interactiva = grafico_interactivo(function)

    return {'tabla': Tabla,
            #'img_interactiva': img_interactiva,
            'mensaje': mensaje
            }


def ejemplo():
    # Ejemplo de uso
    x = np.array([1, 4, 13, 20])  # Ejemplo de puntos x
    y = np.array([-10, 8, -20, 1])  # Ejemplo de puntos y

    Tabla = Newtonint(x, y)['tabla']
    print("Tabla de diferencias divididas de Newton:")
    print(Tabla)


#ejemplo()
