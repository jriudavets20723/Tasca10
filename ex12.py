#Funcions
def menu_principal():
    print("""
            Menú Principal
            1.Calculadora enters
            2.Calculadora reals
            3.Canvis de base
            4.Exit   
          
    """)
    a = int(input("Tria una opció: ")) 
    return a

def calculadora_enters():
    op = 1
    while op>0:
        print("""
              Menú Enters
              1.Sumar
              2.Restar
              3.Multiplicar
              4.Dividir
              5.Exit
        """)
        op = int(input("Elegeix una opcio: "))
        match op: 
            case 1: #sumar
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Introduewix el seguent nombre: "))
                print("{} + {} = {}")
            case 2: #restar
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Introduewix el seguent nombre: "))
                print("{} - {} = {}". format(x, y, x-y))
            case 3: #multiplicar
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Introduewix el seguent nombre: "))
                print("{} * {} = {}". format(x, y, x*y))
            case 4: #dividir
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Introduewix el seguent nombre: "))
                print("{} / {} = {}". format(x, y, x/y))
            case 5: #sortir
                print("Has tornat al menu principal \n\n")
                op = -1
def calculadora_reals():
    op = 1
    while op>0:
        print("""
              Menú Reals
              1.Sumar
              2.Restar
              3.Multiplicar
              4.Dividir
              5.Exit
        """)
        op = int(input("Elegeix una opcio: "))
        match op: 
            case 1: #sumar
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Introduewix el seguent nombre: "))
                print("{} + {} = {}")
            case 2: #restar
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Introduewix el seguent nombre: "))
                print("{} - {} = {}". format(x, y, x-y))
            case 3: #multiplicar
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Introduewix el seguent nombre: "))
                print("{} * {} = {}". format(x, y, x*y))
            case 4: #dividir
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Introduewix el seguent nombre: "))
                print("{} / {} = {}". format(x, y, x/y))
            case 5: #sortir
                print("Has tornat al menu principal \n\n")
                op = -1

def canvis_base():
    cb = 1
    while cb>0:
            print("""
                  Menú canvis de base

                  1.De binari a altres bases
                  2.De octal a altres bases
                  3.De decimal a altres bases
                  4.De hexadecimal a altres bases
                  5.Exit
                  """)

            cb = int(input("Elegeix una opcio: "))
            match cb:
                case 1:#Binari
                    b = input("Introdueix el numero binari: ")
                    o = bintooct(b)
                    d = bintodec(b)
                    h  = bintohex(b)
                    print("El número binari {} és: \n oct --> {} \n dec --> {} \n hex --> {}".format(b, o, d, h))

                case 2:#Octal
                    o = input("Introdueix el numero octal: ")
                    b = octtobin(o)
                    d = octtodec(o)
                    h  = octtohex(o)
                    print("El número octal {} és: \n bin --> {} \n dec --> {} \n hex --> {}".format(o, b, d, h))

                case 3:#Decimal
                    d = input("Introdueix el numero decimal: ")
                    b = dectobin(d)
                    o = dectooct(d)
                    h  = dectohex(d)
                    print("El número decimal {} és: \n bin --> {} \n oct --> {} \n hex --> {}".format(d, b, o, h))

                case 4:#Hexadecimal
                    h = input("Introdueix el numero hexadecimal: ")
                    b = hextobin(h)
                    o = hextooct(h)
                    d = hextodec(h)
                    print("El número hexadecimal {} és: \n bin --> {} \n oct --> {} \n dec --> {}".format(h, b, o, d))

                case 5:#sortir
                    print("Has tornat al menú de inici")
                    cb = -1


#funcion canvis de base
def dectobin(numero):
    #a
    return bin(numero)
def dectooct(numero):
    #a
    return oct(numero)
def dectohex(numero):
    #a
    return hex(numero)
def bintooct(numero):
    #a
    a=int(numero, 2)
    return dectooct(a)
def bintodec(numero):
    #a
    a=int(numero, 2)
    return a
def bintohex(numero):
    #a
    a=int(numero, 2)
    return dectohex(a)
def octtobin(numero):
    #a
    a=int(numero, 8)
    return dectobin(a)
def octtodec(numero):
    #a
    a=int(numero, 8)
    return a
def octtohex(numero):
    #a
    a=int(numero, 8)
    return dectohex(a)
#-----------------------------
def hextodec2(hex):
    hex = hex.lower()
    hex = hex[::-1]
    decimal = 0
    posicio = 0
    for digit in hex:
        valor = hextonum(digit)
        elevat = 16 ** posicio
        pnum = elevat * valor
        decimal += pnum 
    return decimal
def hextobin(numero):
        #a
    a = int(numero, 16)
    return dectobin(a)
def hextooct(numero):
        #a
    a = int(numero, 16)
    return dectooct(a)
def hextodec(numero):
        #a
    a = int(hextodec2(numero))
    return a
#---------------------------------
#Programa principal
a = 1
while a>0:
    a = menu_principal()
    match a: 
        case 1:
            calculadora_enters()
        case 2: 
            calculadora_reals()
        case 3:
            canvis_base()
        case 4:
            a = -1
        case other:
            print("Ópcio no vàlida")