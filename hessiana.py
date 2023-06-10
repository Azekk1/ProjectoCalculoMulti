import sympy as sp

# Definir los símbolos para las variables
x, y = sp.symbols('x y')

# Definir la función
f = ((0.0160743634706346 * (x ** 3)) + (-0.0299717756251621 * (y ** 3)) + (-0.000409375351095420 * (x ** 2) * y) +
     (-0.125435603627039 * x * (y ** 2)) + (-0.0842903336554173 * (x ** 2)) + (0.853906304682340 * (y ** 2)) +
     (1.01637198527351 * x * y) + (-1.28414513927032 * x) + (-5.24815217032369 * y) + 17.7505634568843)

# Calcular los puntos estacionarios
puntos_estacionarios = sp.solve([sp.diff(f, x), sp.diff(f, y)], (x, y))

# Filtrar los puntos estacionarios reales y eliminar la parte imaginaria cercana a cero
puntos_estacionarios_reales = []
for punto in puntos_estacionarios:
    punto_reales = [p.evalf() for p in punto]
    punto_reales_filtrados = [sp.re(p) if abs(sp.im(p)) < 0.1 else p for p in punto_reales]
    puntos_estacionarios_reales.append(punto_reales_filtrados)

print("Puntos estacionarios reales encontrados:")
for punto in puntos_estacionarios_reales:
    print(punto)

# Calcular la matriz Hessiana y el determinante en los puntos estacionarios reales
for punto in puntos_estacionarios_reales:
    hessiana = sp.hessian(f, (x, y)).subs({x: punto[0], y: punto[1]})
    determinante = hessiana.det()
    print("\nPunto estacionario:", punto)
    print("Matriz Hessiana:")
    print(hessiana)
    print("Determinante:", determinante)
