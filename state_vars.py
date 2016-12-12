from calculate_spvol import *
from calculate_potential import *
from calculate_spenthalpy import *
from calculate_spentropy import *
def get_properties(T,ws):
	spv=calculate_spvol(T,ws); # spv = [rhosw,rhow,spvol]
	spe=calculate_spenthalpy(T,ws); # spe = [hw,hsw]
	hsw = spe[1]
	sps=calculate_spentropy(T,ws); # sps = [sw,ssw] 
	ssw = sps[1]
	mup=calculate_potential(T,ws,hsw,ssw); # mup = [muw,mus]
	return [spv[0],spv[1],spv[2],spe[0],spe[1],sps[0],sps[1],mup[0],mup[1]]

#print get_properties(300.0, 0.05)