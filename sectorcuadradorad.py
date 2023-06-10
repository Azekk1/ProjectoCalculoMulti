from p4radiacion import *
from scipy.integrate import dblquad

def integrand(x, y):
    return ((RadiacionM11[0] * (x ** 3)) + (RadiacionM11[1] * (y ** 3)) + (RadiacionM11[2] * (
            x ** 2) * y) +( RadiacionM11[3] * x * (y ** 2) )+ (RadiacionM11[4] * (x ** 2)) +
                 (RadiacionM11[5] * (y ** 2)) + (RadiacionM11[6] * x * y) + (RadiacionM11[7] * x) + (
                             RadiacionM11[8] * y + RadiacionM11[9]))

resultllay, errorllay = dblquad(integrand, 4.99, 5.99, lambda x: 6.29, lambda x: 7.29)

print("Valor de la radiación total en el sector cuadrado en Llay Llay:", resultllay)
print("Error estimado:", errorllay)

resultcat, errorcat = dblquad(integrand, 4.84, 5.84, lambda x: 7.16, lambda x: 8.16)

print("Valor de la radiación total en el sector cuadrado en Catemu:", resultcat)
print("Error estimado:", errorcat)

resultsanf, errorsanf = dblquad(integrand, 6.25, 7.25, lambda x: 7.19, lambda x: 8.19)

print("Valor de la radiación total en el sector cuadrado en San Felipe:", resultsanf)
print("Error estimado:", errorsanf)