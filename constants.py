#General
Wto = 90000 #maxium takeoff weight base version in kg
V_CRUISE = 140 #crusing speed in m/s
ntrans = 0.99 #transmission efficency (gearbox)
nprop = 0.9 #propeller efficeny, variable pitch.
AR = 9 #Aspect Ratio
e0 = 0.8 #Oswald factor
H_CRUISE = 10000 #crusing altitude in m
N_E = 2 #number of engines
N_prop = 3 #number of Blades on the Prop
ToOEI = 80000 #XXX NOT RIGHT VALUE XXX
SeCe = 14000 #Service Ceiling CHECK VALUE!!!!
vvre =  300 # Minimum Vertikal Speed in ft/min CHECK VALUE!!!!
dt = 0  # no temperature difference Temperature(ISA) CHECK VALUE!!!!
ma = 0.5  # chosen Mach number for flight CHECK VALUE!!!!
n_zw = 1 #Load Multiplier Vertical Trajectory
g0 = 9.806 #Gravitationsbeschleunigung

#Cruise chosen values
epsilion = 1/18 #glide ratio 1/(L/D) - middle of range for commercial aircraft turbofans due to worse aerodynamics of LHE aircaft compared to conventional
C_L = 0.5 #lift coefficient cruise

#Choosen Values Take Off
u_roll = 0.03 #Rollreibungskoeffizient
u_aero  = 0.13 #Luftreibungskoeffizient
TRthr_TO = 1 #Power Throttle Ratio
n_prop_TO = 0.7 #Propulsion Efficiency
n_prop_TOCl = 0.8 #Propulsion Efficiency during initial climb phase
c_Lmax_Start = 2 #Coefficient of lift during Take Off, with Flaps and Slats
f_LOF = 1.08 #Speed Coefficient to calculate v_LOF from v_s1g
h_scr = 10.668 #35 ft obstacle height in meters
dT_TO = 0 #Temperature difference at take off in K
h_TO = 0 #height above mean sea level in m
epsilon_TO = 1/10 #Take-Off Epsilon
e_TO = 0.7 #Oswald factor with extended flaps and gear


#Choosen Values Climb OEI
Probef = 0.80
Transef = 0.99
TRthr = 1

# #Choosen Values Climb service
Probef = 0.90
Transef = 0.99
TRthr = 0.9
vvre = 100 #kts


#Choosen Values Landing
v_approach = 140*1.852 #Angabe: Maximum approach speed at maximum landing mass 140 kts (CAS)
v_50_min = v_approach*1.23 #The approach speed must be 23% higher than the minimum speed for steady-state flight,
epsilon_L = 5#Lift, to Discuss
S = 250 #Wing Surface Area, to Dicuss
AR = 9 #Aspect Ratio, to Dicuss
b_M = 9.81/2 #Braking deacceleration [m/s^2], g/2 is appropriate
c_Lmac_Ldg = 2.5 #Angabe: Maximum lift coefficient in landing Configuration: 2.2 … 2.8
safety = 0.6 #According to EASA CAT.POL.A.230 the aircraft must come to a standstill after 60% (or 70% for Turboprops) of the available landing distance.


