# specify temperature and specific volume
T=500+273.15 # K
v=1e-2 # m^3/kg

# import library and set SI units
import pyromat as pm
pm.config['unit_pressure']='Pa' 
pm.config['unit_energy']='J'    
pm.config['unit_molar']='mol'

# instantiate the substance model
# and calculate cv and cp
h2o=pm.get('mp.H2O')
cv=h2o.cv(T=T,v=v)[0] # J/kg/K
cp=h2o.cp(T=T,v=v)[0] # J/kg/K

# print results
print(f'cv = {cv*1e-3:g} (kJ/kg/K)')
print(f'cp = {cp*1e-3:g} (kJ/kg/K)')

# import libraries and classes
import CoolProp as CP
from CoolProp import AbstractState

# instantiate the substance model
h2o=AbstractState('HEOS','Water')

# update the instance according to
# the evaluation data
h2o.update(CP.DmassT_INPUTS, 1/v, T)
cv=h2o.cvmass()
cp=h2o.cpmass()

# print results
print(f'cv = {cv*1e-3:g} (kJ/kg/K)')
print(f'cp = {cp*1e-3:g} (kJ/kg/K)')


