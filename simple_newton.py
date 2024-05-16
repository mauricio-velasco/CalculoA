#Raiz cuadrada de 2 via el método de Newton
res = [1.5]
for k in range(20):
    ant = res[-1]
    sig = ant - (ant**2-2)/(2*ant)
    res.append(sig)