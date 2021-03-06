#!/usr/bin/python

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import math

#Length:m
#Mass:kg
#Time:s

Time = 36.0            #[s]
dt = 0.01                #[s]
now = 0.0               #[s]
PhiInit =0.040 #[m]
Dia = PhiInit
MdotO = 0.686           #[kg/s]
Length = 10.0*10**(-3.0)  #[m] Initial
border = (Dia/4)/Length
RhoF = 1.18*10**3.0
PreA = Dia**2.0*math.pi/4.0
AllLength = np.array([])
AllOF = np.array([])
AllDia = np.array([])
AllMassF = np.array([])
AllMassO = np.array([])
for i in range(0, 300):
	dL = float(i)*10**(-5.0)
	Length = Length + dL
	now = 0.0
	MtotF = 0.0
	n = 0.0
	MassF = 0.0
	MassO = 0.0
	Dia = PhiInit
	PreA = Dia**2.0*math.pi/4.0
	while now <= Time:
		now = now+dt
		border = (Dia/4)/Length
		A = Dia**2.0*math.pi/4.0 #[m2]
		Go = MdotO/A             #[kg/sm2]
		rdot_Mid = 0.03699*Go**(0.5797)*10**-3
		rdot_Bot = 0.2649*Go**(0.3701)*10**-3
		rdot = (1-border)*rdot_Mid+border*rdot_Bot
		#rdot = 0.1358*Go**(0.4161)*10**-3  #[m/s] 15
		#rdot = 0.00765*Go**(0.9487)*10**-3  #[m/s] 7.5
		dr = rdot*dt             #[m]
		dA = A-PreA              #[m2]
		dV = dA*Length           #[m3]
		MdotF = dV*RhoF/dt       #[kg/s]
		Dia = Dia+dr*2.0
		PreA = A
		MtotF = MdotF+MtotF
		n = n+1.0
		MassF = MdotF*dt+MassF
		MassO = MdotO*dt+MassO
		#print Go,rdot,Dia*10**3,MdotF 
	AllLength = np.append(AllLength,Length)
	AvMdotF = MtotF/n
	#OF =  MdotO/AvMdotF
	OF =  MassO/MassF
	if OF >= 50.0 :
		print Length,MassF,MassO,Dia
	#print Length,OF
	AllOF = np.append(AllOF,OF)
	AllDia = np.append(AllDia,Dia)
	AllMassF = np.append(AllMassF,MdotF)
	AllMassO = np.append(AllMassO,MdotO)
#print AllLength,AllOF
print border,rdot_Mid,rdot_Bot,rdot,Dia

#fig, ax1 = plt.subplots()
#ax1.plot(AllLength,AllOF)
#plt.ylim([0,100])
#plt.ylabel('O/F')
#ax2 = ax1.twinx()
#ax2.plot(AllLength,AllDia,color='r')
#plt.ylim([0,1])
#plt.ylabel('Dia[m]')

plt.subplot(3,1,1)
plt.plot(AllLength,AllOF)
plt.ylim([0,100])
plt.ylabel('O/F')
plt.grid()
plt.xlabel('Length[m]')
plt.subplot(3,1,2)
plt.plot(AllLength,AllMassF)
#plt.ylim([0,100])
plt.ylabel('MassF')
plt.grid()
plt.xlabel('Length[m]')
plt.subplot(3,1,3)
plt.plot(AllLength,AllMassO)
#plt.ylim([0,100])
plt.ylabel('MassO')
plt.grid()
plt.xlabel('Length[m]')
plt.show()
