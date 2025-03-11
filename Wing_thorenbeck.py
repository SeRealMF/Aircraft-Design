import numpy as np
import constants as con
import pandas as pd
import math
from Drag_Estimation import t_c
from wing_area import wing_parameter
import isa



def Calc_kst():
    b = wing_parameter(con.AR,con.taper)[0]/2
    con_kst = con.const_kst
    Lamda_LE = con.Lamda_LE
    Wdes = (con.Wto_stretch / 9.806) - (con.m_fStr)
    vD = con.vD
    t_c 
    Lamda_12 = con.Lamda_12

    kst = 1 + con_kst * (b * np.cos(Lamda_LE*(np.pi/180)))**(3)/Wdes * (vD/100/t_c)**(2) * np.cos(Lamda_12*(np.pi/180))

    return(kst)

def Clac_nult():
    Wdes = (con.Wto_stretch / 9.806) - (con.m_fStr)

    Wdes = Wdes * 2.205 #Kg to pound

    nmax = 2.1 + 24000 / (Wdes+10000)
    


    nult = 1.5 * nmax
    return(nult)


def Calc_Wtef():
    kf = con.kf1 + con.kf2
    cons_Wtef = con.cons_Wtef
    def Sub_calc_Sf():
        Sf = 50 #Flaps Area (Calc needed) [m^2]
        return(Sf)
    Sf = Sub_calc_Sf()

    bfs = wing_parameter(con.AR,con.taper)[0]/2

    vlf = 1.8* math.sqrt(2*con.n_zw*con.WS_stretch/((isa.isa_model(con.h_TO,con.dT_TO)[2])*con.c_Lmax_Landing))
    delta_f = con.delta_f 
    Lamda_f = con.Lamda_f
    t_c_f = con.t_c_f

    Wtef = Sf * cons_Wtef * kf * (Sf*bfs)**(3/16)*((vlf/100)**(2)*np.sin(delta_f*np.pi/180)*np.cos(Lamda_f*np.pi/180)/t_c_f)**(0.75)






    return(Wtef)
    

def Calc_Ww():
    Wtef = Calc_Wtef() 
    Wlef = con.S_slat * con.cons_Wlef
    Whld = Wtef + Wlef
    b = wing_parameter(con.AR,con.taper)[0]/2
    bs = b / np.cos(con.Lamda_12*(np.pi/180))
    ke = con.ke
    kuc = con.kuc
    Wdes = (con.Wto_stretch / 9.806) - (con.m_fStr)

    kno = 1 + (con.bref / bs)**(0.5)
    





    Wwbasic = (con.Wto_stretch / 9.806)/10
    f = 100
    print("Iterative Calculation")
    print("###############################################")

    while f >= 0.0001:
        Wwbasic_it = con.const * kno * con.klamb *ke *kuc *Calc_kst() *(con.kb * Clac_nult() * (Wdes - 0.8 * (500/491*Wwbasic + 600/491 * Whld)))**(0.55)*b**(1.675)*t_c**(-0.45)*(np.cos(con.Lamda_12*np.pi/180))**(-1.325)
        f =abs((Wwbasic_it - Wwbasic) / Wwbasic)
        print(f"Pre {Wwbasic} It{Wwbasic_it}")
        Wwbasic = Wwbasic_it
    
    Ww = 500/491 * Wwbasic + 600/491 *  Whld 
    print("###############################################")

    return(Ww)






def Wing_weight_basic():
    const = con.const
    kno = 1 + (con.bref / bs)**(0.5)
    klamb = con.klamb
    ke = con.ke
    kuc = con.kuc
    kst = Calc_kst()
    kb = con.kb
    nult = Clac_nult()
    b = wing_parameter(con.AR,con.taper)[0]/2
    
    Wdes = (con.Wto_stretch / 9.806) - (con.m_fStr)

    bs = b / np.cos(con.Lamda_12*(np.pi/180))


    
print(f"Ww = {Calc_Ww()}")
