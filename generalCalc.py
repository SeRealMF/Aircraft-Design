import constants
import math



def calcParasiticDrag(C_L, e0):

    C_D0 = constants.epsilion * C_L - (1/(math.pi * constants.AR * e0) * math.pow(constants.C_L, 2)) 

    return C_D0

def calcFactorK(e0):

    k = 1/(math.pi * constants.AR * e0)

    return k

def calcEpsilon(q, wingloading, C_L, e0):

    C_D0 = calcParasiticDrag(C_L, e0)
    k = calcFactorK(e0)

    epsilionCalc = (q * C_D0)/wingloading + k * wingloading/q

    return epsilionCalc


def v_TO(W_S):
        vSR=math.sqrt(2*cons.n_zw*W_S/((isa.isa_model(cons.h_TO,cons.dT_TO)[2])*cons.c_Lmax_Start))
        vLOF = 1.08*vSR
        v2 = 1.13*vSR
        return vSR, vLOF, v2