import math
import constants as cons
import wing_area as wing

def stabilizer_dis():
    return cons.k_lf*cons.l_f

def get_wing_parameter():   #return in order: wing area, mean chord, wing span
    return wing.wing_parameter(cons.AR,cons.taper)[4], wing.wing_parameter(cons.AR,cons.taper)[1], wing.wing_parameter(cons.AR,cons.taper)[0]

def horizontal_area():
    return round(cons.coef_h*get_wing_parameter()[0]*get_wing_parameter()[1]/stabilizer_dis(),2)

def vertical_area():
    return round(cons.coef_v*get_wing_parameter()[0]*get_wing_parameter()[2]/stabilizer_dis(),2)

#print("S: ", get_wing_parameter()[0], "chord_mean: ", get_wing_parameter()[1])
#print("l_s: ", stabilizer_dis())
#print("S_h: ", horizontal_area(), "S_v: ", vertical_area())

def horizontal_wing_parameter():
    AR = cons.AR_h
    t = cons.taper_h
    S_h = horizontal_area()
    b_h = math.sqrt(AR * S_h)
    chord_mean_h = S_h / b_h
    chord_root_h = 2 * S_h / (b_h * (t + 1))
    chord_tip_h = t * chord_root_h
    return S_h, b_h, chord_mean_h, chord_root_h, chord_tip_h

def vertical_wing_parameter():
    AR = cons.AR_h
    t = cons.taper_v
    S_v = vertical_area()
    b_v = math.sqrt(AR * S_v)
    chord_mean_v = S_v / b_v
    chord_root_v = 2 * S_v / (b_v * (t + 1))
    chord_tip_v = t * chord_root_v
    return S_v, b_v, chord_mean_v, chord_root_v, chord_tip_v

#print(horizontal_wing_parameter())
#print(vertical_wing_parameter())