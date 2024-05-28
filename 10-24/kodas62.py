import sys
import os

# 5 užduotis
print("\n=== 5 užduotis ===\n")

argumentai = sys.argv[1:]
try:
    failo_pav = argumentai[0]
except IndexError:
    print("Truksta failo pavadinimo")
    sys.exit(1)

try:
    failo_objektas = open(failo_pav, "r")
except FileNotFoundError:
    print("failas nerastas\n")
    sys.exit(1)

eiluciu_sk = len(failo_objektas.readlines())
failo_objektas.seek(0)
print(f"Faile yra {eiluciu_sk} eilutes")

# # 6 užduotis
# print("\n=== 6 užduotis ===\n")

# failo_eilutes = failo_objektas.readlines()
# failo_objektas.seek(0)

# pirmos_eilutes = failo_eilutes[2:6]

# pirmi_duomenys = [[]]

# for index, eilute in enumerate(pirmos_eilutes):
#     for skaicius in eilute.split(' '):
#         if skaicius == '' or skaicius == ' ' or skaicius == "" or skaicius == " " or skaicius.isspace():
#             continue
#         else:
#             try:
#                 pirmi_duomenys[index].append(float(skaicius))
#             except IndexError:
#                 pirmi_duomenys.append([])
#                 pirmi_duomenys[index].append(float(skaicius))

# print("Duomenu pavyzdys:")

# for i in range(0, 4):
#     print(f"{i+1}: ", end="")
#     for duomenys in pirmi_duomenys:
#         print(f"{duomenys[i]}, ", end="")
#     print("")

# # 7 užduotis
# print("\n=== 7 užduotis ===\n")

# max_sk = float('-inf')
# max_ind = 0
# for i in range(0, 4):
#     if pirmi_duomenys[i][2] > max_sk:
#         max_sk = pirmi_duomenys[i][2]
#         max_ind = i
    
# print(max_sk)

# 6 užduotis
print("\n=== 6 užduotis ===\n")

pirmi_stulpeliai = [[], [], [], []]

failo_eilutes = failo_objektas.readlines()
failo_objektas.seek(0)

for eilute in failo_eilutes[2:]:
    eilute = eilute.split()
    for i in range(0,4):
        pirmi_stulpeliai[i].append(eilute[i])

print("Duomenu pavyzdys")
for index, stulpelis in enumerate(pirmi_stulpeliai):
    print(f"{index+1}: ", end="")
    for i in range(0, 4):
        print(f"{stulpelis[i]}", end="")
        if(i == 3):
            print("")
        else:
            print(", ", end="")

# 7 užduotis
print("\n=== 7 užduotis ===\n")

def max_verte(stulpelis):
    max_sk = float('-inf')
    max_ind = 0
    for index, verte in enumerate(stulpelis):
        if float(verte) > max_sk:
            max_sk = float(verte)
            max_ind = index
    return max_ind, max_sk

max_ind, max_sk = max_verte(pirmi_stulpeliai[2])


print(f"Didziausia 3 stulpelio verte: {max_sk}")
print(f"Ja atitinkaniti 2 stulpelio verte: {pirmi_stulpeliai[1][max_ind]}")

# 8 užduotis
print("\n=== 8 užduotis ===\n")

try:
    zingsnis = int(argumentai[1])
except IndexError:
    print("Truksta intervalo dydzio")
    sys.exit(1)
except ValueError:
    print("Intervalas turi buti sveikasis skaicius")
    sys.exit(1)

zingsniu_sk = 0

failo_turinys = failo_eilutes[2:]

class inter_duom:
    def __init__(self, inter, duomenys):
        self.inter = inter
        self.duomenys = duomenys
    def __repr__(self):  
        return f"{self.inter} : {self.duomenys}"
    
def failo_pav(inter_pradzia, zingsnis):
    return f"failas_{inter_pradzia}-{inter_pradzia+zingsnis}.txt"

duomenys = []

intervalai = []

for eilute in failo_turinys:
    intervalo_pradzia = int(float(eilute.split()[0])//zingsnis*zingsnis)
    intervalai.append(intervalo_pradzia)
    duomenys.append(inter_duom(intervalo_pradzia, eilute))

intervalai = sorted(set(intervalai))

for sk in intervalai:
    f_pav = failo_pav(sk, zingsnis)
    try:
        failo_objektas = open(f_pav, "x")
    except FileExistsError:
        # ats = input("Failas jau egzistuoja, ar istrinti(y/n)?: ")
        # if ats.lower() == 'y':
        os.remove(f_pav)
        failo_objektas = open(f_pav, "x")
        # else:
            # print("Testi negalima")
            # sys.exit(1)
    failo_objektas.close()

for item in duomenys:
    f_pav = failo_pav(item.inter, zingsnis)
    try:
        failo_objektas = open(f_pav, "a")
    except FileNotFoundError:
        print("Failas neegzistuoja")
        sys.exit(1)
    failo_objektas.write(item.duomenys)

# suintervaluotas_turinys = {} # kiekvienai eilutei bus priskirtas key kuris rodis intervalo pradzia

# for duomuo in 

# apdorotas_turinys = [[]] # kiekvienam stulpeliui yra atskiras listas liste


# for eilute in failo_turinys:
#     for stulp_nr, stulpelis in enumerate(eilute.split()):
#         if(len(apdorotas_turinys) <= stulp_nr):
#             apdorotas_turinys.append([])
#         apdorotas_turinys[stulp_nr].append(stulpelis)

# apdorotas_turinys.insert(0, [])
# for ind, duomuo in enumerate(apdorotas_turinys[1]):
#     apdorotas_turinys[0].append(float(duomuo)//zingsnis*zingsnis)

# intervalai = sorted(set(apdorotas_turinys[0]))

# for sk in intervalai:
#     f_pav = f"failas_{int(sk)}-{int(sk+zingsnis)}.txt"
#     try:
#         failo_objektas = open(f_pav, "x")
#     except FileExistsError:
#         # ats = input("Failas jau egzistuoja, ar istrinti(y/n)?: ")
#         # if ats.lower() == 'y':
#         os.remove(f_pav)
#         failo_objektas = open(f_pav, "x")
#         # else:
#             # print("Testi negalima")
#             # sys.exit(1)
#     failo_objektas.close()

# for ind, intervalo_pradzia in enumerate(apdorotas_turinys[0]):
#     f_pav = f"failas_{int(intervalo_pradzia)}-{int(intervalo_pradzia+zingsnis)}.txt"
#     failo_objektas = open(f_pav, "a")
#     failo_objektas.write(f"{}")

# 9 užduotis
print("\n=== 9 užduotis ===\n")

for i in intervalai:
    f_pav = failo_pav(i, zingsnis)
    try:
        failo_objektas = open(f_pav, "r")
    except FileNotFoundError:
        print("Failas neegzistuoja")
    max_3_stulp = float('-inf')
    max_2_stulp = -1
    max_ind = 0
    for ind, eil in enumerate(failo_objektas.readlines()):
        eil = eil.split()
        if float(eil[2]) > max_3_stulp:
            max_3_stulp = float(eil[2])
            max_2_stulp = float(eil[1])
            max_ind = ind
    print(f"Failas {f_pav}:")
    print(f"\t- Didziausia 3 stulpelio reiksme: {max_3_stulp}")
    print(f"\t- Ja atitinkanti 2 stulpelio reiksme: {max_2_stulp}")

# 10 užduotis
print("\n=== 10 užduotis ===\n")

try:
    failo_objektas = open(failo_pav, "r")
except FileNotFoundError:
    print("failas nerastas\n")
    sys.exit(1)

for item in failo_objektas.readlines():
    print(item)