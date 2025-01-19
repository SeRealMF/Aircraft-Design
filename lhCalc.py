
import constants
import math

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