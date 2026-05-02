# Inteligencia Artificial - Parcial 2
# Alumna: Elsy Valeria Cuevas de la Torre
# Tema: 03 BusquedaEnProfundidad
# Version de practica con ejemplos y nombres propios.

"""
03 - Busqueda en Profundidad (DFS - Depth-First Search)
Explora cada rama hasta el final antes de retroceder. Usa pila (LIFO),
ya sea explicita o por recursion. No garantiza ruta mas corto.
"""


def dfs(red, origen, objetivo, revisados=None, ruta=None):
    if revisados is None:
        revisados, ruta = set(), [origen]
    revisados.add(origen)
    if origen == objetivo:
        return ruta
    for conexion in red.get(origen, []):
        if conexion not in revisados:
            salida = dfs(red, conexion, objetivo, revisados, ruta + [conexion])
            if salida:
                return salida
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
    print("Ruta DFS Entrada -> Taller:", dfs(red, "Entrada", "Taller"))
