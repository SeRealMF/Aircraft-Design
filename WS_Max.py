import isa.py
#get maximal Wingloading at Sea level

def getWS_Max(landing_altitude, c_L_maxL, v_50):
    WS_Max = isa_model(landing_altitude, 0)/2+c_L_maxL*(v_50/1.23)**2
    return(WS_Max)