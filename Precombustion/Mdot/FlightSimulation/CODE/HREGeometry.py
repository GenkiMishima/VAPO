#!/usr/bin/python
import subprocess as subcmd
import re
import scipy as sp
import numpy as np
#import matplotlib.pyplot as plt
import math
import sys
import csv
from string import *
Gravity = 9.80665

class Pack:
	def __init__(self):
		print ''
	def PrePMMARR(self,GFlux,border):
		Prerdot_Mid = 0.03699*GFlux**(0.5797)*10**-3
		Prerdot_Bot =  0.2649*GFlux**(0.3701)*10**-3
		func = (1-border)*Prerdot_Mid+border*Prerdot_Bot
		return (func)
	def MainPMMARR(self,G):
		func = 0.085*G**(0.55)*10.0**-3
		return (func)
	def GrainGeometry(self,Diameter,PreCrossSectionArea,MdotO,PreRhoF,Length,dt,RRName):
		import HREGeometry
		RR = HREGeometry.Pack()
		border = (Diameter/4)/Length
		CrossSectionArea = Diameter**2.0*math.pi/4.0
		GFlux = MdotO/CrossSectionArea             #[kg/sm2]
		if RRName == "Pre":
			rdot = RR.PrePMMARR(GFlux,border)
		elif RRName == "Main":
			rdot = RR.MainPMMARR(GFlux)
		dr = rdot*dt             #[m]
		dA = CrossSectionArea-PreCrossSectionArea              #[m2]
		dV = dA*Length           #[m3]
		MdotF = dV*PreRhoF/dt +10**(-30)      #[kg/s]
		Diameter = Diameter+dr*2.0
		PreCrossSectionArea = CrossSectionArea
		OF =  MdotO/MdotF
		MdotTotal = MdotO+MdotF
		Oxid = MdotO/MdotTotal
		Fuel = 1.0-Oxid
		return Diameter,PreCrossSectionArea,OF,MdotTotal,Oxid,Fuel

	def PreCEACalc(self,Pressure,Diameter_ratio,OF):
		fl = open('../CALC/CEAdata/PreData.inp','w')
		fl.write('prob rocket fac p,bar=%s,'%Pressure)
		fl.write('ac/at=%s,\n'%Diameter_ratio)
		fl.write('o/f=%s, pi/pe=1, eq\n'%OF)
		fl.write('react\n')
		fl.write('	oxid=O2(L) wt=100\n')
		fl.write('	fuel=PMMA  wt=100 t,k=293.15\n')
		fl.write('	h,kj/mol=-442.14  C 5 H 8 O 2\n')
		fl.write('end')
		fl.close()
		subcmd.call('./PreGo.sh')
	def MainCEACalc(self,Pressure,Diameter_ratio,OF,Oxid,Fuel,Temp):
		fl = open('../CALC/CEAdata/MainData.inp','w')
		fl.write('prob rocket fac p,bar=%s,'%Pressure)
		fl.write('ac/at=%s,\n'%Diameter_ratio)
		fl.write('o/f=%s, pi/pe=1, eq\n'%OF)
		fl.write('react\n')
		fl.write('	oxid=O2  wt=%s'%Oxid)
		fl.write('	t,k=%s\n'%Temp)
		fl.write('	oxid=H2O wt=%s'%(Fuel*3.0/5.0))
		fl.write('	t,k=%s\n'%Temp)
		fl.write('	oxid=CO2 wt=%s'%(Fuel*2.0/5.0))
		fl.write('	t,k=%s\n'%Temp)
		#fl.write('	fuel=PMMA  wt=100 t,k=293.15\n')
		#fl.write('	h,kj/mol=-442.14  C 5 H 8 O 2\n')
		#fl.write('	fuel=PP  wt=100 t,k=293.15\n')
		#fl.write('	h,kj/mol=-78.826  C 3 H 6\n')
		fl.write('	fuel=Paraffin  wt=100 t,k=293.15\n')
		fl.write('	h,kj/mol=-0.6382  C 35 H 72 \n')
		fl.write('end')
		fl.close()
		subcmd.call('./MainGo.sh')

##############Tutorial############################################
#if __name__ == "__main__":
#	import FlightPack
#	FP = FlightPack.Pack()
#	Mach = 1.5
