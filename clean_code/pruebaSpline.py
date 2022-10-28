import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline, CubicSpline
import numpy as np
import pandas as pd

df = pd.read_csv('/home/phoebus/Documents/code_tesis/files/pollutants2018.csv')
df.dateUTCShiftedDown = pd.to_datetime(df.dateUTCShiftedDown)
df = df[(df.id_station_id=="CAM")&
        (df.id_parameter_id=="O3")&
        (df.dateUTCShiftedDown.dt.month==3)&
        (df.dateUTCShiftedDown.dt.hour.between(6,22))]
nulos=[]
#plt.plot(df.original.values)

s = len(df.original.values)
c=0
for i in range(s):
    if np.isnan(df.original.iloc[i]):
        if c == 0:
            nulos.append(i-1)
        c+=1
    else:
        if np.isnan(df.original.iloc[i-1]):
           nulos.append(i) 

#print(nulos)

a = df.original.iloc[nulos[0]-5:nulos[1]+5].interpolate(method="polynomial",order=3).values
j=0

for i in range(nulos[0]-1,nulos[1]+1):
    df.original.iloc[i] = a[j]
    j+=1

#print(df.original.iloc[nulos[0]-1:nulos[1]+1])
#print(a)

df.original.interpolate(method="polynomial", order=3, inplace=True)
df.original.plot.line()
#plt.plot( df.original.values)
y = np.linspace(np.pi/3,2*np.pi,100)

x = CubicSpline(np.arange(df.original.size), df.original.values)
result = x(y)
print(result)
#plt.plot(np.arange(df.original.size), x)

#plt.show()


