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

# Example dictionary for a semi-transparent white box
my_bbox = dict(facecolor='white', edgecolor='none', alpha=0.9, pad=0.5)

# Load data
h2o=pm.get('mp.H2O')

# get critical and triple point information
T_c, p_c, d_c = h2o.critical(density=True)
T_trp, p_trp = h2o.triple()

###########################################
# initialize pv-T figure
###########################################
fig,ax=plt.subplots(figsize=(6,5))
p_min=6e-3 # bar
p_max=1e3 # bar

# temperature curves
T=np.array([5,20,50,100,150,200,250,300,373.95,500,700])+273.15
T_label_xvals=np.array([5e-0,2e-0,4e-1,5e-2,1.5e-2,6e-3,4e-3,3e-3,1.6e-3,4e-3,7e-3])
for Ti in T:
    if Ti < T_c:
        p_s=h2o.ps(T=Ti)
        v_s_liq,v_s_vap=h2o.vs(T=Ti)
        p_low=np.logspace(np.log10(p_trp),np.log10(p_s),101)
        p_high=np.logspace(np.log10(p_s),np.log10(p_max),101)
        p=np.concatenate((p_low,p_high))
        v=np.concatenate((h2o.v(p=p_low[:-1],T=Ti),v_s_vap,v_s_liq,h2o.v(p=p_high[1:],T=Ti)))
    else:
        p=np.logspace(np.log10(p_trp),np.log10(p_max),201)
        v=h2o.v(T=Ti,p=p)
    ax.plot(v,p,color='black',linewidth=1,label=f'{Ti-273.15:g}')

# vapor quality curves
x=np.array([0.01,0.1])
x_label_xvals=np.array([9e-3,8e-2])
for xi in x:
    T=np.linspace(T_trp,T_c-0.001,1001)
    v=h2o.v(T=T,x=xi)
    p=h2o.p(T=T,x=xi)
    ax.plot(v,p,color='black',linestyle='dashed',label=f'{xi:g}',linewidth=1)
    
labelLines(ax.get_lines(),xvals=np.concatenate((T_label_xvals,x_label_xvals)),align=True,fontsize=8,bbox=my_bbox)

# saturation curve
T_s=np.linspace(T_trp,T_c,1001)
p_s=h2o.ps(T=T_s)
v_s_liq,v_s_vap=h2o.vs(T=T_s)
ax.plot(v_s_liq,p_s,color='red',linewidth=2)
ax.plot(v_s_vap,p_s,color='green',linewidth=2)

# set axes
ax.grid(which='major',color='#CCCCCC',linestyle='-',linewidth=0.3)
ax.grid(which='minor',color='#E6E6E6',linestyle='-',linewidth=0.3)
ax.set_ylabel(r'$p\,(\text{bar})$')
ax.set_xlabel(r'$v\,(\text{m}^3/\text{kg})$')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_ylim([p_min,p_max])
line_T = Line2D([0], [0],color="black",linewidth=1)
line_x = Line2D([0], [0],color="black",linewidth=1,linestyle='dashed')
line_liq = Line2D([0], [0],color="red",linewidth=2)
line_vap = Line2D([0], [0],color="green",linewidth=2)
ax.legend(handles=[line_T,line_x,line_liq,line_vap],labels=[r'$T\,(^\circ\text{C})$',r'$x$','Saturated liquid','Saturated vapor'],loc='upper center',frameon=False,bbox_to_anchor=(0.5, 1.08),ncol=4)
plt.savefig('../figs/fig-pv-T-H2O.pdf',bbox_inches='tight')
plt.close(fig)

###########################################
# initialize a vT-p figure
###########################################
fig,ax=plt.subplots(figsize=(6,5))

# pressure isocontours
p=np.array([0.01,0.1,1,10,100,220.64,400,1000]) # bar
p_label_xvals=np.array([70,120,200,300,400,425,450,500])
T_max=273.15+600 # K
for pi in p:
    if pi<p_c:
        T_s=h2o.Ts(p=pi)[0]
        v_s_liq,v_s_vap=h2o.vs(p=pi)
        T_low=np.linspace(T_trp,T_s,101)
        T_high=np.linspace(T_s,T_max,101)
        T=np.concatenate((T_low,T_high))
        v=np.concatenate((h2o.v(T=T_low[:-1],p=pi),v_s_liq,v_s_vap,h2o.v(T=T_high[1:],p=pi)))
    else:
        T=np.linspace(T_trp,T_max,201)
        v=h2o.v(T=T,p=pi)
    ax.plot(T-273.15,v,color='black',linewidth=1,label=f'{pi:g}')

# vapor quality contours
x=np.array([0.01,0.1])
x_label_xvals=np.array([150,150])
for xi in x:
    T=np.linspace(T_trp,T_c,1001)
    v=h2o.v(T=T,x=xi)
    ax.plot(T-273.15,v,color='black',linestyle='dashed',label=f'{xi:g}',linewidth=1)
    
labelLines(ax.get_lines(),xvals=np.concatenate((p_label_xvals,x_label_xvals)),align=True,fontsize=8,bbox=my_bbox)

# saturation curve
T_s=np.linspace(T_trp,T_c,1001)
p_s=h2o.ps(T=T_s)
v_s_liq,v_s_vap=h2o.vs(T=T_s)

ax.plot(T_s-273.15,v_s_liq,color='red',linewidth=2)
ax.plot(T_s-273.15,v_s_vap,color='green',linewidth=2)
ax.grid(which='major',color='#CCCCCC',linestyle='-',linewidth=0.3)
ax.grid(which='minor',color='#E6E6E6',linestyle='-',linewidth=0.3)
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.set_xlabel(r'$T\,(^\circ\text{C})$')
ax.set_ylabel(r'$v\,(\text{m}^3/\text{kg})$')
ax.set_yscale('log')
ax.set_xlim([0,600])
line_p = Line2D([0], [0],color="black",linewidth=1)
line_x = Line2D([0], [0],color="black",linewidth=1,linestyle='dashed')
line_liq = Line2D([0], [0],color="red",linewidth=2)
line_vap = Line2D([0], [0],color="green",linewidth=2)
ax.legend(handles=[line_p,line_x,line_liq,line_vap],labels=[r'$p\,(\text{bar})$',r'$x$','Saturated liquid','Saturated vapor'],loc='upper center',frameon=False,bbox_to_anchor=(0.5, 1.08),ncol=4)
plt.savefig('../figs/fig-vT-p-H2O.pdf',bbox_inches='tight')
plt.close(fig)


###########################################  
# initialize a vT-u figure
###########################################
fig, ax = plt.subplots(figsize=(6, 5))
v_min=1e-3
v_max=1e2
T_min=0+273.15
T_max=600+273.15

# internal energy level sets
v=np.logspace(np.log10(v_min),np.log10(v_max),501)
T=np.linspace(T_trp,T_max,501)
TT,vv=np.meshgrid(T,v)
uu=h2o.e(T=TT,v=vv)
levels=np.array([100,400,800,1300,1900,2500,2600,2700,2800,2900,3000,3100,3200])
CS=ax.contour(TT-273.15,vv,uu,levels=levels,colors='black',linewidths=1)
manual_locations = [
    (23.78, 1e-2),   # 100 
    (94, 1e-2),  # 400
    (175, 1e-2), # 800
    (245, 1e-2), # 1300
    (300, 1e-2), # 1900
    (90, 30), # 2500
    (160, 30), # 2600
    (225, 30), # 2700
    (295, 30), # 2800
    (355, 30), # 2900
    (420, 30), # 3000
    (480, 30), # 3100
    (540, 30), # 3200    
]
clabels = ax.clabel(CS, manual=manual_locations, inline=False, 
                    fontsize=9, fmt='%1.0f', use_clabeltext=True)
for txt in clabels:
    txt.set_bbox(my_bbox)

# Saturation curves
T_s=np.linspace(T_trp, T_c, 500)
v_liq, v_vap = h2o.vs(T=T_s)
ax.plot(T_s-273.15,v_liq,color='red',linewidth=2)
ax.plot(T_s-273.15,v_vap,color='green',linewidth=2)

# Fine-tune the figure
ax.set_yscale('log')
ax.set_xlim(T_min-273.15, T_max-273.15)
ax.set_ylim(v_min, v_max)
ax.grid(which='major',color='#CCCCCC',linestyle='-',linewidth=0.3)
ax.grid(which='minor',color='#E6E6E6',linestyle='-',linewidth=0.3)
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.set_xlabel(r'$T\,(^\circ\text{C})$')
ax.set_ylabel(r'$v\,(\text{m}^3/\text{kg})$')

line_u = Line2D([0], [0],color="black",linewidth=1)
line_liq = Line2D([0], [0],color="red",linewidth=2)
line_vap = Line2D([0], [0],color="green",linewidth=2)
ax.legend(handles=[line_u,line_liq,line_vap],labels=[r'$u\,(\text{kJ}/\text{kg})$','Saturated liquid','Saturated vapor'],loc='upper center',frameon=False,bbox_to_anchor=(0.5, 1.08),ncol=3)

fig.savefig('../figs/fig-vT-u-H2O.pdf',bbox_inches='tight')
plt.close(fig)

########################################################
# initialize the vT-h-figure
########################################################
fig, ax = plt.subplots(figsize=(6, 5))
v_min=1e-3
v_max=1e2
T_min=0+273.15
T_max=600+273.15

# enthalpy level sets
v=np.logspace(np.log10(v_min),np.log10(v_max),501)
T=np.linspace(T_trp,T_max,501)
TT,vv=np.meshgrid(T,v)
hh=h2o.h(T=TT,v=vv)
levels=np.array([100,400,800,1300,1900,2400,2600,2800,3000,3200,3400,3600])
CS=ax.contour(TT-273.15,vv,hh,levels=levels,colors='black',linewidths=1)
manual_locations = [
    (23.78, 1e-2),   # 100 
    (94, 1e-2),  # 400
    (175, 1e-2), # 800
    (245, 1e-2), # 1300
    (300, 1e-2), # 1900
    (420, 3e-3), # 2400
    (480, 4e-3), # 2600
    (540, 4e-3), # 2800
    (160, 30), # 2600
    (55, 30), # 2800
    (280, 30), # 3000
    (360, 30), # 3200
    (460, 30), # 3400
    (550, 30), # 3600
]
clabels = ax.clabel(CS, manual=manual_locations, inline=False, 
                    fontsize=9, fmt='%1.0f', use_clabeltext=True)
for txt in clabels:
    txt.set_bbox(my_bbox)

# Saturation curves
T_s=np.linspace(T_trp, T_c, 500)
v_liq, v_vap = h2o.vs(T=T_s)
ax.plot(T_s-273.15,v_liq,color='red',linewidth=2)
ax.plot(T_s-273.15,v_vap,color='green',linewidth=2)

# Fine-tune and save the figure
ax.set_yscale('log')
ax.set_xlim(T_min-273.15, T_max-273.15)
ax.set_ylim(v_min, v_max)
ax.grid(which='major',color='#CCCCCC',linestyle='-',linewidth=0.3)
ax.grid(which='minor',color='#E6E6E6',linestyle='-',linewidth=0.3)
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.set_xlabel(r'$T\,(^\circ\text{C})$')
ax.set_ylabel(r'$v\,(\text{m}^3/\text{kg})$')

line_h = Line2D([0], [0],color="black",linewidth=1)
line_liq = Line2D([0], [0],color="red",linewidth=2)
line_vap = Line2D([0], [0],color="green",linewidth=2)
ax.legend(handles=[line_h,line_liq,line_vap],labels=[r'$h\,(\text{kJ}/\text{kg})$','Saturated liquid','Saturated vapor'],loc='upper center',frameon=False,bbox_to_anchor=(0.5, 1.08),ncol=3)

fig.savefig('../figs/fig-vT-h-H2O.pdf',bbox_inches='tight')
plt.close(fig)

#####################################################
# initialize a vT-s figure
#####################################################
fig, ax = plt.subplots(figsize=(6, 5))
v_min=1e-3
v_max=1e2
T_min=0+273.15
T_max=600+273.15

# entropy level sets
v=np.logspace(np.log10(v_min),np.log10(v_max),501)
T=np.linspace(T_trp,T_max,501)
TT,vv=np.meshgrid(T,v)
ss=h2o.s(T=TT,v=vv)
levels=np.array([0.5,1.0,1.5,2.0,2.5,3.0,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10])
CS=ax.contour(TT-273.15,vv,ss,levels=levels,colors='black',linewidths=1)
manual_locations = [
    (34.43, 1e-2),   # 0.5 
    (72.6, 1e-2),   # 1 
    (113.3, 1e-2),   # 1.5 
    (154, 1e-2),  # 2
    (193, 1e-2),  # 2.5
    (229, 1e-2), # 3
    (259, 1e-2), # 3.5
    (287, 1e-2), # 4
    (312, 1e-2), # 4.5
    (500, 3e-3), # 5
    (500, 6e-3), # 5.5
    (500, 1.2e-2), # 6
    (500, 3e-2), # 6.5    
    (500, 7e-2), # 7
    (500, 2e-1), # 7.5
    (500, 6e-1), # 8
    (500, 2e-0), # 8.5
    (500, 5e0), # 9
    (500, 1.6e1), # 9.5
    (500, 4.5e1), # 10
]
clabels = ax.clabel(CS, manual=manual_locations,
                    inline=False, 
                    fontsize=9, fmt='%1.1f', use_clabeltext=True)
for txt in clabels:
    txt.set_bbox(my_bbox)

# Saturation curves
T_s=np.linspace(T_trp, T_c, 500)
v_liq, v_vap = h2o.vs(T=T_s)
ax.plot(T_s-273.15,v_liq,color='red',linewidth=2)
ax.plot(T_s-273.15,v_vap,color='green',linewidth=2)

# Fine-tune the figure
ax.set_yscale('log')
ax.set_xlim(T_min-273.15, T_max-273.15)
ax.set_ylim(v_min, v_max)
ax.grid(which='major',color='#CCCCCC',linestyle='-',linewidth=0.3)
ax.grid(which='minor',color='#E6E6E6',linestyle='-',linewidth=0.3)
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.set_xlabel(r'$T\,(^\circ\text{C})$')
ax.set_ylabel(r'$v\,(\text{m}^3/\text{kg})$')

line_s = Line2D([0], [0],color="black",linewidth=1)
line_liq = Line2D([0], [0],color="red",linewidth=2)
line_vap = Line2D([0], [0],color="green",linewidth=2)
ax.legend(handles=[line_s,line_liq,line_vap],labels=[r'$s\,(\text{kJ}/\text{kg}/\text{K})$','Saturated liquid','Saturated vapor'],loc='upper center',frameon=False,bbox_to_anchor=(0.5, 1.08),ncol=3)

fig.savefig('../figs/fig-vT-s-H2O.pdf',bbox_inches='tight')
plt.close(fig)

###################################################
# initialize the ph-T-x figure
###################################################
fig, ax = plt.subplots(figsize=(6, 5))
h_min=0 # kJ/kg
h_max=4000 # kJ/kg
p_min=1e-2 # bar
p_max=1e3 # bar
label_handles=[]
# temperature level sets
T=np.linspace(50,700,14)+273.15 # K
T_label_p=500 # bar
T_label_h=h2o.h(T=T,p=T_label_p) # kJ/kg
for i,Ti in enumerate(T):
    if Ti < T_c:
        p_s=h2o.ps(T=Ti) # bar
        h_s_liq,h_s_vap=h2o.hs(T=Ti) # kJ/kg
        p_vap=np.logspace(np.log10(p_min),np.log10(p_s),101) # bar
        p_liq=np.logspace(np.log10(p_s),np.log10(p_max),101) # bar
        h_vap=h2o.h(p=p_vap[:-1],T=Ti) # kJ/kg
        h_liq=h2o.h(p=p_liq[1:],T=Ti) # kJ/kg
        p=np.concatenate((p_vap,p_liq)) # bar
        h=np.concatenate((h_vap,h_s_vap,h_s_liq,h_liq)) # kJ/kg
    else:
        p=np.logspace(np.log10(p_min),np.log10(p_max),201) # bar
        h=h2o.h(p=p,T=Ti) # kJ/kg
    # plotting twice to make sure the segment where the label is attached is single-valued
    handle,=ax.plot(h[p>T_label_p-100],p[p>T_label_p-100],color='black', linewidth=0.9,label=f'{Ti-273.15:g}')
    label_handles.append(handle)
    ax.plot(h,p,color='black',linewidth=0.9)

# vapor quality and saturation curves
T_s=np.linspace(T_trp, T_c-0.001, 500)
p_s=h2o.ps(T=T_s) # bar
x=np.linspace(0.1,0.9,9)
x_label_p=0.05
x_label_h=h2o.h(x=x,p=x_label_p)
for xi in x:
    h=h2o.h(T=T_s,x=xi)
    handle,=ax.plot(h,p_s,color='black',linestyle='--',linewidth=0.9, label=f'{xi:g}')
    label_handles.append(handle)

label_h_vals=np.concatenate((T_label_h,x_label_h))
labelLines(label_handles, align=True, xvals=label_h_vals, fontsize=9,bbox=my_bbox)
    
# Saturation curves
h_liq, h_vap = h2o.hs(T=T_s)
ax.plot(h_liq,p_s,color='red',linewidth=2)
ax.plot(h_vap,p_s,color='green',linewidth=2)

# fine tune and save the figure
ax.set_yscale('log')
ax.set_xlim(h_min, h_max)
ax.set_ylim(p_min, p_max)
ax.grid(which='major',color='#CCCCCC',linestyle='-',linewidth=0.3)
ax.grid(which='minor',color='#E6E6E6',linestyle='-',linewidth=0.3)
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.set_xlabel(r'$h\,(\text{kJ}/\text{kg})$')
ax.set_ylabel(r'$p\,(\text{bar})$')

line_T = Line2D([0], [0],color="black",linewidth=1)
line_x = Line2D([0], [0],color="black",linewidth=1, linestyle='--')
line_liq = Line2D([0], [0],color="red",linewidth=2)
line_vap = Line2D([0], [0],color="green",linewidth=2)
ax.legend(handles=[line_T,line_x,line_liq,line_vap],labels=[r'$T\,(^\circ\text{C})$',r'$x$','Saturated liquid','Saturated vapor'],loc='upper center',frameon=False,bbox_to_anchor=(0.5, 1.08),ncol=4)

fig.savefig('../figs/fig-ph-T-x-H2O.pdf',bbox_inches='tight')
plt.close(fig)

###################################################
# initialize the Ts-p-h figure
###################################################
fig, ax = plt.subplots(figsize=(6, 5))
p_min=0.02 # bar
p_max=2000 # bar
T_min=0+273.15 # K
T_max=800+273.15 # K
s_min=0 # kJ/kg/K
s_max=12.0 # kJ/kg/K
label_handles=[]

# pressure level sets
p=np.array([0.01,0.02,0.05,0.1,0.2, 0.5,1.0,2, 5,10,20, 50,100,200, 500,1000,2000,5000]) # bar
p_label_T=760+273.15 # K
p_label_s=h2o.s(p=p,T=p_label_T) # kJ/kg
for i,pi in enumerate(p):
    if pi < p_c:
        T_s=h2o.Ts(p=pi)[0] # K
        s_s_liq,s_s_vap=h2o.ss(T=T_s)
        T_low=np.linspace(T_trp,T_s,101)
        T_high=np.linspace(T_s,T_max,101)
        T=np.concatenate((T_low,T_high))
        s=np.concatenate((h2o.s(T=T_low[:-1],p=pi),s_s_liq,s_s_vap,h2o.s(T=T_high[1:],p=pi)))
    else:
        T=np.linspace(T_trp,T_max,201)
        s=h2o.s(T=T,p=pi)
    handle,=ax.plot(s,T-273.15,color='black',linewidth=1,label=f'{pi:g}')
    label_handles.append(handle)
 
# vapor quality and saturation curves
T_s=np.linspace(T_trp, T_c-0.001, 500)
x=np.linspace(0.1,0.9,9)
x_label_T=100+273.15 # K
x_label_s=h2o.s(x=x,T=x_label_T)
for xi in x:
    s=h2o.s(T=T_s,x=xi)
    handle,=ax.plot(s,T_s-273.15,color='black',linestyle='--',linewidth=0.9, label=f'{xi:g}')
    label_handles.append(handle)

label_s_vals=np.concatenate((p_label_s,x_label_s))
labelLines(label_handles, align=True, xvals=label_s_vals, fontsize=9,bbox=my_bbox)
    
# Saturation curves
s_liq, s_vap = h2o.ss(T=T_s)
ax.plot(s_liq,T_s-273.15,color='red',linewidth=2)
ax.plot(s_vap,T_s-273.15,color='green',linewidth=2)

# fine tune and save the figure
ax.set_xlim([s_min,s_max])
ax.set_ylim([T_min-273.15, T_max-273.15])
ax.grid(which='major',color='#CCCCCC',linestyle='-',linewidth=0.3)
ax.grid(which='minor',color='#E6E6E6',linestyle='-',linewidth=0.3)
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.set_xlabel(r'$s\,(\text{kJ}/\text{kg}/\text{K})$')
ax.set_ylabel(r'$T\,(^\circ\text{C})$')

line_p = Line2D([0], [0],color="black",linewidth=1)
line_x = Line2D([0], [0],color="black",linewidth=1, linestyle='--')
line_liq = Line2D([0], [0],color="red",linewidth=2)
line_vap = Line2D([0], [0],color="green",linewidth=2)
ax.legend(handles=[line_T,line_x,line_liq,line_vap],labels=[r'$p\,(\text{bar})$',r'$x$','Saturated liquid','Saturated vapor'],loc='upper center',frameon=False,bbox_to_anchor=(0.5, 1.08),ncol=4)
    
fig.savefig('../figs/fig-Ts-p-H2O.pdf',bbox_inches='tight')
plt.close(fig)


