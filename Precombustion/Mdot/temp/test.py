#!/usr/bin/python
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


A = 0.1358
n = 0.4161

G = 0.0
Vari = open('data.d','w')
while G < 50.0:
	G = G+1.0*0.1
	#print 'ok',G
	D = 0.0
	while D < 100.0:
		D = D+1.0*0.1
		rdot1= G**n*D**(n-1.0)
		if ((G*D<150)and(G*D>130)):
			Vari.write('%s\t'%D)
			Vari.write('%s\n'%rdot1)


