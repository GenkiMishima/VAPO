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
	Time = 0.5            #[s]
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
	PreDia_nozl = 0.0055  #[m]
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
	MainAllTime   = np.array([])
	MainAllOF     = np.array([])
	MainAllPres   = np.array([])
	MainAllTemp   = np.array([])
	MainAllIsp    = np.array([])
	MainAllMdotF  = np.array([])
	MainAllThrust = np.array([])

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
		#MainChamber
		MainA = MainDia**2.0*math.pi/4.0 #[m2]
		#MainGo = PreMtot/MainA             #[kg/sm2]
		MainGo = MdotO/MainA             #[kg/sm2]
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
		MainOF   = MdotO/MainMdotF
		#MainOF   = PreMtot/MainMdotF
		MainMtot = MdotO+MainMdotF
		#MainMtot = PreMtot+MainMdotF
		if MainOF<5.0:
			MainEp = 100000000.0
			for j in range(1,Pres_count):
				P = Pres_start+float(j)*Pres_step
				fl = open('../CALC/CEAdata/MainData.inp','w')
				fl.write('prob rocket fac p,bar=%s,'%P)
				fl.write('ac/at=%s,\n'%MainDia_ratio)
				fl.write('o/f=%s, pi/pe=1, eq\n'%MainOF)
				fl.write('react\n')
				fl.write('	oxid=O2  wt=100')
				fl.write('	t,k=293.15\n')
				#fl.write('	oxid=O2  wt=%s'%PreOxid)
				#fl.write('	t,k=%s\n'%PreTemp)
				#fl.write('	oxid=H2O wt=%s'%(PreFuel*3.0/5.0))
				#fl.write('	t,k=%s\n'%PreTemp)
				#fl.write('	oxid=CO2 wt=%s'%(PreFuel*2.0/5.0))
				#fl.write('	t,k=%s\n'%PreTemp)
				fl.write('	fuel=PMMA  wt=100 t,k=293.15\n')
				fl.write('	h,kj/mol=-442.14  C 5 H 8 O 2\n')
				#fl.write('	fuel=PP  wt=100 t,k=293.15\n')
				#fl.write('	h,kj/mol=-78.826  C 3 H 6\n')
				fl.write('end')
				fl.close()
				subcmd.call('./MainGo.sh')
				data = sp.genfromtxt('../CALC/CEAdata/Main/ReadFile.d',delimiter=',')
				Frac = sp.genfromtxt('../CALC/CEAdata/Main/ReadFrac.d',delimiter=',')
				Pres  = data[0]
				Temp  = data[1]
				Gamma = data[2]
				Mole  = data[3]
				Isp   = data[4]
				CH4   = Frac[0]
				CO2   = Frac[1]
				CO    = Frac[2]
				H     = Frac[3]
				H2    = Frac[4]
				H2O   = Frac[5]
				O     = Frac[6]
				O2    = Frac[7]
				OH    = Frac[8]

				#print data

				#Pres,of,Temp,rho,Mole,Gamma,CStar_th,Isp = ReadClass.Read2(Maininfile)

				#print float(Pres),float(of),float(Temp),float(rho),float(Mole),float(Gamma)
				#print Temp 
		#		#print float(Temp)
				MainMdot_th = Pres*10**5*MainA_nozl*Gamma*((2.0/(Gamma+1.0))**((Gamma+1.0)/(Gamma-1.0)))**(1.0/2.0)/(Gamma*8314.3/Mole*Temp)**(1.0/2.0)
				#print (MainMtot/MainMdot_th-1.0),0.01
				if (MainMtot/MainMdot_th-1.0)<0.0:
				#	break;
				#MainResi = abs(MainMtot/MainMdot_th-1.0)
				#if MainEp<MainResi:
				#if abs(MainResi/MainEp-1.0)<0.003:
					Thrust = MainMtot*float(Isp)
					print 'MainChamber',now,MainOF,MainMdotF,Temp,P,MainMdot_th,MainMtot,Isp,Thrust
					break;
				#MainEp = MainResi

			
			MainAllTime   = np.append(MainAllTime  ,now      )
			MainAllOF     = np.append(MainAllOF    ,MainOF   )
			MainAllPres   = np.append(MainAllPres  ,Pres*0.1 )
			MainAllTemp   = np.append(MainAllTemp  ,Temp     )
			MainAllIsp    = np.append(MainAllIsp   ,Isp/g0   )
			MainAllMdotF  = np.append(MainAllMdotF ,MainMdotF)
			MainAllThrust = np.append(MainAllThrust,Thrust   )
			MainAllCH4    = np.append(MainAllCH4   ,CH4      )
			MainAllCO2    = np.append(MainAllCO2   ,CO2      )
			MainAllCO     = np.append(MainAllCO    ,CO       )
			MainAllH      = np.append(MainAllH     ,H        )
			MainAllH2     = np.append(MainAllH2    ,H2       )
			MainAllH2O    = np.append(MainAllH2O   ,H2O      )
			MainAllO      = np.append(MainAllO     ,O        )
			MainAllO2     = np.append(MainAllO2    ,O2       )
			MainAllOH     = np.append(MainAllOH    ,OH       )


			print CH4, CO2, CO, H, H2, H2O, O, O2, OH
			#MainAllCH4  = np.append(MainAllCH4,CH4) 
			#MainAllCO2  = np.append(MainAllCO2,CO2) 
			#MainAllCO   = np.append(MainAllCO ,CO ) 
			#MainAllH    = np.append(MainAllH  ,H  ) 
			#MainAllH2   = np.append(MainAllH2 ,H2 ) 
			#MainAllH2O  = np.append(MainAllH2O,H2O) 
			#MainAllO    = np.append(MainAllO  ,O  ) 
			#MainAllO2   = np.append(MainAllO2 ,O2 ) 
			#MainAllOH   = np.append(MainAllOH ,OH ) 




	
	#out[:,1] = MainAllTime
	#out[:,2] = MainAllOF
	#out = np.array([MainAllTime,MainAllMdotF]).T
	#print out
	#out = np.array([MainAllTime,MainAllOF]).T
	#print out

	#{{{
	direct = '../OUT/'
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

