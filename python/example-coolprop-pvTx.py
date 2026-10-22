# import libraries and classes
import CoolProp as CP
from CoolProp import AbstractState

# import water as a multiphase substance
h2o=AbstractState('HEOS','Water')

# Use specific volume and temperature to calculate
# pressure and vapor quality.
v=0.1 # m^3/kg
T=150+273.15 # K
h2o.update(CP.DmassT_INPUTS, 1/v, T)
p=h2o.p() # Pa
x=h2o.Q() # dimensionless

# Get critical point information
T_crit=h2o.T_critical() # K
p_crit=h2o.p_critical() # Pa
rho_crit=h2o.rhomass_critical() # kg/m^3

# Get triple line information
T_trp=h2o.Ttriple() # K
p_trp=h2o.trivial_keyed_output(CP.iP_triple) # Pa

# Use temperature to obtain saturation pressure
# and saturation liquid and vapor volumes
T=150+273.15 # K
h2o.update(CP.QT_INPUTS, 0, T)
p_sat=h2o.p() # Pa
v_liq=1/h2o.rhomass() # m^3/kg
h2o.update(CP.QT_INPUTS, 1, T)
v_vap=1/h2o.rhomass() # m^3/kg


