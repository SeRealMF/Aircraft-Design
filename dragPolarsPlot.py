import matplotlib.pyplot as plt
import numpy as np
import constants as cons

ar = cons.AR
c_d0 = 0.0191 #cD0 Base Version
#c_d0 = 0.0191 # cD0 Stretch Version

cl_max_clean = 1.1
cl_max_to = 2.25
cl_max_landing = 2.7

e_clean = 0.8
e_cruise_long_range = 0.75
e_cruise_high_speed = 0.7
e_to = 0.75
e_landing = 0.7

cdc_clean = 0
cdc_cruise_long_range = 0.0005
cdc_cruise_high_speed = 0.002
cdc_to = 0.015
cdc_landing = 0.06
cdc_gear = 0.02

def ld_calc(cl,e,dcd):
    ld = 1 / (c_d0 / cl + cl / (np.pi * ar * e) + dcd / cl)
    return ld

def polar_plot(cl_max, e, dcd):
    datenpunkte = 500
    cd_list = []
    cl_list = []

    for i in range(0, datenpunkte - 1):
        cl = cl_max / datenpunkte * (i + 1)
        cl_list.append(cl)
        cd = c_d0 + cl**2 / (np.pi * e * ar) + dcd
        cd_list.append(cd)

    return cl_list, cd_list

def glide_plot(cl_max, e, dcd):
    datenpunkte = 500
    cl_list = []
    ld_list = []

    for i in range(0, datenpunkte - 1):
        cl = cl_max / datenpunkte * (i + 1)
        cl_list.append(cl)
        ld_list.append(ld_calc(cl,e,dcd))

    return cl_list, ld_list

pt_cl_clean = 0.526
pt_ld_clean = ld_calc(pt_cl_clean,e_clean,0)
pt_cl_to = 2.1
pt_ld_to = ld_calc(pt_cl_to,e_to,0.023)
pt_cl_landing = 2.5
pt_ld_landing = ld_calc(pt_cl_landing,e_landing,0)

#################################### P L O T ###########################################

def plot_high_speed_regime():
    x_clean = np.array(polar_plot(cl_max_clean, e_clean, cdc_clean)[1])
    y_clean = np.array(polar_plot(cl_max_clean, e_clean, cdc_clean)[0])
    x_cruise_long_range = np.array(polar_plot(cl_max_clean, e_cruise_long_range, cdc_cruise_long_range)[1])
    y_cruise_long_range = np.array(polar_plot(cl_max_clean, e_cruise_long_range, cdc_cruise_long_range)[0])
    x_cruise_high_speed = np.array(polar_plot(cl_max_clean,e_cruise_high_speed,cdc_cruise_high_speed)[1])
    y_cruise_high_speed = np.array(polar_plot(cl_max_clean,e_cruise_high_speed,cdc_cruise_high_speed)[0])

    plt.xlim([0, 0.08])
    plt.ylim([0, 1.2])

    plt.plot(x_clean,y_clean, color='tab:green', label='clean configuration')
    plt.plot(x_cruise_long_range,y_cruise_long_range, color='tab:green', label='long range cruise', linestyle='dashdot')
    plt.plot(x_cruise_high_speed,y_cruise_high_speed, color='tab:green', label='high speed cruise', linestyle='dotted')

    plt.xlabel('$C_{D}$')
    plt.ylabel('$C_{L}$')
    plt.legend(loc='lower right',ncol=1, fancybox=True, shadow=True)
    plt.grid()
    plt.show()

    return "High Speed Drag Polar Plot created!"

def plot_low_speed_regime():
    x_clean = np.array(polar_plot(cl_max_clean, e_clean, cdc_clean)[1])
    y_clean = np.array(polar_plot(cl_max_clean, e_clean, cdc_clean)[0])
    x_to = np.array(polar_plot(cl_max_to,e_to,cdc_to)[1])
    y_to = np.array(polar_plot(cl_max_to, e_to, cdc_to)[0])
    x_to_gear = np.array(polar_plot(cl_max_to,e_to,cdc_to+cdc_gear)[1])
    y_to_gear = np.array(polar_plot(cl_max_to, e_to, cdc_to + cdc_gear)[0])
    x_landing = np.array(polar_plot(cl_max_landing,e_landing,cdc_landing)[1])
    y_landing = np.array(polar_plot(cl_max_landing, e_landing, cdc_landing)[0])
    x_landing_gear = np.array(polar_plot(cl_max_landing,e_landing,cdc_landing+cdc_gear)[1])
    y_landing_gear = np.array(polar_plot(cl_max_landing, e_landing, cdc_landing + cdc_gear)[0])

    plt.xlim([0, 0.5])
    plt.ylim([0, 3])

    plt.plot(x_clean, y_clean, color='tab:green', label='clean configuration')
    plt.plot(x_to, y_to, color='tab:red', label='take off', linestyle='dashdot')
    plt.plot(x_to_gear, y_to_gear, color='tab:red', label='take off w.o. landing gear')
    plt.plot(x_landing, y_landing, color='tab:blue', label='approach', linestyle='dashdot')
    plt.plot(x_landing_gear, y_landing_gear, color='tab:blue', label='final approach')

    plt.xlabel('$C_{D}$')
    plt.ylabel('$C_{L}$')
    plt.legend(loc='lower right', ncol=1, fancybox=True, shadow=True)
    plt.grid()
    plt.show()

    return "Low Speed Drag Polar Plot created!"

def plot_glide_ratio():
    x_clean = np.array(glide_plot(cl_max_clean,e_clean,cdc_clean)[0])
    y_clean = np.array(glide_plot(cl_max_clean,e_clean,cdc_clean)[1])
    x_clean_high_speed = np.array(glide_plot(cl_max_clean,e_cruise_high_speed,cdc_cruise_high_speed)[0])
    y_clean_high_speed = np.array(glide_plot(cl_max_clean,e_cruise_high_speed,cdc_cruise_high_speed)[1])
    x_clean_long_range = np.array(glide_plot(cl_max_clean,e_cruise_long_range, cdc_cruise_long_range)[0])
    y_clean_long_range = np.array(glide_plot(cl_max_clean, e_cruise_long_range, cdc_cruise_long_range)[1])
    x_to = np.array(glide_plot(cl_max_to,e_to,cdc_to)[0])
    y_to = np.array(glide_plot(cl_max_to,e_to,cdc_to)[1])
    x_to_gear = np.array(glide_plot(cl_max_to,e_to,cdc_to+cdc_gear)[0])
    y_to_gear = np.array(glide_plot(cl_max_to, e_to, cdc_to + cdc_gear)[1])
    x_landing = np.array(glide_plot(cl_max_landing,e_landing,cdc_landing)[0])
    y_landing = np.array(glide_plot(cl_max_landing, e_landing, cdc_landing)[1])
    x_landing_gear = np.array(glide_plot(cl_max_landing,e_landing,cdc_landing+cdc_gear)[0])
    y_landing_gear = np.array(glide_plot(cl_max_landing, e_landing, cdc_landing + cdc_gear)[1])

    plt.xlim([0, 3.5])
    plt.ylim([0, 20])

    plt.plot(x_clean, y_clean, color='tab:green', label='clean configuration')
    plt.plot(x_clean_long_range, y_clean_long_range, color='tab:green', label='long range cruise', linestyle='dashdot')
    plt.plot(x_clean_high_speed, y_clean_high_speed, color='tab:green', label='high speed cruise', linestyle='dotted')
    plt.plot(x_to, y_to, color='tab:red', label='take off')
    plt.plot(x_to_gear, y_to_gear, color='tab:red', label='take off with gear', linestyle='dashdot')
    plt.plot(x_landing, y_landing, color='tab:blue', label='approach')
    plt.plot(x_landing_gear, y_landing_gear, color='tab:blue', label='final approach', linestyle='dashdot')

    plt.scatter(pt_cl_clean, pt_ld_clean, marker='s', color='tab:green', label='init. est. cruise', zorder=2)
    plt.scatter(pt_cl_to, pt_ld_to, marker='s', color='tab:red', label='init. est. take off', zorder=2)
    plt.scatter(pt_cl_landing, pt_ld_landing, marker='s', color='tab:blue', label='init. est. landing', zorder=2)

    plt.xlabel('$C_{L}$')
    plt.ylabel('L/D')
    plt.legend(fontsize='9', loc='upper right', ncol=1, fancybox=True, shadow=True)
    plt.grid()
    plt.show()

    return "Glide Ratio Plot created!"

plot_high_speed_regime()
plot_low_speed_regime()
plot_glide_ratio()

#################################### A B L A G E ##################################################################
    # plt.plot(x, y)
    # plt.grid()
    # plt.show()

    # plt.axvline(x = getWS_Max(), color='tab:grey', label='W/S Max', linestyle='dashdot')
    # plt.axvline(x = getLandingDistance(), color='darkgreen', label='Landing Distance', linestyle='dashdot')
    # plt.axvline(x = maxlandingWS, color='darkgreen', label='Landing Distance', linestyle='dashdot')
    # plt.axvline(x = 8860, color='darkgreen', label='Landing Distance', linestyle='dashdot')
    #plt.plot(x, Values_Climb_OEI, color='tab:olive', label='Climb OEI')
    #plt.plot(x, Values_calcPowerToWeightCruiseBaseOEI, color='tab:cyan', label='Cruise OEI')
    #plt.plot(x, Values_calcPowerToWeightCruiseBase, color='tab:purple', label='Cruise')
    #plt.plot(x, Values_TO, color='tab:pink', label='Take-off')
    #plt.axhline(y=powerToWeightChosen, color='tab:orange', label='Selected P/W ratio', linestyle='--')
    #plt.scatter(minPWpoint[0], minPWpoint[1], color='tab:brown', label='Minimal Point', zorder=2)
    #plt.scatter(3300, powerToWeightChosen, color='tab:red', label='Design Point', zorder=2)
    #plt.xlim([0, x_max])
    #plt.ylim([0, 100])