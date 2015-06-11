#!/usr/bin/python 
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

data = sp.genfromtxt('DATA/MainThrust.d',delimiter=',')
xval = data[:,0]
yval = data[:,1]
plt.plot(xval,yval)
plt.grid()
plt.title('MdotO:0.327[kg/s]')
#plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
plt.xlabel('Time[s]')
plt.ylabel('Thrust[N]')
#plt.ylim([0,100])
plt.savefig("PLOT/MainThrust.png")
plt.close()
