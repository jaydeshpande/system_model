from calculate_psat import calculate_psat
from math import log
def calculate_diffusivity(Tmf, Tcd, airgap):
    eta = 75.9
    Tavg = (Tmf + Tcd)/2
    pdw = (Tavg**2.072)*1.895e-05 
    R = 8.314
    delta = 159.5e-06
    dp = 236e-09 
    tau = 1.3 
    pmf = calculate_psat(Tmf)
    pcd = calculate_psat(Tcd)
    paln = (pmf - pcd)/log(pmf/pcd)
    permeability = eta*pdw/(R*Tavg*((delta*tau)+airgap)*paln)
    return permeability

