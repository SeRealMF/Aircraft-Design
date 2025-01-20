
import constants
import math

class FlightPhase(enumerate):
    takeOff = 0
    cruise = 1

def calcMinTankVol(mLH: float):
    v = mLH/constants.rhoLH * constants.safteyFacMinTankVol
    return v

def interpolateStackVolRel(fcLoad: float):
    kwPerL33 = 2
    kwPerL100 = 6

    k = (kwPerL100-kwPerL33)/0.67
    d = 2 - k*0.33
    return k*fcLoad + d

def interpolateSystemVolRel(fcLoad: float):
    #is always 4; could have progammed something to calculate anyways for the posibility of future changes, or leave out handover parameter - didnt feel like it
    return 4

def interpolateCoolingVolRel(fcLoad: float):
    #is always 2; could have progammed something to calculate anyways for the posibility of future changes, or leave out handover parameter - didnt feel like it
    return 2

def calcStackVolume(power: float, fcLoad: float):
    stackVol = power/interpolateStackVolRel(fcLoad)
    return stackVol

def calcSystemVolume(power: float, fcLoad: float):
    sysVol = power/interpolateSystemVolRel(fcLoad)
    return sysVol

def calcCoolingVolume(power: float, fcLoad: float):
    coolVol = power/interpolateCoolingVolRel(fcLoad)
    return coolVol

def calcElPower(flightPhase: FlightPhase, powerToWeight: float):
    match flightPhase:
        case FlightPhase.takeOff:
            TRthr = constants.TRthr_TO
            nprop = constants.n_prop_TO
        
        case FlightPhase.cruise:
            TRthr = constants.TRthr_CR
            nprop = constants.n_prop_CR
        
        case _:
            return -1
    
    Pmot = powerToWeight * constants.Wto / (constants.ntrans * nprop)
    P_elFcSys = Pmot * (TRthr + constants.P_elNonPropToMotors) 
    
    return P_elFcSys

def calcDesignStackPower(P_elFcSys: float): #to be calculated under cruise conditions
    fcLoad = 1 - constants.oversizingFc
    n_fcStack = calcNFcStack(fcLoad)
    P_Stack = P_elFcSys/n_fcStack
    return P_Stack

def calcNFcStack(fcLoad: float):
    n_fcStack = -0.213 * fcLoad + 0.67
    return n_fcStack

def calcStackPowerMax(designStackPower: float):
    return designStackPower/(1 -  constants.oversizingFc)

def calcMinElPowBat(stackPowerMax: float, powerToWeight: float):
    P_el = calcElPower(FlightPhase.takeOff, powerToWeight)
    P_elBat = P_el - stackPowerMax * calcNFcStack(1)
    return P_elBat
    