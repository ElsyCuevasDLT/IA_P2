# Inteligencia Artificial - Parcial 2
# Alumna: Elsy Valeria Cuevas de la Torre
# Tema: 02 BusquedaCostoUniforme
# Version de practica con ejemplos y nombres propios.

"""
02 - Busqueda en Anchura de Coste Uniforme (UCS)
Variante de BFS que expande siempre el punto con menor coste acumulado.
Optima cuando los costos de las aristas son no negativos.
Idea principal: fila de prioridad (heap).
"""
import heapq


def ucs(red, origen, objetivo):
    pendientes = [(0, origen, [origen])]
    revisados = {}
    while pendientes:
        coste, punto, ruta = heapq.heappop(pendientes)
        if punto == objetivo:
            return ruta, coste
        if punto in revisados and revisados[punto] <= coste:
            continue
        revisados[punto] = coste
        for conexion, distancia in red.get(punto, []):
            nuevo = coste + distancia
            heapq.heappush(pendientes, (nuevo, conexion, ruta + [conexion]))
    return None, float("inf")


if __name__ == "__main__":
    print("--- Prueba de ejecucion: Elsy ---")
    red = {
        "Entrada": [("Pasillo", 1), ("Laboratorio", 4)],
        "Pasillo": [("Laboratorio", 2), ("Biblioteca", 5)],
        "Laboratorio": [("Biblioteca", 1)],
        "Biblioteca": [],
    }
    ruta, coste = ucs(red, "Entrada", "Biblioteca")
    print(f"Ruta: {ruta}  Coste total: {coste}")
