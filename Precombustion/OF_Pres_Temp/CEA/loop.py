#!/usr/bin/python
import subprocess as subcmd
import re
from string import *

infile = 'file.out'
outfile = '../CEAData/ana.d'
outdat = open(outfile, 'w')
outdat.write('Pres[bar] ,O/F[-] ,Temp[K] ,rho[kg/m^3] ,Gibbs[kJ/kg]\n')
No = 0
OF_start    = 40.0
OF_step     = 1.0
OF_end      = 60.0
OF_count    = int((OF_end-OF_start)/OF_step)
Pres_start  = 40.0
Pres_step   = 1.0
Pres_end    = 60.0
Pres_count  = int((Pres_end-Pres_start)/Pres_step)
Pres_count  = 2
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
		T = 3800.0
		fl = open('file.inp','w')
		fl.write('problem   case=LOXPMMA o/f= %s\n'%of)
		fl.write('      hp   p,bar=%s,'%p)
		fl.write('      t,k  =%s\n'%T)
		fl.write('react\n')
		fl.write('	oxid=O2(L) wt=100\n')
		fl.write('	fuel=PMMA  wt=100 t,k=293.15\n')
		fl.write('	h,kj/mol=-442.14  C 5 H 8 O 2\n')
		fl.write('end')
		fl.close()
		subcmd.call('./a.out')
		print '1'

		indat = open(infile, 'r')
		inline = indat.readline()
		data_dic = {}
		while inline:
			print '2'
			data_list = []
			if re.match(' O/F =', inline):
				of = strip(re.split('=',inline)[1])
			elif re.match(' P, BAR  ', inline):
				Pres = strip(re.split(' ',inline)[14])
			elif re.match(' T, K   ', inline):
				Temp = strip(re.split(' ',inline)[16])
			elif re.match(' RHO, KG/CU M', inline):
				rho = strip(re.split(' ',inline)[7])
			elif re.match(' G, KJ/KG', inline):
				Gibbs = strip(re.split(' ',inline)[10])
				data_list = [Pres,of,Temp,rho,Gibbs]
				data_dic[No] = data_list
		#	elif re.match('', inline):
		#		Temp = strip(re.split(' ',inline)[16])
		#		print (Temp)
			inline = indat.readline()
		
		indat.close()
		outdat = open(outfile, 'a')
		for d in data_dic.keys():
			print '3'
			unpacked = data_dic[d]
			data_str = ",".join([elem for elem in unpacked])
			outdat.write(data_str + "\n")
		
		outdat.close()
