def noms_que_comencen_per(llista, lletra):
    comptador = 0
    llnom = []
    for e in llista:
        if e[0] == lletra:
            llnom.append(e)
            comptador += 1
    print("El número de noms que comencen per el caràcter {} són: {} i són: {}".format(lletra, comptador, llnom))

def llegir_llista():
    # Prec: Llegeix una llista de paraules, en el nostre cas de noms
    # Post: Retorna la llista llegida.
    b = []
    a = "a"
    while a != ".":
        a = input("Introdueixi el següent nom (Introdueix un punt per aturar): ")
        if a != ".":
            b.append(a)
        else:
            return b

# Programa principal
noms = llegir_llista()
lletra = input("Introdueixi el caràcter de referència: ")
noms_que_comencen_per(noms, lletra)