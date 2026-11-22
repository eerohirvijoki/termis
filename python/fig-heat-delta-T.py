import numpy as np
import pyromat as pm
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator,MultipleLocator)
from matplotlib.lines import Line2D
from labellines import labelLines

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "text.latex.preamble": r"""
        \usepackage{amsmath} 
        \usepackage{amssymb}
    """
})

h2o=pm.get('mp.H2O')
T_c,p_c=h2o.critical()

# temperatures and number of steps
T_min=273.15+0.02 # K
T_max=273.15+800 # K
N=501

# constant volume heatin Q/m=Delta u
fig,ax=plt.subplots(figsize=(6,5))
v=np.array([1e-3,1e-2,1e-1,1.0,10.0]) # m^3/kg
v_label_xvals=np.ones(v.shape)*1500
for vx in v:
    T=np.linspace(T_min,T_max,2*N) # K
    u=h2o.e(T=T,v=vx) # kJ/kg
    ax.plot(u-u[0],T-273.15,label=f'{vx:g}',color='black')
labelLines(ax.get_lines(),xvals=v_label_xvals,
           align=True,fontsize=8)
ax.grid(which='major',color='#CCCCCC',linestyle='-',linewidth=1)
ax.grid(which='minor',color='#CCCCCC',linestyle=':',linewidth=0.5)
ax.xaxis.set_major_locator(MultipleLocator(500))
ax.yaxis.set_major_locator(MultipleLocator(100))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.set_xlabel(r'$Q/m\,(\text{kJ}/\text{kg})$')
ax.set_ylabel(r'$T\,(^\circ\text{C})$')
ax.set_xlim([0,4000])
ax.set_ylim([0,T_max-273.15])
line = Line2D([0], [0],color='black',linewidth=1)
ax.legend(handles=[line],labels=[r'$v\,(\text{m}^3/\text{kg})$'],loc='upper center',frameon=False,bbox_to_anchor=(0.5, 1.08),ncol=1)
plt.savefig('../figs/fig-heat-delta-T-isochoric.svg',bbox_inches='tight')
plt.close(fig)

# constant pressure heating Q/m=Delta h
fig,ax=plt.subplots(figsize=(6,5))
p=np.array([0.1,10,100,300,1000]) # bar
p_label_xvals=np.array([1500,1750,2000,2000,2000])
for px in p:
    if px < p_c:
        T_sat=h2o.Ts(p=px)[0] # K 
        h_liq,h_vap=h2o.hs(T=T_sat) # kJ/kg
        T_low=np.linspace(T_min,T_sat,N) # K
        T_high=np.linspace(T_sat,T_max,N) # K
        T=np.concatenate((T_low,T_high)) # K
        h=np.concatenate((h2o.h(T=T_low[:-1],p=px),h_liq,h_vap,h2o.h(T=T_high[1:],p=px))) # kJ/kg
    else:
        T=np.linspace(T_min,T_max,2*N) # K
        h=h2o.h(T=T,p=px) # kJ/kg 
    ax.plot(h-h[0],T-273.15,label=f'{px:g}',color='black')
labelLines(ax.get_lines(),xvals=p_label_xvals,align=True,fontsize=8)
ax.grid(which='major',color='#CCCCCC',linestyle='-',linewidth=1)
ax.grid(which='minor',color='#CCCCCC',linestyle=':',linewidth=0.5)
ax.xaxis.set_major_locator(MultipleLocator(500))
ax.yaxis.set_major_locator(MultipleLocator(100))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.set_xlabel(r'$Q/m\,(\text{kJ}/\text{kg})$')
ax.set_ylabel(r'$T\,(^\circ\text{C})$')
ax.set_xlim([0,4500])
ax.set_ylim([0,T_max-273.15])
line = Line2D([0], [0],color='black',linewidth=1)
ax.legend(handles=[line],labels=[r'$p\,(\text{bar})$'],loc='upper center',frameon=False,bbox_to_anchor=(0.5, 1.08),ncol=1)
plt.savefig('../figs/fig-heat-delta-T-isobaric.svg',bbox_inches='tight')
plt.close(fig)




