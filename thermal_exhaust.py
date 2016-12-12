cp = 4186.0 # water cp
T0 = 293.0 # assuming that the water is brought to equilibrium @ 20 degree C. 
# this value needs to be changed w.r.t. location, time of day etc. interesting parameter imo
import math
def temp_disequilibrium(T):
	sgen = cp*(math.log(T0/T) + (T/T0) -1)
	return sgen
