from calculate_spvol import *
from calculate_potential import *
from calculate_spenthalpy import *
from calculate_spentropy import *
def calculate_exergetic_effciency(Tin, wsin, rr, mfin, mpin):
    mpout = (rr*100.0*mfin) + mpin
    msout = mfin-(rr*100.0*mfin)
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
    ex_sal_in=((calculate_spenthalpy(Tin[0],wsin)[1]-hswr)-(298*(calculate_spentropy(Tin[0],wsin)[1]-sswr))+ (0.05*(musr-musd)) + (0.95*(muwr-muwd)))*mfin;
    ex_permeate_in=((calculate_spenthalpy(Tin[1],0)[0]-hwr)-(298*(calculate_spentropy(Tin[1],wsin)[0]-swr))+ (0.05*(musr-musd)) + (0.95*(muwr-muwd)))*mpin;
    ex_sal_out=((calculate_spenthalpy(Tin[2],wsin)[1]-hswr)-(298*(calculate_spentropy(Tin[2],wsin)[1]-sswr))+ (0.05*(musr-musd)) + (0.95*(muwr-muwd)))*msout;
    ex_permeate_out=((calculate_spenthalpy(Tin[3],0)[0]-hswr)-(298*(calculate_spentropy(Tin[3],wsin)[0]-sswr))+ (0.05*(musr-musd)) + (0.95*(muwr-muwd)))*(mpout);
    ex_destroyed=ex_sal_in+ex_permeate_in-ex_sal_out-ex_permeate_out;
    ex_eff=100*(1-(ex_destroyed/(ex_sal_in+ex_permeate_in)));
    return ex_eff
