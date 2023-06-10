import numdifftools as nd
import math
from sympy import *
import numpy as np
from scipy.optimize import fsolve
from sympy import symbols, diff, Eq, solve


def func(x):
    return ((0.0160743634706346 * (x[0] ** 3)) + (-0.0299717756251621 * (x[1] ** 3)) + (-0.000409375351095420 * (
            x[0] ** 2) * x[1]) +( -0.125435603627039 * x[0] * (x[1] ** 2) )+ (-0.0842903336554173 * (x[0] ** 2)) +
                 (0.853906304682340 * (x[1] ** 2)) + (1.01637198527351 * x[0] * x[1]) + (-1.28414513927032 * x[0]) + (
                             -5.24815217032369 * x[1] + 17.7505634568843))

punto1 = [2.14,6.32]
punto2= [1.64,5.44]
calculox = punto1[0]-punto2[0]
calculoy = punto1[1]-punto2[1]
grad = nd.Gradient(func)([6.49,2.78])
grad4 = nd.Gradient(func)([5.89,1.13])
vector = [calculox, calculoy]
vector2 = [0, 7.02]
vector3 = [3.51,0]
normav3 = math.sqrt((vector3[0])**2+(vector3[1])**2)
normav2 = math.sqrt((vector2[0])**2+(vector2[1])**2)
normav = math.sqrt((calculox)**2+(calculoy)**2)
vectoru = [calculox/normav, calculoy/normav]
vectoru2 = [vector2[0]/normav2, vector2[1]/normav2]
vectoru3 = [vector3[0]/normav3, vector3[1]/normav3]
multgradvec2 = grad*vectoru2
multgradvec3 = grad*vectoru3
sumadir2 = multgradvec2[0]+multgradvec2[1]
sumadir3 = multgradvec3[0]+multgradvec3[1]
grad5 = nd.Gradient(func)([1.64,5.44])
multgradvec = grad5*vectoru
sumadir = multgradvec[0]+multgradvec[1]

x, y = symbols('x y')
f = ((0.0160743634706346 * (x ** 3)) + (-0.0299717756251621 * (y ** 3)) + (-0.000409375351095420 * (
            x ** 2) * y) +( -0.125435603627039 * x * (y ** 2) )+ (-0.0842903336554173 * (x ** 2)) +
                 (0.853906304682340 * (y ** 2)) + (1.01637198527351 * x * y) + (-1.28414513927032 * x) + (
                             -5.24815217032369 * y + 17.7505634568843))
df_dx = diff(f, x)
df_dy = diff(f, y)
soluciones = solve([Eq(df_dx, 0), Eq(df_dy, 0)], (x, y))
for solucion in soluciones:
    print(f"Punto estacionario: x = {solucion[0]}, y = {solucion[1]}")

print(f"La derivada direccional en dirección norte es {sumadir2}")

print(f"La derivada direccional en dirección este es {sumadir3}")

print(f"La derivada direccional de Rodelillo en dirección a Viña es {sumadir}")

print(f"Para que la temperatura disminuya lo más rápido posible debe moverse en la dirección {-(grad4[0])} y {-(grad4[1])}")
