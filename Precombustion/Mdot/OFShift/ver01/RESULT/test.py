#!/usr/bin/python
import subprocess as subcmd
import re
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import math
import sys
import csv
from scipy import interpolate
from string import *
#Length:m
#Mass:kg
#Time:s
def PreVari(dire,MdotO,j):
	
	#Pre{{{
	PreVari = np.genfromtxt(dire+'Variable.d',delimiter=',')
	return PreVari[2:,0],PreVari[2:,j]
	#rawTime = PreVari[2:,0]
	#rawPres = PreVari[2:,1]
	#rawTemp = PreVari[2:,2]
	#rawOF   = PreVari[2:,3]
	#rawMdot = PreVari[2:,4]
	#
	#Time = np.arange(0,rawTime[-1],0.001)
	#newPres = interpolate.splrep(rawTime,rawPres,s=1)
	#newTemp = interpolate.splrep(rawTime,rawTemp,s=1)
	#newOF   = interpolate.splrep(rawTime,rawOF,  s=1)
	#newMdot = interpolate.splrep(rawTime,rawMdot,s=1)
	#Pres = interpolate.splev(Time,newPres,der=0)
	#Temp = interpolate.splev(Time,newTemp,der=0)
	#OF   = interpolate.splev(Time,newOF,  der=0)
	#Mdot = interpolate.splev(Time,newMdot,der=0)
	#
	##print Time[:20]
	##print Pres[:20]
	#
	#plt.plot(Time,Pres)
	#plt.grid()
	###plt.title('MdotO:%s[kg/s]'%MdotO)
	#plt.legend(('LOx:%s[kg/s]'%float(MdotO),))
	#plt.xlabel('Time[s]')
	#plt.ylabel('Pres[MPa]')
	##plt.ylim([0,100])
	#plt.savefig(dire+"Pres_Mdot%s.png"%float(MdotO))
	#plt.close()
	#
	#plt.plot(Time,Temp)
	#plt.grid()
	###plt.title('MdotO:%s[kg/s]'%MdotO)
	#plt.legend(('LOx:%s[kg/s]'%float(MdotO),))
	#plt.xlabel('Time[s]')
	#plt.ylabel('Temp[K]')
	##plt.ylim([0,100])
	#plt.savefig(dire+"Temp_Mdot%s.png"%float(MdotO))
	#plt.close()
	#
	#plt.plot(Time,OF)
	#plt.grid()
	###plt.title('MdotO:%s[kg/s]'%MdotO)
	#plt.legend(('LOx:%s[kg/s]'%float(MdotO),))
	#plt.xlabel('Time[s]')
	#plt.ylabel('OF[-]')
	##plt.ylim([0,100])
	#plt.savefig(dire+"OF_Mdot%s.png"%float(MdotO))
	#plt.close()
	#
	#plt.plot(Time,Mdot)
	#plt.grid()
	###plt.title('MdotO:%s[kg/s]'%MdotO)
	#plt.legend(('LOx:%s[kg/s]'%float(MdotO),))
	#plt.xlabel('Time[s]')
	#plt.ylabel('Mdot[kg/s]')
	##plt.ylim([0,100])
	#plt.savefig(dire+"Mdot_Mdot%s.png"%float(MdotO))
	#plt.close()
	#
	##}}}
	#
	#print 'ok'
	#return rawTime

def PreFrac(dire,MdotO,Time):
	#{{{
	Frac = np.genfromtxt(dire+'Fraction.d',delimiter=',')

	#CH4 = Frac[2:,0]
	#CO2 = Frac[2:,1]
	#CO  = Frac[2:,2]
	#H   = Frac[2:,3]
	#H2  = Frac[2:,4]
	#H2O = Frac[2:,5]
	#O   = Frac[2:,6]
	#O2  = Frac[2:,7]
	#OH  = Frac[2:,8]

	plt.plot(Time,Frac[2:,1])
	plt.plot(Time,Frac[2:,2])
	plt.plot(Time,Frac[2:,3])
	plt.plot(Time,Frac[2:,4])
	plt.plot(Time,Frac[2:,5],'--')
	plt.plot(Time,Frac[2:,6],'--')
	plt.plot(Time,Frac[2:,7],'--')
	plt.plot(Time,Frac[2:,8],'--')
	plt.grid()
	##plt.title('MdotO:%s[kg/s]'%MdotO)
	plt.legend(( 'CO2 ',  'CO ',  'H ',  'H2 ',  'H2O ',  'O ',  'O2 ', 'OH' ))
	plt.xlabel('Time[s]')
	plt.ylabel('Mole Fraction')
	#plt.ylim([0,100])
	plt.savefig(dire+"Frac_Mdot%s.png"%float(MdotO))
	plt.close()
	#}}}

def MainVari(dire,MdotO):
	
	#Pre{{{
	MainVari = np.genfromtxt(dire+'Variable.d',delimiter=',')
	rawTime   = MainVari[2:,0]
	rawPres   = MainVari[2:,1]
	rawTemp   = MainVari[2:,2]
	rawOF     = MainVari[2:,3]
	rawMdot   = MainVari[2:,4]
	rawIsp    = MainVari[2:,5]
	rawThrust = MainVari[2:,6]
	Time = np.arange(0,rawTime[-1],0.001)
	newPres = interpolate.splrep(rawTime,rawPres,s=1)
	Pres = interpolate.splev(Time,newPres,der=0)
	newTemp = interpolate.splrep(rawTime,rawTemp,s=1)
	Temp = interpolate.splev(Time,newTemp,der=0)
	newOF = interpolate.splrep(rawTime,rawOF,s=1)
	OF = interpolate.splev(Time,newOF,der=0)
	newMdot = interpolate.splrep(rawTime,rawMdot,s=1)
	Mdot = interpolate.splev(Time,newMdot,der=0)
	newIsp = interpolate.splrep(rawTime,rawIsp,s=1)
	Isp = interpolate.splev(Time,newIsp,der=0)
	newThrust = interpolate.splrep(rawTime,rawThrust,s=1)
	Thrust = interpolate.splev(Time,newThrust,der=0)
	
	
	#print Time[:20]
	#print Pres[:20]
	
	plt.plot(Time,Pres)
	plt.grid()
	##plt.title('MdotO:%s[kg/s]'%MdotO)
	plt.legend(('LOx:%s[kg/s]'%float(MdotO),))
	plt.xlabel('Time[s]')
	plt.ylabel('Pres[MPa]')
	#plt.ylim([0,100])
	plt.savefig(dire+"Pres_Mdot%s.png"%float(MdotO))
	plt.close()
	
	plt.plot(Time,Temp)
	plt.grid()
	##plt.title('MdotO:%s[kg/s]'%MdotO)
	plt.legend(('LOx:%s[kg/s]'%float(MdotO),))
	plt.xlabel('Time[s]')
	plt.ylabel('Temp[K]')
	#plt.ylim([0,100])
	plt.savefig(dire+"Temp_Mdot%s.png"%float(MdotO))
	plt.close()
	
	plt.plot(Time,OF)
	plt.grid()
	##plt.title('MdotO:%s[kg/s]'%MdotO)
	plt.legend(('LOx:%s[kg/s]'%float(MdotO),))
	plt.xlabel('Time[s]')
	plt.ylabel('OF[-]')
	#plt.ylim([0,100])
	plt.savefig(dire+"OF_Mdot%s.png"%float(MdotO))
	plt.close()
	
	plt.plot(Time,Mdot)
	plt.grid()
	##plt.title('MdotO:%s[kg/s]'%MdotO)
	plt.legend(('LOx:%s[kg/s]'%float(MdotO),))
	plt.xlabel('Time[s]')
	plt.ylabel('Mdot[kg/s]')
	#plt.ylim([0,100])
	plt.savefig(dire+"Mdot_Mdot%s.png"%float(MdotO))
	plt.close()
	
	plt.plot(Time,Isp)
	plt.grid()
	##plt.title('IspO:%s[kg/s]'%IspO)
	plt.legend(('LOx:%s[kg/s]'%float(MdotO),))
	plt.xlabel('Time[s]')
	plt.ylabel('Isp[kg/s]')
	#plt.ylim([0,100])
	plt.savefig(dire+"Isp_Isp%s.png"%float(MdotO))
	plt.close()
	
	plt.plot(Time,Thrust)
	plt.grid()
	##plt.title('ThrustO:%s[kg/s]'%ThrustO)
	plt.legend(('LOx:%s[kg/s]'%float(MdotO),))
	plt.xlabel('Time[s]')
	plt.ylabel('Thrust[kg/s]')
	#plt.ylim([0,100])
	plt.savefig(dire+"Thrust_Thrust%s.png"%float(MdotO))
	plt.close()
	
	#}}}
	
	print 'ok'
	return rawTime
def MainFrac(dire):
	#{{{
	Frac = np.genfromtxt(dire+'Fraction.d',delimiter=',')

	#CH4 = Frac[:,0]
	#CO2 = Frac[:,1]
	#CO  = Frac[:,2]
	#H   = Frac[:,3]
	#H2  = Frac[:,4]
	#H2O = Frac[:,5]
	#O   = Frac[:,6]
	#O2  = Frac[:,7]
	#OH  = Frac[:,8]

	#plt.plot(Time,Frac[2:,1])
	#plt.plot(Time,Frac[2:,2])
	#plt.plot(Time,Frac[2:,3])
	#plt.plot(Time,Frac[2:,4])
	#plt.plot(Time,Frac[2:,5],'--')
	#plt.plot(Time,Frac[2:,6],'--')
	#plt.plot(Time,Frac[2:,7],'--')
	#plt.plot(Time,Frac[2:,8],'--')
	#plt.grid()
	###plt.title('MdotO:%s[kg/s]'%MdotO)
	#plt.legend(( 'CO2 ',  'CO ',  'H ',  'H2 ',  'H2O ',  'O ',  'O2 ', 'OH' ))
	#plt.xlabel('Time[s]')
	#plt.ylabel('Mole Fraction')
	##plt.ylim([0,100])
	#plt.savefig(dire+"Frac_Mdot%s.png"%float(MdotO))
	#plt.close()
	#}}}



if __name__ == "__main__":

	#Spec = open('Spec.d','r')
	#MdotO = Spec.read()
	#Spec.close()
	VariName = ['Pres[MPa]','Temp[K]','OF[-]','Mdot[kg/s]','Isp[s]','Thrust[N]']
	#sys.exit()

	for j in range(1,4,1):
		print j
		NewVari =  np.array([])
		NewMdotO =  np.array([])
		for i in range(30,85,5):
			print i
			MdotO = i/1000.0
			NewMdotO = np.append(NewMdotO,MdotO)

			dire = 'Mdot0%s'%i+'/Pre/'
			rawTime, rawVari = PreVari(dire,MdotO,j)
			Time = np.arange(0,rawTime[-1],0.001)
			AveVari = np.average(rawVari)
			NewVari = np.append(NewVari,AveVari)

		SpVari = interpolate.splrep(NewMdotO,NewVari,s=1)
		Vari = interpolate.splev(NewMdotO,SpVari,der=0)
		plt.plot(NewMdotO,Vari)
		plt.grid()
		plt.xlabel('LOx[kg/s]')
		plt.ylabel('%s'%VariName[j-1])
		Name = j-1
		plt.savefig('Pre/%d.png'%Name)
		plt.close()
		del NewVari
		del NewMdotO

	for j in range(1,7,1):
		print j
		NewVari =  np.array([])
		NewMdotO =  np.array([])
		for i in range(30,85,5):
			print i
			MdotO = i/1000.0
			NewMdotO = np.append(NewMdotO,MdotO)

			dire = 'Mdot0%s'%i+'/Main/'
			rawTime, rawVari = PreVari(dire,MdotO,j)
			Time = np.arange(0,rawTime[-1],0.001)
			AveVari = np.average(rawVari)
			NewVari = np.append(NewVari,AveVari)

		SpVari = interpolate.splrep(NewMdotO,NewVari,s=1)
		Vari = interpolate.splev(NewMdotO,SpVari,der=0)
		plt.plot(NewMdotO,Vari)
		plt.grid()
		plt.xlabel('LOx[kg/s]')
		plt.ylabel('%s'%VariName[j-1])
		Name = j-1
		plt.savefig('Main/%d.png'%Name)
		plt.close()
		del NewVari
		del NewMdotO

	NewVari1 =  np.array([])
	NewVari2 =  np.array([])
	NewVari3 =  np.array([])
	NewVari4 =  np.array([])
	NewVari5 =  np.array([])
	NewVari6 =  np.array([])
	NewVari7 =  np.array([])
	NewVari8 =  np.array([])
	NewMdotO =  np.array([])
	for i in range(30,85,5):
		print i
		MdotO = i/1000.0
		NewMdotO = np.append(NewMdotO,MdotO)

		dire = 'Mdot0%s'%i+'/Main/'
		#rawTime, rawVari = PreVari(dire,MdotO,j)
		Frac = np.genfromtxt(dire+'Fraction.d',delimiter=',')

		#NewVari = np.append(NewVari,AveVari)
		#CH4 = Frac[:,0]
		#CO2 = Frac[:,1]
		#CO  = Frac[:,2]
		#H   = Frac[:,3]
		#H2  = Frac[:,4]
		#H2O = Frac[:,5]
		#O   = Frac[:,6]
		#O2  = Frac[:,7]
		#OH  = Frac[:,8]
		Time = np.arange(0,rawTime[-1],0.001)
		NewVari1 = np.append(NewVari1,Frac[-1,1])
		NewVari2 = np.append(NewVari2,Frac[-1,2])
		NewVari3 = np.append(NewVari3,Frac[-1,3])
		NewVari4 = np.append(NewVari4,Frac[-1,4])
		NewVari5 = np.append(NewVari5,Frac[-1,5])
		NewVari6 = np.append(NewVari6,Frac[-1,6])
		NewVari7 = np.append(NewVari7,Frac[-1,7])
		NewVari8 = np.append(NewVari8,Frac[-1,8])

	SpVari1 = interpolate.splrep(NewMdotO,NewVari1,s=1)
	SpVari2 = interpolate.splrep(NewMdotO,NewVari2,s=1)
	SpVari3 = interpolate.splrep(NewMdotO,NewVari3,s=1)
	SpVari4 = interpolate.splrep(NewMdotO,NewVari4,s=1)
	SpVari5 = interpolate.splrep(NewMdotO,NewVari5,s=1)
	SpVari6 = interpolate.splrep(NewMdotO,NewVari6,s=1)
	SpVari7 = interpolate.splrep(NewMdotO,NewVari7,s=1)
	SpVari8 = interpolate.splrep(NewMdotO,NewVari8,s=1)
	Vari1 = interpolate.splev(NewMdotO,SpVari1,der=0)
	Vari2 = interpolate.splev(NewMdotO,SpVari2,der=0)
	Vari3 = interpolate.splev(NewMdotO,SpVari3,der=0)
	Vari4 = interpolate.splev(NewMdotO,SpVari4,der=0)
	Vari5 = interpolate.splev(NewMdotO,SpVari5,der=0)
	Vari6 = interpolate.splev(NewMdotO,SpVari6,der=0)
	Vari7 = interpolate.splev(NewMdotO,SpVari7,der=0)
	Vari8 = interpolate.splev(NewMdotO,SpVari8,der=0)
	plt.plot(NewMdotO,Vari1)
	plt.plot(NewMdotO,Vari2)
	plt.plot(NewMdotO,Vari3)
	plt.plot(NewMdotO,Vari4)
	plt.plot(NewMdotO,Vari5,'--')
	plt.plot(NewMdotO,Vari6,'--')
	plt.plot(NewMdotO,Vari7,'--')
	plt.plot(NewMdotO,Vari8,'--')
	plt.grid()
	plt.legend(( 'CO2 ',  'CO ',  'H ',  'H2 ',  'H2O ',  'O ',  'O2 ', 'OH' ))
	plt.xlabel('LOx[kg/s]')
	#plt.ylabel('%s'%VariName[j-1])
	plt.savefig('Main/Fraction.png')
	plt.close()
	del NewVari1
	del NewVari2
	del NewVari3
	del NewVari4
	del NewVari5
	del NewVari6
	del NewVari7
	del NewVari8
	del NewMdotO

		#sys.exit()
		#for j in range(1,7,1):
		#	dire = 'Mdot0%s'%i+'/Main/'
		#	#MainTime = MainVari(dire,MdotO)
		#	#MainFrac(dire,MdotO,MainTime)
	#print data

#
#	#Pre{{{
#	dire = 'Pre/'
#	PreVari = sp.genfromtxt(dire+'Variable.d',delimiter=',')
#	Time = PreVari[:,0]
#	Pres = PreVari[:,1]
#	Temp = PreVari[:,2]
#	OF   = PreVari[:,3]
#	Mdot = PreVari[:,4]
#
#
#	#print Time[:20]
#	#print Pres[:20]
#
#	plt.plot(Time,Pres)
#	plt.grid()
#	##plt.title('MdotO:%s[kg/s]'%MdotO)
#	plt.legend(('LOx:%s[kg/s]'%float(MdotO),))
#	plt.xlabel('Time[s]')
#	plt.ylabel('Pres[MPa]')
#	#plt.ylim([0,100])
#	plt.savefig(dire+"Pres_Mdot%s.png"%float(MdotO))
#	plt.close()
#
#	plt.plot(Time,Temp)
#	plt.grid()
#	##plt.title('MdotO:%s[kg/s]'%MdotO)
#	plt.legend(('LOx:%s[kg/s]'%float(MdotO),))
#	plt.xlabel('Time[s]')
#	plt.ylabel('Temp[K]')
#	#plt.ylim([0,100])
#	plt.savefig(dire+"Temp_Mdot%s.png"%float(MdotO))
#	plt.close()
#
#	plt.plot(Time,OF)
#	plt.grid()
#	##plt.title('MdotO:%s[kg/s]'%MdotO)
#	plt.legend(('LOx:%s[kg/s]'%float(MdotO),))
#	plt.xlabel('Time[s]')
#	plt.ylabel('OF[-]')
#	#plt.ylim([0,100])
#	plt.savefig(dire+"OF_Mdot%s.png"%float(MdotO))
#	plt.close()
#
#	plt.plot(Time,Mdot)
#	plt.grid()
#	##plt.title('MdotO:%s[kg/s]'%MdotO)
#	plt.legend(('LOx:%s[kg/s]'%float(MdotO),))
#	plt.xlabel('Time[s]')
#	plt.ylabel('Mdot[kg/s]')
#	#plt.ylim([0,100])
#	plt.savefig(dire+"Mdot_Mdot%s.png"%float(MdotO))
#	plt.close()
#
#	#}}}
#
#
#	Frac = sp.genfromtxt(dire+'Fraction.d',delimiter=',')
#	print sp.genfromtxt(dire+'Fraction.d',delimiter=',')
#
#	CH4 = Frac[:,0]
#	CO2 = Frac[:,1]
#	CO  = Frac[:,2]
#	H   = Frac[:,3]
#	H2  = Frac[:,4]
#	H2O = Frac[:,5]
#	O   = Frac[:,6]
#	O2  = Frac[:,7]
#	OH  = Frac[:,8]
#
#	plt.plot(Time,CH4)
#	plt.plot(Time,Frac[:,1])
#	plt.plot(Time,Frac[:,2])
#	plt.plot(Time,Frac[:,3])
#	plt.plot(Time,Frac[:,4])
#	plt.plot(Time,Frac[:,5])
#	plt.plot(Time,Frac[:,6])
#	plt.plot(Time,Frac[:,7])
#	plt.plot(Time,Frac[:,8])
#	plt.grid()
#	##plt.title('MdotO:%s[kg/s]'%MdotO)
#	plt.legend(('LOx:%s[kg/s]'%float(MdotO),))
#	plt.xlabel('Time[s]')
#	plt.ylabel(' ')
#	#plt.ylim([0,100])
#	plt.savefig(dire+"Frac_Mdot%s.png"%float(MdotO))
#	plt.close()
#
#
#	#Main{{{
#	dire = 'Main/'
#	MainVari = sp.genfromtxt(dire+'Variable.d',delimiter=',')
#	Time = MainVari[:,0]
#	Pres = MainVari[:,1]
#	Temp = MainVari[:,2]
#	OF   = MainVari[:,3]
#	Mdot = MainVari[:,4]
#
#
#	#print Time[:20]
#	#print Pres[:20]
#
#	plt.plot(Time,Pres)
#	plt.grid()
#	##plt.title('MdotO:%s[kg/s]'%MdotO)
#	plt.legend(('LOx:%s[kg/s]'%float(MdotO),))
#	plt.xlabel('Time[s]')
#	plt.ylabel('Pres[MPa]')
#	#plt.ylim([0,100])
#	plt.savefig(dire+"Pres_Mdot%s.png"%float(MdotO))
#	plt.close()
#
#	plt.plot(Time,Temp)
#	plt.grid()
#	##plt.title('MdotO:%s[kg/s]'%MdotO)
#	plt.legend(('LOx:%s[kg/s]'%float(MdotO),))
#	plt.xlabel('Time[s]')
#	plt.ylabel('Temp[K]')
#	#plt.ylim([0,100])
#	plt.savefig(dire+"Temp_Mdot%s.png"%float(MdotO))
#	plt.close()
#
#	plt.plot(Time,OF)
#	plt.grid()
#	##plt.title('MdotO:%s[kg/s]'%MdotO)
#	plt.legend(('LOx:%s[kg/s]'%float(MdotO),))
#	plt.xlabel('Time[s]')
#	plt.ylabel('OF[-]')
#	#plt.ylim([0,100])
#	plt.savefig(dire+"OF_Mdot%s.png"%float(MdotO))
#	plt.close()
#
#	plt.plot(Time,Mdot)
#	plt.grid()
#	##plt.title('MdotO:%s[kg/s]'%MdotO)
#	plt.legend(('LOx:%s[kg/s]'%float(MdotO),))
#	plt.xlabel('Time[s]')
#	plt.ylabel('Mdot[kg/s]')
#	#plt.ylim([0,100])
#	plt.savefig(dire+"Mdot_Mdot%s.png"%float(MdotO))
#	plt.close()
#
#	#Frac = sp.genfromtxt(dire+'Fraction.d',delimiter=',')
#	#print sp.genfromtxt(dire+'Fraction.d',delimiter=',')
#
#	#CH4 = Frac[:,0]
#	#CO2 = Frac[:,1]
#	#CO  = Frac[:,2]
#	#H   = Frac[:,3]
#	#H2  = Frac[:,4]
#	#H2O = Frac[:,5]
#	#O   = Frac[:,6]
#	#O2  = Frac[:,7]
#	#OH  = Frac[:,8]
#
#	#plt.plot(Time,CH4)
#	#plt.plot(Time,Frac[:,1])
#	#plt.plot(Time,Frac[:,2])
#	#plt.plot(Time,Frac[:,3])
#	#plt.plot(Time,Frac[:,4])
#	#plt.plot(Time,Frac[:,5])
#	#plt.plot(Time,Frac[:,6])
#	#plt.plot(Time,Frac[:,7])
#	#plt.plot(Time,Frac[:,8])
#	#plt.grid()
#	###plt.title('MdotO:%s[kg/s]'%MdotO)
#	#plt.legend(('LOx:%s[kg/s]'%float(MdotO),))
#	#plt.xlabel('Time[s]')
#	#plt.ylabel(' ')
#	##plt.ylim([0,100])
#	#plt.savefig(dire+"Frac_Mdot%s.png"%float(MdotO))
#	#plt.close()
#	#}}}
#
##
##	#PLOT{{{
##	plt.plot(PreAllTime,PreAllPres)
##	plt.grid()
##	##plt.title('MdotO:%s[kg/s]'%MdotO)
##	plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
##	plt.xlabel('Time[s]')
##	plt.ylabel('Pres[MPa]')
##	#plt.ylim([0,100])
##	plt.savefig("PrePres_%s.png"%int(PreLength*1000.0))
##	plt.close()
##
##	plt.plot(PreAllTime,PreAllTemp)
##	plt.grid()
##	##plt.title('MdotO:%s[kg/s]'%MdotO)
##	plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
##	plt.xlabel('Time[s]')
##	plt.ylabel('Temp[K]')
##	#plt.ylim([0,100])
##	plt.savefig("PreTemp_%s.png"%int(PreLength*1000.0))
##	plt.close()
##
##	plt.plot(PreAllTime,PreAllOF)
##	plt.grid()
##	##plt.title('MdotO:%s[kg/s]'%MdotO)
##	plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
##	plt.xlabel('Time[s]')
##	plt.ylabel('OF')
##	#plt.ylim([0,100])
##	plt.savefig("PreOF_%s.png"%int(PreLength*1000.0))
##	plt.close()
##
##	plt.plot(PreAllTime,PreAllMdotF)
##	plt.grid()
##	##plt.title('MdotO:%s[kg/s]'%MdotO)
##	plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
##	plt.xlabel('Time[s]')
##	plt.ylabel('MainMdotF[kg/s]')
##	#plt.ylim([0,100])
##	plt.savefig("PreMdotF_%s.png"%int(PreLength*1000.0))
##	plt.close()
##
##	plt.plot(MainAllTime,MainAllMdotF)
##	plt.grid()
##	##plt.title('MdotO:%s[kg/s]'%MdotO)
##	plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
##	plt.xlabel('Time[s]')
##	plt.ylabel('MainMdotF[kg/s]')
##	#plt.ylim([0,100])
##	plt.savefig("MainMdotF_%s.png"%int(PreLength*1000.0))
##	plt.close()
##
##	plt.plot(MainAllTime,MainAllOF)
##	plt.grid()
##	##plt.title('MdotO:%s[kg/s]'%MdotO)
##	plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
##	plt.xlabel('Time[s]')
##	plt.ylabel('MainOF')
##	#plt.ylim([0,100])
##	plt.savefig("MainOF_%s.png"%int(PreLength*1000.0))
##	plt.close()
##
##	plt.plot(MainAllTime,MainAllTemp)
##	plt.grid()
##	##plt.title('MdotO:%s[kg/s]'%MdotO)
##	plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
##	plt.xlabel('Time[s]')
##	plt.ylabel('MainTemp[K]')
##	#plt.ylim([0,100])
##	plt.savefig("MainTemp_%s.png"%int(PreLength*1000.0))
##	plt.close()
##
##	plt.plot(MainAllTime,MainAllPres)
##	plt.grid()
##	##plt.title('MdotO:%s[kg/s]'%MdotO)
##	plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
##	plt.xlabel('Time[s]')
##	plt.ylabel('Pres[MPa]')
##	#plt.ylim([0,100])
##	plt.savefig("MainPres_%s.png"%int(PreLength*1000.0))
##	plt.close()
##
##	plt.plot(MainAllTime,MainAllIsp)
##	plt.grid()
##	##plt.title('MdotO:%s[kg/s]'%MdotO)
##	plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
##	plt.xlabel('Time[s]')
##	plt.ylabel('Isp[s]')
##	#plt.ylim([0,100])
##	plt.savefig("MainIsp_%s.png"%int(PreLength*1000.0))
##	plt.close()
##
##	plt.plot(MainAllTime,MainAllThrust)
##	plt.grid()
##	##plt.title('MdotO:%s[kg/s]'%MdotO)
##	plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
##	plt.xlabel('Time[s]')
##	plt.ylabel('F[N]')
##	#plt.ylim([0,100])
##	plt.savefig("MainThrust_%s.png"%int(PreLength*1000.0))
##	plt.close()
##
##	#plt.show()}}}
