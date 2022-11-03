import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv("data-firearm.csv")
m1 =[]
m2 = []
m3 = []
mtotal = []
p1 = 0
p2 = 0
p3 = 0
r1 = 0
r2 = 0
r3 = 0
pp1 = 0
pp2 = 0
pp3 = 0
name = ["Handgun","Long gun","Other"]
for i in range(55):
  p3 += (df["redemption_handgun"].loc[i])
  r3 += (df["redemption_long_gun"].loc[i])
  pp3 += (df["redemption_other"].loc[i])
mtotal.append(p3)
mtotal.append(r3)
mtotal.append(pp3)

distance = 0.2
separate = (distance, distance, distance)
plt.title("Redemption")
plt.pie(mtotal,autopct='%1.1f%%', explode=separate,labels = name)
