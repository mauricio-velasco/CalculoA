import numpy as np
import matplotlib.pyplot as plt
#Dibujar un direction field:
x = np.arange(-2,2,0.3) 
y = np.arange(-2,2,0.3)
X, Y = np.meshgrid(x,y)

dy = X + Y
dx = np.ones(dy.shape)
norm = np.sqrt(dy**2+dx**2)
dyu = dy/norm
dxu = dx/norm

plt.quiver(X,Y,dxu,dyu,color="blue")
plt.show()

#Ejemplo 2: Dibujar un direction field:
x = np.arange(-2,2,0.3) 
y = np.arange(-2,2,0.3)
X, Y = np.meshgrid(x,y)

dy = X**2+Y**2-1
dx = np.ones(dy.shape)
norm = np.sqrt(dy**2+dx**2)
dyu = dy/norm
dxu = dx/norm

plt.quiver(X,Y,dxu,dyu,color="red")
plt.show()




