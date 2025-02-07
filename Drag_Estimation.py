import constants as cons
import numpy as np
import empennage_dimensioning as emp
import isa

#1.) Drag Estimation Linear Regression aka. Roskam Method
reg_a = -2.5229 #Roskam Regression Factor a
reg_b = 1 #Roskam Regression Factor b
reg_c = 0.0199 #Roskam Regr. Fac. c
reg_d = 0.7531 #Roskam Regr. Fac. d
mto = cons.Wto / 9.81 #mass in kg. MUST BE CONVERTED TO lbs !!!
mto_lbs = mto * 2.2046226218
s_wing = 197.5 #wing area in m^2
s_wing_ft2 = s_wing * 10.7639 #wing area in ft^2

s_wet = 10 ** reg_c * mto_lbs ** reg_d #result in ft^2
s_par = (10 ** reg_a) * (s_wet ** reg_b) #result in ft^2

cd0_roskam = s_par/s_wing_ft2
#print(mto_lbs, s_wet, s_par, cd0_roskam)

#2.) Main Components Drag Estimation
c_dw = 0.007
c_df = 0.0028
c_d_prop = 0.006
c_de = 0.008
delta_cd = 0.15

d_fuselage = (5.56 + 4.47) / 2
l_fuselage = 52.3
d_prop = 4.74
l_prop = 4

s_dw = s_wing
s_df = 0.75 * np.pi * d_fuselage * l_fuselage
s_d_prop = np.pi * d_prop * l_prop
s_de = emp.horizontal_wing_parameter()[0] + emp.vertical_wing_parameter()[0]

cd0_main = 1/s_wing * (c_dw * s_dw + c_df * s_df + c_d_prop * s_d_prop + c_de * s_de)
cd0_main = cd0_main * (1 + delta_cd)

#print(cd0_main)

#3.) Torenbeek Method
#Wing
r_w = 1 #wing form factor: 1 when self-supporting, 1.1 when strutted
t_c = 0.12 #thickness of wing in percent
phi_25 = 21.4 * np.pi / 180 #sweep angle in degrees
s = s_wing

cs_dw = 0.0054 * r_w * (1 + 3 * t_c * np.cos(phi_25) ** 2)

#Fuselage
r_f = 1.3 #0.65 + 1.5 * d_fuselage / l_fuselage
#l_fuselage = 62.93 - (32-27)*0.8 #wide body stretch estimation
w_fuselage = 4.47
#w_fuselage = 4.47 + 1.5 #wide body stretch estimation
h_fuselage = 5.55

cs_df = 0.0031 * r_f * l_fuselage * (w_fuselage + h_fuselage)

#Empennage
cs_de = 0.24 * 1.1 * (cs_dw + cs_df)

#Engine (Turbo Prop)
r_n_bas = 0.1 #Regression factor
r_n = 1.6 #Shape factor of air inlet 1 = ring inlet
p_to = 17.7e6 #take off power, all engines @ SL, ISA
s_n_front = 1.2 * 1.85 #frontal area of engine nacelle, reference EPI TP400 D6

phi_to = p_to / s_n_front

cs_dn = r_n_bas * r_n * p_to / phi_to

#Undercarriage
r_uc = 1.08 #regression factor for main landing gear embedded into fuselage nacelles

#Reynolds number correction factor
v_cruise = cons.ma * isa.isa_model(cons.H_CRUISE, cons.dt)[3]
viscosity = isa.isa_model(cons.H_CRUISE, cons.dt)[5]
re_fuselage = v_cruise * l_fuselage / viscosity #Reynolds number of fuselage @ cruise

r_re = 47 * re_fuselage ** (-0.2)
#print(re_fuselage, r_re)

#parasite drag with 3.) method
cd0_toren = r_re * r_uc * (cs_dw + cs_df + cs_de + cs_dn) / s_wing

print(cd0_roskam, cd0_main, cd0_toren)