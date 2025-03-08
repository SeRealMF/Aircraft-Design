import numpy as np
import constants as con
import pandas as pd
import math
from Drag_Estimation import t_c
from wing_area import phi_25_deg, wing_parameter
import isa
from Wing_thorenbeck import Clac_nult
from Drag_Estimation import s_de

def Calc_Wsc():
    ksc = con.ksc
    Wto = con.Wto_stretch / 9.806

    Wsc = (ksc * 0.768 *Wto**(2/3)) * 1.2

    return(Wsc)



