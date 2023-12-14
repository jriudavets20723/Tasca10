def sumar_llista(a):
    suma = 0
    for i in a:
        suma += i
    return suma

def multiplicar_llista(a):
    multiplicar = 1
    for i in a:
        multiplicar *= i
    return multiplicar

# Ús de les funcions:
x = [3, 4, 5, 7]
print("La suma de tots els elements de la llista és:", sumar_llista(x))
print("La multiplicació de tots els elements de la llista és:", multiplicar_llista(x))
