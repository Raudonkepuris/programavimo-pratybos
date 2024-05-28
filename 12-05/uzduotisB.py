import pandas as pd 
import matplotlib.pyplot as plt

file = open('metai.txt', 'r')
raides =  []

while 1:
    ch = file.read(1)
    if not ch:
        break

    if (ch >= 'A' and ch <= 'Ž') or (ch >= 'a' and ch <= 'ž'):
        raides.append(ch.lower())
        
print(raides)

simboliai = pd.Series(0, index=set(raides))

for ch in raides:
    simboliai[ch] = simboliai[ch] + 1

simboliai = simboliai.sort_index()

print(simboliai)

plot = simboliai.plot.bar()

plt.show()