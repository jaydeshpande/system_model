def calculate_hd_agmd(Tcd, Tpa, l):
    Hw = (1.75535*(Tcd+Tpa)*0.5) + 2024.3
    g = 9.81
    rho = 1000.0
    Mud = 1e-03 
    Kp = 0.615 
    num = g*rho**2*Hw*Kp**3 
    den = l*Mud*(Tcd-Tpa)
    hd = (num/den)**(1/4)