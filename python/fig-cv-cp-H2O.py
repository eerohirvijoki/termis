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

# --- Setup Pyromat and Constants ---
h2o = pm.get('mp.H2O')
T_c, p_c, rho_c = h2o.critical(density=True)
v_c = 1/rho_c
T_trp, p_trp = h2o.triple()

fig_cv, ax_cv = plt.subplots(figsize=(6, 5))
fig_cp, ax_cp = plt.subplots(figsize=(6, 5))

# Define global levels for Cv so the lines match across regions
cv_levels = np.array([1.5, 1.6, 1.7, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.4])
cp_levels = np.array([1.9, 2.0, 2.1, 2.2, 2.3, 2.5, 3.1, 4.0, 6.0, 11])
v_min = 1e-3
v_max = 500
T_max = 800+273.15

# =========================================================
# 2. SUPERHEATED VAPOR (Boundary-Fitted Mesh)
# =========================================================
# T from Triple to Critical (fitting to the curve)
T_sh = np.linspace(T_trp, T_c, 201)
_, v_g_nodes = h2o.vs(T=T_sh)

# Create a normalized grid: eta=0 is saturation, eta=1 is v_max
eta = np.linspace(0.001, 1, 501)
TT_sh, ETA_sh = np.meshgrid(T_sh, eta)

# Exponential spacing from v_g to v_max
vv_sh = v_g_nodes * (v_max / v_g_nodes)**ETA_sh

# Calculate Cv
pp_sh = h2o.p(T=TT_sh, v=vv_sh)
cv_sh = h2o.cv(T=TT_sh, p=pp_sh)
cp_sh = h2o.cp(T=TT_sh, p=pp_sh)

# cv for superheated vapor domain
CS=ax_cv.contour(TT_sh - 273.15, vv_sh, cv_sh, levels=cv_levels, colors='black') #cmap='viridis')
cv_levels_sh=np.array([1.5,1.6])
manual_locations = [
    (175, 1.7),   # 1.5 
    (275, 0.3),  # 1.6 
]
ax_cv.clabel(CS, levels=cv_levels_sh, manual=manual_locations, 
          inline=True, fontsize=9, fmt='%1.1f', use_clabeltext=True)

# cp for superheated vapor domain
CS=ax_cp.contour(TT_sh - 273.15, vv_sh, cp_sh, levels=cp_levels, colors='black') #cmap='viridis')
cp_levels_sh=np.array([1.9,2.0,2.1])
manual_locations = [
    (100, 30),   # 1.9 
    (200, 1.3),  # 2.0
    (300, 0.3),  # 2.1
]
ax_cp.clabel(CS, levels=cp_levels_sh, manual=manual_locations, inline_spacing=5,
         inline=True, fontsize=9, fmt='%1.1f', use_clabeltext=True)


# =========================================================
# 3. SUPERCRITICAL REGION (Standard Grid)
# =========================================================
# Above T_c, the dome doesn't exist, so we use a simple rectangle
T_sc = np.linspace(T_c, T_max, 501)
v_sc = np.geomspace(v_min, v_max, 201)
TT_sc, vv_sc = np.meshgrid(T_sc, v_sc)

pp_sc = h2o.p(T=TT_sc, v=vv_sc)
cv_sc = h2o.cv(T=TT_sc, p=pp_sc)
cp_sc = h2o.cp(T=TT_sc, p=pp_sc)

# cv for T>T_c
CS=ax_cv.contour(TT_sc - 273.15, vv_sc, cv_sc, levels=cv_levels, colors='black') #cmap='viridis')
#cv_levels_sc = np.array([1.7, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.4])
manual_locations = [
    (400, 0.1),   # 1.7 
    (475, 0.05),  # 1.8
    (550, 0.015), # 2.0
    (600, 8e-3), # 2.2
    (650, 3e-3), # 2.4
    (700, 1e-3), # 2.6
    (450, 2e-3), # 2.8
    (425, 3e-3), # 3.0
    (385, 6e-3), # 3.4
]

# For some reason matplotlib throws a tantrum if I try to give it correct labels
ax_cv.clabel(CS, #cv_levels_sc,
             manual=manual_locations, inline_spacing=0.9,
             inline=True, fontsize=9, fmt='%1.1f', use_clabeltext=True)

# cp for T>T_c
CS=ax_cp.contour(TT_sc - 273.15, vv_sc, cp_sc, levels=cp_levels, colors='black') #cmap='viridis')
#cp_levels_sc = np.array([2.2, 2.3, 2.5, 3.1, 4.0, 6.0, 11])
manual_locations = [
    (425, 0.15),  # 2.2
    (475, 8e-2), # 2.3
    (535, 4e-2), # 2.5
    (600, 1.3e-2), # 3.1
    (625, 6e-3), # 4.0
    (500, 2e-3), # 6.0
    (415, 2.3e-3), # 10.0
]
ax_cp.clabel(CS, #levels=cp_levels_sc,
             manual=manual_locations, inline_spacing=2,
             inline=True, fontsize=9, fmt='%1.1f', use_clabeltext=True)

# =========================================================
# 2. SUPERHEATED VAPOR (Boundary-Fitted Mesh)
# =========================================================
# T from Triple to Critical (fitting to the curve)
T_sl = np.linspace(T_trp, T_c, 201)
v_l_nodes, _  = h2o.vs(T=T_sl)

# Create a normalized grid: eta=0 is saturation, eta=1 is v_max
eta = np.linspace(0, 0.999, 201)
TT_sl, ETA_sl = np.meshgrid(T_sl, eta)

# Exponential spacing from v_min to v_l
vv_sl = v_min * (v_l_nodes/v_min)**ETA_sl

# Calculate Cv
pp_sl = h2o.p(T=TT_sl, v=vv_sl)
cv_sl = h2o.cv(T=TT_sl, p=pp_sl)
cp_sl = h2o.cp(T=TT_sl, p=pp_sl)

# Since this is a structured grid now, we use standard contour!
ax_cv.contour(TT_sl - 273.15, vv_sl, cv_sl, levels=cv_levels, colors='black') #cmap='viridis')
ax_cp.contour(TT_sl - 273.15, vv_sl, cp_sl, levels=cp_levels, colors='black') #cmap='viridis')

# =========================================================
# 4. SATURATION CURVES & FORMATTING
# =========================================================
T_s = np.linspace(T_trp, T_c, 500)
v_f, v_g = h2o.vs(T=T_s)

ax_cv.plot(T_s - 273.15, v_f, 'r-', lw=2, label='Sat. Liquid')
ax_cv.plot(T_s - 273.15, v_g, 'g-', lw=2, label='Sat. Vapor')
ax_cv.set_yscale('log')
ax_cv.set_xlim(0, T_max-273.15)
ax_cv.set_ylim(v_min, v_max)
ax_cv.grid(which='major',color='#CCCCCC',linestyle='-',linewidth=0.3)
ax_cv.grid(which='minor',color='#CCCCCC',linestyle='-',linewidth=0.3)
ax_cv.xaxis.set_minor_locator(AutoMinorLocator(5))
ax_cv.set_xlabel(r'$T\,(^\circ\text{C})$')
ax_cv.set_ylabel(r'$v\,(\text{m}^3/\text{kg})$')

ax_cp.plot(T_s - 273.15, v_f, 'r-', lw=2, label='Sat. Liquid')
ax_cp.plot(T_s - 273.15, v_g, 'g-', lw=2, label='Sat. Vapor')

ax_cp.set_yscale('log')
ax_cp.set_xlim(0, T_max-273.15)
ax_cp.set_ylim(v_min, v_max)
ax_cp.grid(which='major',color='#CCCCCC',linestyle='-',linewidth=0.3)
ax_cp.grid(which='minor',color='#CCCCCC',linestyle='-',linewidth=0.3)
ax_cp.xaxis.set_minor_locator(AutoMinorLocator(5))
ax_cp.set_xlabel(r'$T\,(^\circ\text{C})$')
ax_cp.set_ylabel(r'$v\,(\text{m}^3/\text{kg})$')

line_c = Line2D([0], [0],color="black",linewidth=1)
line_liq = Line2D([0], [0],color="red",linewidth=2)
line_vap = Line2D([0], [0],color="green",linewidth=2)
ax_cv.legend(handles=[line_c,line_liq,line_vap],labels=[r'$c_v\,(\text{kJ}/\text{kg}/\text{K})$','Saturated liquid','Saturated vapor'],loc='upper center',frameon=False,bbox_to_anchor=(0.5, 1.08),ncol=4)
ax_cp.legend(handles=[line_c,line_liq,line_vap],labels=[r'$c_p\,(\text{kJ}/\text{kg}/\text{K})$','Saturated liquid','Saturated vapor'],loc='upper center',frameon=False,bbox_to_anchor=(0.5, 1.08),ncol=4)


fig_cv.savefig('../figs/fig-cv-H2O.svg',bbox_inches='tight')
fig_cp.savefig('../figs/fig-cp-H2O.svg',bbox_inches='tight')
plt.close(fig_cv)
plt.close(fig_cp)

