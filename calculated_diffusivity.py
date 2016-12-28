from calculate_psat import calculate_psat
from math import log
def calculate_diffusivity(Tmf, Tcd, airgap):
    eta = 0.759
    Tavg = 293.0
    pdw = (Tmf**2.072)*2.995e-05 
    R = 8.314
    delta = 159.5e-06
    dp = 236e-09 
    tau = 1.3 
    #pmf = calculate_psat(Tmf)
    #pcd = calculate_psat(Tcd)
    pcd = (Tcd/293.0)*101325.0
    pmf = (Tmf/Tcd)*pcd
    #print pmf-pcd
    paln = (pmf - pcd)/log(pmf/pcd)
    permeability = eta*pdw/(R*Tavg*((delta*tau)+airgap)*paln)
    return permeability
