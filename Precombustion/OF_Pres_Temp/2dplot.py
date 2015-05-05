#!/usr/bin/python

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

a = sp.genfromtxt("ExperimentData/OfTempPre.d")
b = sp.genfromtxt("CEAData/OfTempPre_CEA.d")
c = sp.genfromtxt("CEAData/Ideal_0400.d")
d = sp.genfromtxt("CEAData/Ideal_0528.d")
e = sp.genfromtxt("CEAData/Ideal_0600.d")

#X, Y = np.meshgrid(x, y)
#Z = np.sin(X)+ np.cos(Y)
aX,aY,aZ = a[:,0],a[:,1],a[:,2]+273.15 
bX,bY,bZ = b[:,0],b[:,1],b[:,2]
cX,cY,cZ = c[:,0],c[:,1],c[:,2]
dX,dY,dZ = d[:,0],d[:,1],d[:,2]
eX,eY,eZ = e[:,0],e[:,1],e[:,2]
#sZ = np.array[:300]
sY = np.arange(35,150,1)
x,y = np.arange(0.2,0.8,0.1),np.arange(35,150,1)


plt.scatter(aY,aZ,color='r')
plt.scatter(bY,bZ,color='g')
plt.grid()
plt.plot(cY,cZ,color='b')
plt.plot(dY,dZ,color='g')
plt.plot(eY,eZ,color='r')
#plt.plot(sY,sZ)
plt.legend(["Ideal_CEA(0.400MPa)","Ideal_CEA(0.528MPa)","Ideal_CEA(0.600MPa)","Ex","Ex_CEA"],loc = 'upper right')









plt.show()
