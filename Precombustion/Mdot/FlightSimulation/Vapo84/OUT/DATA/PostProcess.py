#!/usr/bin/python
import subprocess as subcmd
import re
import scipy as sp
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import lines
import math
import sys
import csv
from string import *
from scipy import interpolate
#Length:m
#Mass:kg
#Time:s
def integ(x, tck, constant=-1):
    x = np.atleast_1d(x)
    out = np.zeros(x.shape, dtype=x.dtype)
    for n in xrange(len(out)):
        out[n] = interpolate.splint(0, x[n], tck)
    out += constant
    return out


# Cubic-spline
def PreVari(dire,MdotO):
	
	#Pre{{{
	PreVari = sp.genfromtxt(dire+'Variable.d',delimiter=',')
	Time = PreVari[:,0]
	Pres = PreVari[:,1]
	Temp = PreVari[:,2]
	OF   = PreVari[:,3]
	Mdot = PreVari[:,4]
	Gamma= PreVari[:,5]
	Mole = PreVari[:,6]
	
	print len(Time),Pres
	
	#z = np.polyfit(Time,Pres,2)
	#p = np.poly1d(z)
	slope , intercept, _, _,_ = stats.linregress(Time,Pres)
	
	fig = plt.figure()
	ax = fig.add_subplot(111)
	sc = ax.scatter(Time,Pres,s=303, color="b")
	func = lambda x: x * slope + intercept
	line = lines.Line2D([0,303],[Time,func(Time)],color="r")
	#ax.add_line(line)
	#plt.show()
	plt.close()
	
	
	#print Time[:20]
	#print Pres[:20]
	
	plt.plot(Time,Pres)
	#plt.plot(Time,(a*Time+b))
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
	
	plt.plot(Time,Gamma)
	plt.grid()
	##plt.title('MdotO:%s[kg/s]'%MdotO)
	plt.legend(('LOx:%s[kg/s]'%float(MdotO),))
	plt.xlabel('Time[s]')
	plt.ylabel('Mdot[kg/s]')
	#plt.ylim([0,100])
	plt.savefig(dire+"Gamma_Mdot%s.png"%float(MdotO))
	plt.close()
	
	plt.plot(Time,Mole)
	plt.grid()
	##plt.title('MdotO:%s[kg/s]'%MdotO)
	plt.legend(('LOx:%s[kg/s]'%float(MdotO),))
	plt.xlabel('Time[s]')
	plt.ylabel('Mdot[kg/s]')
	#plt.ylim([0,100])
	plt.savefig(dire+"Mole_Mdot%s.png"%float(MdotO))
	plt.close()
	#}}}
	
	return Time

def PreFrac(dire,MdotO,Time):
	#{{{
	Frac = sp.genfromtxt(dire+'Fraction.d',delimiter=',')

	CH4 = Frac[:,0]
	CO2 = Frac[:,1]
	CO  = Frac[:,2]
	H   = Frac[:,3]
	H2  = Frac[:,4]
	H2O = Frac[:,5]
	O   = Frac[:,6]
	O2  = Frac[:,7]
	OH  = Frac[:,8]

	plt.plot(Time,Frac[:,1])
	plt.plot(Time,Frac[:,2])
	plt.plot(Time,Frac[:,3])
	plt.plot(Time,Frac[:,4])
	plt.plot(Time,Frac[:,5],'--')
	plt.plot(Time,Frac[:,6],'--')
	plt.plot(Time,Frac[:,7],'--')
	plt.plot(Time,Frac[:,8],'--')
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
	MainVari = sp.genfromtxt(dire+'Variable.d',delimiter=',')
	Time   = MainVari[:,0]
	Pres   = MainVari[:,1]
	Temp   = MainVari[:,2]
	OF     = MainVari[:,3]
	Mdot   = MainVari[:,4]
	Gamma  = MainVari[:,5]
	Mole   = MainVari[:,6]
	
	
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
	
	plt.plot(Time,Gamma)
	plt.grid()
	##plt.title('MdotO:%s[kg/s]'%MdotO)
	plt.legend(('LOx:%s[kg/s]'%float(MdotO),))
	plt.xlabel('Time[s]')
	plt.ylabel('Mdot[kg/s]')
	#plt.ylim([0,100])
	plt.savefig(dire+"Gamma_Mdot%s.png"%float(MdotO))
	plt.close()
	
	plt.plot(Time,Mole)
	plt.grid()
	##plt.title('MdotO:%s[kg/s]'%MdotO)
	plt.legend(('LOx:%s[kg/s]'%float(MdotO),))
	plt.xlabel('Time[s]')
	plt.ylabel('Mdot[kg/s]')
	#plt.ylim([0,100])
	plt.savefig(dire+"Mole_Mdot%s.png"%float(MdotO))
	plt.close()
	
	#plt.plot(Time,Isp)
	#plt.grid()
	###plt.title('IspO:%s[kg/s]'%IspO)
	#plt.legend(('LOx:%s[kg/s]'%float(MdotO),))
	#plt.xlabel('Time[s]')
	#plt.ylabel('Isp[kg/s]')
	##plt.ylim([0,100])
	#plt.savefig(dire+"Isp_Isp%s.png"%float(MdotO))
	#plt.close()
	#
	#plt.plot(Time,Thrust)
	#plt.grid()
	###plt.title('ThrustO:%s[kg/s]'%ThrustO)
	#plt.legend(('LOx:%s[kg/s]'%float(MdotO),))
	#plt.xlabel('Time[s]')
	#plt.ylabel('Thrust[kg/s]')
	##plt.ylim([0,100])
	#plt.savefig(dire+"Thrust_Thrust%s.png"%float(MdotO))
	#plt.close()
	
	#}}}
	
	return Time
def MainFrac(dire,MdotO,Time):
	#{{{
	Frac = sp.genfromtxt(dire+'Fraction.d',delimiter=',')

	#CH4 = Frac[:,0]
	#CO2 = Frac[:,1]
	#CO  = Frac[:,2]
	#H   = Frac[:,3]
	#H2  = Frac[:,4]
	#H2O = Frac[:,5]
	#O   = Frac[:,6]
	#O2  = Frac[:,7]
	#OH  = Frac[:,8]

	plt.plot(Time,Frac[:,1])
	plt.plot(Time,Frac[:,2])
	plt.plot(Time,Frac[:,3])
	plt.plot(Time,Frac[:,4])
	plt.plot(Time,Frac[:,5],'--')
	plt.plot(Time,Frac[:,6],'--')
	plt.plot(Time,Frac[:,7],'--')
	plt.plot(Time,Frac[:,8],'--')
	plt.grid()
	##plt.title('MdotO:%s[kg/s]'%MdotO)
	plt.legend(( 'CO2 ',  'CO ',  'H ',  'H2 ',  'H2O ',  'O ',  'O2 ', 'OH' ))
	plt.xlabel('Time[s]')
	plt.ylabel('Mole Fraction')
	#plt.ylim([0,100])
	plt.savefig(dire+"Frac_Mdot%s.png"%float(MdotO))
	plt.close()
	#}}}

def Flight(dire):
	
	#Flight{{{
	Flight = sp.genfromtxt(dire+'Flight.d',delimiter=',')
	Time       = Flight[:, 0]
	CF         = Flight[:, 1]
	Thrust     = Flight[:, 2]
	TotallMass = Flight[:, 3]
	CD         = Flight[:, 4]
	Drag       = Flight[:, 5]
	AccelX     = Flight[:, 6]
	AccelY     = Flight[:, 7]
	VeloX      = Flight[:, 8]
	VeloY      = Flight[:, 9]
	Velo       = Flight[:,10]
	Distance   = Flight[:,11]
	Height     = Flight[:,12]
	Angle      = Flight[:,13]
	
	#print Time[:20]
	#print Pres[:20]
	
	plt.plot(Time,Thrust)
	plt.grid()
	##plt.title('MdotO:%s[kg/s]'%MdotO)
	#plt.legend(('LOx:%s[kg/s]'%float(MdotO),))
	plt.xlabel('Time[s]')
	plt.ylabel('Thrust[N]')
	#plt.ylim([0,100])
	plt.savefig(dire+"Thrust.png")
	plt.close()

	plt.plot(Time,Velo)
	plt.grid()
	##plt.title('MdotO:%s[kg/s]'%MdotO)
	#plt.legend(('LOx:%s[kg/s]'%float(MdotO),))
	plt.xlabel('Time[s]')
	plt.ylabel('Velocity[m/s]')
	#plt.ylim([0,100])
	plt.savefig(dire+"Velocity.png")
	plt.close()

	plt.plot(Distance,Height)
	plt.grid()
	##plt.title('MdotO:%s[kg/s]'%MdotO)
	#plt.legend(('LOx:%s[kg/s]'%float(MdotO),))
	plt.xlabel('Distance[m]')
	plt.ylabel('Height[m]')
	#plt.ylim([0,100])
	plt.savefig(dire+"Height.png")
	plt.close()
	
	#}}}
	



if __name__ == "__main__":

	Spec = open('Spec.d','r')
	MdotO = Spec.read()
	Spec.close()
	
	dire = 'Pre/'
	PreTime = PreVari(dire,MdotO)
	PreFrac(dire,MdotO,PreTime)
	print 'Pre'

	dire = 'Main/'
	MainTime = MainVari(dire,MdotO)
	MainFrac(dire,MdotO,MainTime)
	print 'Main'

	dire = 'Flight/'
	Flight(dire)
	print 'Flight'

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
