import numpy as np
from scipy import constants as c
from matplotlib import pyplot as plt

import grafikai.grafikai as gf

def BlackBodySpectrum(wvl, T):
    B = (2 * c.h * c.c**2)/(np.power(wvl, 5)) * 1/(np.exp((c.h * c.c)/(wvl * c.k *T))-1)
    np.savetxt(
        f"{T}K.txt",
        np.column_stack((wvl, B)),
        header = "wavelegth, radience"
    )
    return B

wvl = np.arange(1, 3000, 10)
wvl = wvl/1e+9

stars = {"Saule" : 5800,
          "Didzioji_meska" : 5000,
          "Betelgeize" : 3600}

stars_spectrum = {}

for key, temp in stars.items():
    stars_spectrum[key] = BlackBodySpectrum(wvl, temp)
    
fig, ax = gf.subplots((13, 10))
fig = gf.define_fig(fig)
ax = gf.define_ax(ax, 
                  x_min = 0, y_min = 0,
                  x_max=3100/1e+9, y_max=3e+13,
                  title="Absoliučiai juodo kūno spinduliavimo intesyvumas",
                  x_lab="Bangos ilgis, nm",
                  y_lab= f"Spinduliavimo intesyvumas, $kW(sr \cdot m^2 \cdot nm)$)",
                  x_maj_tick_step=500/1e+9, y_maj_tick_step=0.5e+13,
                  x_maj_tick_div=1e-9, y_maj_tick_div=1e+12,
                  x_min_tick_step=125/1e+9, y_min_tick_step=0.125e+13)

for key, spectrum in stars_spectrum.items():
    ax.plot(wvl, spectrum)
    max = np.max(spectrum)
    ind_max = np.argmax(spectrum)
    ax.axvline(wvl[ind_max], ls="--")
    ax.annotate(f"$\lambda = {round(wvl[ind_max]*1e+9)}nm$", (wvl[ind_max], max))


plt.show()