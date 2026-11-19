import numpy as np
import pyromat as pm
from scipy.integrate import odeint

# load the substance
h2o=pm.get('mp.H2O')

# time rate of change temperature
# in an isochoric choric heating process
def dTdt_isochoric(T,t,v,q_dot):
    cv=h2o.cv(T=T,v=v)[0] # kJ/kg/K
    return q_dot/cv

# specific heat rate
q_dot=10.0 # kJ/s

# initial temperature
T_0=380+273.15 # K

# constant specific volume
v=3e-3 # m^3/kg

# a vector of time values
ts=np.linspace(0,100,101) # s

# list of heat and temperature values
q=q_dot*ts # kJ
Ts=odeint(dTdt_isochoric, T_0, ts, args=(v,q_dot)) # K

# create a figure
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(6,5))
ax.plot(q,Ts-273.15)

plt.show()


    
