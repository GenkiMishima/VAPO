#!/usr/bin/python
import subprocess as subcmd
import re
import numpy as np
import scipy as sp
from string import *

if __name__ == "__main__":
	import CEAReadPack
	ReadClass = CEAReadPack.Pack()
	infile = 'CEAdata.out'
	outfile = '../CEAData/MdotCheck10.d'
	outdat = open(outfile,'w')
	outdat.write('')
	outdat.close()
	No = 0
	#Pres_start  = 4.0
	#Pres_step   = 0.01
	#Pres_end    = 7.0
	#Pres_count  = int((Pres_end-Pres_start)/Pres_step)
	WeightStart = 1
	WeightEnd   = 100
	WeightStep  = 10
	WeightCount = int((WeightEnd-WeightStart)/WeightStep)
	Dia_cham = 0.03
	Dia_nozl = 0.0085
	Dia_ratio = (Dia_cham)**2/(Dia_nozl)**2
	A_nozl = Dia_nozl**2*np.pi/4.0
	for j in range(1,WeightCount):
		No = 1+No
		wt = WeightStart+float(j)*WeightStep
		fl = open('CEAdata.inp','w')
		fl.write('prob rocket fac p,bar=6.2,')
		fl.write('ac/at=%s,\n'%Dia_ratio)
		fl.write('o/f=40, pi/pe=1, eq\n')
		fl.write('react\n')
		fl.write('	oxid=O2(L) wt=%s\n'%wt)
		fl.write('	fuel=PMMA  wt=%s t,k=293.15\n'%wt)
		fl.write('	h,kj/mol=-442.14  C 5 H 8 O 2\n')
		fl.write('end')
		fl.close()
		subcmd.call('./a.out')
		data_dic = {}
		data_list = []
		Pres,of,Temp,rho,Mole,Gamma,CStar_th = ReadClass.Read(infile)
		Mdot_th = float(Pres)*10**5*float(A_nozl)*float(Gamma)*((2.0/(float(Gamma)+1.0))**((float(Gamma)+1.0)/(float(Gamma)-1.0)))**(1.0/2.0)/(float(Gamma)*8314.3/float(Mole)*float(Temp))**(1.0/2.0)
		outdat = open(outfile, 'a')
		data_list = [wt,str(Mdot_th)]
		for d in data_dic.keys():
			unpacked = data_dic[d]
			data_str = ",".join([elem for elem in unpacked])
			outdat.write(data_str + "\n")
		
		outdat.close()
		break;
