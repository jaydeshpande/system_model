def calculate_potential(T,ws,hsw,ssw): #Returns seawater and pure water entropies w.r.t. temperature T and concentration of salt ws 
	b1=-2.348e04;
	b2=3.152e05;
	b3=2.803e06;
	b4=-1.446e07;
	b5=7.826e03;
	b6=-4.417e01;
	b7=2.139e-01;
	b8=-1.991e04;
	b9=2.778e04;
	b10=9.728e01;
	c1=-4.231e02;
	c2=1.463e04;
	c3=-9.880e04;
	c4=3.095e05;
	c5=2.562e01;
	c6=-1.443e-01;
	c7=5.879e-04;
	c8=-6.111e01;
	c9=8.041e01;
	c10=3.035e-01;
	dhsdw=-(b1 + (2*b2*ws) + (3*b3*ws*ws) + (4*b4*ws*ws*ws) + (b5*T) + (b6*T*T) + (b7*T*T*T) + (2*b8*ws*T) + (3*b9*ws*ws*T) + (2*b10*ws*T*T));
	dsdw=-(c1 + (2*c2*ws) + (3*c3*ws*ws) + (4*c4*ws*ws*ws) + (c5*T) + (c6*T*T) + (c7*T*T*T) + (2*c8*ws*T) + (3*c9*ws*ws*T) + (2*c10*ws*T*T));
	dgdw=dhsdw - ((T+273.15)*dsdw);
	gsw=(hsw -((T+273.15)*ssw));
	muw=gsw-(ws*dgdw);
	mus=gsw+((1-ws)*dgdw);
	return [muw, mus]