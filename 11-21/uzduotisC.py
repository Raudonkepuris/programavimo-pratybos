import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style 
import seaborn as sns
import sympy as sym

# 1 užduotis
print("\n=== 1 užduotis ===\n")

def harmonics(period,freq,n=100):
    x = np.linspace(0, period * 2 * np.pi, n)
    return x, np.array(np.sin(freq * x))

x, y = harmonics(10,20)

# 2 užduotis
print("\n=== 2 užduotis ===\n")

def radianticks(period, tpp=4): # tpp = ticks per period, default = 4
    x = np.arange(0,360*period+90,360/tpp)
    x_ticks = np.radians(x)
    x_labels = []
    for i in x:
        c = int(i/x[1])
        label = f"${sym.printing.latex(sym.simplify(2*c*sym.pi/tpp))}$"
        x_labels.append(label)
    return(x_ticks, x_labels)

x, y = harmonics(1,1)
x_ticks, x_labels = radianticks(1)
plt.plot(x,y)
plt.xticks(x_ticks, x_labels)
plt.show()