# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vrCAZJQYh3Bh6Q4RcOHTMq_WlMhMc_DU
"""

import numpy as np
from sympy import init_printing

init_printing(use_unicode=True)
from sympy import symbols
from sympy.matrices import Matrix
from sympy import *
from sympy.solvers.solveset import linsolve


A = Matrix([[4.410944, 160.989184, 14.631424, 48.533504, 2.6896, 29.5936, 8.9216, 1.64, 5.44,1],
            [8, 175.616, 22.4, 62.72, 4, 31.36, 11.2, 2.00, 5.60,1],
            [6.229504, 416.832723, 25.290432, 102.673656, 3.3856, 55.8009, 13.7448, 1.84, 7.47,1],
            [9.800344, 252.435968, 28.943072, 85.476736, 4.5796, 39.9424, 13.5248, 2.14, 6.32,1],
            [32.461759, 743.677416, 92.195466, 261.846684, 10.1761, 82.0836, 28.9014, 3.19, 9.06,1],
            [152.273304, 449.455096, 218.429496, 313.327704, 28.5156, 58.6756, 40.9044, 5.34, 7.66,1],
            [307.546875, 454.756609, 350.375625, 399.168675, 45.5625, 59.1361, 51.9075, 6.75, 7.69,1],
            [165.469149, 313.046839, 204.651279, 253.111509, 30.1401, 46.1041, 37.2771, 5.49, 6.79,1],
            [123.505992, 176.558481, 139.130244, 156.731058, 24.8004, 31.4721, 27.9378, 4.98, 5.61,1],
            [217.081801, 130.323843, 183.128907, 154.486449, 36.1201, 25.7049, 30.4707, 6.01, 5.07,1],
            [322.828856, 134.217728, 240.945152, 179.830784, 47.0596, 26.2144, 35.1232, 6.86, 5.12,1],
            [363.994344, 108.531333, 243.172692, 162.455706, 50.9796, 22.7529, 34.0578, 7.14, 4.77,1],
            [286.191179, 64.481201, 174.146681, 105.967859, 43.4281, 16.0801, 26.4259, 6.59, 4.01,1],
            [786.330467, 41.063625, 293.915505, 109.860075, 85.1929, 11.9025, 31.8435, 9.23, 3.45,1],
            [458.314011, 19.465109, 159.904629, 55.790331, 59.4441, 7.2361, 20.7399, 7.71, 2.69,1],
            [327.082769, 20.796875, 130.548275, 52.105625, 47.4721, 7.5625, 18.9475, 6.89, 2.75,1],
            [273.359449, 21.484952, 117.093878, 50.157316, 42.1201, 7.7284, 18.0422, 6.49, 2.78,1],
            [246.491883, 33.698267, 126.980667, 65.414283, 39.3129, 10.4329, 20.2521, 6.27, 3.23,1],
            [147.197952, 18.821096, 74.156544, 37.359168, 27.8784, 7.0756, 14.0448, 5.28, 2.66,1],
            [458.314011, 8.489664, 121.265964, 32.085936, 59.4441, 4.1616, 15.7284, 7.71, 2.04,1],
            [702.595369, 3.723875, 122.499755, 21.358225, 79.0321, 2.4025, 13.7795, 8.89, 1.55,1],
            [64, 27, 48, 36, 16, 9, 12, 4.00, 3.00,1],
            [47.045881, 9.663597, 27.758373, 16.378209, 13.0321, 4.5369, 7.6893, 3.61, 2.13,1],
            [7.301384, 9.800344, 8.054104, 8.884424, 3.7636, 4.5796, 4.1516, 1.94, 2.14,1],
            [2.146689, 1.860867, 2.046843, 1.951641, 1.6641, 1.5129, 1.5867, 1.29, 1.23,1],
            [120.553784, 0.658503, 21.231132, 3.739086, 24.4036, 0.7569, 4.2978, 4.94, 0.87,1],
            [204.336469, 1.442897, 39.202073, 7.520941, 34.6921, 1.2769, 6.6557, 5.89, 1.13,1],
            [260.917119, 0.148877, 21.641013, 1.794951, 40.8321, 0.2809, 3.3867, 6.39, 0.53,1],
            [513.922401, 0.357911, 45.553671, 4.037841, 64.1601, 0.5041, 5.6871, 8.01, 0.71,1]])

B = Matrix([[9.5],
            [10.7],
            [10.8],
            [12.8],
            [11.0],
            [8.3],
            [9.2],
            [10.6],
            [13.3],
            [11.3],
            [18.4],
            [15.7],
            [13.9],
            [20.3],
            [14.3],
            [8.8],
            [13.5],
            [13],
            [13.3],
            [20.9],
            [16.1],
            [14.1], [7.3], [11.8], [12], [10], [11.3], [14.0], [9.6]])

NuevoA = A.T * A
NuevoB = A.T * B
AFinal = NuevoA.inv()

X = AFinal * NuevoB

print(X)

import numpy as np
from sympy import init_printing

init_printing(use_unicode=True)
from sympy import symbols
from sympy.matrices import Matrix
from sympy import *
from sympy.solvers.solveset import linsolve


#Matriz de coordenadas para los 23 lugares
Estaciones = Matrix([[6.229504, 416.832723, 25.290432, 102.673656, 3.3856, 55.8009, 13.7448, 1.84, 7.47,1],#Quintero
            [9.800344, 252.435968, 28.943072, 85.476736, 4.5796, 39.9424, 13.5248, 2.14, 6.32,1],#ViñaDelMar
            [32.461759, 743.677416, 92.195466, 261.846684, 10.1761, 82.0836, 28.9014, 3.19, 9.06,1],#Zapallar
            [152.273304, 449.455096, 218.429496, 313.327704, 28.5156, 58.6756, 40.9044, 5.34, 7.66,1],#Catemu
            [307.546875, 454.756609, 350.375625, 399.168675, 45.5625, 59.1361, 51.9075, 6.75, 7.69,1],#SanFelipe
            [165.469149, 313.046839, 204.651279, 253.111509, 30.1401, 46.1041, 37.2771, 5.49, 6.79,1],#LlayLlay
            [123.505992, 176.558481, 139.130244, 156.731058, 24.8004, 31.4721, 27.9378, 4.98, 5.61,1],#LlanosDeCaleu
            [217.081801, 130.323843, 183.128907, 154.486449, 36.1201, 25.7049, 30.4707, 6.01, 5.07,1],#Polpaico
            [363.994344, 108.531333, 243.172692, 162.455706, 50.9796, 22.7529, 34.0578, 7.14, 4.77,1],#Colina
            [286.191179, 64.481201, 174.146681, 105.967859, 43.4281, 16.0801, 26.4259, 6.59, 4.01,1],#LoPinto
            [786.330467, 41.063625, 293.915505, 109.860075, 85.1929, 11.9025, 31.8435, 9.23, 3.45,1],#ElColorado
            [458.314011, 19.465109, 159.904629, 55.790331, 59.4441, 7.2361, 20.7399, 7.71, 2.69,1],#Tobalaba
            [327.082769, 20.796875, 130.548275, 52.105625, 47.4721, 7.5625, 18.9475, 6.89, 2.75,1],#QuintaNormal
            [246.491883, 33.698267, 126.980667, 65.414283, 39.3129, 10.4329, 20.2521, 6.27, 3.23,1],#Pudahuel
            [147.197952, 18.821096, 74.156544, 37.359168, 27.8784, 7.0756, 14.0448, 5.28, 2.66,1],#LoPrado
            [458.314011, 8.489664, 121.265964, 32.085936, 59.4441, 4.1616, 15.7284, 7.71, 2.04,1],#LaFlorida
            [702.595369, 3.723875, 122.499755, 21.358225, 79.0321, 2.4025, 13.7795, 8.89, 1.55,1],#SanJoseGuayacan
            [64, 27, 48, 36, 16, 9, 12, 4.00, 3.00,1],#Curacavi
            [47.045881, 9.663597, 27.758373, 16.378209, 13.0321, 4.5369, 7.6893, 3.61, 2.13,1],#Chorombo
            [7.301384, 9.800344, 8.054104, 8.884424, 3.7636, 4.5796, 4.1516, 1.94, 2.14,1],#SanAntonio
            [120.553784, 0.658503, 21.231132, 3.739086, 24.4036, 0.7569, 4.2978, 4.94, 0.87,1],#ElPaico
            [204.336469, 1.442897, 39.202073, 7.520941, 34.6921, 1.2769, 6.6557, 5.89, 1.13,1],#Talagante
            [260.917119, 0.148877, 21.641013, 1.794951, 40.8321, 0.2809, 3.3867, 6.39, 0.53,1]])#ElMilagro





#Para las 00:00 a las 24:00
M00 = Matrix([[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0], [0.0]])
M01 = Matrix([[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0], [0.0]])
M02 = Matrix([[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0], [0.0]])
M03 = Matrix([[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0], [0.0]])
M04 = Matrix([[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0], [0.0]])
M05 = Matrix([[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0], [0.0]])
M06 = Matrix([[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0], [0.0]])
M07 = Matrix([[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0], [0.0]])
M08 = Matrix([[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0], [0.0]])
M09 = Matrix([[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0], [0.0]])
M10 = Matrix([[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0], [0.0]])
M11 = Matrix([[2.7],[2.6],[1.4],[0.0],[2.0],[1.5],[1.0],[0.0],[0.0],[0.0],[0.0],[5.0],[2.2],[4.3],[0.5],[0.0],[2.3],[0.4],[0.2],[0.0],[1.0],[1.3], [2.7]])
M12 = Matrix([[162.4],[84.8],[170.6],[74.9],[213.0],[76.0],[68.2],[103.0],[151.4],[138.4],[38.5],[139.0],[192.0],[137.4],[112.6],[58.2],[51.0],[92.9],[150.1],[119.7],[150.7],[37.2], [174.5]])
M13 = Matrix([[331.8],[334.5],[361.9],[308.6],[262.3],[351.6],[387.1],[175.4],[286.5],[99.4],[376.1],[311.0],[278.1],[367.1],[336.6],[344.9],[392.5],[245.4],[184.0],[329.4],[332.2],[281.1], [334.5]])
M14 = Matrix([[514.8],[509.4],[527.5],[316.3],[194.2],[622.0],[520.9],[485.2],[545.3],[502.0],[470.1],[446.0],[367.9],[374.8],[359.3],[411.8],[333.0],[401.6],[501.2],[523.3],[382.5],[432.1], [543.5]])
M15 = Matrix([[667.0],[659.3],[669.7],[563.2],[731.3],[461.3],[655.4],[709.9],[593.2],[430.1],[669.0],[541.0],[634.0],[714.2],[672.1],[675.1],[436.1],[589.4],[640.0],[678.8],[667.8],[640.1], [696.3]])
M16 = Matrix([[752.9],[773.4],[751.1],[347.7],[799.1],[581.2],[412.5],[677.7],[715.2],[705.9],[820.2],[787.0],[755.5],[790.2],[792.5],[722.3],[665.9],[695.2],[733.2],[780.1],[747.4],[724.1], [783.5]])
M17 = Matrix([[780.1],[808.9],[767.9],[753.2],[351.4],[627.6],[771.2],[744.6],[672.6],[718.3],[763.5],[782.0],[761.0],[823.4],[839.6],[745.1],[686.8],[710.0],[755.8],[810.2],[755.4],[742.1], [795.1]])
M18 = Matrix([[746.8],[763.1],[743.2],[704.5],[685.6],[738.9],[691.1],[683.1],[648.6],[676.5],[804.7],[725.0],[704.1],[777.2],[819.6],[694.3],[651.6],[684.2],[707.8],[768.2],[694.0],[711.5], [735.3]])
M19 = Matrix([[633.1],[641.0],[613.2],[592.5],[540.9],[644.3],[598.0],[561.4],[585.0],[593.3],[649.5],[609.0],[594.7],[664.3],[729.1],[611.8],[560.0],[606.4],[588.6],[650.7],[559.2],[618.0], [601.5]])
M20 = Matrix([[437.4],[466.6],[424.2],[431.8],[376.3],[489.4],[450.9],[419.4],[449.1],[462.3],[504.7],[464.0],[437.0],[501.2],[558.4],[465.2],[425.1],[459.5],[430.3],[471.6],[363.2],[458.7], [414.3]])
M21 = Matrix([[243.3],[276.1],[225.9],[246.8],[190.2],[299.9],[263.8],[247.8],[262.4],[289.1],[275.7],[263.0],[234.2],[287.9],[315.8],[261.7],[42.8],[250.7],[238.9],[238.4],[155.3],[261.8], [213.8]])
M22 = Matrix([[75.5],[79.3],[37.6],[22.1],[26.8],[90.6],[66.8],[69.9],[62.5],[75.9],[70.2],[70.0],[46.1],[76.3],[71.1],[62.2],[12.7],[59.9],[55.3],[58.5],[31.7],[37.9], [43.8]])
M23 = Matrix([[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0], [0.0]])
M24 = Matrix([[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0], [0.0]])

#Desde las 00:00 hasta las 10:00 no existe radiacion en ninguna estaciones por lo cual el resultado siempre dara 0

NuevoEstaciones = Estaciones.T * Estaciones
NuevoM11 = Estaciones.T * M11
EstacionesM11Final = NuevoEstaciones.inv()
RadiacionM11 = EstacionesM11Final * NuevoM11
print("Los coeficientes de radiación a las 11:00 es",RadiacionM11)

NuevoEstaciones = Estaciones.T * Estaciones
NuevoM12 = Estaciones.T * M12
EstacionesM12Final = NuevoEstaciones.inv()
RadiacionM12 = EstacionesM12Final * NuevoM12
print(f"Los coeficientes de radiación a las 12:00 es {RadiacionM12}")

NuevoEstaciones = Estaciones.T * Estaciones
NuevoM13 = Estaciones.T * M13
EstacionesM13Final = NuevoEstaciones.inv()
RadiacionM13 = EstacionesM11Final * NuevoM13
print("Los coeficientes de radiación a las 13:00 es",RadiacionM13)

NuevoEstaciones = Estaciones.T * Estaciones
NuevoM14 = Estaciones.T * M14
EstacionesM14Final = NuevoEstaciones.inv()
RadiacionM14 = EstacionesM14Final * NuevoM14
print("Los coeficientes de radiación a las 14:00 es",RadiacionM14)

NuevoEstaciones = Estaciones.T * Estaciones
NuevoM15 = Estaciones.T * M15
EstacionesM15Final = NuevoEstaciones.inv()
RadiacionM15 = EstacionesM15Final * NuevoM15
print("Los coeficientes de radiación a las 15:00 es",RadiacionM15)

NuevoEstaciones = Estaciones.T * Estaciones
NuevoM16 = Estaciones.T * M16
EstacionesM16Final = NuevoEstaciones.inv()
RadiacionM16 = EstacionesM16Final * NuevoM16
print("Los coeficientes de radiación a las 16:00 es",RadiacionM16)

NuevoEstaciones = Estaciones.T * Estaciones
NuevoM17 = Estaciones.T * M17
EstacionesM17Final = NuevoEstaciones.inv()
RadiacionM17 = EstacionesM17Final * NuevoM17
print("Los coeficientes de radiación a las 17:00 es",RadiacionM17)

NuevoEstaciones = Estaciones.T * Estaciones
NuevoM18 = Estaciones.T * M18
EstacionesM18Final = NuevoEstaciones.inv()
RadiacionM18 = EstacionesM18Final * NuevoM18
print("Los coeficientes de radiación a las 18:00 es",RadiacionM18)

NuevoEstaciones = Estaciones.T * Estaciones
NuevoM19 = Estaciones.T * M19
EstacionesM19Final = NuevoEstaciones.inv()
RadiacionM19 = EstacionesM19Final * NuevoM19
print("Los coeficientes de radiación a las 19:00 es",RadiacionM19)

NuevoEstaciones = Estaciones.T * Estaciones
NuevoM20 = Estaciones.T * M20
EstacionesM20Final = NuevoEstaciones.inv()
RadiacionM20 = EstacionesM20Final * NuevoM20
print("Los coeficientes de radiación a las 20:00 es",RadiacionM20)

NuevoEstaciones = Estaciones.T * Estaciones
NuevoM21 = Estaciones.T * M21
EstacionesM21Final = NuevoEstaciones.inv()
RadiacionM21 = EstacionesM21Final * NuevoM21
print("Los coeficientes de radiación a las 21:00 es",RadiacionM21)

NuevoEstaciones = Estaciones.T * Estaciones
NuevoM22 = Estaciones.T * M22
EstacionesM22Final = NuevoEstaciones.inv()
RadiacionM22 = EstacionesM22Final * NuevoM22
print("Los coeficientes de radiación a las 22:00 es",RadiacionM22)

NuevoEstaciones = Estaciones.T * Estaciones
NuevoM23 = Estaciones.T * M23
EstacionesM23Final = NuevoEstaciones.inv()
RadiacionM23 = EstacionesM23Final * NuevoM23
print("Los coeficientes de radiación a las 23:00 es",RadiacionM23)

NuevoEstaciones = Estaciones.T * Estaciones
NuevoM24 = Estaciones.T * M24
EstacionesM24Final = NuevoEstaciones.inv()
RadiacionM24 = EstacionesM24Final * NuevoM24
print("Los coeficientes de radiación a las 24:00 es",RadiacionM24)
__all__ = [f'RadiacionM{i}' for i in range(11, 25)]
def R(x, y):
    resultado = ((RadiacionM11[0] * (x ** 3)) + (RadiacionM11[1] * (y ** 3)) + (RadiacionM11[2] * (
            x ** 2) * y) +( RadiacionM11[3] * x * (y ** 2) )+ (RadiacionM11[4] * (x ** 2)) +
                 (RadiacionM11[5] * (y ** 2)) + (RadiacionM11[6] * x * y) + (RadiacionM11[7] * x) + (
                             RadiacionM11[8] * y + RadiacionM11[9]))
    return resultado


print(f"La radiación en el punto es: {R(4,8)}")

