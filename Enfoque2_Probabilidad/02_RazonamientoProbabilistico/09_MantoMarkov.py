# Inteligencia Artificial - Parcial 2
# Alumna: Elsy Valeria Cuevas de la Torre
# Tema: 09 MantoMarkov
# Version de practica con ejemplos y nombres propios.

"""
09 - Manto de Markov (Markov Blanket)
El Manto de Markov de un punto X en una red Bayesiana son: sus padres,
sus hijos y los padres de sus hijos. X es independiente del resto de
la red dado su manto.
"""


def manto_markov(punto, padres, hijos):
    manto = set(padres.get(punto, []))
    for h in hijos.get(punto, []):
        manto.add(h)
        manto.update(padres.get(h, []))
    manto.discard(punto)
    return manto


if __name__ == "__main__":
    print("--- Prueba de ejecucion: Elsy ---")
    padres = {"Entrada": [], "Pasillo": ["Entrada"], "Laboratorio": ["Entrada"], "Biblioteca": ["Pasillo", "Laboratorio"], "Salon": ["Biblioteca"]}
    hijos = {"Entrada": ["Pasillo", "Laboratorio"], "Pasillo": ["Biblioteca"], "Laboratorio": ["Biblioteca"], "Biblioteca": ["Salon"], "Salon": []}
    for n in padres:
        print(f"MB({n}) = {manto_markov(n, padres, hijos)}")
