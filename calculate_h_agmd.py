def calculate_h_agmd(jw,b,ky):
    from math import exp
    h = (jw*4185/(1-(exp(-jw*4185*b/ky))))
    return h