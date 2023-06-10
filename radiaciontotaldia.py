from p4radiacion import *
from scipy.integrate import dblquad

localidades = [
    {
        "nombre": "Llay Llay",
        "coordenadas": (4.99, 5.99, 6.29, 7.29)
    },
    {
        "nombre": "Catemu",
        "coordenadas": (4.84, 5.84, 7.16, 8.16)
    },
    {
        "nombre": "San Felipe",
        "coordenadas": (6.25, 7.25, 7.19, 8.19)
    }
]


radiacion_total_localidades = []


for localidad in localidades:
    radiacion_total_localidad = 0.0

    for i in range(11, 23):

        variable_name = "RadiacionM" + str(i)

        matriz_radiacion = globals()[variable_name]

        def integrand(x, y):
            return ((matriz_radiacion[0] * (x ** 3)) + (matriz_radiacion[1] * (y ** 3)) + (matriz_radiacion[2] * (
                x ** 2) * y) + (matriz_radiacion[3] * x * (y ** 2)) + (matriz_radiacion[4] * (x ** 2)) +
                    (matriz_radiacion[5] * (y ** 2)) + (matriz_radiacion[6] * x * y) + (matriz_radiacion[7] * x) + (
                                matriz_radiacion[8] * y + matriz_radiacion[9]))

        result, error = dblquad(integrand, localidad["coordenadas"][0], localidad["coordenadas"][1],
                                lambda x: localidad["coordenadas"][2], lambda x: localidad["coordenadas"][3])

        radiacion_total_localidad += result

    radiacion_total_localidades.append(radiacion_total_localidad)

for i, localidad in enumerate(localidades):
    print("Radiación total del día para la localidad", localidad["nombre"], ":", radiacion_total_localidades[i])
