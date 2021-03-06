#!/usr/bin/python
import subprocess as subcmd
import re
import numpy as np
import scipy as sp
from string import *


class Pack:
	def __init__(self):
		print ''
	def Read(self,infile):
		indat = open(infile, 'r')
		inline = indat.readline()
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
		return Pres,of,Temp,rho,Mole,Gamma,CStar_th

	def MatchMdot(self,Pres,of,Temp,rho,Mole,Gamma,CStar_th):
		Mdot_th = float(Pres)*10**5*float(A_nozl)*float(Gamma)*((2.0/(float(Gamma)+1.0))**((float(Gamma)+1.0)/(float(Gamma)-1.0)))**(1.0/2.0)/(float(Gamma)*8314.3/float(Mole)*float(Temp))**(1.0/2.0)
		Mdot_rad = (Mdot_th - Mdot_act[i])/Mdot_th
		CStar_act = Pres_act[i]*10**6*float(A_nozl)/Mdot_act[i]
		CStar_ratio = CStar_act/float(CStar_th)
		return [str(Pres_act[i]),str(float(Pres)/10),of,Temp,str(Mdot_th),str(CStar_act),CStar_th,str(CStar_ratio)]
		#data_list = [str(Pres_act[i]),str(float(Pres)/10),of,Temp,str(Mdot_th),str(CStar_act),CStar_th,str(CStar_ratio)]
