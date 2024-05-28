import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style 
import math
import seaborn as sns
import itertools

# 1 užduotis
print("\n=== 1 užduotis ===\n")

# nuo1 = 1
# iki1 = 10
# zingsnis1 = 0.001

# x1 = np.arange(nuo1, iki1 + zingsnis1, zingsnis1)
x1 = np.linspace(0, 10, 1000)
y1 = (lambda x: ((x-5)**2) / 4)(x1)

plt.style.use("seaborn-v0_8")
plt.plot(x1, y1)
plt.show()

# 2 užduotis
print("\n=== 2 užduotis ===\n")

x2 = np.linspace(-1, 1,10000)

def asin(x):
    return math.asin(math.pi * x)

# y2sin = np.array([math.sin(math.pi * x) for x in x2])
# y2cos = np.array([math.cos(math.pi * x) for x in x2])

y2sin = np.sin(math.pi * x2)
y2cos = np.cos(math.pi * x2)

plt.plot(x2, y2sin)
plt.plot(x2, y2cos)
plt.show()

# 3 užduotis
print("\n=== 3 užduotis ===\n")

fig, axs = plt.subplots(5, figsize=(5, 9))

x3 = np.linspace(-1, 1,10000)
y3 = []

pallete = itertools.cycle(sns.color_palette())

for i, axi in enumerate(axs):
    k = i + 1
    axi.plot(x3, np.sin(k * np.pi * x3), label = '$y = sin( %i x)$'%i)

# for i in range(0,5):
#     # y3.append(np.array([math.sin((i + 1) * math.pi * x) for x in x3]))
#     y3.append(np.sin((i + 1) * math.pi * x3))
#     axs[i].plot(x3, y3[-1], color=next(pallete), label = '$y = sin( %i x)$'%i)
#     # axs[i].figure(figsize=(3,3))

fig.legend(loc='upper left')
# fig.figure(figsize=(3,3))
plt.show()