# Import and configure libraries
import numpy as np
import pyromat as pm
import matplotlib.pyplot as plt

# Instantiate the substance model
h2o = pm.get('mp.H2O')
T_crit,_ = h2o.critical() # K
T_trp,_ = h2o.triple() # K

# create a figure for plotting
fig,ax=plt.subplots(figsize=(6,5))

# generate data and draw selected isotherms
p_min=10 # bar
p_max=1000 # bar
T=np.array([200,300,400,500])+273.15 # K
styles=['-','--','-.',':']
for Ti,style in zip(T,styles):
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
    ax.plot(v,p,label=f'T={Ti-273.15:g}'+r'$^\circ$C',
            linestyle=style,color='black')

# Add saturated liquid and vapor curves
T=np.linspace(T_trp,T_crit,501) # K
p_sat=h2o.ps(T=T) # bar
v_liq,v_vap=h2o.vs(T=T) # m^3/kg
ax.plot(v_liq,p_sat,color='red')
ax.plot(v_vap,p_sat,color='green')

# Tune and save the figure into a file
ax.legend()
ax.set_ylim([p_min,p_max]) # bar
ax.set_xlim([1e-3,1e0]) # m^3/kg
ax.set_xlabel(r'$v\,(m^3/kg)$')
ax.set_ylabel(r'$p\,(bar)$')
ax.grid(which='major',color='#CCCCCC',linestyle='-',linewidth=1)
ax.grid(which='minor',color='#CCCCCC',linestyle=':',linewidth=0.5)
ax.set_xscale('log')
ax.set_yscale('log')
plt.savefig('../figs/example-fig-pyromat-pv-isotherms-and-saturation-curve.svg',
            bbox_inches='tight')
plt.close(fig)           





