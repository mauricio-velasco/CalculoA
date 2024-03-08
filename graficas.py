#Cargamos las librerias necesarias:
import matplotlib.pyplot as plt
import numpy as np

#0. Especificamos la funcion que queremos
def mi_funcion(x):
    return x*np.sin(1/x)
    #return np.sin(np.cos(x*x+7.0))+3


# 1. Especificamos los puntos X en los que queremos que se evalue la funcion
Xs = np.arange(start = -0.25, stop = 0.25,step=0.0001)
Ys = [mi_funcion(x) for x in Xs]

#2. Hacemos y grabamos la gráfica
plt.plot(Xs,Ys) #Hace la grafica, poniendo puntos en las parebas correspondientes 
plt.axis(xmin = -0.25,xmax = 0.25, ymin=-0.25,ymax=0.25)
#Parámetros de la gráfica:
plt.grid(True)
plt.title("Primer intento Pyplot")
plt.xlabel("Variable independiente")
plt.ylabel("Variable dependiente")
plt.savefig("archivo_imagen") #Graba un archivo con la imagen
plt.show()# Muestra el dibujo

