import random
import matplotlib.pyplot as plt
import time

class koord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def vidurys(self, koord):
        x = (koord.x + self.x) / 2
        y = (koord.y + self.y) / 2
        return self.__class__(x, y)
    
    def __repr__(self):
        return f"{self.x, self.y}"

p = [koord(0,0), koord(5,50), koord(10,0)]
p.append(p[0].vidurys(p[1]))

v1 = p[0].vidurys(p[1])
v = [v1]

for i in range(0,1000):
    pabaiga = p[random.randint(0,2)]

    v.append(v[-1].vidurys(pabaiga))

for vi in v:
    plt.plot(vi.x, vi.y, 'g^', markersize=5)
    
plt.show()
