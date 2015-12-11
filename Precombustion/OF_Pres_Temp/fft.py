#!/usr/bin/python
import scipy as sp
import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt
data = sp.genfromtxt('20150313010035.CSV', delimiter=",")

time_step = 1.0/200.0
time = data[:,0]
sig = data[:,1]/1.012+0.1
#print sig.size, time_step
sample_freq = fftpack.fftfreq(sig.size, d=time_step)
sig_fft = fftpack.fft(sig)
pidxs = np.where(sample_freq > 0)
freqs, power = sample_freq[pidxs], np.abs(sig_fft)[pidxs]
freq = freqs[power.argmax()]

pxx, freq, bins, t=plt.specgram(sig,Fs=2)
#plt.figure()
#plt.plot(freqs, power)
#plt.xlabel('Frequency [Hz]')
#plt.ylabel('plower')
#axes = plt.axes([0.3, 0.3, 0.5, 0.5])
#plt.title('Peak frequency')
#plt.plot(freqs[:8], power[:8])
#plt.setp(axes, yticks=[])
plt.show()
#
