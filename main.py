from Take_Off_Distance import takeOff_pw_ws
from isa import isa_model
from Landing_Distance import getLandingDistance
from WS_Max import getWS_Max
from cruise import calcPowerToWeightCruiseBaseOEI

from Climb_OEI_V1 import Climb_OEI_Graph
#import Climb OEI

from Climb_service_V1 import Clim_Serv

import constants
import matplotlib.pyplot as plt
import numpy as np


#Values Landing




#plotting
x_max = 7000

Values_Climb_OEI = []
Values_Clim_Serv = []
Values_calcPowerToWeightCruiseBaseOEI = []
Values_TO = []


#x = range(0,x_max,10)
WS_Values = np.linspace(100,x_max,100)



for i in WS_Values:
    #Values_Climb_OEI.append(Climb_OEI_Graph(constants.N_E, v2, epsilon_ToOEI, constants.Probef, constants.Transef, constants.TRthr))
    #Values_Clim_Serv.append(Clim_Serv(constants.vvre, constants.SeCe, constants.dt, constants.ma, epsilon_cru))
    #Values_calcPowerToWeightCruiseBaseOEI = calcPowerToWeightCruiseBaseOEI(i)
    Values_TO.append(takeOff_pw_ws(i))
    #WS_Max_Landing = getLandingDistance(i)



plt.axvline(x = getWS_Max(), label = 'W/S max')
#plt.axvline(x = )
#plt.plot(x, Values_Climb_OEI,'r')
#plt.plot(x, Values_Clim_Serv,'g')
#plt.plot(x, Values_calcPowerToWeightCruiseBaseOEI,'b')
#plt.plot(x, Values_TO,'s')
plt.xlim([0, x_max])
plt.xlabel('Wing Loading [N/m^2]')
plt.ylabel('Power to Weight Ratio [W/N]')
plt.show()



