#General
Wto = 889043 #maxium takeoff weight base version in kg
Wto_s = 984936 #stretch
# V_CRUISE = 140 #crusing speed in m/s - disused calc through general calc from mach
ntrans = 0.99 #transmission efficency (gearbox)
nprop = 0.9 #propeller efficeny, variable pitch.
AR = 10 #Aspect Ratio
e0 = 0.8 #Oswald factor
H_CRUISE = 12200 #crusing altitude in m
H_CRUISE_OEI = 3050 #crusing altidude OEI in m
N_E = 3 #number of engines
N_prop = 4 #number of Blades on the Prop
ToOEI = 80000 #XXX NOT RIGHT VALUE XXX
SeCe = 40000/3.28084 #Service Ceiling [m]CHECK VALUE!!!!
vvre =  100*0.00508 # Minimum Vertikal Speed in [m/s] CHECK VALUE!!!!
dt = 0  # no temperature difference Temperature(ISA) CHECK VALUE!!!!
ma = 0.75  # chosen Mach number for flight CHECK VALUE!!!!
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
c_Lmax_Start = 1.8 #Coefficient of lift during Take Off, with Flaps and Slats
f_LOF = 1.08 #Speed Coefficient to calculate v_LOF from v_s1g
h_scr = 10.668 #35 ft obstacle height in meters. CONSTANT! DO NOT CHANGE!
dT_TO = 0 #Temperature difference at take off in K
h_TO = 0 #height above mean sea level in m
e_TO=0.75 #ossi
epsilon_TO = 1/10 #Take-Off Epsilon Annahme
pwsafetyfactor = 1.05


#Choosen Values Climb OEI
Probef_OEI = 0.80
Transef_OEI= 0.99
TRthr_OEI = 1

# #Choosen Values Climb service
Probef_Se = 0.90
Transef_Se = 0.99
TRthr_Se = 0.9



#Choosen Values Landing
h_50=50*0.3048 #height in Meters 50ft.
v_50 = 140*0.514444 #Angabe: Maximum approach speed at maximum landing mass 140 kts (CAS)
v_s = v_50/1.23
if N_E > 2: v_L = v_s*1.08
else: v_L = v_s*1.13 # for 2 Enginies, 1.08 for more Engines
S = 250 #Wing Surface Area, to Dicuss
b_M = -9.81/3 #Braking deacceleration [m/s^2], g/2 is appropriate
c_Lmax_Landing = 2.5 #Angabe: Maximum lift coefficient in landing Configuration: 2.2 … 2.8 because we have an average plane
safety = 0.6 #According to EASA CAT.POL.A.230 the aircraft must come to a standstill after 60% (or 70% for Turboprops) of the available landing distance.
s_L_max = 1900#Maximum Landing Distance lt. Angabe 1900m
landing_altitude = 0
landing_dT = 0

P_b = 20447989*(10**-3) #kW
P_s = 22653528*(10**-3) #kW



