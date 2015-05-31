#!/usr/bin/python
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import math
#Length:m
#Mass:kg
#Time:s
Time = 10.0            #[s]
dt = 0.01                #[s]
MdotO = 0.50          #[kg/s]
now = 0.0               #[s]
PhiInit = 30.0*10**(-3.0) #[m]
Dia = PhiInit
Length = 1.0*10**(-3.0)  #[m] Initial 
RhoF = 1.18*10**3.0      #[kg/m3]
PreA = Dia**2.0*math.pi/4.0  #[m2]Port Area
AllLength = 0.0
AllOF = 0.0
AllLength = np.array([])
AllOF = np.array([])
for i in range(0, 100):
	dL = float(i)*10**(-5.0)
	Length = Length + dL
	now = 0.0
	MtotF = 0.00000000000001
	n = 0.0
	Dia = PhiInit
	PreA = Dia**2.0*math.pi/4.0
	while now <= Time:
		now = now+dt
		A = Dia**2.0*math.pi/4.0 #[m2]
		Go = MdotO/A             #[kg/sm2]
		rdot = 0.1358*Go**(0.4161)*10**-3  #[m/s] For 15
		#rdot = 0.00765*Go**(0.9487)*10**-3  #[m/s] For 7.5
		dr = rdot*dt             #[m]
		dA = A-PreA              #[m2]
		dV = dA*Length           #[m3]
		MdotF = dV*RhoF/dt       #[kg/s]
		Dia = Dia+dr*2.0
		PreA = A
		MtotF = MdotF+MtotF
		n = n+1.0
		#print Go,rdot,Dia*10**3,MdotF 
	AllLength = np.append(AllLength,Length)
	AvMdotF = MtotF/n
	OF =  MdotO/AvMdotF
	#print Length,OF
	AllOF = np.append(AllOF,OF)
#print AvMdotF
plt.plot(AllLength,AllOF)
plt.grid()
#plt.title('MdotO:%s[kg/s]'%MdotO)
plt.legend(('MdotO:%s[kg/s]'%MdotO,))
plt.xlabel('Length[m]')
plt.ylabel('O/F')
plt.ylim([0,100])
#plt.savefig("Length.png")
plt.savefig("Length_%s.png"%int(MdotO*100.0))
#plt.show()
