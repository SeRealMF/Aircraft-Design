import constants 
import math

def calK_prob(N_Prop):
    K_Prop = 0
    N_Prop = int(N_Prop)
    if N_Prop < 2:
        print("Bist du eigentlich a weng deppad im Hirn? A Prop mit am oder Null Blätter den Zeigst ma.")
        exit
    elif N_Prop == 2:
        K_Prop = 0.56
    elif N_Prop == 3:
        K_Prop = 0.52
    elif N_Prop >= 4:
        K_Prop = 0.49
    
    return(K_Prop)

def Engine_power(P,Etha_Trans,N_E):
    Pbr = P * Etha_Trans
    PbrE = Pbr / N_E
    return(PbrE)


def Prop_size(N_Prop,P,Etha_Trans,N_E):
    PbrE = Engine_power(P,Etha_Trans,N_E)
    K_Prop = calK_prob(N_Prop)
    dProp = K_Prop * ((PbrE)**(1/4))
    return(dProp)
