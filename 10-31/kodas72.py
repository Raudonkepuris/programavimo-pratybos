import sys
import os
import matplotlib.pyplot as plt

class Collatz_seka:
    def __skaiciuoti_seka(self):
        seka = [self.n]
        n = self.n
        while n != 1:
            if n % 2 == 0:
                n = n / 2
            else:
                n = 3 * n + 1
            seka.append(int(n))
        return seka;  

    def __skaiciuoti_k(self):
        k = 0
        for ind, x in enumerate(self.seka):
            if x < self.n:
                k = ind
                break
        return k

    def __init__(self, n, seka = []):
        self.n = n
        self.seka = self.__skaiciuoti_seka()
        self.m = len(self.seka) - 1
        self.k = self.__skaiciuoti_k()
        self.a_max = max(self.seka)
        self.failo_pav = f"collatz_{self.n}.txt"

argumentai = sys.argv[1:]

intervalas = [int(x) for x in argumentai[0][1:-1].split(',')]

aplanko_kelias = os.path.join("collatz")

try:
    os.makedirs(aplanko_kelias)
except FileExistsError:
    pass

failu_sarasas = []

collatz_sekos = []

#skaiciavimas, rasymas
for x in range(intervalas[0], intervalas[-1]+1):
    seka = Collatz_seka(x)

    collatz_sekos.append(seka)

    failo_kelias = os.path.join("collatz", seka.failo_pav)

    try:
        failo_objektas = open(failo_kelias, "x")
    except FileExistsError:
        os.remove(failo_kelias)
        failo_objektas = open(failo_kelias, "x")

    failo_objektas.write(f'{x}, {seka.k}, {seka.m}, {seka.a_max}\n')
    failo_objektas.write(f'{str(seka.seka)[1:-1]}\n')

    failo_objektas.close()

#vaizdavimas
atsakymas = input("Koki Collatz seku grafika rodyti:\n  (a) Suskaiciuotas sekas, (x, y) = (i, ai).\n  (b) Maksimalias vertes, (x, y) = (n, amax).\n  (c) Sustojimo laikus, (x, y) = (n, k).\n  (d) Visiško sustojimo laikus, (x, y) = (n, m).\n")

plt.figure()

match atsakymas:
    case 'a':
        maxy = float('-inf')
        maxx = float('-inf')
        for i, seka in enumerate(collatz_sekos):
            if maxx < max([*range(1,len(seka.seka)+1,1)]):
                maxx = max([*range(1,len(seka.seka)+1,1)])
            if maxy < max(seka.seka):
                maxy = max(seka.seka)
            plt.plot([*range(1,len(seka.seka)+1,1)], seka.seka)

            plt.ylim(ymin=0, ymax=maxy)
            plt.xlim(xmin=1, xmax=maxx)

plt.show()