#!/usr/bin/python
import scipy as sp
import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt
Array = []
#DATA{{{
Array.append(sp.genfromtxt('../Result/21.csv', delimiter="\t"))
Array.append(sp.genfromtxt('../Result/22.csv', delimiter="\t"))
Array.append(sp.genfromtxt('../Result/23.csv', delimiter="\t"))
Array.append(sp.genfromtxt('../Result/24.csv', delimiter="\t"))
Array.append(sp.genfromtxt('../Result/25.csv', delimiter="\t"))
Array.append(sp.genfromtxt('../Result/26.csv', delimiter="\t"))
Array.append(sp.genfromtxt('../Result/27.csv', delimiter="\t"))
Array.append(sp.genfromtxt('../Result/28.csv', delimiter="\t"))
Array.append(sp.genfromtxt('../Result/29.csv', delimiter="\t"))
Array.append(sp.genfromtxt('../Result/20.csv', delimiter="\t"))
NameIndex = [
'1-GHePres',
'2-InjPres',
'3-ComPres',
'4-MixPres',
'5-OriTemp',
'6-InjTemp',
'7-NUWTemp',
'8-NUCTemp',
'9-NDCTemp',
'10-FrnTemp',
'11-TbnFlow',
'12-OriBoil',
'13-OriFlow',
'14-InjBoil',
'15-InjFlow',
'16-MixBoil']
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

def plot_Pressure(fig_size=None):
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
		PlData1 = Array[i-1][:,1]
		PlData2 = Array[i-1][:,2]
		PlData3 = Array[i-1][:,3]
		PlData4 = Array[i-1][:,4]
		ax = fig.add_subplot(5,2,i)
		plt.plot(Time,PlData1,label=' 1-GHePres')
		plt.plot(Time,PlData2,label=' 2-InjPres')
		plt.plot(Time,PlData3,label=' 3-ComPres')
		plt.plot(Time,PlData4,label=' 4-MixPres')
		plt.legend(fontsize=15,loc = 'upper right')
		plt.xlabel('Time[s]')
		plt.ylabel('Pressure[MPaA]')
		plt.xlim(0,10)
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

def plot_only(FN,fig_size=None):
	#{{{
	#N = 256
	#hammingWindow = np.hamming(N)
	#hanningWindow = np.hanning(N)
	#kaiserWindow = np.kaiser(N,5)
	fig = plt.figure()
	if fig_size != None:
		fig.set_size_inches(fig_size[0], fig_size[1])
	Time    = Array[FN][:,0 ]
	PlData1 = Array[FN][:,1 ]
	PlData2 = Array[FN][:,2 ]
	PlData3 = Array[FN][:,3 ]
	PlData4 = Array[FN][:,4 ]
	PlData5 = Array[FN][:,5 ]
	PlData6 = Array[FN][:,6 ]
	PlData7 = Array[FN][:,7 ]
	PlData8 = Array[FN][:,8 ]
	PlData9 = Array[FN][:,9 ]
	PlData10= Array[FN][:,10]
	PlData11= Array[FN][:,11]
	PlData12= Array[FN][:,12]
	PlData13= Array[FN][:,13]
	PlData14= Array[FN][:,14]
	PlData15= Array[FN][:,15]
	PlData16= Array[FN][:,16]

	ax = fig.add_subplot(3,1,1)
	plt.plot(Time,PlData1,label=' 1-GHePres')
	plt.plot(Time,PlData2,label=' 2-InjPres')
	plt.plot(Time,PlData3,label=' 3-ComPres')
	plt.plot(Time,PlData4,label=' 4-MixPres')
	plt.legend(fontsize=15,loc = 'upper right')
	plt.xlabel('Time[s]')
	plt.ylabel('Pressure[MPaA]')
	plt.xlim(0,10)
	ax = fig.add_subplot(3,1,2)
	plt.plot(Time,PlData8 ,label=' 8-NUCTemp')
	plt.plot(Time,PlData9 ,label=' 9-NDCTemp')
	plt.plot(Time,PlData10,label='10-FrnTemp')
	plt.plot(Time,PlData16,label='16-MixBoil')
	plt.legend(fontsize=15,loc = 'upper right')
	plt.xlabel('Time[s]')
	plt.ylabel('Temperature[K]')
	plt.xlim(0,10)
	ax = fig.add_subplot(3,1,3)
	plt.plot(Time,PlData11,label='11-TbnFlow')
	plt.plot(Time,PlData13,label='13-OriFlow')
	plt.plot(Time,PlData15,label='15-InjFlow')
	plt.legend(fontsize=15,loc = 'upper right')
	plt.xlabel('Time[s]')
	plt.ylabel('MassFlowRate[kg/s]')
	plt.xlim(0,10)
	#}}}

if __name__ == '__main__':
	##Main###################
	##Spectrogram
	for j in range(1,17):
		plot_specgram(j,x_label='time[s]', y_label='frequency[Hz]',fig_size=(21,29))
		plt.savefig('SpecGram/'+NameIndex[j-1]+'.eps')
		plt.close()
	##History
	##Pressure
	plot_Pressure(fig_size=(21,29))
	plt.savefig('History/Pressure.eps')
	##Temperature
	plot_Temperature(fig_size=(21,29))
	plt.savefig('History/Temperature.eps')
	##MassFlow
	plot_MassFlow(fig_size=(21,29))
	plt.savefig('History/MassFlow.eps')
	##Only
	for FN in range(0,9):
		plot_only(FN,fig_size=(21,29))
		plt.savefig('History/Ex'+str(2)+str(FN)+'.eps')

	##CHECK##################
	#plot_specgram_check(3,1,title='Num21', x_label='time(in seconds)', y_label='frequency',fig_size=(21,29))
	#plt.show()
