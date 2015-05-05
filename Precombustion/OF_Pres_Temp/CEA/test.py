#!/usr/bin/python
import re
from string import *

infile = 'file.out'
outfile = 'ana.d'

indat = open(infile, 'r')
inline = indat.readline()
data_dic = {}
No = 0
print ("Start reading data.")
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
	elif re.match(' G, KJ/KG', inline):
		Gibbs = strip(re.split(' ',inline)[10])
		data_list = [Pres,of,Temp,rho,Gibbs]
		data_dic[No] = data_list
#	elif re.match('', inline):
#		Temp = strip(re.split(' ',inline)[16])
#		print (Temp)
	inline = indat.readline()

print ("End reading data.")
print ("Start writing data.")
indat.close()
outdat = open(outfile, 'w')
outdat.write('No ,Pres ,O/F ,Temp ,rho ,Gibbs\n')
for d in data_dic.keys():
	unpacked = data_dic[d]
	data_str = ",".join([elem for elem in unpacked])
	outdat.write(str(d) + "," + data_str + "\n")

outdat.close()
