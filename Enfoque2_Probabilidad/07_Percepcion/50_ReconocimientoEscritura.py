# Inteligencia Artificial - Parcial 2
# Alumna: Elsy Valeria Cuevas de la Torre
# Tema: 50 ReconocimientoEscritura
# Version de practica con ejemplos y nombres propios.

"""
50 - Reconocimiento de Escritura (OCR simplificado)
Compara una matriz binaria contra plantillas de digitos por distancia
de Hamming.
"""


def distancia(a, b):
    return sum(x != y for fila_a, fila_b in zip(a, b) for x, y in zip(fila_a, fila_b))


def ocr(img, plantillas):
    return min(plantillas, key=lambda d: distancia(img, plantillas[d]))


if __name__ == "__main__":
    print("--- Prueba de ejecucion: Elsy ---")
    cero = [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]]
    uno = [[0, 1, 0], [1, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]]
    siete = [[1, 1, 1], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 0, 0]]
    plantillas = {"0": cero, "1": uno, "7": siete}
    test = [[0, 1, 0], [1, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]]
    print("Digito reconocido:", ocr(test, plantillas))
