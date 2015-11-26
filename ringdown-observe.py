#!/opt/local/bin/python
# Grant David Meadors
# 02015-11-26 (JD 2457353)
# g r a n t . m e a d o r s @ a e i . m p g . d e
# Script to read in the data from the event and test for ringdown

import numpy as np
H1file = 'H1.txt'
L1file = 'L1.txt'

H1data = np.loadtxt(H1file)
print H1data[0:9,1]
