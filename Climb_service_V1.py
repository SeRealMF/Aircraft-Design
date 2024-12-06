import math



# Zusatzvariablen
Probef = 0.90
Transef = 0.99
TRthr = 0.9

def calc_dhds(ne):
    ne = int(ne)
    if ne == 1:
        print("Fehler ein Triebwerk nicht möglich")
        exit
    elif ne == 2:
        dhds = 0.024
    elif ne == 3:
        dhds = 0.027
    elif ne >= 4:
        dhds = 0.03
    return(dhds)


def Climb_OEI(ne, v2, E_ToOEI, Probef, Transef, TRthr, dhds):
    E2nd = E_ToOEI * 0.8

    p1 = dhds + E2nd

    p2 = (v2)/(TRthr * Transef * Probef)

    p3 = (ne)/(ne - 1)

    PoWto = p1 * p2 * p3

    return(PoWto)
    




def Climb_OEI_Graph(ne, v2,E_ToOEI,Probef,Transef,TRthr):
    dhds = calc_dhds(ne)
    PoWto = Climb_OEI(ne, v2, E_ToOEI, Probef, Transef, dhds)
    return(PoWto)

