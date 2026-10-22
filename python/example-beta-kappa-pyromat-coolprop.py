# import library
import pyromat as pm
pm.config['unit_pressure']='Pa' 
pm.config['unit_energy']='J'    
pm.config['unit_molar']='mol'

# instantiate the substance model
# and calculate the state point
h2o=pm.get('mp.H2O')
p=225e5 # Pa
T=376+273.15 # K
v=h2o.v(p=p,T=T)[0] # m^3/kg

# calculate beta_p using a finite
# difference approximation
dT=0.001 # K
dv=h2o.v(T=T+dT,p=p)[0]-v # m^3/kg
beta_p=1/v*dv/dT # 1/K

# calculate kappa_T using a finite
# difference approximation
dp=0.001*1e5 # Pa
dv=h2o.v(T=T,p=p+dp)[0]-v # m^3/kg
kappa_T=-1/v*dv/dp*1e5 # 1/bar

# print results
print(f'beta_p = {beta_p:g} (1/K)')
print(f'kappa_T = {kappa_T:g} (1/bar)')

# import libraries and classes
import CoolProp as CP
from CoolProp import AbstractState

# instantiate the substance model
h2o=AbstractState('HEOS','Water')

# define the state
p=225e5 # Pa
T=376+273.15 # K
h2o.update(CP.PT_INPUTS, p, T)

# extract the coefficients
beta_p=h2o.isobaric_expansion_coefficient() # 1/K
kappa_T=h2o.isothermal_compressibility()*1e5 # 1/bar

# print results
print(f'beta_p = {beta_p:g} (1/K)')
print(f'kappa_T = {kappa_T:g} (1/bar)')
