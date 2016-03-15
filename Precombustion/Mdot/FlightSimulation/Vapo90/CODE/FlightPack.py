#!/usr/bin/python
import subprocess as subcmd
import re
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import math
import sys
import csv
from string import *
Gravity = 9.80665

class Pack:
	def __init__(self):
		print ''
	def ThrustCoefficient(self,Gamma,ExitPressure,TotalPressure,AtmosPressure):#[-,MPaA,MPaA,MPaA],->,[-]
		Sigma_ast=(Gamma*(2.0/(Gamma+1.0))**((Gamma+1.0)/(Gamma-1.0)))**(1.0/2.0)
		CF1=Sigma_ast*(2.0*Gamma/(Gamma-1.0)*(1.0-(ExitPressure/TotalPressure)**((Gamma-1.0)/Gamma)))**(1.0/2.0)
		CF2=Sigma_ast*(ExitPressure/TotalPressure-AtmosPressure/TotalPressure)/((ExitPressure/TotalPressure)**(1.0/Gamma)*(2.0*Gamma/(Gamma-1.0)*(1.0-(ExitPressure/TotalPressure)**((Gamma-1.0)/Gamma)))**(1.0/2.0))
		#print Sigma_ast,CF1,CF2
		return CF1+CF2

	def Thrust(self,ThrustCoefficient,TotalPressure,NozzleThroat):
		Ft = ThrustCoefficient*TotalPressure*NozzleThroat
		return Ft

	def TotalMass(self,PreviousTotalMass,OxidMassFlowRate,FuelMassFlowRate,dt):
		Mt = (OxidMassFlowRate+FuelMassFlowRate)*dt
		return PreviousTotalMass - Mt

	def Accelaration(self,Thrust,Angle,TotalMass,Drag):
		ax = (Thrust*np.cos(Angle)-Drag*np.cos(Angle))/TotalMass
		ay = (Thrust*np.sin(Angle)-Drag*np.sin(Angle)-TotalMass*Gravity)/TotalMass
		return ax,ay

	def Velocity(self,XPreviousVelocity,YPreviousVelocity,XAccelaration,YAccelaration,dt):
		Vx = XPreviousVelocity+XAccelaration*dt
		Vy = YPreviousVelocity+YAccelaration*dt
		return Vx,Vy,(Vx**2+Vy**2)**(1/2)
	
	def HorizontalDistance(self,PreviousDistance,XVelocity,XAccelaration,dt):
		x = PreviousDistance+XVelocity*dt+1.0/2.0*XAccelaration*dt**2
		return x

	def Height(self,PreviousHeight,YVelocity,YAccelaration,dt):
		y = PreviousHeight+YVelocity*dt+1.0/2.0*YAccelaration*dt**2
		return y

	def Angle(self,XVelocity,YVelocity):
		Angle = np.arctan(YVelocity/XVelocity)
		return Angle

	def Drag(self,DragCoefficient,Density,Velocity,CrossSectionArea):
		Drag = 1.0/2.0*DragCoefficient*Density*Velocity**2*CrossSectionArea
		return Drag

	def DragCoefficient(self,Mach):
		data = sp.genfromtxt('CDragSpline.d',delimiter=',')		
		for i in range(0,520):
			if Mach < data[i,0]:
				break;
		return data[i-1,1]

	def AtmosphereCondition(self,Height):
		data = sp.genfromtxt('AC.d',delimiter=',')		
		PresGrand = 0.1013   #[MPa]
		for i in range(0,520):
			if Height < data[i,0]:
				break;
		return data[i-1,1],data[i-1,2]*PresGrand,data[i-1,3]

	#def AtmosphereCondition(self,Height):#[km],->,[MPaA]
	#	Hft = Height*10**(-3)*3.28084
	#	#English Unit
	#	if Hft<36152:
	#		T = 59-0.00356*Hft
	#		P = 2116*((T+459.7)/518.6)**(5.256)
	#	elif 36152<=Hft<82345:
	#		T = -70
	#		P = 473.1*exp(1.73-0.000048*Hft)
	#	elif 82345<=Hft:
	#		T = -205.05+0.0164*Hft
	#		P = 51.97*((T+459.7)/389.98)**(-11.388)
	#	P = P*144.0
	#	rho = P/(1718.0*(T+459.7))
	#	#SI Unit[K,MPa,kg/m3]
	#	T = 5.0/9.0*(T-32)+273.15
	#	#P = P/(4.7880258889*10.0**(-5))
	#	P = P/6894.75729
	#	rho = 0.0019403203319541*rho
	#	return T,P,rho

##############Tutorial############################################
#if __name__ == "__main__":
#	import FlightPack
#	FP = FlightPack.Pack()
#	Mach = 1.5
#	CD = FP.DragCoefficient(Mach)
#	Ta,Pa,rhoa = FP.AtmosphereCondition(0.0)#[km]->[K,MPa,kg/m3]
#	Pe = Pa
#	print Pe,Ta,rhoa
#	P0 = 500.0
#	ArrayCF = np.array([])
#	ArrayAr = np.array([])
	#for i in range(1,100):
	#	f = float(i)*0.1
	#	#Ta,Pa,rhoa = FP.AtmospherePressure(f)#[km]->[K,MPa,kg/m3]
	#	CF = FP.ThrustCoefficient(1.3,f*Pa,P0*Pa,Pa)
	#	print 1.3,f*Pa,P0*Pa,Pa
	#	ArrayCF = np.append(ArrayCF,CF)
	#	ArrayAr = np.append(ArrayAr,f)
	#plt.plot(ArrayAr,ArrayCF)
	#plt.xlabel('Pa/Pe')
	#plt.ylabel('CF')
	#plt.grid()
	#plt.show()
#
