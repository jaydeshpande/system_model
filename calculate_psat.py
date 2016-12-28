from math import exp as exp
def calculate_psat(T):
	A1=23.1964;
	A2=3816.44;
	A3=46.13;
	psat=exp(A1 - (A2/(T-A3)));
	psat = 10 **(8.14 - (1811.0/(244.5+T)))
	return psat