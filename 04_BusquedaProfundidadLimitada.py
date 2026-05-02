# Inteligencia Artificial - Parcial 2
# Alumna: Elsy Valeria Cuevas de la Torre
# Tema: 04 BusquedaProfundidadLimitada
# Version de practica con ejemplos y nombres propios.

"""
04 - Busqueda en Profundidad Limitada (DLS)
DFS con un tope de profundidad maxima para evitar caer en
ramas infinitas o demasiado largas.
"""


def dls(red, punto, objetivo, tope, ruta=None):
    if ruta is None:
        ruta = [punto]
    if punto == objetivo:
        return ruta
    if tope <= 0:
        return None
    for conexion in red.get(punto, []):
        if conexion in ruta:
            continue
        res = dls(red, conexion, objetivo, tope - 1, ruta + [conexion])
        if res:
            return res
    return None


if __name__ == "__main__":
    print("--- Prueba de ejecucion: Elsy ---")
    red = {
        "Entrada": ["Pasillo", "Laboratorio"],
        "Pasillo": ["Biblioteca", "Salon"],
        "Laboratorio": ["Taller"],
        "Biblioteca": [],
        "Salon": ["Taller"],
        "Taller": [],
    }
    print("Tope 1:", dls(red, "Entrada", "Taller", 1))
    print("Tope 2:", dls(red, "Entrada", "Taller", 2))
    print("Tope 3:", dls(red, "Entrada", "Taller", 3))
