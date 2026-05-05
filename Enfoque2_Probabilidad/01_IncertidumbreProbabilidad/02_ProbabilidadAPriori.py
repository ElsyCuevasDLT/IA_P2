# Inteligencia Artificial - Parcial 2
# Alumna: Elsy Valeria Cuevas de la Torre
# Tema: 02 ProbabilidadAPriori
# Version de practica con ejemplos y nombres propios.

"""
02 - Probabilidad a Priori (P(X))
Probabilidad de un evento sin condicionar en evidencia. Aqui se calcula
a partir de una tabla de frecuencias.
"""


def a_priori(tabla):
    total = sum(tabla.values())
    return {k: v / total for k, v in tabla.items()}


if __name__ == "__main__":
    print("--- Prueba de ejecucion: Elsy ---")
    clima = {"sol": 70, "nublado": 20, "lluvia": 10}
    print("P(clima):", a_priori(clima))
