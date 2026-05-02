# Inteligencia Artificial - Parcial 2
# Alumna: Elsy Valeria Cuevas de la Torre
# Tema: 07 BusquedaEnGrafos
# Version de practica con ejemplos y nombres propios.

"""
07 - Busqueda en Grafos (Graph Search generico)
Esquema generalizado de busqueda con conjunto de explorados,
parametrizable por la estrategia (fila, pila, prioridad).
Evita re-expansion de estados ya vistos.
"""
from collections import deque
import heapq


def graph_search(red, origen, objetivo, estrategia="bfs"):
    if estrategia == "bfs":
        pendientes = deque([(origen, [origen])])
        pop = pendientes.popleft
        push = lambda x: pendientes.append(x)
    elif estrategia == "dfs":
        pendientes = [(origen, [origen])]
        pop = pendientes.pop
        push = lambda x: pendientes.append(x)
    else:
        raise ValueError("estrategia debe ser bfs o dfs")
    explorados = set()
    while pendientes:
        punto, ruta = pop()
        if punto == objetivo:
            return ruta
        if punto in explorados:
            continue
        explorados.add(punto)
        for conexion in red.get(punto, []):
            if conexion not in explorados:
                push((conexion, ruta + [conexion]))
    return None


if __name__ == "__main__":
    print("--- Prueba de ejecucion: Elsy ---")
    red = {
        "Entrada": ["Pasillo", "Laboratorio"], "Pasillo": ["Biblioteca"], "Laboratorio": ["Biblioteca", "Salon"],
        "Biblioteca": ["Taller"], "Salon": ["Taller"], "Taller": [],
    }
    print("BFS:", graph_search(red, "Entrada", "Taller", "bfs"))
    print("DFS:", graph_search(red, "Entrada", "Taller", "dfs"))
