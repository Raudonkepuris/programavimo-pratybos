import os

# 1 užduotis
print("\n=== 1 užduotis ===\n")

failo_pavadinimas = input("Ivesti failo pavadinima: ")
# studento_vardas = input("Ivesti studento varda: ")
# dalykas = input("Ivesti studijuojama dalyka: ")
# kursas = input("Ivesti kursa: ")
# pogrupis = input("Ivesti pogrupi: ")

# failo_pavadinimas = "test.txt"
studento_vardas = "Jonas"
dalykas = "Fizika"
kursas = "1"
pogrupis = "A"

failo_objektas = open(failo_pavadinimas, "x")
failo_objektas.write(f"{studento_vardas}. {dalykas}, {kursas}, {pogrupis}\n")
failo_objektas.close()

# 2 užduotis
print("\n=== 2 užduotis ===\n")

failo_pavadinimas = input("Ivesti failo pavadinima: ")
# studento_vardas = input("Ivesti studento varda: ")
# dalykas = input("Ivesti studijuojama dalyka: ")
# kursas = input("Ivesti kursa: ")
# pogrupis = input("Ivesti pogrupi: ")

# failo_pavadinimas = "test.txt"
studento_vardas = "Jonas2"
dalykas = "Fizika2"
kursas = "12"
pogrupis = "A2"

try:
    failo_objektas = open(failo_pavadinimas, "a")
except TypeError:
    print("Neteisingas failo pavadinimas\n")

failo_objektas.write(f"{studento_vardas}. {dalykas}, {kursas}, {pogrupis}\n")
failo_objektas.close()

# 3 užduotis
print("\n=== 3 užduotis ===\n")

zodis = input("Iveskite zodi: ")
failai = []

for i, ch in enumerate(zodis):
    # try:
    failo_objektas = open(f"raide_{i+1}.txt", "w")
    # except FileExistsError:
    #     os.remove(f"raide_{i+1}.txt")
    #     failo_objektas = open(f"raide_{i+1}.txt", "x")
    failai.append(f"raide_{i+1}.txt")
    failo_objektas.write(ch)
    failo_objektas.close()

# 4 užduotis
print("\n=== 4 užduotis ===\n")

atkurtos_raides = []

for failas in failai:
    failo_objektas = open(failas, "r")
    atkurtos_raides.append(failo_objektas.read())
    failo_objektas.close()

atkurtas_zodis = "".join(atkurtos_raides)
print(atkurtas_zodis)