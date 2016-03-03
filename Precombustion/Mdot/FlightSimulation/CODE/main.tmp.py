#!/usr/bin/python
import subprocess as subcmd
import re
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import math
import csv
from string import *

if __name__ == "__main__":
	import CEAReadPack
	ReadClass = CEAReadPack.Pack()
	Preinfile  = 'CEAdata/Pre/'
	Maininfile = 'CEAdata/Main/'
	Time = 6.0            #[s]
	dt = 0.1              #[s]
	now = 0.0             #[s]
	g0 = 9.80665          #[m/s2]
	#LOXMdot
	#MdotO = 0.50          #[kg/s]
	#MdotO = 0.05         #[kg/s]
	MdotO = 0.0394         #[kg/s]
	#Preburner
	PreLength = 0.007        #[m]
	#PreLength = 0.011         #[m]
	PrePhiInit = 30.0*10**(-3.0) #[m]
	PreRhoF = 1.18*10**3.0      #[kg/m3]
	PreDia_cham = 0.03    #[m]
	PreDia_nozl = 0.0045  #[m]
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
	Pres_end    = 15.0       #[bar]
	Pres_count  = int((Pres_end-Pres_start)/Pres_step)

	wt = 100.0
	PreAllTime    = np.array([])
	PreAllOF      = np.array([])
	PreAllPres    = np.array([])
	PreAllTemp    = np.array([])
	PreAllMdotF   = np.array([])
	PreAllIsp     = np.array([])
	PreAllThrust  = np.array([])
	MainAllTime   = np.array([])
	MainAllOF     = np.array([])
	MainAllPres   = np.array([])
	MainAllTemp   = np.array([])
	MainAllIsp    = np.array([])
	MainAllMdotF  = np.array([])
	MainAllThrust = np.array([])

	PreAllCH4     = np.array([])
	PreAllCO2     = np.array([])
	PreAllCO      = np.array([])
	PreAllH       = np.array([])
	PreAllH2      = np.array([])
	PreAllH2O     = np.array([])
	PreAllO       = np.array([])
	PreAllO2      = np.array([])
	PreAllOH      = np.array([])
	MainAllCH4    = np.array([])
	MainAllCO2    = np.array([])
	MainAllCO     = np.array([])
	MainAllH      = np.array([])
	MainAllH2     = np.array([])
	MainAllH2O    = np.array([])
	MainAllO      = np.array([])
	MainAllO2     = np.array([])
	MainAllOH     = np.array([])
	while now <= Time:
		now = now+dt
		#PreChamber{{{
		PreA = PreDia**2.0*math.pi/4.0 #[m2]
		#PreGo = PreMtot/PreA             #[kg/sm2]
		PreGo = MdotO/PreA             #[kg/sm2]
		#Prerdot = 0.0345*PreGo**(0.778)*10.0**-3  #[m/s] For Main
		#Prerdot = 0.085*PreGo**(0.55)*10.0**-3  #[m/s] For Main
		Prerdot = 0.1358*PreGo**(0.4161)*10**-3  #[m/s] For 15
		#Prerdot = 0.00765*Go**(0.9487)*10**-3    #[m/s] For 7.5
		Predr = Prerdot*dt             #[m]
		PredA = PreA-PreAdash              #[m2]
		PredV = PredA*PreLength           #[m3]
		PreMdotF = PredV*PreRhoF/dt +10**(-30)      #[kg/s]
		#print PreMdotF
		PreDia = PreDia+Predr*2.0
		PreAdash = PreA
		PreDia_ratio = PreA/PreA_nozl
		#PreOF =  MdotO/(PreMdotF+PreMdotF)
		PreOF   = MdotO/PreMdotF
		#PreOF   = PreMtot/PreMdotF
		PreMtot = MdotO+PreMdotF
		#PreMtot = PreMtot+PreMdotF
		if PreOF<70.0:
			PreEp = 100000000.0
			for j in range(1,Pres_count):
				P = Pres_start+float(j)*Pres_step
				fl = open('../CALC/CEAdata/PreData.inp','w')
				fl.write('prob rocket fac p,bar=%s,'%P)
				fl.write('ac/at=%s,\n'%PreDia_ratio)
				fl.write('o/f=%s, pi/pe=1, eq\n'%PreOF)
				fl.write('react\n')
				fl.write('	oxid=O2(L)  wt=100\n')
				#fl.write('	oxid=O2  wt=100 t,k=293.15\n')
				fl.write('	fuel=PMMA  wt=100 t,k=293.15\n')
				fl.write('	h,kj/mol=-442.14  C 5 H 8 O 2\n')
				#fl.write('	fuel=PP  wt=100 t,k=293.15\n')
				#fl.write('	h,kj/mol=-78.826  C 3 H 6\n')
				fl.write('end')
				fl.close()
				subcmd.call('./PreGo.sh')
				Predata = sp.genfromtxt('../CALC/CEAdata/Pre/ReadFile.d',delimiter=',')
				PreFrac = sp.genfromtxt('../CALC/CEAdata/Pre/ReadFrac.d',delimiter=',')
				PrePres  = Predata[0]
				PreTemp  = Predata[1]
				PreGamma = Predata[2]
				PreMole  = Predata[3]
				PreIsp   = Predata[4]
				PreCH4   = PreFrac[0]
				PreCO2   = PreFrac[1]
				PreCO    = PreFrac[2]
				PreH     = PreFrac[3]
				PreH2    = PreFrac[4]
				PreH2O   = PreFrac[5]
				PreO     = PreFrac[6]
				PreO2    = PreFrac[7]
				PreOH    = PreFrac[8]

				#print data

				#Pres,of,Temp,rho,Mole,Gamma,CStar_th,Isp = ReadClass.Read2(Preinfile)

				#print float(Pres),float(of),float(Temp),float(rho),float(Mole),float(Gamma)
				#print Temp 
		#		#print float(Temp)
				PreMdot_th = PrePres*10**5*PreA_nozl*PreGamma*((2.0/(PreGamma+1.0))**((PreGamma+1.0)/(PreGamma-1.0)))**(1.0/2.0)/(PreGamma*8314.3/PreMole*PreTemp)**(1.0/2.0)
				#print (PreMtot/PreMdot_th-1.0),0.01
				#if (PreMtot/PreMdot_th-1.0)<0.0:
				if PreMtot<PreMdot_th:
				#	break;
				#PreResi = abs(PreMtot/PreMdot_th-1.0)
				#if PreEp<PreResi:
				#if abs(PreResi/PreEp-1.0)<0.003:
					PreThrust = PreMtot*float(PreIsp)
					print 'PreChamber',now,PreOF,PreMdotF,PreTemp,P,PreMdot_th,PreMtot,PreIsp,PreThrust
					print PreCH4, PreCO2, PreCO, PreH, PreH2, PreH2O, PreO, PreO2, PreOH
					break;
				#PreEp = PreResi

			
			PreAllTime   = np.append(PreAllTime  ,now         )
			PreAllOF     = np.append(PreAllOF    ,PreOF       )
			PreAllPres   = np.append(PreAllPres  ,PrePres*0.1 )
			PreAllTemp   = np.append(PreAllTemp  ,PreTemp     )
			PreAllIsp    = np.append(PreAllIsp   ,PreIsp/g0   )
			PreAllMdotF  = np.append(PreAllMdotF ,PreMdotF    )
			PreAllThrust = np.append(PreAllThrust,PreThrust   )
			PreAllCH4    = np.append(PreAllCH4   ,PreCH4      )
			PreAllCO2    = np.append(PreAllCO2   ,PreCO2      )
			PreAllCO     = np.append(PreAllCO    ,PreCO       )
			PreAllH      = np.append(PreAllH     ,PreH        )
			PreAllH2     = np.append(PreAllH2    ,PreH2       )
			PreAllH2O    = np.append(PreAllH2O   ,PreH2O      )
			PreAllO      = np.append(PreAllO     ,PreO        )
			PreAllO2     = np.append(PreAllO2    ,PreO2       )
			PreAllOH     = np.append(PreAllOH    ,PreOH       )
			#}}}
			#MainChamber{{{
			MainA = MainDia**2.0*math.pi/4.0 #[m2]
			MainGo = PreMtot/MainA             #[kg/sm2]
			#MainGo = MdotO/MainA             #[kg/sm2]
			#Mainrdot = 0.0345*MainGo**(0.778)*10.0**-3  #[m/s] For Main
			Mainrdot = 0.085*MainGo**(0.55)*10.0**-3  #[m/s] For Main
			#Prerdot = 0.1358*PreGo**(0.4161)*10**-3  #[m/s] For 15
			#Prerdot = 0.00765*Go**(0.9487)*10**-3    #[m/s] For 7.5
			Maindr = Mainrdot*dt             #[m]
			MaindA = MainA-MainAdash              #[m2]
			MaindV = MaindA*MainLength           #[m3]
			MainMdotF = MaindV*MainRhoF/dt +10**(-30)      #[kg/s]
			#print MainMdotF
			MainDia = MainDia+Maindr*2.0
			MainAdash = MainA
			MainDia_ratio = MainA/MainA_nozl
			#MainOF =  MdotO/(PreMdotF+MainMdotF)
			#MainOF   = MdotO/MainMdotF
			MainOF   = PreMtot/MainMdotF
			#MainMtot = MdotO+MainMdotF
			MainMtot = PreMtot+MainMdotF
			if MainOF<5.0:
				MainEp = 100000000.0
				for j in range(1,Pres_count):
					P = Pres_start+float(j)*Pres_step
					fl = open('../CALC/CEAdata/MainData.inp','w')
					fl.write('prob rocket fac p,bar=%s,'%P)
					fl.write('ac/at=%s,\n'%MainDia_ratio)
					fl.write('o/f=%s, pi/pe=1, eq\n'%MainOF)
					fl.write('react\n')
					#fl.write('	oxid=O2  wt=100')
					#fl.write('	t,k=293.15\n')
					fl.write('	oxid=CH4  wt=%s'%PreCH4)
					fl.write('	t,k=%s\n'%PreTemp)
					fl.write('	oxid=CO2 wt=%s'%PreCO2)
					fl.write('	t,k=%s\n'%PreTemp)
					fl.write('	oxid=CO wt=%s'%PreCO)
					fl.write('	t,k=%s\n'%PreTemp)
					fl.write('	oxid=H  wt=%s'%PreH)
					fl.write('	t,k=%s\n'%PreTemp)
					fl.write('	oxid=H2 wt=%s'%PreH2)
					fl.write('	t,k=%s\n'%PreTemp)
					fl.write('	oxid=H2O wt=%s'%PreH2O)
					fl.write('	t,k=%s\n'%PreTemp)
					fl.write('	oxid=O  wt=%s'%PreO)
					fl.write('	t,k=%s\n'%PreTemp)
					fl.write('	oxid=O2 wt=%s'%PreO2)
					fl.write('	t,k=%s\n'%PreTemp)
					fl.write('	oxid=OH wt=%s'%PreOH)
					fl.write('	t,k=%s\n'%PreTemp)
					fl.write('	fuel=PMMA  wt=100 t,k=293.15\n')
					fl.write('	h,kj/mol=-442.14  C 5 H 8 O 2\n')
					#fl.write('	fuel=PP  wt=100 t,k=293.15\n')
					#fl.write('	h,kj/mol=-78.826  C 3 H 6\n')
					fl.write('end')
					fl.close()
					subcmd.call('./MainGo.sh')
					Maindata      = sp.genfromtxt('../CALC/CEAdata/Main/ReadFile.d',delimiter=',')
					MainFrac      = sp.genfromtxt('../CALC/CEAdata/Main/ReadFrac.d',delimiter=',')
					MainPres      = Maindata[0]
					MainTemp      = Maindata[1]
					MainGamma     = Maindata[2]
					MainMole      = Maindata[3]
					MainIsp       = Maindata[4]
					MainCH4       = MainFrac[0]
					MainCO2       = MainFrac[1]
					MainCO        = MainFrac[2]
					MainH         = MainFrac[3]
					MainH2        = MainFrac[4]
					MainH2O       = MainFrac[5]
					MainO         = MainFrac[6]
					MainO2        = MainFrac[7]
					MainOH        = MainFrac[8]
	
					#print data
	
					#Pres,of,Temp,rho,Mole,Gamma,CStar_th,Isp = ReadClass.Read2(Maininfile)
	
					#print float(Pres),float(of),float(Temp),float(rho),float(Mole),float(Gamma)
					#print Temp 
			#		#print float(Temp)
					MainMdot_th = MainPres*10**5*MainA_nozl*MainGamma*((2.0/(MainGamma+1.0))**((MainGamma+1.0)/(MainGamma-1.0)))**(1.0/2.0)/(MainGamma*8314.3/MainMole*MainTemp)**(1.0/2.0)
					#print (MainMtot/MainMdot_th-1.0),0.01
					if (MainMtot/MainMdot_th-1.0)<0.0:
					#	break;
					#MainResi = abs(MainMtot/MainMdot_th-1.0)
					#if MainEp<MainResi:
					#if abs(MainResi/MainEp-1.0)<0.003:
						MainThrust = MainMtot*float(MainIsp)
						print 'MainChamber',now,MainOF,MainMdotF,MainTemp,P,MainMdot_th,MainMtot,MainIsp,MainThrust
						print MainCH4, MainCO2, MainCO, MainH, MainH2, MainH2O, MainO, MainO2, MainOH
						break;
					#MainEp = MainResi
	
				
				MainAllTime   = np.append(MainAllTime  ,now      )
				MainAllOF     = np.append(MainAllOF    ,MainOF   )
				MainAllPres   = np.append(MainAllPres  ,MainPres*0.1 )
				MainAllTemp   = np.append(MainAllTemp  ,MainTemp     )
				MainAllIsp    = np.append(MainAllIsp   ,MainIsp/g0   )
				MainAllMdotF  = np.append(MainAllMdotF ,MainMdotF)
				MainAllThrust = np.append(MainAllThrust,MainThrust   )
				MainAllCH4    = np.append(MainAllCH4   ,MainCH4      )
				MainAllCO2    = np.append(MainAllCO2   ,MainCO2      )
				MainAllCO     = np.append(MainAllCO    ,MainCO       )
				MainAllH      = np.append(MainAllH     ,MainH        )
				MainAllH2     = np.append(MainAllH2    ,MainH2       )
				MainAllH2O    = np.append(MainAllH2O   ,MainH2O      )
				MainAllO      = np.append(MainAllO     ,MainO        )
				MainAllO2     = np.append(MainAllO2    ,MainO2       )
				MainAllOH     = np.append(MainAllOH    ,MainOH       )
				#}}}
	#out[:,1] = MainAllTime
	#out[:,2] = MainAllOF
	#out = np.array([MainAllTime,MainAllMdotF]).T
	#print out
	#out = np.array([MainAllTime,MainAllOF]).T
	#print out

	#PreOUT{{{
	direct = '../OUT/DATA/Pre'
	f = open(direct+'MdotF.d','w')
	out = np.array([PreAllTime,PreAllMdotF]).T
	writer = csv.writer(f, lineterminator='\n')
	writer.writerows(out)
	f.close()
	f = open(direct+'OF.d','w')
	out = np.array([PreAllTime,PreAllOF]).T
	writer = csv.writer(f, lineterminator='\n')
	writer.writerows(out)
	f.close()
	f = open(direct+'Pres.d','w')
	out = np.array([PreAllTime,PreAllPres]).T
	writer = csv.writer(f, lineterminator='\n')
	writer.writerows(out)
	f.close()
	f = open(direct+'Temp.d','w')
	out = np.array([PreAllTime,PreAllTemp]).T
	writer = csv.writer(f, lineterminator='\n')
	writer.writerows(out)
	f.close()
	f = open(direct+'Isp.d','w')
	out = np.array([PreAllTime,PreAllIsp]).T
	writer = csv.writer(f, lineterminator='\n')
	writer.writerows(out)
	f.close()
	f = open(direct+'Thrust.d','w')
	out = np.array([PreAllTime,PreAllThrust]).T
	writer = csv.writer(f, lineterminator='\n')
	writer.writerows(out)
	f.close()
	f = open(direct+'CH4.d','w')
	out = np.array([PreAllTime,PreAllCH4]).T
	writer = csv.writer(f, lineterminator='\n')
	writer.writerows(out)
	f.close()
	f = open(direct+'CO2.d','w')
	out = np.array([PreAllTime,PreAllCO2]).T
	writer = csv.writer(f, lineterminator='\n')
	writer.writerows(out)
	f.close()
	f = open(direct+'CO.d','w')
	out = np.array([PreAllTime,PreAllCO]).T
	writer = csv.writer(f, lineterminator='\n')
	writer.writerows(out)
	f.close()
	f = open(direct+'H.d','w')
	out = np.array([PreAllTime,PreAllH]).T
	writer = csv.writer(f, lineterminator='\n')
	writer.writerows(out)
	f.close()
	f = open(direct+'H2.d','w')
	out = np.array([PreAllTime,PreAllH2]).T
	writer = csv.writer(f, lineterminator='\n')
	writer.writerows(out)
	f.close()
	f = open(direct+'H2O.d','w')
	out = np.array([PreAllTime,PreAllH2O]).T
	writer = csv.writer(f, lineterminator='\n')
	writer.writerows(out)
	f.close()
	f = open(direct+'O.d','w')
	out = np.array([PreAllTime,PreAllO]).T
	writer = csv.writer(f, lineterminator='\n')
	writer.writerows(out)
	f.close()
	f = open(direct+'O2.d','w')
	out = np.array([PreAllTime,PreAllO2]).T
	writer = csv.writer(f, lineterminator='\n')
	writer.writerows(out)
	f.close()
	f = open(direct+'OH.d','w')
	out = np.array([PreAllTime,PreAllOH]).T
	writer = csv.writer(f, lineterminator='\n')
	writer.writerows(out)
	f.close()
	#{{{
	#f = open(direct+'.d','w')
	#out = np.array([MainAllTime,MainAll]).T
	#writer = csv.writer(f, lineterminator='\n')
	#writer.writerows(out)
	#f.close()
	#}}}
	#}}}
	#MainOUT{{{
	direct = '../OUT/DATA/Main'
	f = open(direct+'MdotF.d','w')
	out = np.array([MainAllTime,MainAllMdotF]).T
	writer = csv.writer(f, lineterminator='\n')
	writer.writerows(out)
	f.close()
	f = open(direct+'OF.d','w')
	out = np.array([MainAllTime,MainAllOF]).T
	writer = csv.writer(f, lineterminator='\n')
	writer.writerows(out)
	f.close()
	f = open(direct+'Pres.d','w')
	out = np.array([MainAllTime,MainAllPres]).T
	writer = csv.writer(f, lineterminator='\n')
	writer.writerows(out)
	f.close()
	f = open(direct+'Temp.d','w')
	out = np.array([MainAllTime,MainAllTemp]).T
	writer = csv.writer(f, lineterminator='\n')
	writer.writerows(out)
	f.close()
	f = open(direct+'Isp.d','w')
	out = np.array([MainAllTime,MainAllIsp]).T
	writer = csv.writer(f, lineterminator='\n')
	writer.writerows(out)
	f.close()
	f = open(direct+'Thrust.d','w')
	out = np.array([MainAllTime,MainAllThrust]).T
	writer = csv.writer(f, lineterminator='\n')
	writer.writerows(out)
	f.close()
	f = open(direct+'CH4.d','w')
	out = np.array([MainAllTime,MainAllCH4]).T
	writer = csv.writer(f, lineterminator='\n')
	writer.writerows(out)
	f.close()
	f = open(direct+'CO2.d','w')
	out = np.array([MainAllTime,MainAllCO2]).T
	writer = csv.writer(f, lineterminator='\n')
	writer.writerows(out)
	f.close()
	f = open(direct+'CO.d','w')
	out = np.array([MainAllTime,MainAllCO]).T
	writer = csv.writer(f, lineterminator='\n')
	writer.writerows(out)
	f.close()
	f = open(direct+'H.d','w')
	out = np.array([MainAllTime,MainAllH]).T
	writer = csv.writer(f, lineterminator='\n')
	writer.writerows(out)
	f.close()
	f = open(direct+'H2.d','w')
	out = np.array([MainAllTime,MainAllH2]).T
	writer = csv.writer(f, lineterminator='\n')
	writer.writerows(out)
	f.close()
	f = open(direct+'H2O.d','w')
	out = np.array([MainAllTime,MainAllH2O]).T
	writer = csv.writer(f, lineterminator='\n')
	writer.writerows(out)
	f.close()
	f = open(direct+'O.d','w')
	out = np.array([MainAllTime,MainAllO]).T
	writer = csv.writer(f, lineterminator='\n')
	writer.writerows(out)
	f.close()
	f = open(direct+'O2.d','w')
	out = np.array([MainAllTime,MainAllO2]).T
	writer = csv.writer(f, lineterminator='\n')
	writer.writerows(out)
	f.close()
	f = open(direct+'OH.d','w')
	out = np.array([MainAllTime,MainAllOH]).T
	writer = csv.writer(f, lineterminator='\n')
	writer.writerows(out)
	f.close()
	#{{{
	#f = open(direct+'.d','w')
	#out = np.array([MainAllTime,MainAll]).T
	#writer = csv.writer(f, lineterminator='\n')
	#writer.writerows(out)
	#f.close()
	#}}}
	#}}}


#PLOT{{{
	#plt.plot(MainAllTime,MainAllMdotF)
	#plt.grid()
	###plt.title('MdotO:%s[kg/s]'%MdotO)
	#plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
	#plt.xlabel('Time[s]')
	#plt.ylabel('MainMdotF[kg/s]')
	#plt.ylim([0,0.05])
	#plt.savefig("MainMdotF_%s.png"%int(PreLength*1000.0))
	#plt.close()

	#plt.plot(MainAllTime,MainAllOF)
	#plt.grid()
	###plt.title('MdotO:%s[kg/s]'%MdotO)
	#plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
	#plt.xlabel('Time[s]')
	#plt.ylabel('MainOF')
	#plt.ylim([0,1.0])
	#plt.savefig("MainOF_%s.png"%int(PreLength*1000.0))
	#plt.close()

	#plt.plot(MainAllTime,MainAllTemp)
	#plt.grid()
	###plt.title('MdotO:%s[kg/s]'%MdotO)
	#plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
	#plt.xlabel('Time[s]')
	#plt.ylabel('MainTemp[K]')
	#plt.ylim([1500,3000])
	#plt.savefig("MainTemp_%s.png"%int(PreLength*1000.0))
	#plt.close()

	#plt.plot(MainAllTime,MainAllPres)
	#plt.grid()
	###plt.title('MdotO:%s[kg/s]'%MdotO)
	#plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
	#plt.xlabel('Time[s]')
	#plt.ylabel('Pres[MPa]')
	#plt.ylim([0.2,0.5])
	#plt.savefig("MainPres_%s.png"%int(PreLength*1000.0))
	#plt.close()

	#plt.plot(MainAllTime,MainAllIsp)
	#plt.grid()
	###plt.title('MdotO:%s[kg/s]'%MdotO)
	#plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
	#plt.xlabel('Time[s]')
	#plt.ylabel('Isp[s]')
	#plt.ylim([80,100])
	#plt.savefig("MainIsp_%s.png"%int(PreLength*1000.0))
	#plt.close()

	#plt.plot(MainAllTime,MainAllThrust)
	#plt.grid()
	###plt.title('MdotO:%s[kg/s]'%MdotO)
	#plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
	#plt.xlabel('Time[s]')
	#plt.ylabel('F[N]')
	#plt.ylim([50,100])
	#plt.savefig("MainThrust_%s.png"%int(PreLength*1000.0))
	#plt.close()

	#plt.show()
#}}}

