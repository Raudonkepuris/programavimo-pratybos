from math import sqrt, cbrt

x = 5
y = 9
print("x = " + str(x) + ", y = " + str(y))
z = x + y
print("z = " + str(z))
print("x^z = " + str(pow(x, z)) + "\ny^z = " + str(pow(y, z)))
print("sqrt(x) = " + str(sqrt(x)) + ", sqrt(y) = " + str(sqrt(y)))
print("cbrt(x) = " + str(cbrt(z)))
r_1 = (x+y)*(x-y)
r_2 = (x+y)/(x-y)
print("r_1 = " + str(r_1) + "\nr_2 = " + str(r_2))
vardas = input("Ivesti varda: ")
skaicius = input("Ivesti megstama skaiciu: ")
print("Vardas yra " + vardas)
print("Mano vardas yra " + vardas + " ir aš mėgstu skaičių " + skaicius)
print(vardas*int(skaicius))
spalva = input("Ivesti spalva: ")
print(vardas + spalva)