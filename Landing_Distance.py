from urllib.request import request_host

import constants
from constants import c_Lmac_Ldg
from isa import isa_model
import math

from weight_estimation import fuelFactor


#W_L            ...Wingload[]
# S             ...Wing platform area[m^2]
# n_E           ...numbers of Engines[n]
# c_Lmac_Ldg    ...maximum lift coefficient at landing
# epsilon_L     ...Lift anything? don't know
# b_M           ...Braking deacceleration [m/s^2]


def getLanding_distance(W_L,S,n_E,c_Lmac_Ldg, epsilon_L,b_M, safety):
    rho = (isa_model(0,20)[2])# get density at Sea level
    rho_0 = (isa_model(0,20)[2])
    g_0 = 9.81 #m/s
    h_50 = 50*0.3048 #50 feet flight level to meters

    #calculating v_s...stall speed[m/s]
    v_s = math.sqrt((2/rho*c_Lmac_Ldg)*(W_L/S))*math.sqrt(rho_0/rho)#corrected for altitude but we only need Sea Level

    #v_50...velocity at begin of runway altitude 50ft above runway
    v_50 = 1.23*v_s # Taking into account the operational rule that the approach speed must be 23% higher than the minimum
    # speed for steady-state flight, a given maximum approach speed results in a maximum landing area load of

    #n_E...numbers of Engines
    #v_L...speed at landing
    #v_s...stall speed
    if n_E < 2: print("We need more Engines!")#landing speed depends on number of Engines, values for 1g stall
    elif 2<=n_E<=3: v_L = 1.13*v_s
    elif n_E > 3: v_L = 1.13*v_s


    #Energy balance
    E_50 = W_L*v_50*v_50/(2*g_0) + W_L*h_50 #Energie at begin of runway altitude 50ft above runway
    E_L = W_L*v_L*v_50/(2*g_0) #Energy landed

    deceleration_Energy = E_50-E_L #Energy from 50ft to landing
    # deceleration_Energy is also D*s_50
    #s_50...distance on runway from 50ft to landing
    #D...Drag (force)

    #s_50=deceleration_Energy/D

    # with W_L/D=1/epsilon_L
    #W_L...Wingload
    #S...Wing platform area[m^2]

    #s_50 = (W_L/D)*(1/(2*g_0))*(v_50*v_50-v_l*v_L)+(W_L/D)*h_50
    #changes to

    s_50 = (1/(2*g_0*epsilon_L))*(v_50*v_50-v_L*v_L)+h_50/epsilon_L


    s_R=(v_L*v_L)/(2*b_M)

    s_L=s_50+s_R

    s_L_ops = s_L*(1/safety) # Aircraft moust be capable to stop at 70% of the Runway

    return (s_L_ops)

print(getLanding_distance(1,2,3,4,5,6,7))

def getLanding_Wingloading(Wingloading):

    rho = (isa_model(0,0)[2])

    s_50 = Wingloading(1 / (2 * g_0 * constants.epsilon_L)) * (constants.v_50 * constants.v_50_min - constants.v_L * constants.v_L) + h_50 / epsilon_L

    s_R = -Wingloading*(1.13^2) / (rho * constants.c_Lmac_Ldg * b_M)

    s_L = s_50 + s_R

    s_L_ops = s_L*(1/safety)

    return (s_L_ops)

#tuwel.tuwien.ac.at/pluginfile.php/4235978/mod_resource/content/0/2024_11_04_propulsion_systems_dimensioning.pdf

