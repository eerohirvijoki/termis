# Import library and revert to SI-units (if desired)
import pyromat as pm
pm.config['unit_pressure']='Pa' # default is (bar)
pm.config['unit_energy']='J'    # default is (kJ)
pm.config['unit_molar']='mol'   # default is (kmol)

# Instantiate the multiphase substance model for water
h2o=pm.get('mp.H2O')

# Use specific volume and temperature to calculate pressure.
# Use density and temperature to calculate vapor quality.
v=0.1 # m^3/kg
d=1/v # kg/m^3
T=150+273.15 # K
p=h2o.p(v=v,T=T) # Pa
x=h2o.x(d=d,T=T) # dimensionless

# Use specific volume and temperature to calculate
# all data with one call
state=h2o.state(v=v,T=T)
p=state.get('p') # Pa
x=state.get('x') # dimensionless
    
# Get critical point information
T_crit,p_crit,rho_crit=h2o.critical(density=True) # K, Pa, kg/m^3

# Get triple line information
T_trp,p_trp=h2o.triple() # K, Pa

# Use temperature to obtain saturation pressure
# and saturation liquid and vapor volumes
T=150+273.15 # K
p_sat=h2o.ps(T=T) # Pa
v_liq,v_vap=h2o.vs(T=T) # m^3/kg



