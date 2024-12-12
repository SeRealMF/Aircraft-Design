from isa import isa_model
import constants
#get maximal Wingloading at Sea level

def getWS_Max():
    rho = isa_model(constants.landing_altitude, constants.landing_dT)[2]
    #print(rho)
    WS_Max = rho/2*constants.c_Lmax_Landing*(constants.v_L)**2
    return(WS_Max)

#print(getWS_Max())