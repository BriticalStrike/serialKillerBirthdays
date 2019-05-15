import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv("DataFiles\SKSigns.csv", index_col=0)

s=df1['Sign'].value_counts()

s.plot.bar()

plt.title("Serial Killers' Zodiac Signs")
plt.ylabel('Number of Serial Killers')
plt.xlabel('Astrological Sign')

plt.show()