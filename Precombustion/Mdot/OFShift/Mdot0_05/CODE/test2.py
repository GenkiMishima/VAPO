#!/usr/bin/python
import subprocess as subcmd
import re
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import math
import sys
from string import *
#Length:m
#Mass:kg
#Time:s
if __name__ == "__main__":
	Preinfile  = '../CALC/CEAdata/Pre/'
	Maininfile = '../CALC/CEAdata/Main/'
	filename = Preinfile+'ReadFile.d'
	f = open(filename,'r')
	print filename
	#data = f.read()
	#print data
	
	for line in f:
		itemList = itemList.append[line]

	print itemList

	#Predata = sp.genfromtxt(filename,delimiter='\t')
	#print Predata
	sys.exit()
