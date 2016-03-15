#!/usr/bin/python
import subprocess as subcmd
import re
import numpy as np
import scipy as sp
from string import *

infile = 'file.out'
outfile = '../CEAData/ana.d'
outdat = open(outfile, 'w')
outdat.write('Pres[bar] ,O/F[-] ,Temp[K] ,rho[kg/m^3] ,Gibbs[kJ/kg],Mole[-],Gamma[-]\n')
No = 0
OF_start    = 40.0
OF_step     = 1.0
OF_end      = 60.0
OF_count    = int((OF_end-OF_start)/OF_step)
Pres_start  = 4.0
Pres_step   = 1.0
Pres_end    = 6.0
Pres_count  = int((Pres_end-Pres_start)/Pres_step)
Dia_cham = 0.03
Dia_nozl = 0.0085
Dia_ratio = (Dia_cham)**2/(Dia_nozl)**2
A_nozl = Dia_nozl**2*np.pi/4.0
print ('OF_start    =%s'%OF_start   )
print ('OF_step     =%s'%OF_step    )
print ('OF_end      =%s'%OF_end     )
print ('OF_count    =%s'%OF_count   )
print ('Pres_start  =%s'%Pres_start )
print ('Pres_step   =%s'%Pres_step  )
print ('Pres_end    =%s'%Pres_end   )
print ('Pres_count  =%s'%Pres_count )
for i in range(1,OF_count):
	of = OF_start+float(i)*OF_step
	for j in range(1,Pres_count):
		No = 1+No
		p = Pres_start+float(j)*Pres_step
		fl = open('file.inp','w')
		fl.write('prob rocket fac p,bar=%s,'%p)
		fl.write('ac/at=%s,\n'%Dia_ratio)
		fl.write('o/f=%s, pi/pe=1, eq\n'%of)
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
				CStar = strip(re.split(' ',inline)[18])
				break;

		#	elif re.match('', inline):
		#		Temp = strip(re.split(' ',inline)[16])
		#		print (Temp)
			inline = indat.readline()
		
		indat.close()
		Mdot_th = float(Pres)*10**5*float(A_nozl)*float(Gamma)*((2.0/(float(Gamma)+1.0))**((float(Gamma)+1.0)/(float(Gamma)-1.0)))**(1.0/2.0)/(float(Gamma)*8314.3/float(Mole)*float(Temp))**(1.0/2.0)
		print Mdot_th

		data_list = [Pres,of,Temp,rho,Gamma,CStar]
		data_dic[No] = data_list
		outdat = open(outfile, 'a')
		for d in data_dic.keys():
			unpacked = data_dic[d]
			data_str = ",".join([elem for elem in unpacked])
			outdat.write(data_str + "\n")
		
		outdat.close()
