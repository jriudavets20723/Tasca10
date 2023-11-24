#Funcions
def menu_principal():
    print("""
        Menú Principal
            1.Calculadora enters
            2.Calculadora reals
            3.Exit
              
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
                print("{} + {} = {}". format(x, y, x+y))

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
                print("Adeú, has tornat al menu principal \n\n")
                op = -1


def calculadora_reals():
    cal = 1
    while cal>0:
        print("""
              Menú Reals
              
              1.Sumar
              2.Restar
              3.Multiplicar
              4.Dividir
              5.Exit
        """)
        cal = int(input("Elegeix una opcio: "))
        match cal: 
            case 1: #sumar
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Introduewix el seguent nombre"))
                print("{} + {} = {}". format(x, y, x+y))

            case 2: #restar
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Introduewix el seguent nombre"))
                print("{} - {} = {}". format(x, y, x-y))
            
            case 3: #multiplicar
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Introduewix el seguent nombre"))
                print("{} * {} = {}". format(x, y, x*y))
            
            case 4: #dividir
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Introduewix el seguent nombre"))
                print("{} / {} = {}". format(x, y, x/y))

            case 5: #sortir
                print("Has tornat al menu principal \n\n")
                cal = -1                
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
            a = -1
        case other:
            print("Ópcio no vàlida")