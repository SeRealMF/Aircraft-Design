import math
import constants as cons
import isa

v_cruise = 239.6
q_OEI = 0.5*isa.isa_model(cons.H_CRUISE,0)[2]*v_cruise**2
v_OEI = math.sqrt(2*q_OEI/isa.isa_model(cons.H_CRUISE_OEI,0)[2])
k_OEI=1/(3.141*cons.AR*cons.e0)
print(v_OEI)