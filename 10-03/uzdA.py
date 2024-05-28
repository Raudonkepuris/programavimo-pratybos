from math import floor

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = 1234567890

# i=0
# for x in letters:
#     print(x, " ", i)
#     i+=1

# print([(i, l) for i, l in enumerate(letters)])


vardas = letters[11].upper() + letters[8] + letters[20] + letters[19] + letters[0] + letters[20] + letters[17] + letters[0] + letters[18]
print(vardas)

auditorija = str(numbers)[2] + str(numbers)[0] + str(numbers)[0]
# print(auditorija)

sakinys = "Padalinkite auditorijos numeri˛ iš šiame sakinyje esanˇciu˛ simboliu˛ skaiˇciaus"
sakinio_len = len(sakinys)
dalyba = floor(int(auditorija)/sakinio_len)
liekana = int(auditorija)%sakinio_len
# print("Auditorijos numeris: ", auditorija)
# print("Sakinio ilgis: ", len(sakinys))
# print(auditorija, "//", sakinio_len, " = ", str(dalyba), "(liekana ",  str(liekana), ")")

print(f"Auditorijos numeris: {auditorija}")
print(f"Sakinio ilgis: {sakinio_len:d}")
print(f"{auditorija} // {sakinio_len:d} = {dalyba:d} (liekana {liekana:d})")

trecia_raide = vardas[2]
vardas = vardas.replace(trecia_raide, "X")
print(vardas)

duomenys = "Radial velocity = -55.423 dispersion = 0.902 FWHM = 12.129, 912 lines matched out of 5014"
skaitines_vertes = []

# print(duomenys.split())
for x in duomenys.split():
    if x.replace(".", "").replace("-", "").replace(",", "").isnumeric():
        skaitines_vertes.append(x.replace(",", ""))

print(skaitines_vertes)

skaitines_reiksmes = {
    "rv" : float(skaitines_vertes[0]),
    "disp" : float(skaitines_vertes[1]),
    "FWHM" : float(skaitines_vertes[2]),
    "matched_lines" : int(skaitines_vertes[3]),
    "all_lines" : int(skaitines_vertes[4])
}

proc_rastu_liniju = skaitines_reiksmes["matched_lines"] / skaitines_reiksmes["all_lines"] * 100
print(f"{proc_rastu_liniju:.2f}%")

duomenys = duomenys + f", percentage of found lines is {proc_rastu_liniju:.2f}%"
print(duomenys)

