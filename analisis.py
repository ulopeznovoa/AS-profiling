import random
import sys


def generar_datos(numero_elementos):
    random.seed(33)
    return [
        random.randint(1, numero_elementos // 5)
        for _ in range(numero_elementos)
    ]

def obtener_elementos_unicos(datos):
    unicos = []

    for elemento in datos:
        if elemento not in unicos:
            unicos.append(elemento)

    return unicos

def contar_elementos(datos, unicos):
    frecuencias = {}

    for elemento in unicos:
        frecuencias[elemento] = datos.count(elemento)

    return frecuencias

def analizar(numero_elementos):
    datos = generar_datos(numero_elementos)
    unicos = obtener_elementos_unicos(datos)
    frecuencias = contar_elementos(datos, unicos)

    print(f"Elementos procesados: {len(datos)}")
    print(f"Elementos diferentes: {len(unicos)}")
    print(f"Frecuencia total: {sum(frecuencias.values())}")

if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 30000
    analizar(n)
