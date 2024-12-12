#this script shall calculate the power to weight ratio from the wingloading of an aircraft in cruise condition

import constants
import math
from isa import isa_model
import generalCalc

#specific constants
TR_THR = 0.8 #power throttle ratio in cruise flight
TR_THR_OEI = 0.95 #power throttle ratio in cruise flight with one engine inop

#assumptions
k_c = 0.99 #fuel factor due to weight loss of fuel in climb
epsilion_OEI = 1.1 * constants.epsilion #glide ratio in OEI case
dT = 0 
fac_k_OEI = 1.3

def calcInducedDrag():

    C_Di = 1/(math.pi * constants.AR * constants.e0) * math.pow(constants.C_L, 2)

    return C_Di


def calcPowerToWeightCruiseBase(wingloading: float | int):
    v = calcVCruise()
    q = generalCalc.calcDynamicPressure(constants.H_CRUISE, dT, v)
    k = generalCalc.calcFactorK(constants.e0)
    epsililonCalc = generalCalc.calcEpsilon(q, wingloading, constants.C_L, constants.e0)

    ratioP_0ToW_TO =  epsililonCalc * (k_c * v)/(TR_THR * constants.ntrans * constants.nprop)

    return ratioP_0ToW_TO

def calcPowerToWeightCruiseBaseOEI(wingloading: float | int):

    v_OEI = calcCruiseVelocityOEI()
    q = generalCalc.calcDynamicPressure(constants.H_CRUISE_OEI, dT, v_OEI)
    C_D0 = generalCalc.calcParasiticDrag(constants.C_L, constants.e0)
    k_OEI = generalCalc.calcFactorK(constants.e0) * fac_k_OEI

    ratioP_0ToW_TO = (((q * C_D0)/wingloading) + k_OEI * wingloading/q) * ((k_c * v_OEI)/(TR_THR_OEI * constants.ntrans * constants.nprop)) * (constants.N_E / (constants.N_E - 1))

    return ratioP_0ToW_TO

def calcCruiseVelocityOEI():
    v = calcVCruise()
    q = generalCalc.calcDynamicPressure(constants.H_CRUISE, dT, v)
    rho = isa_model(constants.H_CRUISE_OEI, dT)[2]

    v_OEI = math.sqrt(2 * q/rho)

    return v_OEI

def calcVCruise():
    
    v = generalCalc.calcV(constants.H_CRUISE, constants.dt, constants.ma)
    
    return v