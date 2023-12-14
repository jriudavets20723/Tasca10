def mostrar_majors_que(t, nreferencia):
    print("Tots els números majors de {} són: ".format(nreferencia))
    for e in t:
        if e > int(nreferencia):
            print("{} ".format(e))

def llegir_llista():
    # Prec: Llegeix una llista de números
    # Post: Retorna la llista llegida.
    b = []
    a = "a"
    while a != ".":
        a = input("Introdueixi el següent número (Introdueix un punt per acabar): ")
        if a != ".":
            b.append(int(a))
        else:
            return b

# Programa principal
i = input("Introdueixi el número que voleu comparar: ")
x = llegir_llista()
a = tuple(x)
mostrar_majors_que(a, i)
