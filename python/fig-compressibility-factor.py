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

fig,ax=plt.subplots(figsize=(6,5))
names=[r'$T_r\,(\text{CH}_4)$',r'$T_r\,(\text{N}_2)$',r'$T_r\,(\text{CO}_2)$']#,r'$T_r\,(\text{N}_2)$']
keys=['mp.CH4','mp.N2','mp.CO2']
colors=['blue','red','green']

for i,key in enumerate(keys):
    substance=pm.get(key)
    T_c,p_c=substance.critical() # K, bar
    print(T_c-273.15,p_c)
    R_s=substance.R() # 
    T_min,T_max=substance.Tlim()
    p_min,p_max=substance.plim()
    T_rmin=T_min/T_c; T_rmax=T_max/T_c
    p_rmin=p_min/p_c; p_rmax=p_max/p_c
    print(p_rmin,p_rmax)
    print(T_rmin,T_rmax)
    T_r=np.array([0.8,1.0,1.4,2.0,3.0])
    p_r=np.logspace(np.log10(0.1),np.log10(10),201)
    for j,T_ri in enumerate (T_r):
        v=substance.v(T=T_ri*T_c,p=p_r*p_c)
        Z=p_r*p_c*1e2*v/(R_s*T_ri*T_c)
        ax.plot(p_r,Z,color=colors[i],label=f'{T_ri:g}',linewidth=1)

labelLines(
    ax.get_lines(),
    align=True,
    fontsize=9
)

line_0 = Line2D([0], [0],color=colors[0],linewidth=1)
line_1 = Line2D([0], [0],color=colors[1],linewidth=1)
line_2 = Line2D([0], [0],color=colors[2],linewidth=1)
ax.legend(handles=[line_0,line_1,line_2
                   ],labels=names,loc='upper center',frameon=False,bbox_to_anchor=(0.5, 1.08),ncol=3)

ax.grid(which='major',color='#CCCCCC',linestyle='-',linewidth=1)
ax.grid(which='minor',color='#CCCCCC',linestyle=':',linewidth=0.5)
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(0.2))
ax.xaxis.set_minor_locator(AutoMinorLocator(4))
ax.yaxis.set_minor_locator(AutoMinorLocator(4))
ax.set_xlim([0,7])
ax.set_xlabel(r'$p_r$')
ax.set_ylabel(r'$Z$')
plt.savefig('../figs/fig-compressibility-factor.svg',bbox_inches='tight')
plt.close(fig)
    



