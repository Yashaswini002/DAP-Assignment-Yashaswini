import pandas as pd
from matplotlib import pyplot as plt

data=pd.read_csv("reviews_data.csv")
dataframe=pd.DataFrame(data)
dfhead=dataframe.head(25)
dfhead.plot(x="location",y="Rating",kind="bar",title="Starbucks reviews")
plt.show()