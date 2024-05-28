import matplotlib.pyplot as plt
import sys

def arange(start, stop, step):
    steps = []
    i = start
    while i <= stop:
        steps.append(round(i, 11))
        i+=step
    return steps

def poly(x, coefs):
    y = 0
    for n, coef in enumerate(coefs):
        y += coef * pow(x, n)
    return y

def derivative(X, Y):
    Xder = X[:-1]
    Yder = []
    for n, x in enumerate(Xder):
        Yder.append((Y[n+1]-Y[n])/(X[n+1]-x))
    return Xder, Yder

def integrate(X, Y):
    I = [0]
    for n, x in enumerate(X[:-1]):
        I.append(I[n]+(((Y[n+1]+Y[n])/(2))*(X[n+1]-X[n])))
    return I

def polinomas(coefs):
    pol = "P(x)="
    for n, coef in enumerate(coefs):
        if coef != 0:
            if coef > 0:
                pol += f" +{coef}*x^{n}"
            else:
                pol += f" {coef}*x^{n}"
    return pol

# def saknys(x_i, x_f, coefs):
#     delta = 0.1
#     X_skn = []
#     while x_i < x_f:
#         if (poly(x_i-delta, coefs) < 0 and poly(x_i+delta, coefs) > 0) or (poly(x_i-delta, coefs) > 0 and poly(x_i+delta, coefs) < 0):
#             X_skn.append(x_i)
#         x_i+=delta
#     return X_skn

def saknys(X, Y):
    X_skn = []
    for n, y in enumerate(Y):
        



# 1 užduotis
print("\n=== 1 užduotis ===\n")

argumentai = sys.argv[1:]

intervalas = [float(x) for x in argumentai[0][1:-1].split(',')]
koeficientai = [int(x) for x in sys.argv[2:]]

print(f"Intervalas {intervalas}")
print(f"Koeficientai {koeficientai}")

# 2 užduotis
print("\n=== 2 užduotis ===\n")

dx = 0.1

X = arange(intervalas[0], intervalas[-1], dx)
Y = [poly(x, koeficientai) for x in X]

print(X)

# 3 užduotis
print("\n=== 3 užduotis ===\n")

# 4 užduotis
print("\n=== 4 užduotis ===\n")

Xder, Yder = derivative(X, Y)

print(derivative([0,1,2,3], [1,2,5,10]))

# 5 užduotis
print("\n=== 5 užduotis ===\n")

I = integrate(X,Y)

# 6 užduotis
print("\n=== 6 užduotis ===\n")

plt.plot(X,Y)
plt.plot(Xder,Yder)
plt.plot(X, I)

plt.legend(["$P(x)$", "$P^\prime(x)$", "$\int_a^x P(y) dy$"])

plt.show()

# 7 užduotis
print("\n=== 7 užduotis ===\n")

print(polinomas(koeficientai))

# 8 užduotis
print("\n=== 8 užduotis ===\n")

print(saknys(intervalas[0], intervalas[-1], koeficientai))