import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style 
import math
import seaborn as sns
import itertools
import sympy as sym

# 1 užduotis
print("\n=== 1 užduotis ===\n")

def fizika(x, a, b, c):
    x = np.array(x)
    return np.array(a * np.exp(-1 * b * x) + c)

# 2 užduotis
print("\n=== 2 užduotis ===\n")

a = 2.5
b = 1.3
c = 0.5

x = np.linspace(0, 5, 20)

y = np.array(fizika(x, a, b, c))

# 3 užduotis
print("\n=== 3 užduotis ===\n")

y_matavimai = np.array(y + ( y * ((0.5 + 0.5) * np.random.random_sample(20) - 0.5) ))

# 4 užduotis
print("\n=== 4 užduotis ===\n")

coefs = np.polyfit(x, y_matavimai, 2)

x_apskaiciuotiems = np.linspace(0, 5, 100)
y_apskaiciuoti = np.array(coefs[0] * x_apskaiciuotiems**2 + coefs[1] * x_apskaiciuotiems + coefs[2])

# 5 užduotis
print("\n=== 5 užduotis ===\n")

sx = sym.symbols("x")
eq = sym.printing.latex(sym.Poly(reversed(np.round(coefs,3)),sx).as_expr())

plt.style.use("seaborn-v0_8")
plt.plot(x, y, "--", label="Nežinomas fizikos desnis") # punktyrin˙e linija
plt.plot(x, y_matavimai, "o", label="Matavimai") # burbuliukai
plt.plot(x_apskaiciuotiems, y_apskaiciuoti, label="$y={}$".format(eq))
plt.title("Matavimu, aproksimacija kvadratiniu polinomu")
plt.legend()
plt.show()
plt.show()