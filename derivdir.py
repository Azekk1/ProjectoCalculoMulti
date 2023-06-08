import numdifftools as nd
import math
from sympy import *

def func(x):
    return ((0.0160743634706346 * (x[0] ** 3)) + (-0.0299717756251621 * (x[1] ** 3)) + (-0.000409375351095420 * (
            x[0] ** 2) * x[1]) +( -0.125435603627039 * x[0] * (x[1] ** 2) )+ (-0.0842903336554173 * (x[0] ** 2)) +
                 (0.853906304682340 * (x[1] ** 2)) + (1.01637198527351 * x[0] * x[1]) + (-1.28414513927032 * x[0]) + (
                             -5.24815217032369 * x[1] + 17.7505634568843))

punto1 = [2.14,6.32]
punto2= [1.64,5.44]
grad = nd.Gradient(func)([6.49,9.8])
grad2 =nd.Gradient(func)([10,2.78])
calculox = punto1[0]-punto2[0]
calculoy = punto1[1]-punto2[1]
print(f"{calculox} y {calculoy}")
grad3 = nd.Gradient(func)([calculox,calculoy])
grad4 = nd.Gradient(func)([5.89,1.13])
vector = [calculox, calculoy]
normav = math.sqrt((calculox)**2+(calculoy)**2)
vectoru = [calculox/normav, calculoy/normav]
grad5 = nd.Gradient(func)([1.64,5.44])
multgradvec = grad5*vectoru
sumadir = multgradvec[0]+multgradvec[1]

x = Symbol('x')
y = Symbol('y')
f = ((0.0160743634706346 * (x ** 3)) + (-0.0299717756251621 * (y ** 3)) + (-0.000409375351095420 * (
            x ** 2) * y) +( -0.125435603627039 * x * (y ** 2) )+ (-0.0842903336554173 * (x ** 2)) +
                 (0.853906304682340 * (y ** 2)) + (1.01637198527351 * x * y) + (-1.28414513927032 * x) + (
                             -5.24815217032369 * y + 17.7505634568843))
derivada_x = f.diff(x)
derivada_y = f.diff(y)
A = np.array([])


print(f"la derivada direccional en dirección norte es {math.sqrt((grad[0])**2+(grad[1])**2)}")

print(f"la derivada direccional en dirección este es {math.sqrt((grad2[0])**2+(grad2[1])**2)}")

print(f"la derivada direccional de Rodelillo en dirección a Viña es (maxima derivada dir) {math.sqrt((grad3[0])**2+(grad3[1])**2)}")
print(f"la derivada direccional de Rodelillo en dirección a Viña es (derivada dir con vector) {sumadir}")

print(f"Para que la temperatura disminuya lo más rápido posible debe moverse en la dirección {-(grad4[0])} y {-(grad4[1])}")