import pyromat as pm

# Critical point data for carbon dioxide
co2=pm.get('mp.CO2')
T_c_CO2,p_c_CO2,rho_c_CO2=co2.critical(density=True) # K, bar, kg/m^3

# requested state for carbon dioxide
T_CO2=20+273.15 # K
rho_CO2=230 # kg/m^3
    
# reduced variables according to carbon dioxide state
T_r=T_CO2/T_c_CO2 # dimensionless
rho_r=rho_CO2/rho_c_CO2 # dimensionless

# Data for methane
ch4=pm.get('mp.CH4')
T_c_CH4,p_c_CH4,rho_c_CH4=ch4.critical(density=True) # K, bar, kg/m^3

# corresponding state temperature, volume, and pressure for methane
T_CH4=T_r*T_c_CH4 # K
rho_CH4=rho_r*rho_c_CH4 # kg/m^3
p_CH4=ch4.p(T=T_CH4,d=rho_CH4)[0] # bar

# reduced pressure according to methane
p_r=p_CH4/p_c_CH4 # dimensionless 

# estimate for the carbon dioxide pressure
p_CO2=p_r*p_c_CO2 # bar

# accurate value for carbon dioxide density
p_CO2_acc=co2.p(T=T_CO2,d=rho_CO2)[0] # bar

# ideal gas estimate for carbon dioxide density
R_s=co2.R()*1e-2 # bar*m^3/kg/K
p_CO2_ideal=rho_CO2*R_s*T_CO2 # bar

# print results for comparison
print(f'p_CO2 (corr. state value) = {p_CO2:g} (bar)')
print(f'p_CO2 (accurate value)    = {p_CO2_acc:g} (bar)')
print(f'p_CO2 (ideal gas value)   = {p_CO2_ideal:g} (bar)')
