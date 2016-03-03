#!/usr/bin/python
import scipy as sp
import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt
data = sp.genfromtxt('../Result/5.csv', delimiter=",")

time_step = 1.0/200.0
time = data[:,0]
sig1 = data[:,1]#GHe
sig2 = data[:,2]#Ori
sig3 = data[:,3]#Inj
sig4 = data[:,4]#Pre
sig5 = data[:,5]#Mix
sig6 = data[:,6]#Flx
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
pxx, freq, bins, t = plt.specgram(sig4,NFFT = N,Fs = 400,noverlap=100,window=kaiserWindow)
plt.subplot(3,1,2)
plt.title('Mixing Pressure')
plt.ylabel('Frequency[Hz]')
plt.tick_params(labelbottom='off')
pxx, freq, bins, t = plt.specgram(sig5,NFFT = N,Fs = 400,noverlap=100,window=kaiserWindow)
plt.subplot(3,1,3)
plt.title('Mass Flux')
plt.ylabel('Frequency[Hz]')
plt.tick_params(labelbottom='off')
pxx, freq, bins, t = plt.specgram(sig6,NFFT = N,Fs = 400,noverlap=100,window=kaiserWindow)
#plt.figure()
#plt.plot(freqs, power)
#plt.xlabel('Frequency [Hz]')
#plt.ylabel('plower')
#axes = plt.axes([0.3, 0.3, 0.5, 0.5])
#plt.title('Peak frequency')
#plt.plot(freqs[:8], power[:8])
#plt.setp(axes, yticks=[])
plt.savefig('output/kaiser.png')
plt.show()
#
