# Inteligencia Artificial - Parcial 2
# Alumna: Elsy Valeria Cuevas de la Torre
# Tema: 08 ReglaCadena
# Version de practica con ejemplos y nombres propios.

"""
08 - Regla de la Cadena
P(X1, ..., Xn) = Producto de P(Xi | X1, ..., X(i-1)).
En una red Bayesiana se simplifica a producto de P(Xi | padres(Xi)).
"""


def cadena(orden, conjuntas_marginales):
    p = 1.0
    historia = ""
    for v in orden:
        cond = conjuntas_marginales[v].get(historia, conjuntas_marginales[v][""])
        p *= cond
        historia += v
    return p


if __name__ == "__main__":
    print("--- Prueba de ejecucion: Elsy ---")
    P = {"Entrada": {"": 0.6}, "Pasillo": {"Entrada": 0.8, "": 0.5}, "Laboratorio": {"AB": 0.3, "Entrada": 0.4, "": 0.2}}
    print("P(A,B,C) por regla de cadena:", cadena(["Entrada", "Pasillo", "Laboratorio"], P))
