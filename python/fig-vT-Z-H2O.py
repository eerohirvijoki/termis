import numpy as np
import pyromat as pm
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator,MultipleLocator)
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

# load substance data
h2o = pm.get('mp.H2O')
T_c, p_c, rho_c = h2o.critical(density=True)
v_c = 1/rho_c
T_trp, p_trp = h2o.triple()
R_s=h2o.R()*1e-2 # bar*m^3/kg/K

# initialize a figure
fig, ax = plt.subplots(figsize=(6, 5))
v_min = 1e-3 # m^3/kg
v_max = 500 # m^3/kg
T_max = 800+273.15 # K 
T_min = 273.16 # K

# Define levels for Z
Z_levels = np.array([0.001,0.01,0.1,
                     0.4,0.7,
                     0.9,0.99,0.999,0.9999])

# calculate the Z-values onto a mesh
nv=1001
nT=1001
v=np.logspace(np.log10(v_min),np.log10(v_max),nv)
T=np.linspace(T_min,T_max,nT)
TT,vv=np.meshgrid(T,v)
pp = h2o.p(T=TT, v=vv)
ZZ=pp*vv/(R_s*TT)

# contour the Z-values
CS=ax.contour(TT-273.15, vv, ZZ, levels=Z_levels, colors='black') # cmap='viridis')
manual_locations = [
    (40, 2e-2),   # 0.001 
    (100, 2e-2),  # 0.01
    (180, 2e-2), # 0.1
    (320, 1e-2), # 0.4
    (440, 1e-2), # 0.7
    (560, 2e-2), # 0.9
    (560, 2e-1), # 0.99
    (560, 2e0), # 0.999
    (560, 2e1), # 0.9999
]
labels=ax.clabel(CS, levels=Z_levels,
                 manual=manual_locations,
                 inline=False, fontsize=9, fmt='%g', use_clabeltext=True)
for label in labels:
    label.set_bbox(dict(facecolor='white',edgecolor='none',pad=0.1))


# plot the saturation curve
T_s = np.linspace(T_trp, T_c, 500)
v_f, v_g = h2o.vs(T=T_s)
ax.plot(T_s - 273.15, v_f, 'r-', lw=2, label='Sat. Liquid')
ax.plot(T_s - 273.15, v_g, 'g-', lw=2, label='Sat. Vapor')

# tune the figure
ax.set_yscale('log')
ax.set_xlim(0, T_max-273.15)
ax.set_ylim(v_min, v_max)
ax.grid(which='major',color='#CCCCCC',linestyle='-',linewidth=0.3)
ax.grid(which='minor',color='#CCCCCC',linestyle='-',linewidth=0.3)
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.set_xlabel(r'$T\,(^\circ\text{C})$')
ax.set_ylabel(r'$v\,(\text{m}^3/\text{kg})$')

# add the contour labels
line_c = Line2D([0], [0],color="black",linewidth=1)
line_liq = Line2D([0], [0],color="red",linewidth=2)
line_vap = Line2D([0], [0],color="green",linewidth=2)
ax.legend(handles=[line_c,line_liq,line_vap],labels=[r'$Z$','Saturated liquid','Saturated vapor'],loc='upper center',frameon=False,bbox_to_anchor=(0.5, 1.08),ncol=3)

# save the figure
fig.savefig('../figs/fig-vT-Z-H2O.svg',bbox_inches='tight')
plt.close(fig)

