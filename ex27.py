s = input("Introdueix una frase: ")

def majuscules_frase(s):
    num_maj = 0
    num_min = 0
    for e in s:
        if e.isupper():
            num_maj += 1
        elif e.islower():
            num_min += 1
    print("La frase '{}' té {} majúscules i {} minúscules.".format(s, num_maj, num_min))

majuscules_frase(s)