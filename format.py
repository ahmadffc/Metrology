#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 21:47:49 2020

@author: apple
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 03:54:57 2020

@author: apple
"""

#Applying Translation and Rotation to pins
import csv
import numpy as np

#import matplotlib.pyplot as plt
#import shapely
from shapely.geometry import LineString, Point
import math 

from func_Metrology import GC,GC2,angle, length, Tria, GCenter

from numpy import genfromtxt
import pandas as pd

#df = pd.read_excel("data1.xlsx", "Module4_R2_Brown")
#df = pd.read_excel("data1.xlsx", "Module4_R2_Brown_standard")
#df = pd.read_excel("data1.xlsx", "Module4_R2_with_standard")
#df = pd.read_excel("data1.xlsx", "Module4_R2_with_standard_bot_re")
df = pd.read_excel("file.xlsx", "Module4_R2")

df1 = pd.DataFrame(df, columns= ['x'])
df2 = pd.DataFrame(df, columns= ['y'])

px = df1['x']; py = df2['y']


nt = []; nb = []; mt = []; mb = []
for x in range(0,4):
    nt.append(np.array([px[x],py[x]],dtype=np.float))
for x in range(4,8):
    nb.append(np.array([px[x],py[x]],dtype=np.float))
for x in range(8,12):
    mt.append(np.array([px[x],py[x]],dtype=np.float))
for x in range(12,16):
    mb.append(np.array([px[x],py[x]],dtype=np.float))    

print('array nt = ',nt, '\narray nb = ',nb, '\narray mt = ',mt, '\narray mb = ',mb)

#df.to_excel('output.xlsx', 'Sheet1')
with open('file.txt','w') as outfile:
    df.to_string(outfile)

