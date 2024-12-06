from isa import isa_model
#get maximal Wingloading at Sea level

def getWS_Max(landing_altitude, c_L_maxL, v_approach):
    rho = isa_model(landing_altitude, 0)[2]
    print(rho)
    WS_Max = rho/2*c_L_maxL*(v_approach)**2
    return(WS_Max)

#print(getWS_Max(0, 2.5, 140))