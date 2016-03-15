import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import csv
from scipy import interpolate

def integ(x, tck, constant=-1):
    x = np.atleast_1d(x)
    out = np.zeros(x.shape, dtype=x.dtype)
    for n in xrange(len(out)):
        out[n] = interpolate.splint(0, x[n], tck)
    out += constant
    return out


# Cubic-spline

#x = np.arange(0, 2*np.pi+np.pi/4, 2*np.pi/8)
#y = np.sin(x)
#data = sp.genfromtxt('DragCoefficient.d',delimiter='\t')
data = sp.genfromtxt('AtmosphereCondition.d',delimiter='\t')
x = data[:,0]
y = data[:,1]
z = data[:,2]
h = data[:,3]
tck1 = interpolate.splrep(x, y, s=0)
tck2 = interpolate.splrep(x, z, s=0)
tck3 = interpolate.splrep(x, h, s=0)
xnew = np.arange(0.0,1000000.0,1.0)
ynew = interpolate.splev(xnew, tck1, der=0)
znew = interpolate.splev(xnew, tck2, der=0)
hnew = interpolate.splev(xnew, tck3, der=0)
#yint = integ(xnew, tck)

OutFile = open('AC.d','w')
csvOutFile = csv.writer(OutFile)
for i in range(0,520):
	#print xnew[i],ynew[i]
	a = xnew[i]
	b = ynew[i]
	c = znew[i]
	d = hnew[i]
	OutArray = np.array([a,b,c,d])
	csvOutFile.writerow(OutArray)

plt.figure()
#plt.plot(x, y, 'x', xnew, ynew)
#plt.plot(x, z, 'x', xnew, znew)
plt.plot(x, h, 'x', xnew, hnew)
plt.legend(['Linear', 'Cubic Spline'])
plt.title('Cubic-spline interpolation')
plt.show()
