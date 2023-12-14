from random import randint

def llista_20_elements():
    l = [randint(1, 100) for _ in range(20)]
    return l

def hi_ha_duplicats(a):
    seen = set()
    dupes = [x for x in a if x in seen or seen.add(x)]
    if len(dupes) > 0:
        print("La llista {} té elements duplicats {}".format(a, dupes))
    else:
        print("La llista {} no té elements duplicats {}".format(a, dupes))

# Programa principal
x = llista_20_elements()
hi_ha_duplicats(x)
