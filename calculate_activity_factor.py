def calculate_activity_factor(salinity):
    mass_salt = salinity/1000.0 # mass in kg 
    mass_water = 1.0 # since salinity is g of salt / kg of water 
    moles_salt = mass_salt/62.8 # equivalent molecular weight of sea-salt is 62.8
    moles_water = mass_water/18.016 # moles of water 
    mole_frac_salt = moles_salt/(moles_salt+moles_water)
    mole_frac_water = 1 - mole_frac_salt
    gamma = 1.0-(0.5*mole_frac_salt) - (10.0*mole_frac_salt**2)
    activity_factor = mole_frac_water*gamma 
    return activity_factor

