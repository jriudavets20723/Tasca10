a = int(input("introdueix un nombre: "))
b = int(input("Introdueix un segon nombre: "))

def gran():
    if a>b:
        return a
    elif b>a:
        return b
    else:
        print("Són iguals")
        
print(gran())