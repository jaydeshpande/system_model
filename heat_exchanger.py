cp = 4186.0 # cp of water assuming the heat exchanger only operates with water as fluid 
# isobaric operation is considered to model approximate heat exchanger 
T0 = 293.0
import math
def heat_exchange_loss(m1,m2,T):
	sgen = (m1+m2)*cp*math.log(T/T0)
	return sgen 
#NOTE: here sgen is NOT specific!! DO NOT MULTIPLY WITH MASSFLOW RATE AGAIN 
#NOTE: T0 needs to be changed per operational conditions, used as 20 degree C like everywhere else