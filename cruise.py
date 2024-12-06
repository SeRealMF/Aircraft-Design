#this script shall calculate the power to weight ratio from the wingloding of an aircraft in cruise condition

import constants
import math
from isa import isa_model

#specific constants
TR_THR = 0.8 #power throttle ratio in cruise flight

#assumptions
k_c = 0.99 #fuel factor due to weight loss of fuel in climb
epsilion = 1/18 #glide ratio 1/(L/D) - middle of range for commercial aircraft turbofans due to worse aerodynamics of LHE aircaft compared to conventional
C_L = 0.5 #lift coefficient cruise

def calcInducedDrag():

    C_Di = 1/(math.pi * constants.AR * constants.e0) * math.pow(C_L, 2)

    return C_Di

def calcParasiticDrag():

    C_D0 = epsilion * C_L - 1/(math.pi * constants.AR * constants.e0) * math.pow(C_L, 2) 

    return C_D0

def calcDynamicPressure(h, dT):

    q = 1/2 * isa_model(h, dT)

    return q

def calcPowerToWeightCruiseBase(wingloading):

    q = calcDynamicPressure(constants.H_CRUISE, 23)

    ratioP_0ToW_TO = ((q * calcParasiticDrag())/wingloading + (1/(math.pi * constants.AR * constants.e0)) * pow(C_L, 2) * wingloading/q) * (k_c * constants.V_CRUISE)/(TR_THR * constants.ntrans * constants.nprop)

    return ratioP_0ToW_TO
