import numpy as np
import constants as con
import pandas as pd
import math
from Prop_Dim_V1 import Engine_power

def Calc_Wn():
    Wn_cons = con.Wn_constant
    ESHP = (Engine_power(con.P_s) * 1.36 )* con.N_E
    

    Wn = (Wn_cons*ESHP)

    return(Wn)



def Calc_We():
    EtSHP = (Engine_power(con.P_s)*con.TRthr_TO) * 1.36
    kpg = con.kpg
    Ne = con.N_E
    We = con.M_engine
    W_prop = 0.109 * EtSHP

    Wpg =  Ne * (We + 0.109 * EtSHP)

    return(Wpg)

