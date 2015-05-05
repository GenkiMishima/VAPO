#!/usr/bin/python
import numpy as np
import scipy as sp

P = 0.5*10**6
A = (0.0085)**2*np.pi/4.0
k = 1.342
R = 257.58
T = 575.08
Mdot = P*A*k*((2.0/(k+1.0))**((k+1.0)/(k-1.0)))**(1.0/2.0)/(k*R*T)**(1.0/2.0)
print Mdot
