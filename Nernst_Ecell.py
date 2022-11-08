#Nernst equation for determining full cell electric potential
import math
from math import log
#constants
Rydb = 8.314 #J/(K*mol) universal gas constant
Fara = 96485.33 #(C/mol) faraday constant
#variables
# TempK = float(input('temperature(K):')) #around 270
# E_s = float(input('standard cell potential:')) #need to be drop down for element reactions
# z = float(input('electron exchange number:')) #electron transfer *will be auto input from previous answer*
# Q = float(input('reaction quotient:')) #reaction quotient 0<x<1 *element dependent*
# E_cell = float()
#
def Potential(TempK, E_s, z, Q):
    E_cell = E_s - (Rydb*TempK)/(z*Fara)*(log(Q))

    return E_cell

# E1 = Potential(TempK, E_s, z, Q)
# print('The full-cell electric potential is:', E1,'volts')


