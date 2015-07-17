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
def PreVari(dire,MdotO):
	
	#Pre{{{
	PreVari = np.genfromtxt(dire+'Variable.d',delimiter=',')
	rawTime = PreVari[2:,0]
	rawPres = PreVari[2:,1]
	rawTemp = PreVari[2:,2]
	rawOF   = PreVari[2:,3]
	rawMdot = PreVari[2:,4]
	
	Time = np.arange(0,rawTime[-1],0.001)
	newPres = interpolate.splrep(rawTime,rawPres,s=0)
	newTemp = interpolate.splrep(rawTime,rawTemp,s=0)
	newOF   = interpolate.splrep(rawTime,rawOF,  s=0)
	newMdot = interpolate.splrep(rawTime,rawMdot,s=0)
	Pres = interpolate.splev(Time,newPres,der=0)
	Temp = interpolate.splev(Time,newTemp,der=0)
	OF   = interpolate.splev(Time,newOF,  der=0)
	Mdot = interpolate.splev(Time,newMdot,der=0)
	
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
	
	#}}}
	
	print 'ok'
	return rawTime

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
	
	#Main{{{
	MainVari = np.genfromtxt(dire+'Variable.d',delimiter=',')
	rawTime   = MainVari[2:,0]
	rawPres   = MainVari[2:,1]
	rawTemp   = MainVari[2:,2]
	rawOF     = MainVari[2:,3]
	rawMdot   = MainVari[2:,4]
	rawIsp    = MainVari[2:,5]
	rawThrust = MainVari[2:,6]
	Time = np.arange(0,rawTime[-1],0.001)
	newPres   = interpolate.splrep(rawTime,rawPres,  s=1)
	newTemp   = interpolate.splrep(rawTime,rawTemp,  s=0)
	newOF     = interpolate.splrep(rawTime,rawOF,    s=0)
	newMdot   = interpolate.splrep(rawTime,rawMdot,  s=1)
	newIsp    = interpolate.splrep(rawTime,rawIsp,   s=0)
	newThrust = interpolate.splrep(rawTime,rawThrust,s=0)
	Pres   = interpolate.splev(Time,newPres,  der=0)
	Temp   = interpolate.splev(Time,newTemp,  der=0)
	OF     = interpolate.splev(Time,newOF,    der=0)
	Mdot   = interpolate.splev(Time,newMdot,  der=0)
	Isp    = interpolate.splev(Time,newIsp,   der=0)
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
def MainFrac(dire,MdotO,Time):
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



if __name__ == "__main__":

	Spec = open('Spec.d','r')
	MdotO = Spec.read()
	Spec.close()
	
	dire = 'Pre/'
	PreTime = PreVari(dire,MdotO)
	PreFrac(dire,MdotO,PreTime)

	dire = 'Main/'
	MainTime = MainVari(dire,MdotO)
	MainFrac(dire,MdotO,MainTime)
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
##
