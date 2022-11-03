import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv("data-firearm.csv")

k = []
l = []
z = []
s = []
z1 = []

for x in range(55):
  K = (df["handgun"].loc[x])
  L = (df["state"].loc[x])
  l.append(L)
  k.append(K)

for i in range(55):
  Z = (df["long_gun"].loc[i])
  S = (df["state"].loc[i])
  z.append(Z)
  s.append(S)

for i1 in range(55):
  Z1 = (df["permit"].loc[i1])
  z1.append(Z1)

#print(z)
#print(s)
#print(k)
#print(l)

ind = np.arange(len(l))
width = 0.275

f, ax = plt.subplots(figsize=(10,50))
plt.title("Data of Gun Ownership")
plt.xlabel("quantity")
plt.ylabel("State")
plt.yticks(ind+width,l)
plt.barh(ind,z1, width,color ='red', label = 'Permit')
plt.barh(ind + width,k, width,color ='blue', label = 'Handgun')
plt.barh(ind + width*2,z, width,color ='gold', label = 'Long gun')
ax.legend(fontsize = 10)
plt.show()
