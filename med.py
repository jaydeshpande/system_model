from math import log
import pandas as pd
n = 12.0 # no. of effects in MED
xb = 72.0 # exit brine salinity
xf = 46.0 # feed salinity
C = 4000.0 # water specific heat
L =  2260000.0 # water latent heat of evap
d = 139.0 # distillate output in kg/s (dummy value, can be changed)
Tb = 65.0 # entrance brine temperature water (this is a typical value)
Tn = 38.0 # exit temperature of last effect (this is a typical value)
Tc = 28.0 # condenser temperature 
T12 = 35.0 # temperature at the condenser exit
BPE = 1.0 # boiling point elevation due to salt * we can add real equation here to get more accurate value
Mc = 935.7 # mass flow rate of coolant in the condenser (it should be treated as a variable)
Ue = 3.0 # effective heat transfer coeff for effect kW/m2C
Uf = 2.6 # effective heat transfer coeff for heat exchangers feed and condenser 
deltT = (Tb-Tn)/(n-1) # effect in each stage 
# deltT is the temperature drop across each stage 
t1 = T12 + (n-1)*deltT # temperature after the first stage 
fd = xb/ (xb-xf) # fd is the feed to distillate ratio 
f = d*fd # feed requirement
y = C*deltT/L # fraction of water evaporated in each staging 
by = (1/(1-((1-y)**n))) - fd # bypass to recovery ratio in every stage (beta/y)
beta = by*y
D1 = (by*y)*d + y*f #(by*y*d) = beta*D
S = D1 + (f*C*(Tb-t1)/L)
B1 = f - D1 # brine out from 1st stage 
saltin = f*xf # mass of salt flowing in the system
X1 = saltin/B1 # salinity after the first effect 
loadone = S*L
area1 = loadone/(1000.0*Ue*(deltT-BPE))
#print "dT", deltT,"t1", t1,"fd", fd,"f", f,"y", y,"beta", by*y,"D1", D1,"S", S
D, Df, Db, X, F, B, t, T, load, lmtd, Af, Ae, Sgen = ([] for i in range(13))
T.append(Tb)
Df.append((by*y)*d)
Db.append(y*f)
D.append(D1)
t.append(t1)
X.append(X1)
B.append(B1)
F.append(f)
load.append(loadone)
Sgen.append(loadone/t1)
Ae.append(area1)
Af.append(0.0)
for i in range(1,11,1):
    F.append(B[-1])
    Df.append(beta*d)
    Db.append(y*B[-1])
    D.append(Df[-1] + Db[-1])
    B.append(f-sum(D))
    X.append(X[-1]*B[-2]/B[-1])
    t.append(t[-1]-deltT)
    T.append(T[-1]-deltT)
    load.append(2333.0*beta*d)
    Ae.append(load[-1]/(Ue*(deltT-BPE)))
    lmtd.append(deltT/log((T[-2]-BPE-t[-1])/(T[-2]-BPE-t[-2])))
    Af.append(f*C*deltT/(1000.0*Uf*lmtd[-1]))
    Sgen.append(load[-1]/t[-1])
# final stage yield is calculated from the cooling effort in the condenser 
D12 = Mc*C*(t[-1]-Tc)/L
D.append(D12)
F.append(B[-1])
B.append(B[-1]-D12)
t.append(T12)
T.append(T[-1]-deltT)
Df.append(Df[-1])
Db.append(D12-Df[-1])
X.append(saltin/B[-1])
Ae.append(Ae[-1])
Af.append(Af[-1])
Sgen.append(Sgen[-1])
print Sgen, len(Sgen)
pd.set_option('precision', 2)
df = pd.DataFrame({ 'T' : T,
                    't' : t,
                    'F' : F,
                    'Db' : Db,
                    'Df' : Df,
                    'D' : D,
                    'B' : B,
                    'X' : X,
                    'Ae' : Ae,
                    'Af' : Af,
                    'Sgen' : Sgen})

#df = df[df.columns[::-1]]
df = df[['T','t','F','Db','Df','D','B','X','Ae','Af','Sgen']]
print df 



# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('verification.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()