# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


# In[3]:


df = pd.read_csv(r'https://d.docs.live.net/f607172ee80dedaa/Documents/sea.xlsx')


# In[ ]:


df.plot.scatter(x='Year', y="CSIRO Adjusted Sea Level", figsize=(25, 10))
sr1 = pd.Series([int(i) for i in range(1880, 2050)])

# First best line
slope, intercept, r_value, p_value, std_err  = linregress(df['Year'], df["CSIRO Adjusted Sea Level"])
plt.plot(sr1, intercept + slope*sr1, 'r', label='best fit line from 1880 to 2050')

# Second best line after year 2000
recent = df[df['Year'] >= 2000]
slope, intercept, r_value, p_value, std_err  = linregress(recent['Year'], recent["CSIRO Adjusted Sea Level"])

sr2 = pd.Series([int(i) for i in range(2000, 2050)])
recent.append(sr2, ignore_index=True)
plt.plot(sr2, intercept + slope*sr2, 'r', label='new best fit line after year 2000', color="pink")

plt.title("Rise in Sea Level")
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.legend()

plt.show()

