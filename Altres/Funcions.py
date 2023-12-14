def canvi(l, m, n):
    print("{}{} \n {}".format(l, m, n))
    l = "Adeu"
    m = "Jrdi"
    n = "Que vagi bé"
    print("2) {}{} \n".format(l, m, n))
#programa principal
a = "Hola, "
b  = "Jordi"
c = "Que vagi bé"
print("El valor de la variable abans de cambiar és: {}{}\n {}".format(a, b, c))
canvi(a, b, c)
print("El valor de la variable despres de cambiar és: {}{}\n {}".format(a, b, c))








("""def canvi(l):
    x = input("Introdueix la calu per canviar: ")
    l[x] = int(input("Introdueix el nou valor per aquesta clau: "))
#programa principal
a = {"a":3, "b":4, "c":5, "d":7, "e":9, "f":10}
print("El valor de la lista abans de canviar és: {}".format(a))
canvi(a)
print("El valor de la llista després de canviar és: {}".format(a))""")









("""def canvi(l):
    x = int(input("Introdueix el valor a inserir al conjunt: "))
    l.add(x)
#programa principal
a = {3, 4, 5, 7, 10}
print("El valor del conjunt abans de canviar és: {}".format(a))
canvi(a)
print("El valor del conjunt després de canviar és: {}".format(a))""")









("""def canvi(l):
    x = int(input("Introdueix la posició modificar: "))
    l[x] = input("Introdueix el valor inserir: ")
#programa principal
a = [3, 4, 5, 6, 7, 8, "a", (1, 2), (3, 4), 10]
print("El valor de la lista abans de canviar és: {}".format(a))
canvi(a)
print("El valor de la llista després de canviar és: {}".format(a))""")