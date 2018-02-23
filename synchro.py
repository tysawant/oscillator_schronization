# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 22:48:03 2018

@author: Tushar
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
"""
def animate(i):
    line.set_ydata(y[i,:])
"""
T = 100
N = 20
k = 0.7
d = np.array([0] * N)
d_C = np.array([0]*N)
y = np.zeros((5000,N))
y_c = np.zeros((5000,N))
c = np.random.randint(T, size=20)
print('The initial array is:')
np.set_printoptions(threshold=np.nan)
print(d)
while (d.all() != 1):
    for a in range(N):
        #print((a+1)*np.not_equal(a,N-1))
        if d[a-1] == 1 or d[(a+1)*np.not_equal(a,N-1)] == 1:
            c[a] = c[a] + k*c[a]
        else:
            c[a] = c[a]+1
        if c[a]>=T:
            d_C[a] = 1
            c[a] = 0
        else:
            d_C[a] = 0
    d = d_C
    #print(d)   # uncomment to see all the arrays
print('The final array is:')
print(d)