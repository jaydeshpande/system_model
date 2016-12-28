#  Program aims to study relative efficiencies of desal techniques
#---------------------------
# Define fixed parameters (Geometrical) 
from math import sqrt as sqrt
from calculate_psat import * 
from calculated_diffusivity import *
from calculate_activity_factor import *
#---------------------------
L=0.07 # Length of the module 
dx=0.022 # Flow channel width 
B=0.006 # Height of the module
dm=0.000160 # m Thickness of membrane 
da=0.003 # m Thickness of airgap
dp=0.0015 # m thickness of coolant plate
salinity=0.075 # g/kg salinity in the feed
#---------------------------
# Hydraulic diameter, Dh
Dh = (2*dx*B)/(dx+B)
#---------------------------
# Calculate the membrane diffusivity 
#---------------------------
eta=0.9
xeta=1.1
Mv=18.0
R=8314.4598
diff = 0.000035
K_p1=diff*eta*Mv/(dm*xeta*R)
#---------------------------
# Get inputs from the user 
#---------------------------
# Res=float(input('\n Enter Saline Side Reynolds Number: ')) # Reynolds number on Feed Side
# Rep=float(input('\n Enter Permeate Side Reynolds Number: ')) # Reynolds number on permeate/coolant
# Ts=float(input('\n Enter Bulk Feed Temperature: ')) # Bulk temperature on feed
# Tp=float(input('\n Enter Bulk Coolant Temperature: ')) # Bulk tempereature on permeate/coolant
# code test section - verification values of mass flow rates

Ts = 40.0
Tp = 30.0
#---------------------------
# Define constants 
#---------------------------
porosity=0.8 # porosity of the membrane 
Kw=0.6 # W/m-K Thermal conductivity of water 
Cp=4.1785e03 # J/kg-K  Specific heat of water 
Mus= (4e-12*Ts**6) - (2e-09*Ts**5) + (3e-07*Ts**4) - (2e-05*Ts**3) + (0.0014*Ts**2) - (0.0602*Ts + 1.7869) # Ns/m2 Dynamic viscosity of water on feed side 
Mup= (4e-12*Tp**6) - (2e-09*Tp**5) + (3e-07*Tp**4) - (2e-05*Tp**3) + (0.0014*Tp**2) - (0.0602*Tp + 1.7869) # Ns/m2 Dynamic viscosity of water on permeate/coolant side 
km=0.25 # W/m-k Conductivity of the membrane material -- PTFE
ka=0.025 # W/m-K conductivity of air
kc=180.0 # W/m-K conductivity of the coolant plate -- copper 
#---------------------------
massin = 0.05
vin = 0.05/(1000.0*dx*B)
Res = 1000.0*vin*Dh/Mus
Rep = 1000.0*vin*Dh/Mup

# Calculate non-dimensional groups 
#---------------------------
Prs=Mus*Cp/Kw # Prandtl number on feed
Prp=Mup*Cp/Kw # Prandtl number on permeate/coolant 
#Nus=0.664*sqrt(Res)*(Prs**(1.0/3.0)) # Nusselt number on feed
#Nup=0.664*sqrt(Rep)*(Prp**(1.0/3.0)) # Nusselt number on coolant 
# test Nu values
if (Res>4000):
        Nus = 0.023 *(Res**0.8)*(Prs**0.33)*((2*Mus/(Mus+Mup))**0.14)
else:
        Nus = 1.86*(Res*Prs*Dh/L)**0.33

if (Rep>4000):
        Nup = 0.023 *(Rep**0.8)*(Prp**0.33)*((2*Mup/(Mus+Mup))**0.14)
else:
        Nup = 1.86*(Rep*Prp*Dh/L)**0.33

#---------------------------
# Calcualte derived quantities 
#---------------------------
hs=Kw*Nus/Dh # W/m2-K heat transfer coefficient on feed-membrane interface 
hp=Kw*Nup/Dh # W/m2-K heat transfer coefficient on coolant-membrane or coolant-plate interface
vfin=Mup*Res/(1000.0*Dh)
vpin=Mup*Rep/(1000.0*Dh)
mfin=1000.0*dx*B*vfin
mpin=1000.0*dx*B*vpin
K_mem = ((eta/ka)+((1-eta)/km))**(-1)
print hs, hp, (da/K_mem)

#---------------------------
# Calculation for DCMD
#---------------------------
membrane_area = dx*L
resistance_dcmd=(1/hs)+(dm/K_mem)+(1/hp)
Q_dcmd=(Ts-Tp)/(resistance_dcmd)
T_dcmd=[Ts, Ts-(Q_dcmd/hs), Ts-(Q_dcmd/hs)-(Q_dcmd*dm/km), Tp]
x_dcmd=[0, dx, dx+dm, dx+dm+dx]
permeability = calculate_diffusivity(T_dcmd[1],T_dcmd[2],0)
activity_factor = calculate_activity_factor(salinity)
m_dcmd=permeability*((activity_factor*calculate_psat(T_dcmd[1]))-calculate_psat(T_dcmd[2]))
rr_dcmd=100.0*m_dcmd*membrane_area/mfin
mdcmdr=(rr_dcmd*mfin)+mpin
tperout=(1.0/mdcmdr)*((Q_dcmd/Cp)+(mfin*Tp))
#---------------------------
# Calculation for AGMD
#---------------------------
membrane_area = L*dx
resistance_agmd=(1/hs)+(dm/K_mem)+(da/ka)+(1/hp)
Q_agmd=(Ts-Tp)/(resistance_agmd)
T_agmd=[Ts, Ts-(Q_agmd/hs), 
        Ts-(Q_agmd/hs)-(Q_agmd*dm/K_mem), 
        Ts-(Q_agmd/hs)-(Q_agmd*dm/K_mem)-(Q_agmd*da/ka), 
        Ts-(Q_agmd/hs)-(Q_agmd*dm/K_mem)-(Q_agmd*da/ka)-(Q_agmd/hp), 
        Tp]
x_agmd=[0, dx, dx+dm, dx+dm+da, dx+dm+da+(dp/2), dx+dm+da+dp, dx+dm+da+dp+dx]
permeability = calculate_diffusivity(T_dcmd[1],T_dcmd[2],da)
m_agmd=permeability*((activity_factor*calculate_psat(T_agmd[1]))-calculate_psat(T_agmd[2]))
rr_agmd=100.0*m_agmd*membrane_area/mfin 

print 3600*m_agmd, rr_agmd
# #---------------------------
# # Calculation for CGMD
# #---------------------------
# resistance_cgmd=(1/hs)+(dm/km)+((da-dcg)/ka)+(dcg/keff)+(dp/kc)+(1/hp)
# Q_cgmd=(Ts-Tp)/(resistance_cgmd)
# T_cgmd=[Ts ...
#     Ts-(Q_cgmd/hs) ...
#     Ts-(Q_cgmd/hs)-(Q_cgmd*dm/km) ...
#     Ts-(Q_cgmd/hs)-(Q_cgmd*dm/km)-(Q_cgmd*(da-dcg)/ka) ...
#     Ts-(Q_cgmd/hs)-(Q_cgmd*dm/km)-(Q_cgmd*(da-dcg)/ka)-(Q_cgmd*dcg/keff)...
#     Ts-(Q_cgmd/hs)-(Q_cgmd*dm/km)-(Q_cgmd*(da-dcg)/ka)-(Q_cgmd*dcg/keff)-(Q_cgmd*dp/kc) ...
#     Ts-(Q_cgmd/hs)-(Q_cgmd*dm/km)-(Q_cgmd*(da-dcg)/ka)-(Q_cgmd*dcg/keff)-(Q_cgmd*dp/kc)-(Q_cgmd/hp) ...
#     Tp]
# x_cgmd=[0 dx dx+dm dx+dm+da-dcg dx+dm+da dx+dm+da+(dp/2) dx+dm+da+dp dx+dm+da+dp+dx]
# psatavg=(calculate_psat(T_cgmd(2))+calculate_psat(T_cgmd(3)))/2
# tavg=(T_cgmd(2)+T_cgmd(3))/2
# ptot=(10e05)+(psatavg)
# m_cgmd=(K_p1*ptot/(tavg*psatavg))*(((1-salinity)*T_cgmd(2)*calculate_psat(T_cgmd(2)))-calculate_psat(T_cgmd(3)))
# rr_cgmd=100*m_cgmd*B*L/mfin
#---------------------------
# Plot
#---------------------------
# scatter(x_dcmd,T_dcmd,'r')
# hold on
# scatter(x_agmd,T_agmd,'b')
# hold on
# scatter(x_cgmd,T_cgmd,'k')
# xlabel('Distance Along the Module (m)')
# ylabel('Temperature (K)')
# legend('DCMD','AGMD','CGMD') 
# plot([dx,dx],[Tp-5,Ts+5],'k--')
# hold on
# plot([dx+dm,dx+dm],[Tp-5,Ts+5],'k--')
# hold on
# plot([dx+dm+da,dx+dm+da],[Tp-5,Ts+5],'k--')
# hold on
# plot([dx+dm+da+dp/2,dx+dm+da+dp/2],[Tp-5,Ts+5],'k--')
# hold off