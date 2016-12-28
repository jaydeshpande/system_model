def calculate_overall_h_agmd(hd,hf,h,hc,l,kc):
    hp = (1/hd) + (l/kc) + (1/hc)
    overall_h = (1/hp) + (1/hf) + (1/h)
    return (1/overall_h)