from p4radiacion import *
from scipy.integrate import dblquad

def integrand(x, y):
    return ((RadiacionM14[0] * (x ** 3)) + (RadiacionM14[1] * (y ** 3)) + (RadiacionM14[2] * (
            x ** 2) * y) +( RadiacionM14[3] * x * (y ** 2) )+ (RadiacionM14[4] * (x ** 2)) +
                 (RadiacionM14[5] * (y ** 2)) + (RadiacionM14[6] * x * y) + (RadiacionM14[7] * x) + (
                             RadiacionM14[8] * y + RadiacionM14[9]))

resultllay, errorllay = dblquad(integrand, 4.99, 5.99, lambda x: 6.29, lambda x: 7.29)

print("Valor de la radiación total en el sector cuadrado en Llay Llay:", resultllay)
print("Error estimado:", errorllay)

resultcat, errorcat = dblquad(integrand, 4.84, 5.84, lambda x: 7.16, lambda x: 8.16)

print("Valor de la radiación total en el sector cuadrado en Catemu:", resultcat)
print("Error estimado:", errorcat)

resultsanf, errorsanf = dblquad(integrand, 6.25, 7.25, lambda x: 7.19, lambda x: 8.19)

print("Valor de la radiación total en el sector cuadrado en San Felipe:", resultsanf)
print("Error estimado:", errorsanf)