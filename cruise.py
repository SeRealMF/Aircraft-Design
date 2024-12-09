#this script shall calculate the power to weight ratio from the wingloading of an aircraft in cruise condition

import constants
import math
from isa import isa_model

#specific constants
TR_THR = 0.8 #power throttle ratio in cruise flight
TR_THR_OEI = 0.95 #power throttle ratio in cruise flight with one engine inop

#assumptions
k_c = 0.99 #fuel factor due to weight loss of fuel in climb
C_L = 0.5 #lift coefficient cruise
epsilion_OEI = 1.1 * constants.epsilion #glide ratio in OEI case
dT = 0 
fac_k_OEI = 1.3

def calcInducedDrag():

    C_Di = 1/(math.pi * constants.AR * constants.e0) * math.pow(C_L, 2)

    return C_Di

def calcParasiticDrag():

    C_D0 = constants.epsilion * C_L - (1/(math.pi * constants.AR * constants.e0) * math.pow(C_L, 2)) 

    return C_D0

def calcParasiticDragOEI():

    C_D0 = epsilion_OEI * C_L - (1/(math.pi * constants.AR * constants.e0) * math.pow(C_L, 2)) 

    return C_D0

def calcDynamicPressure(h: float | int, dT: float | int):

    q = 1/2 * isa_model(h, dT)[2] * math.pow(constants.V_CRUISE, 2)

    return q

def calcPowerToWeightCruiseBase(wingloading: float | int):

    q = calcDynamicPressure(constants.H_CRUISE, dT)

    ratioP_0ToW_TO = ((q * calcParasiticDrag())/wingloading + (1/(math.pi * constants.AR * constants.e0)) * pow(C_L, 2) * wingloading/q) * (k_c * constants.V_CRUISE)/(TR_THR * constants.ntrans * constants.nprop)

    return ratioP_0ToW_TO

def calcPowerToWeightCruiseBaseOEI(wingloading: float | int):

    v_OEI = calcCruiseVelocityOEI()
    q = calcDynamicPressure(constants.H_CRUISE, dT)
    C_D0 = calcParasiticDragOEI()
    k_OEI = (1/(math.pi * constants.AR * constants.e0)) * fac_k_OEI

    ratioP_0ToW_TO = (((q * C_D0)/wingloading) + k_OEI * wingloading/q) * ((k_c * v_OEI)/(TR_THR_OEI * constants.ntrans * constants.nprop)) * (constants.N_E / (constants.N_E - 1))

    return ratioP_0ToW_TO

def calcCruiseVelocityOEI():

    q = calcDynamicPressure(constants.H_CRUISE, dT)
    rho = isa_model(constants.H_CRUISE, dT)[2]

    v_OEI = math.sqrt(2 * q/rho)

    return v_OEI