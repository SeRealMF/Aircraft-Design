import math 
import constants as co
import generalCalc as ge


# Zusatzvariablen
Probef = 0.90
Transef = 0.99
TRthr = 0.9
vvre = 100 #kts




def Clim_Serv(vvre,SeCe,dt,ma,Ecru):
    #Conversion Faktor
    fkt = 0.0098747 #ft/min to kts
    mskt = 1.943844 # ms to kts
    ftm = 3.28084 #ft to m
    ktms = 0.51444444 #kts to ms

    #Descriptions
    vvre = vvre #Minimum Vertikal Speed in ft/min
    SeCe = SeCe #Service ceiling
    dt = dt # differnce Temperature(ISA)
    ma = ma #chosen Mach number for flight
    Ecru = Ecru #Epsilon Cruise

    SeCem = SeCe / ftm
    from isa import isa_model
    isa = ()
    isa = isa_model(SeCem,dt)
    a = isa[3]
    vkts = (a*ma) * mskt
    vvkts = vvre * fkt
    vhkts = (((vkts)**2)-((vvkts)**2))**(1/2)
    v = vkts * ktms
    pt1 = ((vvkts/vhkts)+Ecru)
    pt2 = (v)/(TRthr * Transef * Probef)

    PoWtoCe = pt1 * pt2
    return(PoWtoCe) 



def Clim_Serv_out():
    #Conversion Faktor
    fkt = 0.0098747 #ft/min to kts
    mskt = 1.943844 # ms to kts
    ftm = 3.28084 #ft to m
    ktms = 0.51444444 #kts to ms

    #Descriptions
    vvre = co.vvre #Minimum Vertikal Speed in ft/min
    SeCe = co.SeCe #Service ceiling
    dt = co.dt # differnce Temperature(ISA)
    ma = co.ma #chosen Mach number for flight
    Ecru = co.epsilion #Epsilon Cruise

    SeCem = SeCe / ftm
    from isa import isa_model
    isa = ()
    isa = isa_model(SeCem,dt)
    a = isa[3]
    vkts = (a*ma) * mskt
    vvkts = vvre * fkt
    vhkts = (((vkts)**2)-((vvkts)**2))**(1/2)
    v = vkts * ktms
    pt1 = ((vvkts/vhkts)+Ecru)
    pt2 = (v)/(co.TRthr_Se * co.Transef_Se * co.Probef_Se)

    PoWtoCe = pt1 * pt2
    return(PoWtoCe)   
    









