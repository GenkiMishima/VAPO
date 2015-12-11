#!/usr/bin/python
import subprocess as subcmd
import re
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import math
import sys
import csv
from string import *
#Length:m
#Mass:kg
#Time:s
if __name__ == "__main__":
	import CEAReadPack
	ReadClass = CEAReadPack.Pack()
	Preinfile  = '../CALC/CEAdata/Pre/'
	Maininfile = '../CALC/CEAdata/Main/'
	PreOutfile  = '../OUT/DATA/Pre/'
	MainOutfile = '../OUT/DATA/Main/'

	PreOutVari = open(PreOutfile+'Variable.d','w')
	PreOutFrac = open(PreOutfile+'Fraction.d','w')
	MainOutVari = open(MainOutfile+'Variable.d','w')
	MainOutFrac = open(MainOutfile+'Fraction.d','w')
	PreOutVari.write('Time[s]'+','+'Pres[MPa]'+','+'Temp[K]'+','+'OF[-]'+','+'PreMtot[kg/s]\n')
	PreOutFrac.write('CH4'+','+ 'CO2'+','+ 'CO'+','+ 'H'+','+ 'H2'+','+ 'H2O'+','+ 'O'+','+ 'O2'+','+'OH\n'  )
	MainOutVari.write( 'Time[s]'+','+'Pres[MPa]'+','+'Temp[K]'+','+'OF[-]'+','+'MainMtot[kg/s]'+','+'Isp[s]'+','+'Thrust[N]\n' )
	MainOutFrac.write( 'CH4'+','+ 'CO2'+','+ 'CO'+','+ 'H'+','+ 'H2'+','+ 'H2O'+','+ 'O'+','+ 'O2'+','+'OH\n'  )
	csvPreVari  = csv.writer(PreOutVari)
	csvPreFrac  = csv.writer(PreOutFrac)
	csvMainVari = csv.writer(MainOutVari)
	csvMainFrac = csv.writer(MainOutFrac)
	#PreOutVari.close() 
	#PreOutFrac.close()
	#MainOutVari.close()
	#MainOutFrac.close()
	#sys.exit()
	
	Time = 10.0            #[s]
	dt = 0.05              #[s]
	now = 0.0             #[s]
	g0 = 9.80665          #[m/s2]
	#LOXMdot
	#MdotO = 0.50          #[kg/s]
	#MdotO = 0.05         #[kg/s]
	#MdotO = 0.01         #[kg/s]
	MdotO = 10.0         #[kg/s]
	#Preburner
	PreLength = 0.011       #[m]
	#PreLength = 0.011         #[m]
	PrePhiInit = 30.0*10**(-3.0) #[m]
	PreRhoF = 1.18*10**3.0      #[kg/m3]
	PreDia_cham = 0.03    #[m]
	PreDia_nozl = 0.0085  #[m]
	#PreDia_nozl = 0.0033  #[m]
	#PreDia_nozl = 0.01  #[m]
	PreDia = PreDia_cham
	PreAdash = PreDia**2.0*math.pi/4.0  #[m2]Port Area
	PreA_nozl = PreDia_nozl**2*np.pi/4.0
	PreDia_ratio = PreAdash/PreA_nozl

	#MainChamber
	MainLength = 0.50         #[m]
	MainRhoF = 1.18*10**3.0      #[kg/m3]
	#MainRhoF = 9.46*10**3.0      #[kg/m3]
	MainDia_cham = 0.04    #[m]
	#MainDia_nozl = 0.025  #[m]
	#MainDia_nozl = 0.018  #[m]
	MainDia_nozl = 0.0145  #[m]
	MainDia = MainDia_cham
	MainAdash = MainDia**2.0*math.pi/4.0  #[m2]Port Area
	MainDia_ratio = (MainDia_cham)**2/(MainDia_nozl)**2
	MainA_nozl = MainDia_nozl**2*np.pi/4.0

	Pres_start  = 1.0        #[bar]
	Pres_step   = 0.01     #[bar]
	Pres_end    = 50.0       #[bar]
	Pres_count  = int((Pres_end-Pres_start)/Pres_step)

	wt = 100.0
	#PreAllTime    = np.array([])
	#PreAllOF      = np.array([])
	#PreAllPres    = np.array([])
	#PreAllTemp    = np.array([])
	#PreAllMdotF   = np.array([])

	PreAllFrac     = np.array([])
	MainAllFrac    = np.array([])

	#PreAllCH4     = np.array([])
	#PreAllCO2     = np.array([])
	#PreAllCO      = np.array([])
	#PreAllH       = np.array([])
	#PreAllH2      = np.array([])
	#PreAllH2O     = np.array([])
	#PreAllO       = np.array([])
	#PreAllO2      = np.array([])
	#PreAllOH      = np.array([])

	#MainAllTime   = np.array([])
	#MainAllOF     = np.array([])
	#MainAllPres   = np.array([])
	#MainAllTemp   = np.array([])
	#MainAllIsp    = np.array([])
	#MainAllMdotF  = np.array([])
	#MainAllThrust = np.array([])

	OutSpec = open('../OUT/DATA/Spec.d','w')
	OutSpec.write(str(MdotO)+'\n')
	OutSpec.close() 

	while now <= Time:
		now = now+dt
		#Preburner
		PreA = PreDia**2.0*math.pi/4.0 #[m2]
		PreGo = MdotO/PreA             #[kg/sm2]
		Prerdot = 0.1358*PreGo**(0.4161)*10.0**-3  #[m/s] For 15
		#Prerdot = 0.00765*Go**(0.9487)*10**-3  #[m/s] For 7.5
		Predr = Prerdot*dt             #[m]
		PredA = PreA-PreAdash              #[m2]
		PredV = PredA*PreLength           #[m3]
		PreMdotF = PredV*PreRhoF/dt +10**(-30)      #[kg/s]
		PreDia = PreDia+Predr*2.0
		PreAdash = PreA
		PreOF =  MdotO/PreMdotF
		PreMtot = MdotO+PreMdotF
		PreOxid = MdotO/PreMtot
		PreFuel = 1.0-PreOxid
		#print PreOF

		if PreOF<100.0:
			PreEp = 100000000.0
			for j in range(1,Pres_count):
				P = Pres_start+float(j)*Pres_step
				fl = open('../CALC/CEAdata/PreData.inp','w')
				fl.write('prob rocket fac p,bar=%s,'%P)
				fl.write('ac/at=%s,\n'%PreDia_ratio)
				fl.write('o/f=%s, pi/pe=1, eq\n'%PreOF)
				fl.write('react\n')
				fl.write('	oxid=O2(L) wt=100\n')
				fl.write('	fuel=PMMA  wt=100 t,k=293.15\n')
				fl.write('	h,kj/mol=-442.14  C 5 H 8 O 2\n')
				fl.write('end')
				fl.close()
				subcmd.call('./PreGo.sh')

				Pres,Temp,Gamma,Mole,Isp = ReadClass.Read4(Preinfile)
				#sys.exit()
				#print Pres,'end'

				PreMdot_th =  (Pres)*10**5* (PreA_nozl)* (Gamma)*((2.0/( (Gamma)+1.0))**(( (Gamma)+1.0)/( (Gamma)-1.0)))**(1.0/2.0)/( (Gamma)*8314.3/ (Mole)* (Temp))**(1.0/2.0)
				PreResi = abs(PreMtot/PreMdot_th-1.0)
				#if PreEp<PreResi:
				#print abs(PreMtot/PreMdot_th-1.0),0.001
				#if abs(PreMtot/PreMdot_th-1.0)<0.001:
				#print PreMdot_th, (PreMtot/PreMdot_th-1.0)
				if (PreMtot/PreMdot_th-1.0)<0.0:
				#if abs(PreResi/PreEp-1.0)<0.001:
					print 'PreChamber',now,Pres,PreOF,Temp,PreMdot_th,Isp/g0,Prerdot
					break;
				PreEp = PreResi

			PreFrac = ReadClass.Read5(Preinfile)
	
			PreTemp     = Temp
			#PreAllTime  = np.append(PreAllTime,now)
			#PreAllOF    = np.append(PreAllOF,PreOF)
			#PreAllPres  = np.append(PreAllPres,Pres*0.1)
			#PreAllTemp  = np.append(PreAllTemp,Temp)
			#PreAllMdotF = np.append(PreAllMdotF,PreMdotF)

			PreVari = np.array([now ,Pres*0.1 ,Temp, PreOF ,PreMtot])
			csvPreVari.writerow(PreVari)
			csvPreFrac.writerow(PreFrac)

			#csvPreVari = csv.writer(PreOutVari)
			#PreOutVari.write (Time ,Pres ,Temp, PreOF  ,PreMdotF)

			#print Frac[:9]
			#PreAllCH4   = np.append(PreAllCH4,CH4)
			#PreAllCO2   = np.append(PreAllCO2,CO2)
			#PreAllCO    = np.append(PreAllCO ,CO )
			#PreAllH     = np.append(PreAllH  ,H  )
			#PreAllH2    = np.append(PreAllH2 ,H2 )
			#PreAllH2O   = np.append(PreAllH2O,H2O)
			#PreAllO     = np.append(PreAllO  ,O  )
			#PreAllO2    = np.append(PreAllO2 ,O2 )
			#PreAllOH    = np.append(PreAllOH ,OH )
			
#			#MainChamber
#			MainA = MainDia**2.0*math.pi/4.0 #[m2]
#			MainGo = PreMtot/MainA             #[kg/sm2]
#			#Mainrdot = 0.0345*MainGo**(0.778)*10.0**-3  #[m/s] For Main
#			Mainrdot = 0.085*MainGo**(0.55)*10.0**-3  #[m/s] For Main
#			#Prerdot = 0.1358*PreGo**(0.4161)*10**-3  #[m/s] For 15
#			#Prerdot = 0.00765*Go**(0.9487)*10**-3    #[m/s] For 7.5
#			Maindr = Mainrdot*dt             #[m]
#			MaindA = MainA-MainAdash              #[m2]
#			MaindV = MaindA*MainLength           #[m3]
#			MainMdotF = MaindV*MainRhoF/dt +10**(-30)      #[kg/s]
#			#print MainMdotF
#			MainDia = MainDia+Maindr*2.0
#			MainAdash = MainA
#			MainDia_ratio = MainA/MainA_nozl
#			#MainOF =  MdotO/(PreMdotF+MainMdotF)
#			MainOF   = PreMtot/MainMdotF
#			MainMtot = PreMtot+MainMdotF
#			if MainOF<5.0:
#				MainEp = 100000000.0
#				for j in range(1,Pres_count):
#					P = Pres_start+float(j)*Pres_step
#					fl = open('../CALC/CEAdata/MainData.inp','w')
#					fl.write('prob rocket fac p,bar=%s,'%P)
#					fl.write('ac/at=%s,\n'%MainDia_ratio)
#					fl.write('o/f=%s, pi/pe=1, eq\n'%MainOF)
#					fl.write('react\n')
#					fl.write('	oxid=O2  wt=%s'%PreOxid)
#					fl.write('	t,k=%s\n'%PreTemp)
#					fl.write('	oxid=H2O wt=%s'%(PreFuel*3.0/5.0))
#					fl.write('	t,k=%s\n'%PreTemp)
#					fl.write('	oxid=CO2 wt=%s'%(PreFuel*2.0/5.0))
#					fl.write('	t,k=%s\n'%PreTemp)
#					fl.write('	fuel=PMMA  wt=100 t,k=293.15\n')
#					fl.write('	h,kj/mol=-442.14  C 5 H 8 O 2\n')
#					#fl.write('	fuel=PP  wt=100 t,k=293.15\n')
#					#fl.write('	h,kj/mol=-78.826  C 3 H 6\n')
#					fl.write('end')
#					fl.close()
#					subcmd.call('./MainGo.sh')
#					Pres,Temp,Gamma,Mole,Isp = ReadClass.Read4(Maininfile)
#
#					#print float(Pres),float(of),float(Temp),float(rho),float(Mole),float(Gamma)
#					#print Temp 
#					#print float(Temp)
#					MainMdot_th =  (Pres)*10**5*MainA_nozl* (Gamma)*((2.0/( (Gamma)+1.0))**(( (Gamma)+1.0)/( (Gamma)-1.0)))**(1.0/2.0)/( (Gamma)*8314.3/ (Mole)* (Temp))**(1.0/2.0)
#					#print (MainMtot/MainMdot_th-1.0),0.01
#					#if (MainMtot/MainMdot_th-1.0)<0.0:
#					#	break;
#					MainResi = abs(MainMtot/MainMdot_th-1.0)
#					#if MainEp<MainResi:
#					if (MainMtot/MainMdot_th-1.0)<0.0:
#					#if abs(MainResi/MainEp-1.0)<0.003:
#						Thrust = MainMtot*float(Isp)
#						print 'MainChamber',now,Pres,MainOF,Temp,MainMtot,Isp/g0,Thrust
#						break;
#					MainEp = MainResi
#
#				MainFrac = ReadClass.Read5(Maininfile)
#
#				#MainAllTime   = np.append(MainAllTime,now)
#				#MainAllOF     = np.append(MainAllOF,MainOF)
#				#MainAllPres   = np.append(MainAllPres,float(Pres)*0.1)
#				#MainAllTemp   = np.append(MainAllTemp,float(Temp))
#				#MainAllIsp    = np.append(MainAllIsp,float(Isp)/g0)
#				#MainAllMdotF  = np.append(MainAllMdotF,MainMdotF)
#				#MainAllThrust = np.append(MainAllThrust,Thrust)
#
#				MainVari = np.array([now ,Pres*0.1 ,Temp, MainOF  ,MainMdot_th, Isp/g0,Thrust])
#				csvMainVari.writerow(MainVari)
#				csvMainFrac.writerow(MainFrac)
#
#
#		#AllLength = np.append(AllLength,Length)
#		#AvMdotF = MtotF/float(n)
#		#OF =  MdotO/AvMdotF
#		#print Length,OF
#		#AllMdotO = np.append(AllMdotO,MdotO)
	#print AvMdotF
#
#	#PLOT{{{
#	plt.plot(PreAllTime,PreAllPres)
#	plt.grid()
#	##plt.title('MdotO:%s[kg/s]'%MdotO)
#	plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
#	plt.xlabel('Time[s]')
#	plt.ylabel('Pres[MPa]')
#	#plt.ylim([0,100])
#	plt.savefig("PrePres_%s.png"%int(PreLength*1000.0))
#	plt.close()
#
#	plt.plot(PreAllTime,PreAllTemp)
#	plt.grid()
#	##plt.title('MdotO:%s[kg/s]'%MdotO)
#	plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
#	plt.xlabel('Time[s]')
#	plt.ylabel('Temp[K]')
#	#plt.ylim([0,100])
#	plt.savefig("PreTemp_%s.png"%int(PreLength*1000.0))
#	plt.close()
#
#	plt.plot(PreAllTime,PreAllOF)
#	plt.grid()
#	##plt.title('MdotO:%s[kg/s]'%MdotO)
#	plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
#	plt.xlabel('Time[s]')
#	plt.ylabel('OF')
#	#plt.ylim([0,100])
#	plt.savefig("PreOF_%s.png"%int(PreLength*1000.0))
#	plt.close()
#
#	plt.plot(PreAllTime,PreAllMdotF)
#	plt.grid()
#	##plt.title('MdotO:%s[kg/s]'%MdotO)
#	plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
#	plt.xlabel('Time[s]')
#	plt.ylabel('MainMdotF[kg/s]')
#	#plt.ylim([0,100])
#	plt.savefig("PreMdotF_%s.png"%int(PreLength*1000.0))
#	plt.close()
#
#	plt.plot(MainAllTime,MainAllMdotF)
#	plt.grid()
#	##plt.title('MdotO:%s[kg/s]'%MdotO)
#	plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
#	plt.xlabel('Time[s]')
#	plt.ylabel('MainMdotF[kg/s]')
#	#plt.ylim([0,100])
#	plt.savefig("MainMdotF_%s.png"%int(PreLength*1000.0))
#	plt.close()
#
#	plt.plot(MainAllTime,MainAllOF)
#	plt.grid()
#	##plt.title('MdotO:%s[kg/s]'%MdotO)
#	plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
#	plt.xlabel('Time[s]')
#	plt.ylabel('MainOF')
#	#plt.ylim([0,100])
#	plt.savefig("MainOF_%s.png"%int(PreLength*1000.0))
#	plt.close()
#
#	plt.plot(MainAllTime,MainAllTemp)
#	plt.grid()
#	##plt.title('MdotO:%s[kg/s]'%MdotO)
#	plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
#	plt.xlabel('Time[s]')
#	plt.ylabel('MainTemp[K]')
#	#plt.ylim([0,100])
#	plt.savefig("MainTemp_%s.png"%int(PreLength*1000.0))
#	plt.close()
#
#	plt.plot(MainAllTime,MainAllPres)
#	plt.grid()
#	##plt.title('MdotO:%s[kg/s]'%MdotO)
#	plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
#	plt.xlabel('Time[s]')
#	plt.ylabel('Pres[MPa]')
#	#plt.ylim([0,100])
#	plt.savefig("MainPres_%s.png"%int(PreLength*1000.0))
#	plt.close()
#
#	plt.plot(MainAllTime,MainAllIsp)
#	plt.grid()
#	##plt.title('MdotO:%s[kg/s]'%MdotO)
#	plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
#	plt.xlabel('Time[s]')
#	plt.ylabel('Isp[s]')
#	#plt.ylim([0,100])
#	plt.savefig("MainIsp_%s.png"%int(PreLength*1000.0))
#	plt.close()
#
#	plt.plot(MainAllTime,MainAllThrust)
#	plt.grid()
#	##plt.title('MdotO:%s[kg/s]'%MdotO)
#	plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
#	plt.xlabel('Time[s]')
#	plt.ylabel('F[N]')
#	#plt.ylim([0,100])
#	plt.savefig("MainThrust_%s.png"%int(PreLength*1000.0))
#	plt.close()
#
#	#plt.show()}}}
#



