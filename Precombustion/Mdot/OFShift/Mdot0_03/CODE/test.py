#!/usr/bin/python
import subprocess as subcmd
import re
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import math
from string import *
#Length:m
#Mass:kg
#Time:s
if __name__ == "__main__":
	import CEAReadPack
	ReadClass = CEAReadPack.Pack()
	infile = 'CEAdata/Pre'

	filename = infile+'Pressure.d'
	print filename
	Pres = sp.genfromtxt(filename,delimiter = ' ')
	print Pres
	#Time = 0.5            #[s]
	#dt = 0.1              #[s]
	#now = 0.0             #[s]
	##MainChamber
	#MainLength = 0.50         #[m]
	##Length = 1.0*10**(-3.0)  #[m] Initial 
	#MainRhoF = 1.18*10**3.0      #[kg/m3]
	##MainRhoF = 9.46*10**3.0      #[kg/m3]
	#MainDia_cham = 0.04    #[m]
	##MainDia_nozl = 0.025  #[m]
	##MainDia_nozl = 0.018  #[m]
	#MainDia_nozl = 0.0145  #[m]
	#MainDia = MainDia_cham
	#MainAdash = MainDia**2.0*math.pi/4.0  #[m2]Port Area
	#MainDia_ratio = (MainDia_cham)**2/(MainDia_nozl)**2
	#MainA_nozl = MainDia_nozl**2*np.pi/4.0

	#MdotO = 0.0394
	#while now <= Time:
	#	now = now+dt
	#	#MaPreinChamber
	#	MainA = MainDia**2.0*math.pi/4.0 #[m2]
	#	MainGo = MdotO/MainA             #[kg/sm2]
	#	Mainrdot = 0.0345*MainGo**(0.778)*10.0**-3  #[m/s] For Main
	#	#Prerdot = 0.1358*PreGo**(0.4161)*10**-3  #[m/s] For 15
	#	#Prerdot = 0.00765*Go**(0.9487)*10**-3    #[m/s] For 7.5
	#	Maindr = Mainrdot*dt             #[m]
	#	MaindA = MainA-MainAdash              #[m2]
	#	MaindV = MaindA*MainLength           #[m3]
	#	MainMdotF = MaindV*MainRhoF/dt +10**(-30)      #[kg/s]
	#	MainDia = MainDia+Maindr*2.0
	#	MainAdash = MainA
	#	#MainOF =  MdotO/(PreMdotF+MainMdotF)
	#	#MainOF =  PreMtot/MainMdotF
	#	#MainMtot = PreMtot+MainMdotF

	#	print MainMdotF

	P = 6.0
	of = 1.05432
	T = 2846.36
	rho = 0.378
	Mole = 22.2
	Gamma = 1.2286
	CStar = 1517.9
	A_nozl = 1.6512*10**(-4)
	Isp = 1068.4
	Mdot = ReadClass.MatchMdot(P,of,T,rho,Mole,Gamma,CStar,A_nozl)	
	F = Mdot*Isp
	print Mdot,F

