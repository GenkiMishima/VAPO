#!/usr/bin/python

import scipy.optimize
import numpy as np
import sys,math,pylab
import matplotlib.pyplot as plt

def modelfunc(x,p):
	func = p[1]*x**p[0]
	return (func)

def residue(p,y,x,err):
	res = ((y - modelfunc(x,p))/err)
	return (res)

if __name__ == "__main__":
	p0 = [0.0,0.0]
	infile = 'L7_5.d'
	p0[0] = 0.0
	p0[1] = 0.0
	x = []
	ymeas = []
	yerr = []
	fin = open(infile,'r')
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
	ans1 = A*G**n
	
	print A,n
	plt.plot(G,ans1)
	plt.scatter(xarray,yarray)

	infile = 'L15.d'
	p0[0] = 0.0
	p0[1] = 0.0
	x = []
	ymeas = []
	yerr = []
	fin = open(infile,'r')
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
	ans2 = A*G**n
	
	print A,n
	plt.plot(G,ans2)
	plt.scatter(xarray,yarray)
	plt.xlabel('Go')
	plt.ylabel('rdot')
	plt.legend(['7.5','15'])
	plt.grid()

	plt.show()
