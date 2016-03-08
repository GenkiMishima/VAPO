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
data = sp.genfromtxt('DragCoefficient.d',delimiter='\t')
x = data[:,0]
y = data[:,1]
tck = interpolate.splrep(x, y, s=0)
xnew = np.arange(0.2,5.4,0.01)
ynew = interpolate.splev(xnew, tck, der=0)
#yint = integ(xnew, tck)

OutFile = open('CDragSpline.d','w')
csvOutFile = csv.writer(OutFile)
for i in range(0,520):
	#print xnew[i],ynew[i]
	a = xnew[i]
	b = ynew[i]
	OutArray = np.array([a,b])
	csvOutFile.writerow(OutArray)

plt.figure()
plt.plot(x, y, 'x', xnew, ynew)
plt.legend(['Linear', 'Cubic Spline'])
plt.title('Cubic-spline interpolation')
plt.show()
