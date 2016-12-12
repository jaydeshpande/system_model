def chem_disequilibrium(mb,mr,go,gb,gs): #mb is the exhaust flow rate, mr is a dummy reservoir 
#go is the Gibb's free energy of the exhaust, gs is the gibb's free energy of the reservoir
# idea is to assume a reservoir large enough that it does not have a direct effect on the system
# sensitivity study is needed to truly establish the independence. 
	return -((mb+mr)*go -mb*gb - mr*gs)
	