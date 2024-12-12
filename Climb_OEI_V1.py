"""
The second climb segment begins when the landing gear has been retracted. The required climb
gradients after critical engine failure can be adimensional, especially for twin-engine aircraft. The
required climb gradients at speed v2 are as followed (CS 25)

Wichtig!!!!!!!!
Thorkbeck schreibt G/F für W/S
"""
import numpy as np
import constants as co
import generalCalc as gen
import isa as isa

# Zusatzvariablen
Probef = 0.80
Transef = 0.99
TRthr = 1

def calc_dhds(ne):
    ne = int(ne)
    if ne == 1:
        print("Fehler ein Triebwerk nicht möglich")
        exit
    elif ne == 2:
        dhds = 0.024
    elif ne == 3:
        dhds = 0.027
    elif ne >= 4:
        dhds = 0.03
    return(dhds)


def Climb_OEI(ne, v2, E_ToOEI, Probef, Transef, TRthr, dhds):
    E2nd = E_ToOEI * 0.8

    p1 = dhds + E2nd

    p2 = (v2)/(TRthr * Transef * Probef)

    p3 = (ne)/(ne - 1)

    PoWto = p1 * p2 * p3

    return(PoWto)
    




def Climb_OEI_Graph(ne, v2,E_ToOEI,Probef,Transef,TRthr):
    dhds = calc_dhds(ne)
    PoWtoClimbOEI = Climb_OEI(ne, v2, E_ToOEI, Probef, Transef, TRthr, dhds)
    return(PoWtoClimbOEI)

def Climb_OEI_Out(W_S):
    dhds = calc_dhds(co.N_E)
    q_OEI = 0.5*isa.isa_model(co.h_TO,co.dT_TO)[2]*gen.v_TO(W_S)[2]**2
    k_OEI = 1/(np.pi*co.AR+co.e_TO)
    c_D_TO = co.c_Lmax_Start*co.epsilon_TO-1/(np.pi*co.AR*co.e_TO)*co.c_Lmax_Start**2
    e_TO_OEI = q_OEI * c_D_TO / W_S + k_OEI * W_S / q_OEI
    PoWtoClimbOEI = Climb_OEI(co.N_E, gen.v_TO(W_S)[2], e_TO_OEI, co.Probef, co.Transef, co.TRthr, calc_dhds(co.N_E))
    return(PoWtoClimbOEI)




    


