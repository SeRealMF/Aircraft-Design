import numpy as np
import constants as con
import pandas as pd
import math

import isa


def Calc_under_Main():
   kuc = con.kuc
   A_u_m = con.A_u_m
   B_u_m = con.B_u_m
   C_u_m = con.C_u_m
   D_u_m = con.D_u_m
   Wto = con.Wto_stretch / 9.806

   Wuc_m = kuc * (A_u_m + B_u_m * Wto **(3/4) + C_u_m * Wto + D_u_m * Wto ** (3/2))
   return(Wuc_m)

def Calc_under_Nose():
   kuc = con.kuc
   A_u_n = con.A_u_n
   B_u_n = con.B_u_n
   C_u_n = con.C_u_n
   D_u_n = con.D_u_n
   Wto = con.Wto_stretch / 9.806

   Wuc_n = kuc * (A_u_n + B_u_n * Wto **(3/4) + C_u_n * Wto + D_u_n * Wto ** (3/2))
   return(Wuc_n)


def Calc_under():
   Wuc = Calc_under_Main() + Calc_under_Nose()
   return(Wuc)

