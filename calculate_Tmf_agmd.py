def calculate_Tmf_agmd(Tc, Tf, jw, h, hf, ho):
    Hw = 4186.0
    Tmf = Tf - (ho/hf)*((Tf-Tc)+(jw*Hw/h))
    Tcd = Tc + (ho/hf)*((Tf-Tc)+(jw*Hw/h))
    return [Tmf, Tcd]