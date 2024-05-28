import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1 užduotis
print("\n=== 1 užduotis ===\n")

start = 0.25
stop = 1
step = 0.25

S1 = np.arange(start, stop+step, step)
S1 = pd.Series(S1)

S2 = pd.Series([5, 2, 3, 1], index=['a', 'b', 'c', 'd'])

# 2 užduotis
print("\n=== 2 užduotis ===\n")

S1[1] = -0.5

S1[S1>0] = 2

S2['c'] = -1

print(S1)
print(S2)

# 3 užduotis
print("\n=== 3 užduotis ===\n")

Miestai = pd.DataFrame({
    "Miestas" : ["Vilnius", "Kaunas", "Klaipeda", "Siauliai"],
    "Gyventojai" : [593436, 319790, 166292, 104300],
    "Plotas" : [401, 157, 98, 81]
})

Miestas = pd.DataFrame({
    "Miestas" : ["Moletai"],
    "Gyventojai" : [3000],
    "Plotas" : [10]
})

Miestai = pd.concat([Miestai, Miestas], ignore_index=True)

Miestai["Tankis"] = (Miestai["Gyventojai"] / Miestai["Plotas"])

print(Miestai)

print(f"Gyv sk sum = {Miestai.loc[:,'Gyventojai'].sum(axis=0)}\n")
print(f"Ploto sum = {Miestai.loc[:,'Plotas'].sum(axis=0)}\n")

Miestai = Miestai.set_index("Miestas")

print(Miestai)

plot = Miestai.plot.pie(y='Gyventojai')
plt.show()