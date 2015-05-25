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
sZ = 300
x,y = np.arange(0.2,0.8,0.1),np.arange(35,150,10)
sX, sY = np.meshgrid(x, y)
print aZ-bZ

fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel("Pressure[MPa]")
ax.set_ylabel("O/F[-]")
ax.set_zlabel("Temp[K]")
ax.scatter3D(np.ravel(aX),np.ravel(aY),np.ravel(aZ),color='r')
ax.scatter3D(np.ravel(bX),np.ravel(bY),np.ravel(bZ),color='b')
ax.scatter3D(np.ravel(cX),np.ravel(cY),np.ravel(cZ),color='y')
ax.scatter3D(np.ravel(dX),np.ravel(dY),np.ravel(dZ),color='b')
ax.scatter3D(np.ravel(eX),np.ravel(eY),np.ravel(eZ),color='y')
ax.plot_wireframe(sX,sY,sZ, rstride=1, cstride=1)

plt.show()
