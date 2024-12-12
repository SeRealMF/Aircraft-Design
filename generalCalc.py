import constants
import math
import isa



def calcParasiticDrag():

    C_D0 = constants.epsilion * constants.C_L - (1/(math.pi * constants.AR * constants.e0) * math.pow(constants.C_L, 2)) 

    return C_D0

def calcEpsilon(q, wingloading, k):

    C_D0 = calcParasiticDrag()

    epsilionCalc = (q * C_D0)/wingloading + k * wingloading/q

    return epsilionCalc

def v_TO(W_S):
        vSR=math.sqrt(2*constants.n_zw*W_S/((isa.isa_model(constants.h_TO,constants.dT_TO)[2])*constants.c_Lmax_Start))
        vLOF = 1.08*vSR
        v2 = 1.13*vSR
        return vSR, vLOF, v2