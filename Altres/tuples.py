def tercera_ocurrencia(l, e):
    a = l.count(e)
    if a == 0:
        print("no hi ha cap ocurrencia")
    elif a == 1:
        print("La primera ocurrencia de l'element esta en la posicio {}".format(l.index(e)))
    elif a>2:
        print("hi ha més de dues ocurrencies de {}".format(e))
        p = l.index(e)
        so = l.index(e, (p+1))
        print(so)
    elif a==2:
        print("Hi ha mes de una ocurrencia de {}".format(e))
        p = l.index(e)
        so = l.index(e, (p+1))
        to = l.index(e, (so+1))
        print(to)
    else: 
        print("Només hi ha zero, una o dos ocurrències")

#programa principal
l = (1, 4, 2, (1, 3, 3), 3, 4, 2, 3, 1, 1, 4)
x = int(input("Elegeix l'element que volo cercar la 3a ocurrencia:  "))
tercera_ocurrencia(l, x)