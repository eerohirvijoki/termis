import numpy as np
import pyromat as pm
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator,MultipleLocator)
from labellines import labelLines
from matplotlib.lines import Line2D
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "text.latex.preamble": r"""
        \usepackage{amsmath} 
        \usepackage{amssymb}
    """
})


co2=pm.get('mp.CO2')
T_c,p_c,d_c=co2.critical(density=True)
T_trp,p_trp=co2.triple()

### p-v diagram ###
fig,ax=plt.subplots(figsize=(6,5))

p_min=p_c-40
p_max=p_c+40
T=np.array([12,30.98,50])+273.15
for Ti in T:
    if Ti < T_c:
        p_s=co2.ps(T=Ti)
        v_s_liq,v_s_vap=co2.vs(T=Ti)
        p_low=np.linspace(p_min,p_s,101)
        p_high=np.linspace(p_s,p_max,101)
        p=np.concatenate((p_low,p_high))
        v=np.concatenate((co2.v(p=p_low[:-1],T=Ti),v_s_vap,v_s_liq,co2.v(p=p_high[1:],T=Ti)))
    else:
        p=np.linspace(p_min,p_max,1001)
        v=co2.v(T=Ti,p=p)
    ax.plot(v,p,color='black',linewidth=1,label=f'{Ti-273.15:g}')
    
# Van der Waals
R=8.3145 # J/mol/K
M=co2.mw() # g/mol
R_s=R/(M*1e-3) # J/kg/K
a_svdw=27/64*R_s**2*T_c**2/(p_c*1e5) # SI-units
b_svdw=R_s*T_c/(8*p_c*1e5) # SI-units
a_sdtr=4*np.exp(-2)*R_s**2*T_c**2/(p_c*1e5) # SI-units
b_sdtr=np.exp(-2)*R_s*T_c/(p_c*1e5) # SI-units
a_srk=1/(9*(2**(1/3)-1))*R_s**2*T_c**(5/2)/(p_c*1e5) # SI-units
b_srk=(2**(1/3)-1)/3*R_s*T_c/(p_c*1e5) # SI-units
def vdw(v,T):
    return (R_s*T/(v-b_svdw)-a_svdw/v**2)*1e-5 # bar
def dietericci(v,T):
    return R_s*T/(v-b_sdtr)*np.exp(-a_sdtr/(v*R_s*T))*1e-5 # bar
def ideal(v,T):
    return R_s*T/v*1e-5 # bar
def redlichkwong(v,T):
    return (R_s*T/(v-b_srk)-a_srk/(np.sqrt(T)*v*(v+b_srk)))*1e-5 # bar


v=np.linspace(0.0012,0.02,1001)
for Ti in T:
    p_vdw=vdw(v,Ti)
    p_ideal=ideal(v,Ti)
    p_rk=redlichkwong(v,Ti)
    #ax.plot(v,p_vdw,color='black',linewidth=1,label=f'{Ti-273.15:g}',linestyle='--')
    ax.plot(v,p_ideal,color='black',linewidth=1,label=f'{Ti-273.15:g}',linestyle='-.')
    ax.plot(v,p_rk,color='black',linewidth=1,linestyle='--')

labelLines(
    ax.get_lines(),
    xvals=np.ones(6)*0.01,
    align=True,
    fontsize=10
)

T_s=np.linspace(co2.Ts(p=p_min)[0],T_c,301)
p_s=co2.ps(T=T_s)
v_s_liq,v_s_vap=co2.vs(T=T_s)
ax.plot(v_s_liq,p_s,color='red',linewidth=1.5)
ax.plot(v_s_vap,p_s,color='green',linewidth=1.5)


# set axes
ax.grid(which='major',color='#CCCCCC',linestyle='-',linewidth=0.3)
ax.grid(which='minor',color='#CCCCCC',linestyle=':',linewidth=0.1)
ax.xaxis.set_minor_locator(AutoMinorLocator(4))
ax.yaxis.set_minor_locator(AutoMinorLocator(4))
ax.yaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_major_locator(MultipleLocator(0.002))
ax.set_ylabel(r'$p\,(\text{bar})$')
ax.set_xlabel(r'$v\,(\text{m}^3/\text{kg})$')
ax.set_ylim([p_min,p_max])
ax.set_xlim([0.001,0.015])

# annotations
line_data = Line2D([0], [0],color="black",linewidth=1)
line_rk = Line2D([0], [0],color="black",linewidth=1,linestyle='--')
line_ideal = Line2D([0], [0],color="black",linewidth=1,linestyle='-.')
line_liq = Line2D([0], [0],color="red",linewidth=2)
line_vap = Line2D([0], [0],color="green",linewidth=2)
ax.legend(handles=[line_data,line_rk,line_ideal,line_liq,line_vap],labels=[r'Data $T\,(^\circ\text{C})$','Redlich-Kwong equation','Ideal gas equation','Saturated liquid','Saturated vapor'],loc='upper center',frameon=False,bbox_to_anchor=(0.5, 1.2),ncol=2)
plt.savefig('../figs/fig-pv-T-CO2-eos-comparison.pdf',dpi=600,bbox_inches='tight')
plt.close(fig)


