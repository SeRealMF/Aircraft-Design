#General
Wto = 90000 #maxium takeoff weight base version in kg
V_CRUISE = 140 #crusing speed in m/s
ntrans = 0.99 #transmission efficency (gearbox)
nprop = 0.9 #propeller efficeny, variable pitch
AR = 9 #Aspect Ratio
e0 = 0.8 #Oswald factor
H_CRUISE = 10000 #crusing altitude in m
N_E = 2 #number of engines
ToOEI = 80000 #XXX NOT RIGHT VALUE XXX
SeCe = 14000 #Service Ceiling CHECK VALUE!!!!
vvre =  300 # Minimum Vertikal Speed in ft/min CHECK VALUE!!!!
dt = 0  # no temperature differnce Temperature(ISA) CHECK VALUE!!!!
ma = 0.5  # chosen Mach number for flight CHECK VALUE!!!!

#Cruise chosen values
epsilion = 1/18 #glide ratio 1/(L/D) - middle of range for commercial aircraft turbofans due to worse aerodynamics of LHE aircaft compared to conventional

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


