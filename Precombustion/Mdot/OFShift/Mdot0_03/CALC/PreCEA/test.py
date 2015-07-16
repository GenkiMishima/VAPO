#!/usr/bin/python
import subprocess as subcmd
import re
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from string import *

if __name__ == "__main__":
	P = 0.5*(10.0)**(6)
	r = 1.2
	ga = 1.4
	u = (2.0*ga/(ga+1.0)*P/r)
	print u
