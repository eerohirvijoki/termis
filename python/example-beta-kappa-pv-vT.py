import numpy as np
import pyromat as pm
pm.config['unit_pressure']='bar' 
pm.config['unit_energy']='kJ'    
pm.config['unit_molar']='kmol'   
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

fig,ax=plt.subplots(figsize=(6,5))
h2o=pm.get('mp.H2O')
T_c,p_c= h2o.critical()
T=np.array([370,372,374,376,378,380,382])+273.15 # K
T_label_xvalues=np.array([4.8,4.9,5.0,5.13,5.27,5.4,5.55])*1e-3
p_min=210
p_max=230
for Ti in T:
    if Ti < T_c:
        p_sat=h2o.ps(Ti)
        v_liq,v_vap=h2o.vs(T=Ti)
        p_high=np.linspace(p_sat,p_max,201)
        p_low=np.linspace(p_min,p_sat,201)
        p=np.concatenate((p_low,p_high))
        v=np.concatenate((h2o.v(p=p_low[:-1],T=Ti),v_vap,
                          v_liq,h2o.v(p=p_high[1:],T=Ti)))
    else:
        p=np.linspace(p_min,p_max,401)
        v=h2o.v(p=p,T=Ti)
    ax.plot(v,p,color='black',label=f'{Ti-273.15:g}')
  
labelLines(
    ax.get_lines(),
    xvals=T_label_xvalues,
    align=True,
    fontsize=10
)

T=np.linspace(h2o.Ts(p=p_min)[0],T_c,301)
p_sat=h2o.ps(T=T)
v_liq,v_vap=h2o.vs(T=T) # m^3/kg
ax.plot(v_liq,p_sat,color='red')
ax.plot(v_vap,p_sat,color='green')

# slope
px=225
Tx=376+273.15
vx=h2o.v(T=Tx,p=px)[0]
dp=0.01
dv=h2o.v(T=Tx,p=px+dp)[0]-vx
p0=px-200*dp
p1=px+200*dp
v0=vx-200*dv
v1=vx+200*dv
ax.plot([v0,v1],[p0,p1],color='blue')
ax.plot([v0,v1],[p0,p0],color='blue')
ax.plot([v1,v1],[p0,p1],color='blue')
ax.plot(vx,px,marker='o',linestyle='',color='blue',markersize=3)
print('pv-diagram')
print(f'delta_p = {abs(400*dp):g} (bar)')
print(f'delta_v = {abs(400*dv):g} (m^3/kg)')


line_T = Line2D([0], [0],color="black",linewidth=1)
line_liq = Line2D([0], [0],color="red",linewidth=2)
line_vap = Line2D([0], [0],color="green",linewidth=2)
ax.legend(handles=[line_T,line_liq,line_vap],labels=[r'$T\,(^\circ\text{C})$','Saturated liquid','Saturated vapor'],loc='upper center',frameon=False,bbox_to_anchor=(0.5, 1.1),ncol=3)


ax.set_xlabel(r'$v\,(\text{m}^3/\text{kg})$')
ax.set_ylabel(r'$p\,(\text{bar})$')
ax.set_ylim([p_min,p_max])
ax.set_xlim([0.002,0.006])
ax.grid(which='major',color='#CCCCCC',linestyle='-',linewidth=1)
ax.grid(which='minor',color='#CCCCCC',linestyle=':',linewidth=0.5)
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.xaxis.set_major_locator(MultipleLocator(0.001))
ax.xaxis.set_minor_locator(AutoMinorLocator(10))
ax.yaxis.set_minor_locator(AutoMinorLocator(10))
plt.savefig('../figs/example-fig-kappa-pv.pdf',bbox_inches='tight')
plt.close(fig)

# vT diagram
fig,ax=plt.subplots(figsize=(6,5))
p=np.array([215,220,225,230,235,240]) # bar
T_min=370 # C
T_max=380 # C
for pi in p:
    if pi < p_c:
        T_sat=h2o.Ts(p=pi)[0]
        v_liq,v_vap=h2o.vs(T=T_sat)
        T_high=np.linspace(T_sat,T_max+273.15,201)
        T_low=np.linspace(T_min+273.15,T_sat,201)
        T=np.concatenate((T_low,T_high))
        v=np.concatenate((h2o.v(T=T_low[:-1],p=pi),v_liq,
                          v_vap,h2o.v(T=T_high[1:],p=pi)))
    else:
        T=np.linspace(T_min,T_max,401)+273.15
        v=h2o.v(p=pi,T=T)
    ax.plot(T-273.15,v,color='black',label=f'{pi:g}')
  
labelLines(
    ax.get_lines(),
    #xvals=T_label_xvalues,
    align=True,
    fontsize=10
)

T=np.linspace(T_min+273.15,T_c,301)
v_liq,v_vap=h2o.vs(T=T) # m^3/kg
ax.plot(T-273.15,v_liq,color='red')
ax.plot(T-273.15,v_vap,color='green')

# slope
px=225
Tx=376+273.15
vx=h2o.v(T=Tx,p=px)[0]
dT=0.01
dv=h2o.v(T=Tx+dT,p=px)[0]-vx
T0=Tx-100*dT
T1=Tx+100*dT
v0=vx-100*dv
v1=vx+100*dv
ax.plot([T0-273.15,T1-273.15],[v0,v1],color='blue')
ax.plot([T0-273.15,T1-273.15],[v0,v0],color='blue')
ax.plot([T1-273.15,T1-273.15],[v0,v1],color='blue')
ax.plot(Tx-273.15,vx,marker='o',linestyle='',color='blue',markersize=3)
deltaT=abs(100*dT)
deltav=abs(100*dv)
print('vT-diagram')
print(f'delta_T = {abs(200*dT):g} (C)')
print(f'delta_v = {abs(200*dv):g} (m^3/kg)')


line_p = Line2D([0], [0],color="black",linewidth=1)
line_liq = Line2D([0], [0],color="red",linewidth=2)
line_vap = Line2D([0], [0],color="green",linewidth=2)
ax.legend(handles=[line_T,line_liq,line_vap],labels=[r'$p\,(\text{bar})$','Saturated liquid','Saturated vapor'],loc='upper center',frameon=False,bbox_to_anchor=(0.5, 1.1),ncol=3)

ax.set_ylabel(r'$v\,(\text{m}^3/\text{kg})$')
ax.set_xlabel(r'$T\,(^\circ\text{C})$')
ax.set_xlim([T_min,T_max])
ax.set_ylim([0.002,0.006])
ax.grid(which='major',color='#CCCCCC',linestyle='-',linewidth=1)
ax.grid(which='minor',color='#CCCCCC',linestyle=':',linewidth=0.5)
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(0.001))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(10))
plt.savefig('../figs/example-fig-beta-vT.pdf',bbox_inches='tight')
plt.close(fig)
