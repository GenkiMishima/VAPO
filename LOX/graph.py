#/usr/bin/python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
a = sp.genfromtxt("DATA/Oxygen50.d")

aX,aY,aZ = a[:,0]
