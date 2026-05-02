# Inteligencia Artificial - Parcial 2
# Alumna: Elsy Valeria Cuevas de la Torre
# Tema: 05 BusquedaProfundidadIterativa
# Version de practica con ejemplos y nombres propios.

"""
05 - Busqueda en Profundidad Iterativa (IDDFS)
Combina ventajas de BFS (completitud, optimalidad en grafos sin pesos)
con la baja memoria de DFS, repitiendo busquedas con tope creciente.
"""


def dls(red, punto, objetivo, tope, ruta):
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


def iddfs(red, origen, objetivo, max_profundidad=20):
    for tope in range(max_profundidad + 1):
        res = dls(red, origen, objetivo, tope, [origen])
        if res:
            return res, tope
    return None, -1


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
    ruta, nivel = iddfs(red, "Entrada", "Taller")
    print(f"Ruta: {ruta}  Profundidad: {nivel}")
