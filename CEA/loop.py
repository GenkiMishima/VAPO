#!/usr/bin/python

import subprocess
for i in xrange(100):
	a = 50.0+i
	for j in yrange(200):
		b = 0.6-(0.01*j)
		cmd = "echo ok"
		subprocess.call(cmd, shell=True)
