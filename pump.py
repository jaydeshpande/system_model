cp = 4186.0 # specific heat
etap = 0.98 # pump efficiency (get this value from the standards
R = 8.314 # universal gas constant 
# assuming pumping work is performed at atmospheric pressure, value of p1 is taken as 101325
import math
def get_pump_entropy(p):
	logtrm = 1 - ((1/etap)*(1 - math.pow((p/101325.0),(R/cp))))
	sgen = cp*math.log(logtrm) - R*math.log(p/101325.0)
	return sgen 