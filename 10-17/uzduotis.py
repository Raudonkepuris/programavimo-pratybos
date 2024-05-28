# 1 užduotis
print("\n=== 1 užduotis ===\n")

# zodis = input("iveskite zodi: ")
# skaicius = input("iveskite skaiciu: ")

zodis = "fdsafsa"
skaicius = "4"

i = 0
while i < int(skaicius):
    print(zodis)
    i+=1

# 2 užduotis
print("\n=== 2 užduotis ===\n")

# pradzia = input("ivesti intervalo pradzia: ")
# pabaiga = input("ivesti intervalo pabaiga: ")

pradzia = "1"
pabaiga = "11"

print(f"nelyginiai skaiciai intervale [{pradzia},{pabaiga}]: ", end="")

i = int(pradzia)
while i <= int(pabaiga):
    if(i%2!=0):
        print(f"{i}", end="")
        if(int(pabaiga)-i>1):
            print(", ", end="")
    i+=1
print("\n")

# 3 užduotis
print("\n=== 3 užduotis ===\n")

zodynas = {
    "Jonas":1.85,
    "Gabija":1.75,
    "Erika":1.9
}

# 4 užduotis
print("\n=== 4 užduotis ===\n")

for key, val in zodynas.items():
    print(f"vardas: {key}, ugis: {val}")

# 5 užduotis
print("\n=== 5 užduotis ===\n")

ugiu_list = list(zodynas.values())

vardu_list = list(zodynas.keys())

# listsad = [k for k, v in zodynas.items() if v==max(zodynas.values())]

didziausias_ugis = max(ugiu_list)

didziausio_ugio_turetojo_ind = ugiu_list.index(didziausias_ugis)
print(f"Auksciausias zmogus yra {vardu_list[didziausio_ugio_turetojo_ind]}")

# 6 užduotis
print("\n=== 6 užduotis ===\n")

while input("Ar norite prideti nauja irasa? ").lower() ==  "taip":
    n_vardas = input("Iveskite nauja varda: ")
    n_ugis = input("Iveskite nauja ugi: ")
    zodynas[n_vardas] = float(n_ugis)

for key, val in zodynas.items():
    print(f"vardas: {key}, ugis: {val}")