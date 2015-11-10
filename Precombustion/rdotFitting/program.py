#!/usr/bin/python

import scipy.optimize
import numpy as np
import sys,math,pylab
import matplotlib.pyplot as plt
#Module{{{
def modelfunc(x,p):
	func = p[1]*x**p[0]
	return (func)

def residue(p,y,x,err):
	res = ((y - modelfunc(x,p))/err)
	return (res)
def calc(filearray,counter):
	filename = filearray[counter]
	counter=counter+1
	p0[0] = 0.0
	p0[1] = 0.0
	x = []
	ymeas = []
	yerr = []
	fin = open(filename,'r')
	for line in fin:
		linedata = line.split()
		x.append(float(linedata[0]))
		ymeas.append(float(linedata[1]))
		yerr.append(float(linedata[1]))
	xarray = pylab.array(x)
	yarray = pylab.array(ymeas)
	yerarray = pylab.array(yerr)
	param_output = scipy.optimize.leastsq(residue, p0, args=(yarray,xarray,yerarray),full_output=True)
	n = param_output[0][0]
	A = param_output[0][1]
	
	G = np.linspace(50,80,100)
	ans = A*G**n
	
	print filename
	print A,n
	plt.plot(G,ans)
	plt.scatter(xarray,yarray)

	return(counter)
#}}}

if __name__ == "__main__":
	p0 = [0.0,0.0]
	#namearray=['L7_5.d','L15.d','L15Middle.d','L15Rear.d','L7_5_L15Middle.d']
	namearray=['L15.d','L15Rear.d','L7_5_L15Middle.d']
	counter=0
	num = len(namearray)
	while num > counter:
		counter = calc(namearray,counter)

	Go = np.linspace(50,80,100)
	Origin = 0.0145*Go**(0.749)
	Syutodai = 0.14*Go**(0.16)

	legendarray = np.append(namearray,['Origin','Syutodai'])
	plt.xlabel('Go[kg/(s*m2)]')
	plt.ylabel('rdot[mm/s]')
	plt.plot(Go,Origin)
	plt.plot(Go,Syutodai)
	plt.legend(legendarray,loc='upper right')
	plt.xlim([50,80])
	plt.grid()
	plt.savefig('graph.png')
	plt.show()
