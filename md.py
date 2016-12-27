#  Program aims to study relative efficiencies of desal techniques
#---------------------------
# Define fixed parameters (Geometrical) 
from math import sqrt as sqrt
from calculate_psat import * 
import matplotlib.pyplot as plt
#---------------------------
L=1 # Length of the module 
dx=0.5e-02 # Flow channel width 
B=0.1 # Height of the module
dm=250e-06 # m Thickness of membrane 
da=3.5e-03 # m Thickness of airgap
dv=500e-03 # m thickness of vacuum
dp=1e-03 # m thickness of coolant plate
dcg=3e-03 # m thickness of mesh
salinity=0.25 # g/kg salinity in the feed
#---------------------------
# Calculate the membrane diffusivity 
#---------------------------
eta=0.8
xeta=1.3
Mv=18
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
Res = 100.0
Rep = 100.0
Ts = 80.0
Tp = 20.0
#---------------------------
# Define constants 
#---------------------------
porosity=0.8 # porosity of the membrane 
Kw=0.06 # W/m-K Thermal conductivity of water 
Cp=4.1785e03 # J/kg-K  Specific heat of water 
Mus=0.5e-03 # Ns/m2 Dynamic viscosity of water on feed side 
Mup=1e-03 # Ns/m2 Dynamic viscosity of water on permeate/coolant side 
km=0.25 # W/m-k Conductivity of the membrane material -- PTFE
ka=0.027 # W/m-K conductivity of air
kc=400 # W/m-K conductivity of the coolant plate -- copper 
#---------------------------
# Calculate non-dimensional groups 
#---------------------------
Prs=Mus*Cp/Kw # Prandtl number on feed
Prp=Mup*Cp/Kw # Prandtl number on permeate/coolant 
Nus=0.664*sqrt(Res)*(Prs**(1/3)) # Nusselt number on feed
Nup=0.664*sqrt(Rep)*(Prp**(1/3)) # Nusselt number on coolant 
#---------------------------
# Calcualte derived quantities 
#---------------------------
hs=Kw*Nus/L # W/m2-K heat transfer coefficient on feed-membrane interface 
hp=Kw*Nup/L # W/m2-K heat transfer coefficient on coolant-membrane or coolant-plate interface
hf=0.943*(9.81*1000*(1000-0.804)*2257*1000*(0.06**3)/(Mup*(373-Tp)*L))**(1/4) # W/m2-K overall heat transfer coefficient for condensate film
df=Kw/hf # m thickness of condensate film
keff=ka*(Kw+kc-((1-porosity)*(Kw-kc)))/(Kw+kc+((1-porosity)*(Kw-kc))) # W/m-K effective conductivity of the mesh+air gap
vfin=Res/(1000*L)
vpin=Rep/(1000*L)
mfin=1000*dx*B*vfin
mpin=1000*dx*B*vpin
#---------------------------
# Calculation for DCMD
#---------------------------
resistance_dcmd=(1/hs)+(dm/km)+(1/hp)
Q_dcmd=(Ts-Tp)/(resistance_dcmd)
T_dcmd=[Ts, Ts-(Q_dcmd/hs), Ts-(Q_dcmd/hs)-(Q_dcmd*dm/km), Tp]
x_dcmd=[0, dx, dx+dm, dx+dm+dx]
psatavg=(calculate_psat(T_dcmd[2])+calculate_psat(T_dcmd[3]))/2
tavg=(T_dcmd[2]+T_dcmd[3])/2
ptot=(10e05)+(psatavg)
m_dcmd=(K_p1*ptot/(tavg*psatavg))*(((1-salinity)*T_dcmd[2]*calculate_psat(T_dcmd[2]))-calculate_psat(T_dcmd[3]))
rr_dcmd=100*m_dcmd*B*L/mfin
mdcmdr=(rr_dcmd*mfin)+mpin
tperout=(1/mdcmdr)*((Q_dcmd/Cp)+(mfin*Tp))

#---------------------------
# Calculation for AGMD
#---------------------------
resistance_agmd=(1/hs)+(dm/km)+((da-df)/ka)+(dp/kc)+(1/hf)+(1/hp)
Q_agmd=(Ts-Tp)/(resistance_agmd)
T_agmd=[Ts, Ts-(Q_agmd/hs), Ts-(Q_agmd/hs)-(Q_agmd*dm/km), Ts-(Q_agmd/hs)-(Q_agmd*dm/km)-(Q_agmd*(da-df)/ka), Ts-(Q_agmd/hs)-(Q_agmd*dm/km)-(Q_agmd*(da-df)/ka)-(Q_agmd/hf), Ts-(Q_agmd/hs)-(Q_agmd*dm/km)-(Q_agmd*(da-df)/ka)-(Q_agmd/hf)-(Q_agmd*dp/kc), Ts-(Q_agmd/hs)-(Q_agmd*dm/km)-(Q_agmd*(da-df)/ka)-(Q_agmd/hf)-(Q_agmd*dp/kc)-(Q_agmd/hp), Tp]
x_agmd=[0, dx, dx+dm, dx+dm+da-df, dx+dm+da, dx+dm+da+(dp/2), dx+dm+da+dp, dx+dm+da+dp+dx]
psatavg=(calculate_psat(T_agmd[2])+calculate_psat(T_agmd[3]))/2
tavg=(T_agmd[2]+T_agmd[3])/2
ptot=(10e05)+(psatavg)
m_agmd=(K_p1*ptot/(tavg*psatavg))*(((1-salinity)*T_agmd[2]*calculate_psat(T_agmd[2]))-calculate_psat(T_agmd[3]))
rr_agmd=100*m_agmd*B*L/mfin
plt.plot(x_dcmd, T_dcmd, 'r')
#plt.figure(2)
#plt.plot(x_agmd, T_agmd, 'g')
print "Sgen = ", mfin*(Q_dcmd/Tp)

plt.show()
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