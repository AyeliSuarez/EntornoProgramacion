import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("weekly",
                   parse_dates=True, index_col="Date")

#print(data.sample(5))

#data.plot(y="MSFT", figsize=(9, 6))
#data.plot.line(y="MSFT", title="Microsoft Stocks",
#               ylabel= "USD", xlabel="Week")

#data.plot(kind="area", stacked=False)
#data.plot=(kind="area")

#data_3Months = data.resample(rule="M").mean()[-3:]

#data_3Months.plot(kind="bar", stacked=True, ylabel="Price")
#data_3Months

#data.plot()

plt.show()