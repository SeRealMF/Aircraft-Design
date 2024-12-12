import constants
import math
import isa

def calcV(h, dT, m):
    return isa.isa_model(h, dT)[3]*m

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

    return (epsilionCalc)

def v_TO(W_S):
    vSR=math.sqrt(2*constants.n_zw*W_S/((isa.isa_model(constants.h_TO,constants.dT_TO)[2])*constants.c_Lmax_Start))
    vLOF = 1.08*vSR
    v2 = 1.13*vSR
    return vSR, vLOF, v2
    
def calcDynamicPressure(h: float | int, dT: float | int, v: float | int):

    q = 1/2 * isa.isa_model(h, dT)[2] * math.pow(v, 2)

    return q