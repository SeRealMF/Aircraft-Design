import constants
import math



def calcParasiticDrag():

    C_D0 = constants.epsilion * constants.C_L - (1/(math.pi * constants.AR * constants.e0) * math.pow(constants.C_L, 2)) 

    return C_D0

def calcEpsilon(q, wingloading, k):

    C_D0 = calcParasiticDrag()

    epsilionCalc = (q * C_D0)/wingloading + k * wingloading/q

    return epsilionCalc