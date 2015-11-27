#!/opt/local/bin/python
# Grant David Meadors
# 02015-11-26 (JD 2457353)
# g r a n t . m e a d o r s @ a e i . m p g . d e
# Script to read in the data from the event and test for ringdown

import numpy as np
import matplotlib.pyplot as plt

# Sampling frequency and observation time
Fsample = 16384.0
Tobs = 2.0

H1file = 'H1.txt'
L1file = 'L1.txt'
# Load in the data
H1data = np.loadtxt(H1file)
L1data = np.loadtxt(L1file)
# Define a function to zero out non-event portions
def zeroData(dataArray, gpsStart, gpsStop):
    dataZeroed = dataArray
    dataZeroed[ (dataArray[:,0] < gpsStart),:] = 0
    dataZeroed[ (dataArray[:,0] > gpsStop),:] = 0
    return dataZeroed
# If needed, we can add or remove sections of zero-padding,
# but consider that later

# Approximation of actual times of the event
gpsStartEvent = 1126259462.39
gpsStopEvent = 1126259462.43
# For testing purposes
#gpsStartEvent = 0
#gpsStopEvent = 1e12
H1dataZeroed = zeroData(H1data, gpsStartEvent, gpsStopEvent)
L1dataZeroed = zeroData(L1data, gpsStartEvent, gpsStopEvent)

# Frequency bins of the FFT
fftBins = np.linspace(0, Fsample, Fsample*Tobs)

# FFT the data
H1fft = np.fft.fft(H1dataZeroed[:,1])
L1fft = np.fft.fft(L1dataZeroed[:,1])
H1asd = np.absolute(H1fft)
L1asd = np.absolute(L1fft)

# Plot the data
def plotASD(xBins, asdData, fileName):
    fig = plt.figure()
    plt.plot(fftBins,H1asd)
    plt.axis([100,300,0,2e-17])
    fig.savefig(fileName)
    plt.close()

plotASD(fftBins, H1asd, 'H1asd.png')
plotASD(fftBins, L1asd, 'L1asd.png')
