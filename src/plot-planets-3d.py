
#!/usr/bin/python2.7
import math, csv, os, sys, string
#from pylab import *
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

f = open('sssoutput.data','r')
lines = f.readlines()
numoflinesinfile = len(lines)

jd=[]
mer_x_km=[]
mer_y_km=[]
mer_z_km=[]
ven_x_km=[]
ven_y_km=[]
ven_z_km=[]
ear_x_km=[]
ear_y_km=[]
ear_z_km=[]
mar_x_km=[]
mar_y_km=[]
mar_z_km=[]
jup_x_km=[]
jup_y_km=[]
jup_z_km=[]
sat_x_km=[]
sat_y_km=[]
sat_z_km=[]
urn_x_km=[]
urn_y_km=[]
urn_z_km=[]
nep_x_km=[]
nep_y_km=[]
nep_z_km=[]
plu_x_km=[]
plu_y_km=[]
plu_z_km=[]
ss1_x_km=[]
ss1_y_km=[]
ss1_z_km=[]
ss2_x_km=[]
ss2_y_km=[]
ss2_z_km=[]

i = -1
while i <= numoflinesinfile -2:
  i = i + 1
  words = str.split(lines[i])
  j = -1
  if i > 1:
     j = j + 1
     jd.append(float(words[0]))
     mer_x_km.append(float(words[1]))
     mer_y_km.append(float(words[2]))
     mer_z_km.append(float(words[3]))
     ven_x_km.append(float(words[4]))
     ven_y_km.append(float(words[5]))
     ven_z_km.append(float(words[6]))
     ear_x_km.append(float(words[7]))
     ear_y_km.append(float(words[8]))
     ear_z_km.append(float(words[9]))
     mar_x_km.append(float(words[10]))
     mar_y_km.append(float(words[11]))
     mar_z_km.append(float(words[12]))
     jup_x_km.append(float(words[13]))
     jup_y_km.append(float(words[14]))
     jup_z_km.append(float(words[15]))
     sat_x_km.append(float(words[16]))
     sat_y_km.append(float(words[17]))
     sat_z_km.append(float(words[18]))
     urn_x_km.append(float(words[19]))
     urn_y_km.append(float(words[20]))
     urn_z_km.append(float(words[21]))
     nep_x_km.append(float(words[22]))
     nep_y_km.append(float(words[23]))
     nep_z_km.append(float(words[24]))
     plu_x_km.append(float(words[25]))
     plu_y_km.append(float(words[26]))
     plu_z_km.append(float(words[27]))
     ss1_x_km.append(float(words[28]))
     ss1_y_km.append(float(words[29]))
     ss1_z_km.append(float(words[30]))
     ss2_x_km.append(float(words[28]))
     ss2_y_km.append(float(words[29]))
     ss2_z_km.append(float(words[30]))


mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.plot(mer_x_km, mer_y_km, mer_z_km, label='Mercury')
ax.plot(ven_x_km, ven_y_km, ven_z_km, label='Venus')
ax.plot(ear_x_km, ear_y_km, ear_z_km, label='Earth')
ax.plot(mar_x_km, mar_y_km, mar_z_km, label='Mars')
ax.plot(jup_x_km, jup_y_km, jup_z_km, label='Jupiter')
ax.plot(sat_x_km, sat_y_km, sat_z_km, label='Saturn')
ax.plot(urn_x_km, urn_y_km, urn_z_km, label='Uranus')
ax.plot(nep_x_km, nep_y_km, nep_z_km, label='Neptune')
ax.plot(plu_x_km, plu_y_km, plu_z_km, label='Pluto')
ax.plot(ss1_x_km, ss1_y_km, ss1_z_km, label='SS1')
ax.plot(ss2_x_km, ss2_y_km, ss2_z_km, label='SS1')
ax.legend()
ax.set_xlim3d(-8e9,8e9)
ax.set_ylim3d(-8e9,8e9)
ax.set_zlim3d(-3e9,3e9)
#ax.set_xlim3d(-2e9,2e9)
#ax.set_ylim3d(-2e9,2e9)
#ax.set_zlim3d(-1e9,1e9)
plt.show()
