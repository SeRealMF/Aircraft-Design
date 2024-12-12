from Take_Off_Distance import takeOff_pw_ws
from isa import isa_model
from Landing_Distance import getLanding_distance
from WS_Max import getWS_Max
from cruise import calcPowerToWeightCruiseBaseOEI

from Climb_OEI_V1 import Climb_OEI_Graph
#import Climb OEI

from Climb_service_V1 import Clim_Serv

import constants
import matplotlib.pyplot as plt
import numpy as np







#Values Landing

#Landing Distance
#Angabe: Maximum landing distance 1,900 m (SL, ISA).
print ('Landing Distance =', getLanding_distance(1000,constants.S,constants.N_E,constants.c_Lmac_Ldg,constants.epsilon_L,constants.b_M,constants.safety))
WS_Max = getWS_Max(0,constants.c_Lmac_Ldg, constants.v_approach)


v2 = 300 #NOCH VONE GEORG ZU BERECHNEN
epsilon_ToOEI = 1 # NOCH VONE GEORG ZU BERECHNEN
epsilon_cru = 1  # Epsilon Cruise CHECK VALUE!!!!
Climb_OEI_Graph(constants.N_E, v2 ,epsilon_ToOEI,constants.Probef, constants.Transef, constants.TRthr)

Clim_Serv(constants.vvre,constants.SeCe,constants.dt,constants.ma,epsilon_cru)

print ('WS_Max =', WS_Max)



#plotting
x_max = 7000

Values_Climb_OEI = []
Values_Clim_Serv = []
Values_calcPowerToWeightCruiseBaseOEI = []
Values_TO = []


#x = np.linspace(0,x_max,10)
x = range(0,x_max,10)
for i in x:
    Values_Climb_OEI.append(Climb_OEI_Graph(constants.N_E, v2, epsilon_ToOEI, constants.Probef, constants.Transef, constants.TRthr))
    Values_Clim_Serv.append(Clim_Serv(constants.vvre, constants.SeCe, constants.dt, constants.ma, epsilon_cru))
    Values_calcPowerToWeightCruiseBaseOEI = calcPowerToWeightCruiseBaseOEI(x)
    Values_TO.append(takeOff_pw_ws(x))


plt.axvline(x = WS_Max, label = 'W/S max')
plt.plot(x, Values_Climb_OEI)
plt.plot(x, Values_Clim_Serv)
plt.plot(x, Values_calcPowerToWeightCruiseBaseOEI)
plt.plot(x, Values_TO)
plt.xlim([0, x_max])
plt.xlabel('Wing Loading [N/m^2]')
plt.ylabel('Power to Weight Ratio [W/N]')
plt.show()



