from isa import isa_model
from Landing_Distance import getLanding_distance
from WS_Max import getWS_Max

from Climb_OEI_V1 import Climb_OEI_Graph
#import Climb OEI

import matplotlib.pyplot as plt
import numpy as np


#Choosen Values Climb
Probef = 0.80
Transef = 0.99
TRthr = 1






#Values Landing
v_approach = 140*1.852 #Angabe: Maximum approach speed at maximum landing mass 140 kts (CAS)
v_50_min = v_approach*1.23 #The approach speed must be 23% higher than the minimum speed for steady-state flight,
epsilon_L = 5#Lift, to Discuss
S = 250 #Wing Surface Area, to Dicuss
AR = 9 #Aspect Ratio, to Dicuss
n_E = 2 #Number of Engines, to Discuss
b_M = 9.81/2 #Braking deacceleration [m/s^2], g/2 is appropriate
c_Lmac_Ldg = 2.5 #Angabe: Maximum lift coefficient in landing Configuration: 2.2 … 2.8
safety = 0.6 #According to EASA CAT.POL.A.230 the aircraft must come to a standstill after 60% (or 70% for Turboprops) of the available landing distance.

#Landing Distance
#Angabe: Maximum landing distance 1,900 m (SL, ISA).
print ('Landing Distance =', getLanding_distance(1000,S,n_E,c_Lmac_Ldg,epsilon_L,b_M,safety))
WS_Max = getWS_Max(0,c_Lmac_Ldg, v_approach)
print ('WS_Max =', WS_Max)



#plotting
x_max = 200000

x = np.linspace(0,x_max,10)
plt.axvline(x = WS_Max, label = 'W/S max')
plt.xlim([0, x_max])
plt.xlabel('Wing Loading [N/m^2]')
plt.ylabel('Power to Weight Ratio [W/N]')
plt.show()



