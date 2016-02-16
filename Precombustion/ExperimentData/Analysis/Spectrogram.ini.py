#!/usr/bin/python
import scipy as sp
import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt
data = sp.genfromtxt('../Result/21.csv', delimiter="\t")
#SpectroGram{{{
time_step = 1.0/200.0
time  = data[:, 0]#Time
sig1  = data[:, 1]#GHePres
sig2  = data[:, 2]#InjPres
sig3  = data[:, 3]#ComPres
sig4  = data[:, 4]#MixPres
sig5  = data[:, 5]#OriTemp
sig6  = data[:, 6]#InjTemp
sig7  = data[:, 7]#NUWTemp
sig8  = data[:, 8]#NUCTemp
sig9  = data[:, 9]#NDCTemp
sig10 = data[:,10]#FrnTemp
sig11 = data[:,11]#TbnFlow
sig12 = data[:,12]#OriBoil
sig13 = data[:,13]#OriFlow
sig14 = data[:,14]#InjBoil
sig15 = data[:,15]#InjFlow
sig16 = data[:,16]#MixBoil
N = 256
hammingWindow = np.hamming(N)
hanningWindow = np.hanning(N)
kaiserWindow = np.kaiser(N,5)

#print sig.size, time_step
#sample_freq = fftpack.fftfreq(sig.size, d=time_step)
#sig_fft = fftpack.fft(sig)
#pidxs = np.where(sample_freq > 0)
#freqs, power = sample_freq[pidxs], np.abs(sig_fft)[pidxs]
#freq = freqs[power.argmax()]
#plt.subplot(6,1,1)
#pxx, freq, bins, t = plt.specgram(sig1,NFFT = N,Fs = 400,noverlap=20,window=kaiserWindow)
#plt.subplot(6,1,2)
#pxx, freq, bins, t = plt.specgram(sig2,NFFT = N,Fs = 400,noverlap=20,window=kaiserWindow)
#plt.subplot(6,1,3)
#pxx, freq, bins, t = plt.specgram(sig3,NFFT = N,Fs = 400,noverlap=20,window=kaiserWindow)
plt.subplot(3,1,1)
plt.title('Preburner Pressure')
plt.ylabel('Frequency[Hz]')
plt.tick_params(labelbottom='off')
pxx, freq, bins, t = plt.specgram(sig1 ,NFFT = N,Fs = 400,noverlap=100,window=kaiserWindow)
plt.subplot(3,1,2)
plt.title('Mixing Pressure')
plt.ylabel('Frequency[Hz]')
plt.tick_params(labelbottom='off')
pxx, freq, bins, t = plt.specgram(sig3 ,NFFT = N,Fs = 400,noverlap=100,window=kaiserWindow)
plt.subplot(3,1,3)
plt.title('Mass Flux')
plt.ylabel('Frequency[Hz]')
plt.tick_params(labelbottom='off')
pxx, freq, bins, t = plt.specgram(sig10,NFFT = N,Fs = 400,noverlap=100,window=kaiserWindow)
#plt.figure()
#plt.plot(freqs, power)
#plt.xlabel('Frequency [Hz]')
#plt.ylabel('plower')
#axes = plt.axes([0.3, 0.3, 0.5, 0.5])
#plt.title('Peak frequency')
#plt.plot(freqs[:8], power[:8])
#plt.setp(axes, yticks=[])
#}}}
plt.savefig('SpecGramKaiser21.png')
#plt.show()
#
