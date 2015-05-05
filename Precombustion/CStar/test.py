#!/usr/bin/python
import numpy as np
import scipy as sp
import math

Mole = 31.99886*0.95+18.0153*0.02+44.0095*0.03
k=1.25
R=8314.3/Mole
T=168.47+273.15
M=0.0683+0.00153
A=(0.0085**2)*math.pi/4
P=0.616*10**6
Ct=(k*R*T)**(1.0/2.0)/(k*((2.0/(k+1.0))**((k+1.0)/(k-1.0)))**(1.0/2.0))
Ca=P*A/M
print Ct,Ca,Ca/Ct
