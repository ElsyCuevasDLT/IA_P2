# Inteligencia Artificial - Parcial 2
# Alumna: Elsy Valeria Cuevas de la Torre
# Tema: 01 BusquedaEnAnchura
# Version de practica con ejemplos y nombres propios.

"""
01 - Busqueda en Anchura (BFS - Breadth-First Search)
Explora el red nivel por nivel desde el punto inicial, garantizando
encontrar la solucion mas corta en numero de aristas.
Idea principal: Fila FIFO.
"""
from collections import deque


def bfs(red, origen, objetivo):
    revisados = {origen}
    fila = deque([(origen, [origen])])
    while fila:
        punto, ruta = fila.popleft()
        if punto == objetivo:
            return ruta
        for conexion in red.get(punto, []):
            if conexion not in revisados:
                revisados.add(conexion)
                fila.append((conexion, ruta + [conexion]))
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
    print("Ruta BFS Entrada -> Taller:", bfs(red, "Entrada", "Taller"))
