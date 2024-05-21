import numpy as np
import matplotlib.pyplot as plt
#Queremos resolver una ecuacion diferencial con el método de Euler
def modelo_poblacion_0(x,y):
    return y

def euler(funcion_rhs, x_inicial,x_final,y_inicial, step_size_h):
    R = np.arange(x_inicial, x_final, step_size_h)    
    h = step_size_h
    x_res = [x_inicial]
    y_res = [y_inicial]
    for x in R:
        current_y = y_res[-1]
        next_y = current_y + h*funcion_rhs(x,current_y)
        next_x = x+h
        y_res.append(next_y)
        x_res.append(next_x)

    return x_res, y_res

#Creamos la figura:
fig, ax = plt.subplots()
ax.set(xlabel='Var independiente', ylabel='Var dependiente')
ax.grid()
#Y ponemos en ella varios intentos para diferentes h
x_inicial = 0.0
x_final = 15.0
y_inicial = 1.0

x_res, y_res = euler(modelo_poblacion_0, x_inicial = x_inicial,x_final=x_final, y_inicial = y_inicial, step_size_h = 0.1 )
ax.plot(x_res,y_res, label="Euler_h_0.1")
#Segundo intento
x_res, y_res = euler(modelo_poblacion_0, x_inicial = x_inicial,x_final = x_final, y_inicial = y_inicial, step_size_h = 0.05 )
ax.plot(x_res,y_res, label="Euler_h_0.01")
#Tercer intento
x_res, y_res = euler(modelo_poblacion_0, x_inicial = x_inicial,x_final = x_final, y_inicial = y_inicial, step_size_h = 0.01 )
ax.plot(x_res,y_res, label="Euler_h_0.001")
#Verdadero
x_res = np.arange(x_inicial,x_final, 0.001)
y_res = np.exp(x_res)
ax.plot(x_res,y_res, label="Sol analitica")

ax.legend(loc=2)
plt.show()


import numpy as np
import matplotlib.pyplot as plt
#Dibujar un direction field:
x = np.arange(-2,2,0.3) 
y = np.arange(-2,2,0.3)
X, Y = np.meshgrid(x,y)

dy = X + Y
dx = 1
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
dx = 1
norm = np.sqrt(dy**2+dx**2)
dyu = dy/norm
dxu = dx/norm

plt.quiver(X,Y,dxu,dyu,color="red")
plt.show()




