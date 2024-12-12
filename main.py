from PIL.GimpGradientFile import linear
from fontTools.misc.py23 import isclose
from Take_Off_Distance import takeOff_pw_ws
from isa import isa_model
from Landing_Distance import getLandingDistance
from WS_Max import getWS_Max
from cruise import calcPowerToWeightCruiseBaseOEI, calcPowerToWeightCruiseBase
from Climb_OEI_V1 import Climb_OEI_Out
from Climb_service_V1 import Clim_Serv_out
import matplotlib.pyplot as plt
import numpy as np
import Prop_Dim_V1
import constants as con


Values_Climb_OEI = []
Values_calcPowerToWeightCruiseBaseOEI = []
Values_calcPowerToWeightCruiseBase = []
Values_TO = []
Values_Clim_Serv_out = []
x_max = 7000#plot from 0 to this value
WS_Values = np.linspace(100,x_max,100)

for i in WS_Values:
    Values_Climb_OEI.append(Climb_OEI_Out(i))
    Values_calcPowerToWeightCruiseBaseOEI.append(calcPowerToWeightCruiseBaseOEI(i))
    Values_calcPowerToWeightCruiseBase.append(calcPowerToWeightCruiseBase(i))
    Values_TO.append(takeOff_pw_ws(i))
    Values_Clim_Serv_out.append(Clim_Serv_out(i))


#plotting

x = WS_Values
plt.axvline(x = getWS_Max(), color='tab:grey', label='W/S Max', linestyle='--')
plt.axvline(x = getLandingDistance(), color='tab:red', label='Landing Distance', linestyle='dashdot')
plt.axhline(y=23, color='tab:orange', label='Selected P/W ratio', linestyle='--')
plt.plot(x,Values_Clim_Serv_out, color='tab:green', label='Service Ceiling')
plt.plot(x, Values_Climb_OEI, color='tab:olive', label='Climb OEI')
plt.plot(x, Values_calcPowerToWeightCruiseBaseOEI, color='tab:cyan', label='Cruise OEI')
plt.plot(x, Values_calcPowerToWeightCruiseBase, color='tab:purple', label='Cruise')
#plt.plot([3300,23], label='design point')
plt.plot(x, Values_TO, color='tab:pink', label='Take-off')
plt.xlim([0, x_max])
plt.ylim([0, 100])
plt.xlabel('Wing Loading [N/m^2]')
plt.ylabel('Power to Weight Ratio [W/N]')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),ncol=3, fancybox=True, shadow=True)
plt.show()

Prop_Base = Prop_Dim_V1.Prop_size(con.P_b)
Prop_Stretch = Prop_Dim_V1.Prop_size(con.P_s)

print("Prop_Base",Prop_Base)
print("Prop_Stretch",Prop_Stretch)
