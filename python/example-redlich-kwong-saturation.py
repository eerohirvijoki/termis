import numpy as np
from scipy.optimize import brentq

# evaluates pressure
def p_func(v,T,R_s,a,b):
    return R_s*T/(v-b)-a/(np.sqrt(T)*v*(v+b))

# finds v larger than b that
# satisfy the equation of state
def v_func(p,T,R_s,a,b):
    coeff=[1,-R_s*T/p,a/(p*np.sqrt(T))-R_s*T*b/p-b**2,-a*b/(p*np.sqrt(T))]
    all_roots=np.roots(coeff)
    return np.sort(all_roots[all_roots>b])

# finds v larger than b for which the
# derivative of pressure with respect to v
# is zero
def dp_dv_zeros_func(T,R_s,a,b):
    coeff=[1, 2*(b-a/(R_s*T**(3/2))),b**2*(1+3*a/(b*R_s*T**(3/2))),
           0,-a*b**3/(R_s*T**(3/2))]
    all_roots=np.roots(coeff)
    return np.sort(all_roots[all_roots>b])

# compute the residual of the Maxwell condition
def delta_func(p_sat,T,R_s,a,b):
    v_liq,_,v_vap=v_func(p_sat,T,R_s,a,b)
    integral=R_s*T*np.log((v_vap-b)/(v_liq-b)) \
        -a/(b*np.sqrt(T))*np.log(v_vap/v_liq*(v_liq+b)/(v_vap+b))
    return p_sat*(v_vap-v_liq)-integral

# solve for the saturation state
# as a function of temperature
def psat_vliq_vvap(T,R_s,a,b):
    v_min,v_max=dp_dv_zeros_func(T,R_s,a,b)
    p_min=p_func(v_min,T,R_s,a,b)
    p_max=p_func(v_max,T,R_s,a,b)
    eps=1e-8
    delta_p=eps*max(abs(p_min),abs(p_max))
    p_lower=max(delta_p,p_min+delta_p)
    p_upper=p_max-delta_p
    p_sat=brentq(f=delta_func,a=p_lower,b=p_upper,args=(T,R_s,a,b))
    v_liq,_,v_vap=v_func(p_sat,T,R_s,a,b)
    return p_sat,v_liq,v_vap

# model specific parameters 
R=8.3145 # J/mol/K
M=44.01 # g/mol
T_c=30.98+273.15 # K
p_c=73.77 # bar
R_s=(0.01*R)/(M*1e-3) # bar*l/kg/K
a=1/(9*(2**(1/3)-1))*R_s**2*T_c**(5/2)/p_c # bar*l^2/kg^2 
b=(2**(1/3)-1)/3*R_s*T_c/p_c # l/kg

# temperature
T=12+273.15 # K

# estimates for the saturation properties
p_sat,v_liq,v_vap=psat_vliq_vvap(T,R_s,a,b) # bar, l/kg, l/kg

# print the results
print(r'    T = {:g} (C)'.format(T-273.15))
print(r'p_sat = {:g} (bar)'.format(p_sat))
print(r'v_liq = {:g} (l/kg)'.format(v_liq))
print(r'v_vap = {:g} (l/kg)'.format(v_vap))

#### This is for plotting the example figure only, not to the notes ####
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator,MultipleLocator)
import pyromat as pm
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
T_crit,p_crit,d_crit=co2.critical(density=True)
T_trp,p_trp=co2.triple()

### p-v diagram ###
fig,ax=plt.subplots(figsize=(6,5))
# figure limits
p_min=30 # bar
p_max=90 # bar
v_min=0.001 # m^3/kg
v_max=0.010 # m^3/kg
# plot the correct isotherm
T=T
p_s=co2.ps(T=T)
v_s_liq,v_s_vap=co2.vs(T=T)
p_low=np.linspace(p_min,p_s,101)
p_high=np.linspace(p_s,p_max,101)
p=np.concatenate((p_low,p_high))
v=np.concatenate((co2.v(p=p_low[:-1],T=T),v_s_vap,v_s_liq,co2.v(p=p_high[1:],T=T)))
ax.plot(v,p,color='black',linewidth=1,label=f'{T-273.15:g}')
# plot the redlich-kwong isotherm and the maxwell construction
v=np.linspace(b*1.01,3*v_vap,501) # l/kg
ax.plot(v*1e-3,p_func(v,T,R_s,a,b),color='black',linestyle='--')
ax.plot([v_liq*1e-3,v_vap*1e-3],[p_sat,p_sat],color='black',linestyle=':')
# plot the saturation curves
T_s=np.linspace(co2.Ts(p=p_min)[0],T_crit,301)
p_s=co2.ps(T=T_s)
v_s_liq,v_s_vap=co2.vs(T=T_s)
ax.plot(v_s_liq,p_s,color='red',linewidth=1.5)
ax.plot(v_s_vap,p_s,color='green',linewidth=1.5)
# set figure labels and grid
line_data = Line2D([0], [0],color="black",linewidth=1)
line_rk = Line2D([0], [0],color="black",linewidth=1,linestyle='--')
line_maxwell = Line2D([0], [0],color="black",linewidth=1,linestyle=':')
line_liq = Line2D([0], [0],color="red",linewidth=2)
line_vap = Line2D([0], [0],color="green",linewidth=2)
ax.legend(handles=[line_data,line_rk,line_maxwell,line_liq,line_vap],labels=[r'Data $T=12^\circ\text{C}$','Redlich-Kwong','Maxwell construct','Saturated liquid','Saturated vapor'],loc='upper center',frameon=False,bbox_to_anchor=(0.5, 1.2),ncol=2)
# set labels and grid, and adjust ranges
ax.set_xlabel(r'$v\,(\text{m}^3/\text{kg})$')
ax.set_ylabel(r'$p\,(\text{bar})$')
ax.set_ylim([p_min,p_max])
ax.set_xlim([v_min,v_max])
ax.grid(which='major',color='#CCCCCC',linestyle='-',linewidth=0.3)
ax.grid(which='minor',color='#CCCCCC',linestyle=':',linewidth=0.1)
ax.yaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_major_locator(MultipleLocator(0.002))
ax.xaxis.set_minor_locator(AutoMinorLocator(4))
ax.yaxis.set_minor_locator(AutoMinorLocator(4))
# save figure
plt.savefig('../figs/example-fig-redlich-kwong-saturation.pdf',bbox_inches='tight')
plt.close(fig)

