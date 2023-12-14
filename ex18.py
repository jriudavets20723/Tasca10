def invertir(a):
    b = list(a)
    c = b[::-1]
    r = "".join(c)
    return r

# Programa principal
s = "Això és una cadena que s’ha de girar"
print("La cadena:", s, "girada és:", invertir(s))