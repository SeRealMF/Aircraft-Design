import numpy as np
import constants as con
import pandas as pd
import math

import isa


def Calc_Wsc():
    ksc = con.ksc
    Wto = con.Wto_stretch / 9.806

    Wsc = (ksc * 0.768 *Wto**(2/3)) * 1.2

    return(Wsc)



