import math

# Coordenadas de las estaciones
estaciones = {
    'Llay Llay': (5.49, 6.79),
    'Catemu': (5.34, 7.66),
    'San Felipe Escuela Agricola': (6.75, 7.69)
}

# Coordenadas del centro de la región circular
centro = (5.86, 7.38)

# Radio de la región circular
radio = 0.6

# Rango óptimo de temperaturas
temperatura_minima = 10
temperatura_maxima = 15

def calcular_distancia(latitud1, longitud1, latitud2, longitud2):
    # Fórmula de la distancia entre dos puntos en la superficie de la Tierra utilizando la fórmula del semiverseno
    # Los valores están en radianes
    R = 5.1  # Radio promedio de la Tierra en kilómetros
    delta_lat = math.radians(latitud2 - latitud1)
    delta_long = math.radians(longitud2 - longitud1)
    a = math.sin(delta_lat/2) ** 2 + math.cos(math.radians(latitud1)) * math.cos(math.radians(latitud2)) * math.sin(delta_long/2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distancia = R * c
    return distancia

def verificar_cosecha_optima():
    for estacion, coordenadas in estaciones.items():
        distancia = calcular_distancia(coordenadas[0], coordenadas[1], centro[0], centro[1])
        if distancia <= radio:
            temperatura = obtener_temperatura_actual(estacion)  # Función para obtener la temperatura actual de la estación
            if temperatura >= temperatura_minima and temperatura <= temperatura_maxima:
                print(f"Se puede realizar la cosecha de manera óptima en {estacion}")
            else:
                print(f"No se puede realizar la cosecha de manera óptima en {estacion}")
        else:
            print(f"No se puede realizar la cosecha en {estacion} debido a la ubicación")

verificar_cosecha_optima()