def gran(a, b, c):
    if a>b>c:
        print("{} és major que {} que és major que {}".format(a,b,c))
    elif b>a>c:
        print("{} és major que {} que és major que {}".format(b,a,c))
    elif a>c>b:
        print("{} és major que {} que és major que {}".format(a,c,b))
    elif b>c>a:
        print("{} és major que {} que és major que {}".format(b,c,a))
    elif c>a>b:
        print("{} és major que {} que és major que {}".format(c,b,a))
    elif c>b>a:
        print("{} és major que {} que és major que {}".format(c,b,a))
    elif a>b==c:
        print("{} és major que {} que és igual que {}".format(a, b, c))
    elif a==b>c:
        print("{} i {} són iguals i majors que {}".format(a, b, c))
    elif a==c>b:
        print("{} i {} són iguals i majors que {}".format(a, c, b))
    elif b>a==c:
        print("{} és major que {} que és igual que {}".format(b, a, c))
    elif b==c>a:
        print("{} i {} són iguals i majors que {}".format(b, c, a))
    elif c>b==a:
        print("{} és major que {} que és igual que {}".format(c, b, a))
    else:
        print("Són iguals")

#Programa principal
a = int(input("introdueix un nombre: "))
b = int(input("Introdueix un segon nombre: "))
c = int(input("Introdueix un tercer nombre: "))
gran(a, b, c)