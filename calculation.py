from calculate_spvol import *
from calculate_potential import *
from calculate_spenthalpy import *
from calculate_spentropy import *
T0=25;
#--------------------------
# Pass temperature and velocity values from program
T=25; #dead state temperature
ws=35e-03; #dead state salinity -- can be varied if needed 

spv=calculate_spvol(T,ws); # spv = [rhosw,rhow,spvol]
rhoswd=spv[0];
rhowd=spv[1];
spvold=spv[2];

spe=calculate_spenthalpy(T,ws); # spe = [hw,hsw]
hw=spe[0];
hsw=spe[1];
hwd=hw;
hswd=hsw;

sps=calculate_spentropy(T,ws); # sps = [sw,ssw] 
sw=sps[0];
ssw=sps[1];
swd=sw;
sswd=ssw;

mup=calculate_potential(T,ws,hsw,ssw); # mup = [muw,mus]
muw=mup[0];
mus=mup[1];
muwd=muw;
musd=mus;

# Thermodynamic Properties of Restricted Dead State
ws=50e-03; # This is the working salinity, it can be alterated per need
spv=calculate_spvol(T,ws); # spv = [rhosw,rhow,spvol]
rhoswr=spv[0];
rhowr=spv[1];
spvolr=spv[2];

spe=calculate_spenthalpy(T,ws); # spe = [hw,hsw]
hw=spe[0];
hsw=spe[1];
hwr=hw;
hswr=hsw;

sps=calculate_spentropy(T,ws); # sps = [sw,ssw] 
sw=spe[0];
ssw=spe[1];
swr=sw;
sswr=ssw;
	
mup=calculate_potential(T,ws,hsw,ssw); # mup = [muw,mus]
muwr=mup[0];
musr=mup[1];
#-------------------------
# Physical Parameter Calculation Complete
#-------------------------
# Calculate flow exergies and exergy destroyed across MD
# ex_sal_in=((hsw_saline_in-hswr)-(298*(ssw_saline_in-sswr))+ (0.05*(musr-musd)) + (0.95*(muwr-muwd)))*mass_flux_saline_inlet;
# ex_permeate_in=((hw_permeate_in-hwr)-(298*(sw_permeate_in-swr))+ (0.05*(musr-musd)) + (0.95*(muwr-muwd)))*mass_flux_permeate_inlet;
# ex_sal_out=((hsw_saline_out-hswr)-(298*(ssw_saline_out-sswr))+ (0.05*(musr-musd)) + (0.95*(muwr-muwd)))*mass_flux_saline_outlet;
# ex_permeate_out=((hw_permeate_out-hswr)-(298*(sw_permeate_out-sswr))+ (0.05*(musr-musd)) + (0.95*(muwr-muwd)))*(mass_flux_permeate_inlet+mass_flux_permeate);
# ex_destroyed(n)=ex_sal_in+ex_permeate_in-ex_sal_out-ex_permeate_out;
# ex_eff(n)=100*(1-(ex_destroyed(n)/(ex_sal_in+ex_permeate_in)));

