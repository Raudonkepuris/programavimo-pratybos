import pandas as pd
import matplotlib.pyplot as plt
from numpy import nan
import numpy as np
from scipy.optimize import curve_fit

def tiese(x, a, b):
    return a * x + b

data = pd.read_csv("data.csv")

print(data)

data.plot.scatter(x="D", y="z")

data[data["D"] > 8000] = nan

data["v"] = data["z"] * 3e5

plt.show()

data.plot.scatter(x="D", y="v")

plt.show()

# 5 uzd

data = data[data["Method"].isin(data[(data["Method"] != "Tully-Fisher") & (data["Method"].str.contains("SNI")) & (data["Method"].str.contains("SDSS") == False)]["Method"].unique())]

# 6 uzd

data["pub_date"] = data["ref"].str[:4]

data = data.sort_values(by=["ID", "pub_date"])
data = data.drop_duplicates(subset=["ID", "pub_date"], keep="first")

# 7 uzd

data = data.dropna(subset=['D','v'])

popt, pcov = curve_fit(tiese, data.loc[:, "D"], data.loc[:, "v"])

fig, ax = plt.subplots()

ax.plot(data.loc[:, "D"], tiese(data.loc[:, "D"], *popt))

ax.scatter(data.loc[:, "D"], data.loc[:, "v"], s=5, c='orange')

plt.show()

print(popt[0])

# 8 uzd

data["1D"] = 1 / data["D"]

popt, pcov = curve_fit(tiese, data.loc[:, "D"], data.loc[:, "v"], sigma=data.loc[:,"1D"], absolute_sigma=True)

fig, ax = plt.subplots()

ax.plot(data.loc[:, "D"], tiese(data.loc[:, "D"], *popt))

ax.scatter(data.loc[:, "D"], data.loc[:, "v"], s=5, c='orange')

plt.show()

print(popt[0])

