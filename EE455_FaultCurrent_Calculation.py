# EE 455 Fault Current Calculation
# Matrix methods problem data
import numpy as np

# Number of transmission lines, nline
nline = 7

# Number of buses, nbus
nbus = 6

# Line resistances, R
R = np.zeros(nline)

# Line reactances, X
X = [ 0.10, 0.05, 0.10, 0.14, 0.10, 0.05, 0.05 ]

# Line admittances, G and B
G = np.zeros(nline) # This creates the arrays in the proper size
B = np.zeros(nline)

for line in range(1, nline+1):
    zsquared = R[line] * R[line] + X[line] * X[line]
    G[line] = R[line] / zsquared
    B[line] = -X[line] / zsquared

# Line charging, BC (Half total charging, in p.u. VARs)
BC = np.zeros(nline)

# Transmission line buses:
# F - From end buses
# T - To end buses
F = [ 1, 1, 2, 3, 3, 4, 5 ]
T = [ 4, 2, 5, 4, 6, 5, 6 ]

# Load at each bus, per unit, 100MVA base
# Pload - Real load, p.u. Watts
# Qload - Reactive load, p.u. VAR

Pload = [ 0.0, 0.0, 0.0, 1.0, 0.5, 1.1 ]
Qload = [ 0.0, 0.0, 0.0, 0.4, 0.3, 0.4 ]

# Generator real power at each bus, p.u. Watts, Pgen
Pgen = [ 0.7, 0.9, 1.0, 0.0, 0.0, 0.0 ]

# Generator sequence reactances, per unit
# Xgenplus - Positive Sequence
# Xgenminus - Negative Sequence
# Xgenzero - Zero Sequence (does NOT include the effects of ground connections)
# Groundgen - 1 if generator is grounded Y, else 0
Xgenplus = [ 0.02, 0.02, 0.02, 0.0, 0.0, 0.0 ]
Xgenminus = [ 0.02, 0.02, 0.01, 0.0, 0.0, 0.0 ]
Xgenzero = [ 0.005, 0.005, 0.005, 0.0, 0.0, 0.0 ]
Groundgen = [ 0, 1, 1, 0, 0, 0 ]

# Prefault voltages (p.u. Volts)
# Vprefault - Magnitude
# Thetapfd - Angle, degrees
# Thetapf - Angle, radians
Vprefault = [ 1.050, 1.050, 1.050, 1.021, 1.017, 1.015 ]
Thetapfd = [ 0.0, 0.164, -1.645, -4.083, -4.328, -5.278 ]
Thetapf = Thetapfd * np.pi / 180.0