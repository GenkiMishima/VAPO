#!/usr/bin/python
import subprocess as subcmd
import re
import numpy as np
import scipy as sp
from string import *

if __name__ == "__main__":
	infile = 'file.out'
	outfile = '../CEAData/ana.d'
	outdat = open(outfile, 'w')
	outdat.write('Pres_act[MPa] ,Pres_th[MPa] ,O/F[-] ,Temp[K] ,Mdot_th[kg/s] ,CStar_th[m/s] ,CStar_act[m/s] ,CStar_ratio[-] \n')
	No = 0
	Pres_start  = 4.0
	Pres_step   = 0.01
	Pres_end    = 7.0
	Pres_count  = int((Pres_end-Pres_start)/Pres_step)
	Dia_cham = 0.03
	Dia_nozl = 0.0085
	Dia_ratio = (Dia_cham)**2/(Dia_nozl)**2
	A_nozl = Dia_nozl**2*np.pi/4.0
	#INPUT
	Pres_act = sp.array([0.46,0.61,0.55,0.53,0.48])
	OF_act = sp.array([35.2,40.8,39.5,37.3,36.2])
	Mdot_act = sp.array([0.048+0.00137,0.062+0.00153,0.058+0.00146,0.052+0.00141,0.048+0.00133])
	print len(Mdot_act),Mdot_act.ndim
	redi = 0.001
	print ('Pres_start  =%s'%Pres_start )
	print ('Pres_step   =%s'%Pres_step  )
	print ('Pres_end    =%s'%Pres_end   )
	print ('Pres_count  =%s'%Pres_count )
	for i in range(0,len(Mdot_act)) :
		print i,Mdot_act[i]
		#break;
		for j in range(1,Pres_count):
			No = 1+No
			p = Pres_start+float(j)*Pres_step
			fl = open('file.inp','w')
			fl.write('prob rocket fac p,bar=%s,'%p)
			fl.write('ac/at=%s,\n'%Dia_ratio)
			fl.write('o/f=%s, pi/pe=1, eq\n'%OF_act[i])
			fl.write('react\n')
			fl.write('	oxid=O2(L) wt=100\n')
			fl.write('	fuel=PMMA  wt=100 t,k=293.15\n')
			fl.write('	h,kj/mol=-442.14  C 5 H 8 O 2\n')
			fl.write('end')
			fl.close()
			subcmd.call('./a.out')
		
			indat = open(infile, 'r')
			inline = indat.readline()
			data_dic = {}
			while inline:
				data_list = []
				if re.match(' O/F =', inline):
					of = strip(re.split('=',inline)[1])
				elif re.match(' P, BAR  ', inline):
					Pres = strip(re.split(' ',inline)[14])
				elif re.match(' T, K   ', inline):
					Temp = strip(re.split(' ',inline)[16])
				elif re.match(' RHO, KG/CU M', inline):
					rho = strip(re.split(' ',inline)[7])
				elif re.match(' M,', inline):
					Mole = strip(re.split(' ',inline)[12])
				elif re.match(' GAMMAs ', inline):
					Gamma = strip(re.split(' ',inline)[13])
				elif re.match(' CSTAR, M/SEC', inline):
					CStar_th = strip(re.split(' ',inline)[18])
					break;
		
			#	elif re.match('', inline):
			#		Temp = strip(re.split(' ',inline)[16])
			#		print (Temp)
				inline = indat.readline()
			
			indat.close()
			Mdot_th = float(Pres)*10**5*float(A_nozl)*float(Gamma)*((2.0/(float(Gamma)+1.0))**((float(Gamma)+1.0)/(float(Gamma)-1.0)))**(1.0/2.0)/(float(Gamma)*8314.3/float(Mole)*float(Temp))**(1.0/2.0)
			Mdot_rad = (Mdot_th - Mdot_act[i])/Mdot_th
			CStar_act = Pres_act[i]*10**6*float(A_nozl)/Mdot_act[i]
			CStar_ratio = CStar_act/float(CStar_th)
			if abs(Mdot_rad) <= redi :
				print 'ok'
				data_list = [str(Pres_act[i]),str(float(Pres)/10),of,Temp,str(Mdot_th),str(CStar_act),CStar_th,str(CStar_ratio)]
				data_dic[No] = data_list
				outdat = open(outfile, 'a')
				for d in data_dic.keys():
					unpacked = data_dic[d]
					data_str = ",".join([elem for elem in unpacked])
					outdat.write(data_str + "\n")
				
				outdat.close()
				break;
