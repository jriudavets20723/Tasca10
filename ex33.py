def comptar_vocals(a):
    b = ('a', 'e', 'i', 'o', 'u', 'altres')
    vocals = [0, 0, 0, 0, 0, 0]
    for i, e in enumerate(a):
        if e.lower() == 'a' or e.lower() == 'à' or e.lower() == 'á':
            vocals[0] += 1
        elif e.lower() == 'e' or e.lower() == 'è' or e.lower() == 'é':
            vocals[1] += 1
        elif e.lower() == 'i' or e.lower() == 'í':
            vocals[2] += 1
        elif e.lower() == 'o' or e.lower() == 'ò' or e.lower() == 'ó':
            vocals[3] += 1
        elif e.lower() == 'u' or e.lower() == 'ú':
            vocals[4] += 1
        else:
            vocals[5] += 1
    for i, e in enumerate(vocals):
        print("La vocal {} apareix {} vegades".format(b[i], vocals[i]))

# Programa principal
a = input("Introdueixi una paraula a analitzar: ")
comptar_vocals(a)