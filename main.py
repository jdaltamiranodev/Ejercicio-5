# Escribe una función que pueda decirte si un año
# (número entero) es bisiesto o no.

def bisiesto(anio):
    es_bisiesto = ""
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        es_bisiesto = "es bisiesto"
    else:
        es_bisiesto = "no es bisiesto"

    return es_bisiesto

print("Acontinuación se va a determinar si un año es bisiesto o no\n")
opcion_anio = int(input("Digite un número entero: "))

anio_bisiesto = bisiesto(opcion_anio)
print("El año ", opcion_anio, " ", anio_bisiesto)