#!/opt/local/bin/python
# Grant David Meadors
# 02015-11-26 (JD 2457353)
# g r a n t . m e a d o r s @ a e i . m p g . d e
# Script to read in the data from the event and test for ringdown

import numpy as np
import matplotlib.pyplot as plt
H1file = 'H1.txt'
L1file = 'L1.txt'

H1data = np.loadtxt(H1file)
L1data = np.loadtxt(L1file)
H1fft = np.fft.fft(H1data[:,1])
L1fft = np.fft.fft(L1data[:,1])
H1asd = np.absolute(H1fft)
L1asd = np.absolute(L1fft)
fig = plt.figure()
plt.plot(H1asd)
fig.savefig('H1asd.png')
plt.close()
print H1asd[0:9]
