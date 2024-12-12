from Take_Off_Distance import takeOff_pw_ws
from isa import isa_model
from Landing_Distance import getLandingDistance
from WS_Max import getWS_Max
from cruise import calcPowerToWeightCruiseBaseOEI

from Climb_OEI_V1 import Climb_OEI_Out
#import Climb OEI

from Climb_service_V1 import Clim_Serv_out

import constants
import matplotlib.pyplot as plt
import numpy as np


#Values Landing




#plotting
x_max = 7000

Values_Climb_OEI = []
Values_calcPowerToWeightCruiseBaseOEI = []
Values_TO = []
WS_Max_Landing = []

#x = range(0,x_max,10)
WS_Values = np.linspace(100,x_max,100)



for i in WS_Values:
    Values_Climb_OEI.append(Climb_OEI_Out(i))
    #Values_calcPowerToWeightCruiseBaseOEI = calcPowerToWeightCruiseBaseOEI(i)
    Values_TO.append(takeOff_pw_ws(i))


x=WS_Values
plt.axvline(x = getWS_Max(), label = 'W/S max')
plt.axvline(x = getLandingDistance(), label = 'W/S max Landing')
plt.axvline(x = Clim_Serv_out(), label = 'Clim_Serv')
plt.plot(x, Values_Climb_OEI)
#plt.plot(x, Values_Clim_Serv)
plt.axvline(x, WS_Max_Landing)
#plt.plot(x, Values_calcPowerToWeightCruiseBaseOEI)
#plt.plot(x, Values_TO,'s')
plt.xlim([0, x_max])
plt.xlabel('Wing Loading [N/m^2]')
plt.ylabel('Power to Weight Ratio [W/N]')
plt.show()



