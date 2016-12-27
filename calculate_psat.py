from math import exp as exp
def calculate_psat(T):
	A1=16.2620;
	A2=3799.89;
	A3=-226.35;
	psat=exp(A1 - (A2/(T-A3)));
	return psat