#!/usr/bin/python 
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

#Pre
InputDirectry  = 'DATA/'
OutputDirectry = 'PLOT/'

Prefix   = 'Pre'
Element  = 'Pres'
#set{{{
data = sp.genfromtxt(InputDirectry+Prefix+Element+'.d',delimiter=',')
xval = data[:,0]
yval = data[:,1]
plt.plot(xval,yval)
plt.grid()
plt.title('MdotO:0.327[kg/s]')
#plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
plt.xlabel('Time[s]')
plt.ylabel(Element)
plt.ylim([0.5,0.8])
plt.savefig(OutputDirectry+Prefix+Element+".png")
plt.close()
#}}}
Element  = 'Pres'
#set{{{
data = sp.genfromtxt(InputDirectry+Prefix+Element+'.d',delimiter=',')
xval = data[:,0]
yval = data[:,1]
plt.plot(xval,yval)
plt.grid()
plt.title('MdotO:0.327[kg/s]')
#plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
plt.xlabel('Time[s]')
plt.ylabel(Element)
plt.ylim([0.5,1.1])
plt.savefig(OutputDirectry+Prefix+Element+".png")
plt.close()
#}}}
Element  = 'Temp'
#set{{{
data = sp.genfromtxt(InputDirectry+Prefix+Element+'.d',delimiter=',')
xval = data[:,0]
yval = data[:,1]
plt.plot(xval,yval)
plt.grid()
plt.title('MdotO:0.327[kg/s]')
#plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
plt.xlabel('Time[s]')
plt.ylabel(Element)
#plt.ylim([0,100])
plt.savefig(OutputDirectry+Prefix+Element+".png")
plt.close()
#}}}
Element  = 'Isp'
#set{{{
data = sp.genfromtxt(InputDirectry+Prefix+Element+'.d',delimiter=',')
xval = data[:,0]
yval = data[:,1]
plt.plot(xval,yval)
plt.grid()
plt.title('MdotO:0.327[kg/s]')
#plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
plt.xlabel('Time[s]')
plt.ylabel(Element)
#plt.ylim([0,100])
plt.savefig(OutputDirectry+Prefix+Element+".png")
plt.close()
#}}}
Element  = 'MdotF'
#set{{{
data = sp.genfromtxt(InputDirectry+Prefix+Element+'.d',delimiter=',')
xval = data[:,0]
yval = data[:,1]
plt.plot(xval,yval)
plt.grid()
plt.title('MdotO:0.327[kg/s]')
#plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
plt.xlabel('Time[s]')
plt.ylabel(Element)
#plt.ylim([0,100])
plt.savefig(OutputDirectry+Prefix+Element+".png")
plt.close()
#}}}
Element  = 'Thrust'
#set{{{
data = sp.genfromtxt(InputDirectry+Prefix+Element+'.d',delimiter=',')
xval = data[:,0]
yval = data[:,1]
plt.plot(xval,yval)
plt.grid()
plt.title('MdotO:0.327[kg/s]')
#plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
plt.xlabel('Time[s]')
plt.ylabel(Element)
#plt.ylim([0,100])
plt.savefig(OutputDirectry+Prefix+Element+".png")
plt.close()
#}}}

Prefix   = 'Main'
Element  = 'Pres'
#set{{{
data = sp.genfromtxt(InputDirectry+Prefix+Element+'.d',delimiter=',')
xval = data[:,0]
yval = data[:,1]
plt.plot(xval,yval)
plt.grid()
plt.title('MdotO:0.327[kg/s]')
#plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
plt.xlabel('Time[s]')
plt.ylabel(Element)
plt.ylim([0.5,1.1])
plt.savefig(OutputDirectry+Prefix+Element+".png")
plt.close()
#}}}
Element  = 'Temp'
#set{{{
data = sp.genfromtxt(InputDirectry+Prefix+Element+'.d',delimiter=',')
xval = data[:,0]
yval = data[:,1]
plt.plot(xval,yval)
plt.grid()
plt.title('MdotO:0.327[kg/s]')
#plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
plt.xlabel('Time[s]')
plt.ylabel(Element)
#plt.ylim([0,100])
plt.savefig(OutputDirectry+Prefix+Element+".png")
plt.close()
#}}}
Element  = 'Isp'
#set{{{
data = sp.genfromtxt(InputDirectry+Prefix+Element+'.d',delimiter=',')
xval = data[:,0]
yval = data[:,1]
plt.plot(xval,yval)
plt.grid()
plt.title('MdotO:0.327[kg/s]')
#plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
plt.xlabel('Time[s]')
plt.ylabel(Element)
#plt.ylim([0,100])
plt.savefig(OutputDirectry+Prefix+Element+".png")
plt.close()
#}}}
Element  = 'MdotF'
#set{{{
data = sp.genfromtxt(InputDirectry+Prefix+Element+'.d',delimiter=',')
xval = data[:,0]
yval = data[:,1]
plt.plot(xval,yval)
plt.grid()
plt.title('MdotO:0.327[kg/s]')
#plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
plt.xlabel('Time[s]')
plt.ylabel(Element)
#plt.ylim([0,100])
plt.savefig(OutputDirectry+Prefix+Element+".png")
plt.close()
#}}}
Element  = 'Thrust'
#set{{{
data = sp.genfromtxt(InputDirectry+Prefix+Element+'.d',delimiter=',')
xval = data[:,0]
yval = data[:,1]
plt.plot(xval,yval)
plt.grid()
plt.title('MdotO:0.327[kg/s]')
#plt.legend(('MdotO:%s[kg/s]'%float(MdotO),))
plt.xlabel('Time[s]')
plt.ylabel(Element)
#plt.ylim([0,100])
plt.savefig(OutputDirectry+Prefix+Element+".png")
plt.close()
#}}}
