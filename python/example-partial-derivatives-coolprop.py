# import libraries and classes
import CoolProp as CP
from CoolProp import AbstractState

# instantiate the substance model
h2o=AbstractState('HEOS','Water')

# define the state
p=225e5 # Pa
T=376+273.15 # K
h2o.update(CP.PT_INPUTS, p, T)

# Compute (dp/dT) at constant density
dp_dT_rho = h2o.first_partial_deriv(CP.iP, CP.iT, CP.iDmass)*1e-5 # bar/K
# Compute (dT/drho) at constant pressure
dT_drho_p = h2o.first_partial_deriv(CP.iT, CP.iDmass, CP.iP) # K*m^3/kg
# Compute (drho/dp) at constant temperature
drho_dp_T = h2o.first_partial_deriv(CP.iDmass, CP.iP, CP.iT)*1e5 # kg/m^3/bar

# print the partial derivative values
print(f'dp_dT_rho = {dp_dT_rho:g} (bar/K)')
print(f'dT_drho_p = {dT_drho_p:g} (K*m^3/kg)')
print(f'drho_dp_T = {drho_dp_T:g} (kg/m^3/bar)')

# verify the triple product result
print(f'dp_dT_rho * dT_drho_p * drho_dp_T = ' + \
      f'{dp_dT_rho * dT_drho_p * drho_dp_T:g}')
