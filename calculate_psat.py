from math import exp as exp
def calculate_psat(T):
	''' A1=23.1964;
	A2=3816.44;
	A3=46.13;
	psat=exp(A1 - (A2/(T-A3))); '''
	A = 7.96681
	B = 1609.21
	C = 228.0
	psat = 133.322365*(10.0**(A - (B/(C+T))))
	
	psat = 133.322365*(10.0**(8.4831 - (1690.63/(233.426+T))))
	return psat