from math import tan, radians

a = input("Įvesti lygiakraščio daugiakampio kraštinės ilgį: ")
n = input("Įvesti lygiakraščio daugiakampio kampų skaičių: ")

a = int(a)
n = int(n)

P = a * n
a = (a) / (2 * tan(radians(180)/n))

S = (P * a) / 2

print("Plotas = ", S)