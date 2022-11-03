import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv("data-firearm.csv")
c = 0.25
k = []
l = []
z = []
z1 = []
s = []

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

bar1 = np.arange(len(l))
bar2 = [q+c for q in bar1]
bar3 = [q+c for q in bar2]

f, ax = plt.subplots(figsize=(30,5))
plt.xticks(bar1+c,l,rotation=90)
plt.title("Data of Gun Ownership")
plt.xlabel("State")
plt.ylabel("quantity")

plt.bar(bar1,z1,color ='red',width = 0.25, label = 'Permit')
plt.bar(bar2,k,color ='blue',width = 0.25, label = 'Handgun')
plt.bar(bar3,z,color ='gold',width = 0.25, label = 'Long gun')

ax.legend(fontsize = 10)
plt.show()
