#!/usr/bin/python
import subprocess as subcmd
for i in range(0,100):
	of = 50.0+float(i)*0.1
	for j in range(0,10):
		p = 5.0+float(j)
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
