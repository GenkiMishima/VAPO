#!/usr/bin/python
#{{{
import subprocess as subcmd
import re
import scipy as sp
import numpy as np
#import matplotlib.pyplot as plt
import math
import sys
import csv
from string import *
#}}}
#Length:m
#Mass:kg
#Time:s
if __name__ == "__main__":
	import CEAReadPack
	import HREGeometry
	import FlightPack
	FP = FlightPack.Pack()
	HREG = HREGeometry.Pack()
	#IOSetting{{{
	ReadClass = CEAReadPack.Pack()
	Preinfile  = '../CALC/CEAdata/Pre/'
	Maininfile = '../CALC/CEAdata/Main/'
	PreOutfile  = '../OUT/DATA/Pre/'
	MainOutfile = '../OUT/DATA/Main/'
	FlightOutfile = '../OUT/DATA/Flight/'

	PreOutVari = open(PreOutfile+'Variable.d','w')
	PreOutFrac = open(PreOutfile+'Fraction.d','w')
	MainOutVari = open(MainOutfile+'Variable.d','w')
	MainOutFrac = open(MainOutfile+'Fraction.d','w')
	FlightOutVari = open(FlightOutfile+'Flight.d','w')
	PreOutVari.write('Time[s]'+','+'Pres[MPa]'+','+'Temp[K]'+','+'OF[-]'+','+'PreMtot[kg/s]'+','+'Gamma[-]'+','+'Mole[-]\n')
	PreOutFrac.write('CH4'+','+ 'CO2'+','+ 'CO'+','+ 'H'+','+ 'H2'+','+ 'H2O'+','+ 'O'+','+ 'O2'+','+'OH\n'  )
	MainOutVari.write( 'Time[s]'+','+'Pres[MPa]'+','+'Temp[K]'+','+'OF[-]'+','+'MainMtot[kg/s]'+','+'Gamma[-]'+','+'Mole[-]\n')
	MainOutFrac.write( 'CH4'+','+ 'CO2'+','+ 'CO'+','+ 'H'+','+ 'H2'+','+ 'H2O'+','+ 'O'+','+ 'O2'+','+'OH\n'  )
	FlightOutVari.write( 'Time[s]'+','+'CF'+','+'Thrust[N]'+','+'TotalMass[kg]'+','+'CD'+','+'Drag[N]'+','+'AccelX[m/s2]'+','+'AccelY[m/s2]'+','+'VeloX[m/s]'+','+'VeloY[m/s]'+','+'Velo[m/s]'+','+'Distance[m]'+','+'Height[m]'+','+'Angle[rad]\n')
	#print CF,F,TotalMass,CD,Drag,AccelX,AccelY,VeloX,VeloY,Velo,Distance,Height,Angle
	csvPreVari  = csv.writer(PreOutVari)
	csvPreFrac  = csv.writer(PreOutFrac)
	csvMainVari = csv.writer(MainOutVari)
	csvMainFrac = csv.writer(MainOutFrac)
	csvFlightVari = csv.writer(FlightOutVari)
	#}}}
	
	Time = 36.50*2.0            #[s]
	now = 0.0             #[s]
	dt = 0.1              #[s]
	g0 = 9.80665          #[m/s2]
	#LOXMdot
	MdotO = 0.696         #[kg/s]
#
#	#PreBurnerICSetting{{{
#	#Preburner
#	PreLength = 0.050       #[m]
#	#PreLength = 0.011         #[m]
#	#PrePhiInit = 100.0*10**(-3.0) #[m]
#	PreRhoF = 1.18*10**3.0      #[kg/m3]
#	PreDia_cham = 0.040    #[m]
#	PreDia_nozl = 0.008  #[m]
#	#PreDia_nozl = 0.0033  #[m]
#	#PreDia_nozl = 0.01  #[m]
#	PreDia = PreDia_cham
#	border = (PreDia/4)/PreLength
#	PreAdash = PreDia**2.0*math.pi/4.0  #[m2]Port Area
#	PreA_nozl = PreDia_nozl**2*np.pi/4.0
#	PreDia_ratio = PreAdash/PreA_nozl
#
#	PreGeoValue    = [PreDia,PreAdash]
#	#}}}
#
	#MainBurnerICSetting{{{
	#MainChamber
	MainLength = 1.14         #[m]
	MainRhoF = 1.18*10**3.0      #[kg/m3]
	#MainRhoF = 0.927*10**3.0      #[kg/m3]Parafin
	#MainRhoF = 9.46*10**3.0      #[kg/m3]
	MainDia_cham = 0.040   #[m]
	MainDia_nozl = 0.025  #[m]
	#MainDia_nozl = 0.018  #[m]
	#MainDia_nozl = 0.104  #[m]
	MainDia = MainDia_cham
	MainAdash = MainDia**2.0*math.pi/4.0  #[m2]Port Area
	MainDia_ratio = (MainDia_cham)**2/(MainDia_nozl)**2
	MainA_nozl = MainDia_nozl**2*np.pi/4.0
	#}}}

	#RocketSetting{{{
	dH = 0.0              #[m]
	Height = 0.0          #[m]
	Distance = 0.0        #[m]
	Angle = 88.0              
	Angle = Angle * math.pi/180.0 #[rad]
	TotalMass = 75.5     #[kg]
	OxidMass = 18.9      #[kg]
	PreFuelMass = 0.378      #[kg]
	MainFuelMass = 12.4      #[kg]
	PreMdotF = 0.0
	MainMdotF = 0.0
	Mach = 0.0          #[-]
	Velo = 0.0          #[m/s]
	VeloX = 0.0          #[m/s]
	VeloY = 0.0          #[m/s]
	HRECrossSectionArea = 0.135#[m]
	tmp0,ExitPressure,tmp1 = FP.AtmosphereCondition(Height)
	#}}}

	Pres_start  = 1.0        #[bar]
	Pres_step   = 0.5       #[bar]
	Pres_end    = 80.0      #[bar]
	Pres_count  = int((Pres_end-Pres_start)/Pres_step)

	wt = 100.0

	PreAllFrac     = np.array([])
	MainAllFrac    = np.array([])

	OutSpec = open('../OUT/DATA/Spec.d','w')
	OutSpec.write(str(MdotO)+'\n')
	OutSpec.close() 

	#while now <= Time:
	while Height >= 0.0:
		print Height
		now = now+dt
		OxidMass = OxidMass - MdotO*dt

		##Preburner{{{
		#PreFuelMass = PreFuelMass - PreMdotF*dt
		#PreDia,PreAdash,PreOF,PreMtot,PreMdotF,PreOxid,PreFuel = HREG.GrainGeometry(PreDia,PreAdash,MdotO,PreRhoF,PreLength,dt,"Pre")
		#if PreOF<100.0:
		#	PreEp = 100000000.0
		#	for j in range(1,Pres_count):
		#		if OxidMass < 0.0 :
		#			print 'Oxid is empty'
		#			MdotO = 0.0
		#			break;
		#		elif PreFuelMass < 0.0 :
		#			print 'PreFuel is empty'
		#			PreMdotF = 0.0
		#			break;
		#		P = Pres_start+float(j)*Pres_step
		#		HREG.PreCEACalc(P,PreDia_ratio,PreOF)
		#		Pres,Temp,Gamma,Mole,Isp = ReadClass.Read4(Preinfile)
		#		PreMdot_th =  (Pres)*10**5* (PreA_nozl)* (Gamma)*((2.0/( (Gamma)+1.0))**(( (Gamma)+1.0)/( (Gamma)-1.0)))**(1.0/2.0)/( (Gamma)*8314.3/ (Mole)* (Temp))**(1.0/2.0)
		#		PreResi = abs(PreMtot/PreMdot_th-1.0)
		#		if (PreMtot/PreMdot_th-1.0)<0.0:
		#			print 'PreChamber',now,Pres,PreOF,Temp,PreMdot_th,PreDia,PreMdotF
		#			break;
		#		PreEp = PreResi

		#	PreFrac = ReadClass.Read5(Preinfile)
	
		#	PreTemp     = Temp

		#	PreVari = np.array([now ,Pres*0.1 ,Temp, PreOF ,PreMtot,Gamma,Mole])
		#	csvPreVari.writerow(PreVari)
		#	csvPreFrac.writerow(PreFrac)
		##}}}
			
		#MainChamber{{{
		MainFuelMass = MainFuelMass - MainMdotF*dt
		MainDia,MainAdash,MainOF,MainMtot,MainMdotF,MainOxid,MainFuel = HREG.GrainGeometry(MainDia,MainAdash,MdotO,MainRhoF,MainLength,dt,"Main")
		#print MainOF
		if MainOF<100.0:
			MainEp = 100000000.0
			for j in range(1,Pres_count):
				if OxidMass < 0.0 :
					print 'Oxid is empty'
					MdotO = 0.0
					break;
				elif MainFuelMass < 0.0 :
					print 'MainFuel is empty'
					MainMdotF = 0.0
					break;
				P = Pres_start+float(j)*Pres_step
				HREG.MainCEACalc(P,MainDia_ratio,MainOF)
				Pres,Temp,Gamma,Mole,Isp = ReadClass.Read4(Maininfile)
				MainMdot_th =  (Pres)*10**5* (MainA_nozl)* (Gamma)*((2.0/( (Gamma)+1.0))**(( (Gamma)+1.0)/( (Gamma)-1.0)))**(1.0/2.0)/( (Gamma)*8314.3/ (Mole)* (Temp))**(1.0/2.0)
				PreResi = abs(MainMtot/MainMdot_th-1.0)
				if (MainMtot/MainMdot_th-1.0)<0.0:
					print 'MainChamber',now,Pres,MainOF,Temp,MainMdot_th,MainDia,MainMdotF
					break;
				PreEp = PreResi
	
			MainFrac = ReadClass.Read5(Maininfile)
		
			MainTemp     = Temp
	
			MainVari = np.array([now ,Pres*0.1 ,Temp, MainOF ,MainMtot,Gamma,Mole])
			csvMainVari.writerow(MainVari)
			csvMainFrac.writerow(MainFrac)
		#}}}

			#FlightSimulation{{{
			AtmosTemp,AtmosPres,AtmosDens = FP.AtmosphereCondition(Height)
			if OxidMass < 0.0 :
				print 'Oxid is empty'
				MdotO = 0.0
				CF = 0.0
			elif MainFuelMass < 0.0 :
				print 'MainFuel is empty'
				MainMdotF = 0.0
				CF = 0.0
			else:
				CF = FP.ThrustCoefficient(Gamma,ExitPressure,Pres*0.1,AtmosPres)
			F = FP.Thrust(CF,Pres*0.1,MainA_nozl*10**6)
			TotalMass = FP.TotalMass(TotalMass,MdotO,PreMdotF+MainMdotF,dt)
			CD = FP.DragCoefficient(Mach)
			Drag = FP.Drag(CD,AtmosDens,Velo,HRECrossSectionArea)
			AccelX, AccelY = FP.Accelaration(F,Angle,TotalMass,Drag)
			VeloX,VeloY,Velo = FP.Velocity(VeloX,VeloY,AccelX,AccelY,dt)
			Distance = FP.HorizontalDistance(Distance,VeloX,AccelX,dt)
			Height = FP.Height(Height,VeloY,AccelY,dt)
			Angle = FP.Angle(VeloX,VeloY)
			Mach = (1.4*AtmosPres/AtmosDens)**(1.0/2.0)
			#print CF,F,TotalMass,CD,Drag,AccelX,AccelY,VeloX,VeloY,Velo,Distance,Height,Angle
			FlightVari = np.array([now,CF,F,TotalMass,CD,Drag,AccelX,AccelY,VeloX,VeloY,Velo,Distance,Height,Angle])
			csvFlightVari.writerow(FlightVari)
			#}}}
