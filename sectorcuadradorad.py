import numpy as np
from scipy.integrate import dblquad

def integrand(x, y):
    return ((-2.31027939033521 * (x ** 3)) + (1.36482656572787 * (y ** 3)) + (2.58594297267661 * (
            x ** 2) * y) +( 0.217498187061778 * x * (y ** 2) )+ (28.1083524480346 * (x ** 2)) +
                 (-16.1548399689464 * (y ** 2)) + (-23.4735123185110 * x * y) + (-96.7826181598430 * x) + (
                             84.9863452703576 * y + 184.652642106492))

resultllay, errorllay = dblquad(integrand, 4.99, 5.99, lambda x: 6.29, lambda x: 7.29)

print("Valor de la radiación total en el sector cuadrado en Llay Llay:", resultllay)
print("Error estimado:", errorllay)

resultcat, errorcat = dblquad(integrand, 4.84, 5.84, lambda x: 7.16, lambda x: 8.16)

print("Valor de la radiación total en el sector cuadrado en Catemu:", resultcat)
print("Error estimado:", errorcat)

resultsanf, errorsanf = dblquad(integrand, 6.25, 7.25, lambda x: 7.19, lambda x: 8.19)

print("Valor de la radiación total en el sector cuadrado en San Felipe:", resultsanf)
print("Error estimado:", errorsanf)