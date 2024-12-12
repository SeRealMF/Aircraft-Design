import constants as co



def calK_prob():
    N_Prop = co.N_prop
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

def Engine_power(P):
    N_E = co.N_E
    Etha_Trans = co.Transef
    Pbr = P * Etha_Trans
    PbrE = Pbr / N_E
    return(PbrE)


def Prop_size(P):
    PbrE = Engine_power(P)
    K_Prop = calK_prob()
    dProp = K_Prop * ((PbrE)**(1/4))
    return(dProp)
