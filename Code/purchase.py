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
  p1 += (df["prepawn_handgun"].loc[i])
  p2 += (df["rentals_handgun"].loc[i])
  p3 += (df["private_sale_handgun"].loc[i])
  totalp = p1+p2+p3

m1.append(totalp)


for i1 in range(55):
  r1 += (df["prepawn_long_gun"].loc[i1])
  r2 += (df["rentals_long_gun"].loc[i1])
  r3 += (df["private_sale_long_gun"].loc[i1])
  totalr = r1+r2+r3

m2.append(totalr)

for i2 in range(55):
  pp1 += (df["prepawn_other"].loc[i2])
  pp2 += (df["private_sale_other"].loc[i2])
  totalpp = pp1+pp2

m3.append(totalpp)

mtotal.append(m1)
mtotal.append(m2)
mtotal.append(m3)

distance = 0.2
separate = (distance, distance, distance)
plt.title("Buying Gun")
plt.pie(mtotal,autopct='%1.1f%%', explode=separate,labels = name)
