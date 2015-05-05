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
	outdat.write('Pres,Temp,O/F,MdotOxi,MdotTot\n')
	outdat.close()
	No = 0
	Pres_start  = 4.0
	Pres_step   = 1.0
	Pres_end    = 15.0
	Pres_count  = int((Pres_end-Pres_start)/Pres_step)
	of = 40.0
	#P = 6.2*2.0
	#WeightStart = 1.0
	#WeightEnd   = 100.0
	#WeightStep  = 10.0
	#WeightCount = int((WeightEnd-WeightStart)/WeightStep)
	wt = 100.0
	Dia_cham = 0.03
	Dia_nozl = 0.0085
	Dia_ratio = (Dia_cham)**2/(Dia_nozl)**2
	A_nozl = Dia_nozl**2*np.pi/4.0
	for j in range(1,Pres_count):
		No = 1+No
		P = Pres_start+float(j)*Pres_step
		fl = open('CEAdata.inp','w')
		fl.write('prob rocket fac p,bar=%s,'%P)
		fl.write('ac/at=%s,\n'%Dia_ratio)
		fl.write('o/f=%s, pi/pe=1, eq\n'%of)
		fl.write('react\n')
		fl.write('	oxid=O2(L) wt=100\n')
		fl.write('	fuel=PMMA  wt=100 t,k=293.15\n')
		fl.write('	h,kj/mol=-442.14  C 5 H 8 O 2\n')
		fl.write('end')
		fl.close()
		subcmd.call('./a.out')
		data_dic = {}
		data_list = []
		Pres,of,Temp,rho,Mole,Gamma,CStar_th = ReadClass.Read(infile)
		Mdot_th = float(Pres)*10**5*float(A_nozl)*float(Gamma)*((2.0/(float(Gamma)+1.0))**((float(Gamma)+1.0)/(float(Gamma)-1.0)))**(1.0/2.0)/(float(Gamma)*8314.3/float(Mole)*float(Temp))**(1.0/2.0)
		outdat = open(outfile, 'a')
		data_list = [str(P),Temp,str(of),str(Mdot_th)]
		data_dic[No] = data_list
		for d in data_dic.keys():
			unpacked = data_dic[d]
			data_str = ",".join([elem for elem in unpacked])
			outdat.write(data_str + "\n")
		
		outdat.close()
