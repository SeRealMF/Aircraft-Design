import numpy as np
import constants as con
import pandas as pd
import math
import isa


def Calc_Wieg():
    kieg = con.kieg
    WDE = con.mOE_s
    RD = con.RC #Fehler aber nicht bessser möglich (Ja scheiße)

    Wieg = kieg * WDE **(5/9) * RD **(1/4)

    return(Wieg)



def Calc_Whp(): #Berechnung nach Formel 8-38, Berechnung Hydraulics and Pneumatics
    WDE = con.mOE_s
    Whp = 0.011 * WDE + 181 #kg

    return(Whp)



