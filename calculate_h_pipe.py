def calculate_h_pipe(Re,Pr,Dh,k):
    Nu=0.664*sqrt(Re)*(Pr**(1/3)) 
    h = k*Nu/Dh
    return h