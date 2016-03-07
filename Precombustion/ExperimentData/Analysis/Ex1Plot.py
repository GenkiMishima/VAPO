#!/usr/bin/python
import scipy as sp
import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt
Array = []
#DATA{{{
Array.append(sp.genfromtxt('../Result/11.csv', delimiter="\t"))
#Array.append(sp.genfromtxt('../Result/12.csv', delimiter="\t"))
#Array.append(sp.genfromtxt('../Result/13.csv', delimiter="\t"))
#Array.append(sp.genfromtxt('../Result/14.csv', delimiter="\t"))
Array.append(sp.genfromtxt('../Result/15.csv', delimiter="\t"))
NameIndex = [
'1-OriPres',
'2-InjPres',
'3-ComPres',
'4-MixPres',
'5-GHePres',
'6-InjTemp',
'7-NUWTemp',
'8-NUCTemp',
'9-NDCTemp',
'10-FrnTemp',
'11-Temp',
'12-Dens',
'13-TbnFlow',
'14-OriFlow',
'15-MixBoil']
#}}}
def plot_specgram_check(plot,number,title='', x_label='', y_label='', fig_size=None):
	#{{{
	PlData = Array[5][:,plot]
	N = 256
	hammingWindow = np.hamming(N)
	hanningWindow = np.hanning(N)
	kaiserWindow = np.kaiser(N,5)
	fig = plt.figure()
	if fig_size != None:
		fig.set_size_inches(fig_size[0], fig_size[1])
	pxx, freq, t, cax = plt.specgram(PlData, Fs=200,window=kaiserWindow)
	fig.colorbar(cax).set_label('Intensity [dB]')
	#}}}

def plot_specgram(PlotIndex,x_label='', y_label='', fig_size=None):
	#{{{
	N = 256
	hammingWindow = np.hamming(N)
	hanningWindow = np.hanning(N)
	kaiserWindow = np.kaiser(N,5)
	fig = plt.figure()
	if fig_size != None:
		fig.set_size_inches(fig_size[0], fig_size[1])
	for i in range(0,10):
		PlData = Array[i-1][:,PlotIndex]
		ax = fig.add_subplot(5,2,i)
		#ax.set_title(NameIndex[PlotIndex-1])
		ax.set_xlabel(x_label)
		ax.set_ylabel(y_label)
		pxx, freq, t, cax = plt.specgram(PlData, Fs=200,window=kaiserWindow)
		fig.colorbar(cax).set_label('Intensity [dB]')
	#}}}

def plot1(fig_size=None):
	#{{{
	N = 256
	hammingWindow = np.hamming(N)
	hanningWindow = np.hanning(N)
	kaiserWindow = np.kaiser(N,5)
	fig = plt.figure()
	if fig_size != None:
		fig.set_size_inches(fig_size[0], fig_size[1])
	Time     = Array[1][:,0]
	PlData1  = Array[1][:,1]
	PlData2  = Array[1][:,2]
	PlData3  = Array[1][:,3]
	PlData4  = Array[1][:,4]
	PlData5  = Array[1][:,5]
	PlData6  = Array[1][:,6]
	PlData7  = Array[1][:,7]
	PlData8  = Array[1][:,8]
	PlData9  = Array[1][:,9]
	PlData10 = Array[1][:,10]
	PlData11 = Array[1][:,11]
	PlData12 = Array[1][:,12]
	PlData13 = Array[1][:,13]
	PlData14 = Array[1][:,14]
	PlData15 = Array[1][:,15]
	ax = fig.add_subplot(3,1,1)
	plt.plot(Time,PlData1,label='1-OriPres')
	plt.plot(Time,PlData2,label='2-InjPres')
	plt.plot(Time,PlData3,label='3-ComPres')
	plt.plot(Time,PlData4,label='4-MixPres')
	plt.plot(Time,PlData5,label='5-GHePres')
	plt.legend(fontsize=15,loc = 'upper right')
	plt.xlabel('Time[s]')
	plt.ylabel('Pressure[MPaA]')
	plt.xlim(0,5)
	ax = fig.add_subplot(3,1,2)
	plt.plot(Time,PlData6,label='6-InjTemp')
	plt.plot(Time,PlData15,label='15-MixBoil')
	plt.legend(fontsize=15,loc = 'upper right')
	plt.xlabel('Time[s]')
	plt.ylabel('Temperature[K]')
	plt.xlim(0,5)
	ax = fig.add_subplot(3,1,3)
	plt.plot(Time,PlData13,label='13-TbnFlow')
	plt.plot(Time,PlData14,label='14-OriFlow')
	plt.legend(fontsize=15,loc = 'upper right')
	plt.xlabel('Time[s]')
	plt.ylabel('MassFlowRate[kg/s]')
	plt.xlim(0,5)
	plt.ylim(0,0.05)
	#}}}

def plot_Temperature(fig_size=None):
	#{{{
	N = 256
	hammingWindow = np.hamming(N)
	hanningWindow = np.hanning(N)
	kaiserWindow = np.kaiser(N,5)
	fig = plt.figure()
	if fig_size != None:
		fig.set_size_inches(fig_size[0], fig_size[1])
	for i in range(0,10):
		Time = Array[i-1][:,0]
		PlData1 = Array[i-1][:, 5]
		PlData2 = Array[i-1][:, 6]
		PlData3 = Array[i-1][:, 7]
		PlData4 = Array[i-1][:, 8]
		PlData5 = Array[i-1][:, 9]
		PlData6 = Array[i-1][:,10]
		PlData7 = Array[i-1][:,16]
		ax = fig.add_subplot(5,2,i)
		#plt.legend((NameIndex[5],NameIndex[6],NameIndex[7],NameIndex[8],NameIndex[9],NameIndex[10]),'upper left')
		#plt.plot(Time,PlData1,label=' 5-OriTemp')
		#plt.plot(Time,PlData2,label=' 6-InjTemp')
		#plt.plot(Time,PlData3,label=' 7-NUWTemp')
		plt.plot(Time,PlData4,label=' 8-NUCTemp')
		plt.plot(Time,PlData5,label=' 9-NDCTemp')
		plt.plot(Time,PlData6,label='10-FrnTemp')
		plt.plot(Time,PlData7,label='16-MixBoil')
		plt.legend(fontsize=15,loc = 'upper right')
		plt.xlabel('Time[s]')
		plt.ylabel('Temperature[K]')
		plt.xlim(0,10)
		plt.ylim(-200,1400)
	#}}}

def plot_MassFlow(fig_size=None):
	#{{{
	N = 256
	hammingWindow = np.hamming(N)
	hanningWindow = np.hanning(N)
	kaiserWindow = np.kaiser(N,5)
	fig = plt.figure()
	if fig_size != None:
		fig.set_size_inches(fig_size[0], fig_size[1])
	for i in range(0,10):
		Time = Array[i-1][:,0]
		PlData1 = Array[i-1][:, 11]
		PlData2 = Array[i-1][:, 13]
		PlData3 = Array[i-1][:, 15]
		ax = fig.add_subplot(5,2,i)
		#plt.legend((NameIndex[5],NameIndex[6],NameIndex[7],NameIndex[8],NameIndex[9],NameIndex[10]),'upper left')
		plt.plot(Time,PlData1,label='11-TbnFlow')
		plt.plot(Time,PlData2,label='13-OriFlow')
		plt.plot(Time,PlData3,label='15-InjFlow')
		plt.legend(fontsize=15,loc = 'upper right')
		plt.xlabel('Time[s]')
		plt.ylabel('MassFlowRate[kg/s]')
		plt.xlim(0,10)
	#}}}

if __name__ == '__main__':
	##Main###################
	##Spectrogram
	#for j in range(1,17):
	#	plot_specgram(j,x_label='time[s]', y_label='frequency[Hz]',fig_size=(21,29))
	#	plt.savefig('SpecGram/'+NameIndex[j-1]+'.eps')
	#	plt.close()
	##History
	##Pressure
	plot1(fig_size=(21,29))
	plt.savefig('History/Data2.eps')
	##Temperature
	#plot_Temperature(fig_size=(21,29))
	#plt.savefig('History/Temperature1.eps')
	##MassFlow
	#plot_MassFlow(fig_size=(21,29))
	#plt.savefig('History/MassFlow1.eps')

	##CHECK##################
	#plot_specgram_check(3,1,title='Num21', x_label='time(in seconds)', y_label='frequency',fig_size=(21,29))
	
	#plt.show()
