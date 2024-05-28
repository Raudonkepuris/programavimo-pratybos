from math import sqrt

#UZD 1

# zodis = input("Ivesti zodi turinti ne maziau nei 10 raidziu.\n")
zodis = "adsadfasdfasdf"

if len(zodis) >= 10:
    if len(zodis) % 2 == 0:
        pozymis = "lyginis"
    else:
        pozymis = "nelygis"
else:
    print("Zodis per trumpas\n")
    exit()

print(f"Žodyje {zodis} yra {pozymis} raidžių skaičius.")

#UZD 2

zodzio_lst = list(zodis)

for ch in zodzio_lst:
    print(ch, end=" ")
print("\n")

#UZD 3

# xy = input("Ivesti dvizenkli skaiciu\n")
# xy_ch = input("Ivesti dvi bet kokias raides\n")

xy = "29"
xy_ch = "XW"

if len(xy) > 2 or len(xy_ch) > 2:
    print("Ivestis neteisinga\n")
    exit()

xy_lst = list(xy)
xy_ch_lst = list(xy_ch)

for i, n in enumerate(xy_lst):
    ind = 0
    if int(n) == 0:
        ind = 10
    else:
        ind = int(n)
    zodzio_lst[ind-1] = xy_ch_lst[i]

for ch in zodzio_lst:
    print(ch, end=" ")
print("\n")

#UZD 4

naujas_zodis = "-".join(zodzio_lst)
print(naujas_zodis)

#UZD 5

# sarasas_a = sarasas_b = sarasas_c = list()

sarasai_abc = [list(), list(), list()]
salygos = ["dalijasi is 3 ir 4", "dalijasi is 3 bet ne is 4", "dalijasi is 3 arba 6, bet ne is 4"]
for i in range(1, 101):
    if i % 3 == 0 and i % 4 == 0:
        sarasai_abc[0].append(i)
    if i % 3 == 0 and i % 4 != 0:
        sarasai_abc[1].append(i)
    # if i % 6 == 0 and i % 4 != 0:
    #     sarasai_abc[2].append(i)
    if (i % 3 == 0 or i % 6 == 0) and i % 4 != 0:
        sarasai_abc[2].append(i)

for n, lst in enumerate(sarasai_abc):
    print(f"Skaiciai kurie {salygos[n]}:")
    for i in lst:
        print(i, end=" ")
    print("\n")

#UZD 6

b1 = 1
q = 2

geometr_seka = list()

for i in range(1,20):
    geometr_seka.append(b1*pow(q, i))
for x in geometr_seka:
    print(x, end=" ")
print("\n")

#UZD 7
sum = 0
for x in geometr_seka:
    sum += x
print(sum)

#UZD 8
# sakinys = print("Ivesti sakini is minimum 3 zodziu\n")
sakinys = "Jonas yra puikus fizikas"
sakinio_zdz_lst = sakinys.split(" ")
print(f"Sakinyje yra {len(sakinio_zdz_lst)} zodziai")
sakinio_rdz_lst = list(sakinys)
balses = ["a", "e", "i", "o", "u"]

balses_cnt = priebalses_cnt = 0

for raide in sakinio_rdz_lst:
    if raide == " ":
        continue
    elif raide.lower() in balses:
        balses_cnt += 1
    else:
        priebalses_cnt += 1

print(f"Sakinyje yra {balses_cnt} balses ir {priebalses_cnt} priebalses")

#UZD 9
matavimai = [17.5, 18.7, 18.8, 20.4, 23.4, 19.7, 16.0, 16.6, 16.7, 17.4,
18.9, 21.1, 21.4, 21.9, 23.8, 24.3, 23.8, 24.6, 24.3, 19.8, 19.8, 22.1,
23.4, 24.6, 23.8, 20.3, 23.9, 22.4, 21.3, 17.7, 14.4]

# matavimai = [10, 12, 23, 23, 16, 23, 21, 16]

sum = 0
for m in matavimai:
    sum += m
vidurkis = sum / len(matavimai)
print(vidurkis)

matavimai_cp = sorted(matavimai)

mediana = 0
if len(matavimai_cp) % 2 == 0:
    mediana_ind = int(len(matavimai_cp) / 2)
    mediana = (matavimai_cp[mediana_ind] + matavimai_cp[mediana_ind-1]) / 2.0
else:
    mediana_ind = int((len(matavimai_cp) / 2) - 0.5)
    mediana = matavimai_cp[mediana_ind]

print(mediana)

skaitiklis = 0
for i in matavimai:
    skaitiklis += (i-vidurkis)**2

std_nuokrypis = sqrt(skaitiklis/len(matavimai))
print(std_nuokrypis)