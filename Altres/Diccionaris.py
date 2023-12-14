dic = {"nom":"Pepe", "cognom":"Riudavets", "edat":"16", "telefon":"650090989"}
for element in dic:
    print("La clau {} té el valor {}".format(element, dic[element]))
#segona forma
for x,y in dic.items():
    print("La clau és {} i el seu valor és {}".format(x, y))
#dic.clear()
b = {"nom":"Pere", "cognom":"Pons", "edat":"26", "telefon":"777777777", "direccio":"cameva"}
dic.update(b)
print(dic)