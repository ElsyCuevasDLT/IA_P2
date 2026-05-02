# Inteligencia Artificial - Parcial 2
# Alumna: Elsy Valeria Cuevas de la Torre
# Tema: 06 BusquedaBidireccional
# Version de practica con ejemplos y nombres propios.

"""
06 - Busqueda Bidireccional
Lanza dos BFS simultaneas: una desde el origen y otra desde la objetivo.
Termina cuando ambas fronteras se encuentran. Reduce drasticamente
el espacio explorado: 2 * b^(d/2) en lugar de b^d.
"""
from collections import deque


def expandir(red, pendientes, padres, otra_frontera):
    nuevos = {}
    for punto in pendientes:
        for conexion in red.get(punto, []):
            if conexion not in padres:
                padres[conexion] = punto
                nuevos[conexion] = True
                if conexion in otra_frontera:
                    return conexion, nuevos
    return None, nuevos


def bidireccional(red, origen, objetivo):
    if origen == objetivo:
        return [origen]
    padres_i = {origen: None}
    padres_m = {objetivo: None}
    front_i = {origen: True}
    front_m = {objetivo: True}
    while front_i and front_m:
        encuentro, front_i = expandir(red, front_i, padres_i, padres_m)
        if encuentro:
            return reconstruir(padres_i, padres_m, encuentro)
        encuentro, front_m = expandir(red, front_m, padres_m, padres_i)
        if encuentro:
            return reconstruir(padres_i, padres_m, encuentro)
    return None


def reconstruir(padres_i, padres_m, encuentro):
    ruta = []
    n = encuentro
    while n is not None:
        ruta.append(n)
        n = padres_i.get(n)
    ruta.reverse()
    n = padres_m.get(encuentro)
    while n is not None:
        ruta.append(n)
        n = padres_m.get(n)
    return ruta


if __name__ == "__main__":
    print("--- Prueba de ejecucion: Elsy ---")
    red = {
        "Entrada": ["Pasillo", "Laboratorio"], "Pasillo": ["Entrada", "Biblioteca"], "Laboratorio": ["Entrada", "Salon"],
        "Biblioteca": ["Pasillo", "Taller"], "Salon": ["Laboratorio", "Taller"], "Taller": ["Biblioteca", "Salon", "G"], "G": ["Taller"],
    }
    print("Ruta bidireccional A -> G:", bidireccional(red, "Entrada", "G"))
