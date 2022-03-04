# %%

import numpy as np

"""Fun facts about Kvilldal found everywhere: 
Tverrsnittet på tilløpstunnelen er på hele 160 m2

"""
# %%

rho = 999 # kg m^-3 # 
dvis = 1.793 # dynamic viscosity
kvis = 1.787 # kinematic viscosity
g = 9.81 #gravitational constant

height_net = 538 #HEAD net meters (approx 10% loss)
power_peak = 1240 # peak performance over 4 units in MW
energy_yearly = 3000 # yearly production GWh (3 TWh)
power_mean = 3000*1e3/(365*24) # back to MW 

efficiency_turbin = 0.9 # estimated efficiency loss through turbin and generator (probably high)
efficiency_head = 0.9 # estimated loss of potential energy 
TP = 1 # Throughput coefficient 



flow_rate_peak = (efficiency_turbin * power_peak*1e6) / (1000*9.81*(height_net * efficiency_head)) # as m^3/s
print("peak flow rate is ", np.round(flow_rate_peak), "m^3/s - or ", np.round(flow_rate_peak*1000), "liters per second through 4 units")

flow_rate_peak = (efficiency_turbin * power_mean*1e6) / (1000*9.81*(height_net * efficiency_head)) # as m^3/s
print("mean flow rate is ", np.round(flow_rate_peak), "m^3/s - or ", np.round(flow_rate_peak*1000), "liters per second through 4 units")

#"""Electric effect of hydropower plant"""
#pp_eq = efficiency_turbin * rho * g * (height_net * efficiency_head) * TP
#netpp_potential = mass * gravity * height * efficiency


#test = efficiency_turbin*efficiency_head*1000*234*g*height_net

# %%
