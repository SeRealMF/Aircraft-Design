
import constants
from constants import s_L_max, c_Lmax_Landing
from isa import isa_model
import math

import generalCalc



#W_L            ...Wingload[]
# S             ...Wing platform area[m^2]
# n_E           ...numbers of Engines[n]
# c_Lmac_Ldg    ...maximum lift coefficient at landing
# epsilon_L     ...Lift anything? don't know
# b_M           ...Braking deacceleration [m/s^2]

def LandingDistance(Wingloading):


    rho = (isa_model(0,0)[2])
    q = generalCalc.calcDynamicPressure(0, 0, constants.v_50)
    #print(q)
    epsilon_L = generalCalc.calcEpsilon(q, Wingloading, c_Lmax_Landing, constants.e0)
    epsilon_L = constants.Epsilon_Landing
    #print('epsilon_L: ', epsilon_L)
    s_50 = Wingloading*(1 / (9.81 * epsilon_L * rho * constants.c_Lmax_Landing)) * (1.23**2 - 1.13**2) + constants.h_50 / epsilon_L
    #print('s_50: ',s_50)

    s_R = (-Wingloading*1.13*1.13) / (rho * constants.c_Lmax_Landing * constants.b_M)
    #print('s_R: ',s_R)

    s_L = s_50 + s_R
    #print('s_L: ',s_L)

    s_L_ops = s_L*(1/constants.safety)

    return(s_L_ops)

def getLandingDistance():
    for i in range(10, 100000, 10):
        if (LandingDistance(i) > constants.s_L_max):
            return(i)

print(getLandingDistance())


#tuwel.tuwien.ac.at/pluginfile.php/4235978/mod_resource/content/0/2024_11_04_propulsion_systems_dimensioning.pdf

