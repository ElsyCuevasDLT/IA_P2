# Inteligencia Artificial - Parcial 2
# Alumna: Elsy Valeria Cuevas de la Torre
# Tema: 33 RefuerzoPasivo
# Version de practica con ejemplos y nombres propios.

"""
33 - Aprendizaje por Refuerzo Pasivo
Politica fija: el agente solo evalua V_pi(s) a partir de episodios.
Aqui se usa Monte Carlo first-visit.
"""
import random


def mc_pasivo(politica, episodios_gen, n=500, gamma=0.9):
    V = {}
    cuenta = {}
    for _ in range(n):
        ep = episodios_gen(politica)
        G = 0
        visto = set()
        for t in reversed(range(len(ep))):
            s, _, r = ep[t]
            G = gamma * G + r
            if s not in visto:
                visto.add(s)
                V[s] = V.get(s, 0.0) + (G - V.get(s, 0.0)) / (cuenta.get(s, 0) + 1)
                cuenta[s] = cuenta.get(s, 0) + 1
    return V


if __name__ == "__main__":
    print("--- Prueba de ejecucion: Elsy ---")
    estados = ["Entrada", "Pasillo", "Laboratorio", "T"]
    politica = {"Entrada": "der", "Pasillo": "der", "Laboratorio": "der"}

    def episodio(pi):
        s = "Entrada"
        ep = []
        while s != "T":
            a = pi[s]
            sp = {"Entrada": "Pasillo", "Pasillo": "Laboratorio", "Laboratorio": "T"}[s]
            r = -1 if sp != "T" else 10
            ep.append((s, a, r))
            s = sp
        return ep

    V = mc_pasivo(politica, episodio)
    print("V(pi):", {k: round(v, 3) for k, v in V.items()})
