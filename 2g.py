import numpy as np
from scipy.optimize import minimize

# Función objetivo (temperatura)
def temperatura(x, y):
    return ((0.0160743634706346 * (x ** 3)) + (-0.0299717756251621 * (y ** 3)) + (-0.000409375351095420 * (x ** 2) * y) +
            (-0.125435603627039 * x * (y ** 2)) + (-0.0842903336554173 * (x ** 2)) + (0.853906304682340 * (y ** 2)) +
            (1.01637198527351 * x * y) + (-1.28414513927032 * x) + (-5.24815217032369 * y) + 17.7505634568843)

# Restricción (circunferencia)
def restriccion(x, y):
    return (x - 6.0711351571994)**2 + (y - 7.4832782020965)**2 - 0.8620954713041

# Función de Lagrange
def lagrange(xy_lambda):
    x, y, l = xy_lambda
    return temperatura(x, y) - l * restriccion(x, y)

# Restricción para el optimizador
def constraint(xy_lambda):
    x, y, l = xy_lambda
    return restriccion(x, y)

# Condición inicial
x0 = [6.0711351571994, 7.4832782020965, 0]

# Restricción para el optimizador
cons = {'type': 'eq', 'fun': constraint}

# Optimización
res_min = minimize(lagrange, x0, constraints=cons)
res_max = minimize(lambda xy_lambda: -lagrange(xy_lambda), x0, constraints=cons)

# Resultados
min_temp = temperatura(res_min.x[0], res_min.x[1])
max_temp = temperatura(res_max.x[0], res_max.x[1])

print("Temperatura mínima:", min_temp)
print("Temperatura máxima:", max_temp)