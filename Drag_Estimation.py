import constants as cons
import numpy as np
import matplotlib as mat
import empennage_dimensioning as emp

#1.) Drag Estimation Linear Regression aka. Roskam Method
reg_a = -2.5229 #Roskam Regression Factor a
reg_b = 1 #Roskam Regression Factor b
reg_c = 0.0199 #Roskam Regr. Fac. c
reg_d = 0.7531 #Roskam Regr. Fac. d
mto = cons.Wto / 9.81 #mass in kg. MUST BE CONVERTED TO lbs !!!
mto_lbs = mto * 2.2046226218
s_wing = 240.28 #wing area in m^2
s_wing_ft2 = s_wing * 10.7639 #wing area in ft^2

s_wet = 10 ** reg_c * mto_lbs ** reg_d #result in ft^2
s_par = 10 ** (reg_a) * s_wet ** reg_b #result in ft^2

cd0_roskam = s_par/s_wing_ft2
#print(mto_lbs, s_wet, s_par, cd0_roskam)

#2.) Main Components Drag Estimation
c_dw = 0.007
c_df = 0.0028
c_d_prop = 0.006
c_de = 0.008
delta_cd = 0.15

d_fuselage = 5
l_fuselage = 50
d_prop = 4.74
l_prop = 6

s_dw = s_wing
s_df = 0.75 * np.pi * d_fuselage * l_fuselage
s_d_prop = np.pi * d_prop * l_prop
s_de = emp.horizontal_wing_parameter()[0] + emp.vertical_wing_parameter()[0]

cd0_main = 1/s_wing * (c_dw * s_dw + c_df * s_df + c_d_prop * s_d_prop + c_de * s_de)
cd0_main = cd0_main * (1 + delta_cd)

#print(cd0_main)

#3.) Torenbeek Method
#Wing
r_w = 1 #wing form fator: 1 when self supporting, 1.1 when strutted
t_c = 0.12 #thickness of wing in percent
phi_25 = 10 #sweep angle in degrees
s = s_wing

cs_dw = 0.0054 * r_w * (1 + 3 * t_c * np.cos(phi_25) ** 2)

#Fuselage
r_f = 0.65 * 1.5 * d_fuselage / l_fuselage
w_fuselage = d_fuselage #PRELIMINARY VALUES!
h_fuselage = d_fuselage #PRELIMINARY VALUES!

cs_df = 0.0031 * r_f * l_fuselage * (w_fuselage + h_fuselage)

#Empennage
cs_de = 0.24 * (cs_dw + cs_df)

#