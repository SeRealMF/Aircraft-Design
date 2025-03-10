import numpy as np
import constants as con
import pandas as pd
import math
from Drag_Estimation import t_c
from wing_area import phi_25_deg, wing_parameter
import isa
from Wing_thorenbeck import Clac_nult
from Drag_Estimation import s_de
from Prop_Dim_V1 import Engine_power


def Calc_Wieg():
    kieg = con.kieg
    WDE = con.mOE_s
    RD = con.RC #Fehler aber nicht bessser möglich (Ja scheiße)

    Wieg = kieg * WDE **(5/9) * RD **(1/4)

    return(Wieg)

def Calc_Whpe():
    WE 
