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

def ThrustCoefficient(Gamma,ExitPressure,TotalPressure,AtmosPressure):#[-,MPaA,MPaA,MPaA],->,[-]
	Sigma_ast=(Gamma*(2.0/(Gamma+1.0))**((Gamma+1.0)/(Gamma-1.0)))**(1.0/2.0)
	CF1=Sigma_ast*(2.0*Gamma/(Gamma-1.0)*(1.0-(ExitPressure/TotalPressure)**((Gamma-1.0)/Gamma)))**(1.0/2.0)
	CF2=Sigma_ast*(ExitPressure/TotalPressure-AtmosPressure/TotalPressure)/((ExitPressure/TotalPressure)**(1.0/Gamma)*(2.0*Gamma/(Gamma-1.0)*(1.0-(ExitPressure/TotalPressure)**((Gamma-1.0)/Gamma)))**(1.0/2.0))
	#print Sigma_ast,CF1,CF2
	return CF1+CF2
def AtmospherePressure(Height):#[km],->,[MPaA]
	Hft = Height*10**(-3)*3.28084
	#America Unit
	if Hft<36152:
		T = 59-0.00356*Hft
		P = 2116*((T+459.7)/518.6)**(5.256)
	elif 36152<=Hft<82345:
		T = -70
		P = 473.1*exp(1.73-0.000048*Hft)
	elif 82345<=Hft:
		T = -205.05+0.0164*Hft
		P = 51.97*((T+459.7)/389.98)**(-11.388)
	rho = P/(1718*(T+459.7))
	#SI Unit
	T = 5.0/9.0*(T-32)+273.15
	P = 

if __name__ == "__main__":
	Pe = AtmospherePressure(0.0)*10**(-4)#[MPa]
	for i in range(0,100):
		f = float(i)
		Pa = AtmospherePressure(f)*10**(-4)#[MPa]
		CF = ThrustCoefficient(1.3,Pe,500.0*Pe,Pa)
		print f,Pa,CF
