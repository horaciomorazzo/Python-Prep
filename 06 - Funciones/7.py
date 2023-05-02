# Ingresando número negativo se convierte a positivo.
# Los no enteros se convierten a la parte entera.
def factorial(n):
    entero = abs(int(n))
    if entero > 1:
        entero = entero * factorial(entero - 1)
    return entero


