import numpy as np
import matplotlib.pyplot as plt

# Definir la función
def f(x, y):
    return 0.0160743634706346*x**3 - 0.0299717756251621*y**3 - 0.000409375351095420*x**2*y - \
           0.125435603627039*x*y**2 - 0.0842903336554173*x**2 + 0.853906304682340*y**2 + \
           1.01637198527351*x*y - 1.28414513927032*x - 5.24815217032369*y + 17.7505634568843

# Definir el rango de valores para x e y
x_vals = np.linspace(-10, 10, 100)
y_vals = np.linspace(-10, 10, 100)

# Crear una malla de coordenadas x, y
X, Y = np.meshgrid(x_vals, y_vals)

# Calcular los valores de z = f(x, y) para cada par de coordenadas x, y
Z = f(X, Y)

# Valor deseado para la curva de nivel
valor_deseado = 12.9

# Graficar la curva de nivel para el valor deseado
plt.contour(X, Y, Z, levels=[valor_deseado])

# Configuraciones adicionales del gráfico
plt.xlabel('x')
plt.ylabel('y')
plt.title('Curva de nivel para f(x, y) = 11.1')
plt.grid(True)

# Mostrar el gráfico
plt.show()
