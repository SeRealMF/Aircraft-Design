from isa import isa_model
from Landing_Distance import getLanding_distance
#from weight_estimation import

import matplotlib.pyplot as plt
import numpy as np

#Choosen Values
epsilon_L = 5#Lift
S = 500 #Wing Surface Area
AR = 10 #Aspect Ratio
n_E = 2#Number of Engines
b_M = 5 #Braking deacceleration [m/s^2]
c_Lmac_Ldg = 0.5 #maximum Lift Coefficient at Landing




x = np.linspace(0, 7000, 10)
plt.plot(np.linspace(getLanding_distance(0,S,n_E,c_Lmac_Ldg,epsilon_L,b_M), 10), x)
#plt.set_xlim((0, 7000))
#plt.set_xlim(([0, 7000))
plt.xlabel('Wing Loading [N/m^2]')
plt.ylabel('Power to Weight Ratio [W/N]')
plt.show()