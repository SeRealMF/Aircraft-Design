import numpy as np
import constants as con
import pandas as pd
import math
from Drag_Estimation import t_c
from wing_area import phi_25_deg, wing_parameter
import isa
from Wing_thorenbeck import Clac_nult
from Drag_Estimation import s_de

def Calc_W_tail():
    nult = Clac_nult()
    k_wt = con.k_wt
    S_tail = s_de

    W_tail = k_wt * (nult * S_tail**(2))**(0.75)
    W_tail = W_tail * con.Cor_factor_Ttail
    return(W_tail)

 #Check if realistic (might need correction factor)