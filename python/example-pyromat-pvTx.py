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

# Import and configure libraries
import numpy as np
import pyromat as pm
pm.config['unit_pressure']='Pa' 
pm.config['unit_energy']='J'    
pm.config['unit_molar']='mol'   
import matplotlib.pyplot as plt

# Instantiate the substance model
h2o = pm.get('mp.H2O')
T_crit,_ = h2o.critical() # K

# Draw selected isotherms
fig,ax=plt.subplots(figsize=(6,5))
p_min=0.1*1e5 # Pa
p_max=1000*1e5 # Pa
T=np.array([100,200,300,400,500])+273.15 # K
for Ti in T:
    if Ti < T_crit:
        p_sat=h2o.ps(Ti)
        v_liq,v_vap=h2o.vs(T=Ti)
        p_high=np.logspace(np.log10(p_sat),np.log10(p_max),101)
        p_low=np.logspace(np.log10(p_min),np.log10(p_sat),101)
        p=np.concatenate((p_low,p_high))
        v=np.concatenate((h2o.v(p=p_low[:-1],T=Ti),v_vap,
                          v_liq,h2o.v(p=p_high[1:],T=Ti)))
    else:
        p=np.logspace(np.log10(p_min),np.log10(p_max),201)
        v=h2o.v(p=p,T=Ti)
    ax.plot(v,p*1e-5,label=f'T={Ti-273.15:g} (C)')

# Add saturated liquid and vapor curves
T=np.linspace(T_trp,T_crit,201) # K
p_sat=h2o.ps(T=T) # bar
v_liq,v_vap=h2o.vs(T=T) # m^3/kg
ax.plot(v_liq,p_sat*1e-5,color='black')
ax.plot(v_vap,p_sat*1e-5,color='black')

# Add selected vapor quality curves
styles=['--','-.',':']
x=np.array([0.001,0.01,0.1]) # dimensionless
for i,xi in enumerate(x):
    v=h2o.v(x=xi,T=T) # m^3/kg
    ax.plot(v,p_sat*1e-5,color='black',
            linestyle=styles[i],label=f'x={xi:g}')

# Tune and save the figure into a file
ax.legend()
ax.set_ylim([p_min*1e-5,p_max*1e-5])
ax.set_xlabel('v (m^3/kg)')
ax.set_ylabel('p (bar)')
ax.grid(True,which='both',linewidth=0.3)
ax.set_xscale('log')
ax.set_yscale('log')
plt.savefig('example-pyromat-pv.pdf',bbox_inches='tight')
plt.close(fig)           





