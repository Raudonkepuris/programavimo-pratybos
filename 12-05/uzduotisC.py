import pandas as pd
import matplotlib.pyplot as plt

covid = pd.read_csv("covid.csv")

covid['Date'] = pd.to_datetime(covid['Date'])
covid.set_index("Date", inplace=True)

baltics = covid.loc[covid["Country"].isin(["Lithuania", "Latvia", "Estonia"])]

pivot = baltics.pivot_table(
    index="Date",
    columns="Country",
    values="New cases"
)

print(pivot)

pivot.plot()
plt.show()