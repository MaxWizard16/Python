import numpy as np
arr = np.random.rand(1000)
mean = arr.mean()
median = np.median(arr)
variance = arr.var()
print(mean, median, variance)

import numpy as np
from scipy import linalg
A = np.array([[4,2,1],[0,1,-1],[2,3,0]],float)
detA = linalg.det(A)
invA = linalg.inv(A)
eigvals, eigvecs = linalg.eig(A)
print(detA, invA, eigvals)

import numpy as np
from scipy import linalg
A = np.array([[4,2,1],[0,1,-1],[2,3,0]],float)
detA = linalg.det(A)
invA = linalg.inv(A)
eigvals, eigvecs = linalg.eig(A)
print(detA, invA, eigvals)

import numpy as np
from scipy.interpolate import interp1d
x = np.linspace(0,10,11)
y = np.sin(x) + 0.1*np.random.randn(len(x))
f = interp1d(x,y,kind='cubic')
x2 = np.linspace(0,10,200)
y2 = f(x2)
print(y2)

import numpy as np
from scipy import signal
t = np.linspace(0,10,500)
sig = np.sin(2*np.pi*1*t) + 0.5*np.random.randn(len(t))
b,a = signal.butter(4,0.1)
filt = signal.filtfilt(b,a,sig)
print(filt)

import numpy as np
sales = np.random.randint(50,500,(12,4))
total = sales.sum()
avg = sales.mean(axis=0)
maxp = sales.max(axis=0)
best = sales.sum(axis=1).argmax()+1
worst = sales.sum(axis=1).argmin()+1
print(total, avg, maxp, best, worst)

import numpy as np
names = np.array(['Arin','Aditya','Chirag','Gurleen','Kunal'])
marks = np.array([[85,78,92,88],
                  [79,82,74,90],
                  [90,85,89,92],
                  [66,75,80,78],
                  [70,68,75,85]])
totals = marks.sum(axis=1)
averages = marks.mean(axis=1)
subject_avg = marks.mean(axis=0)
top = names[totals.argmax()]
bottom = names[totals.argmin()]
passing = (marks>=40).all(axis=1).mean()*100
print(totals, averages, subject_avg, top, bottom, passing)

import numpy as np
from scipy.optimize import curve_fit
t = np.array([0,1,2,3,4,5],float)
v = np.array([2,3.1,7.9,18.2,34.3,56.2],float)
def f(t,a,b,c): return a*t**2 + b*t + c
popt,_ = curve_fit(f,t,v)
print(popt)

import numpy as np
import matplotlib.pyplot as plt
names=['Arin','Aditya','Chirag','Gurleen','Kunal']
marks=np.array([[85,78,92,88],
                [79,82,74,90],
                [90,85,89,92],
                [66,75,80,78],
                [70,68,75,85]])
x=np.arange(len(names))
plt.bar(x-0.3,marks[:,0],0.2)
plt.bar(x-0.1,marks[:,1],0.2)
plt.bar(x+0.1,marks[:,2],0.2)
plt.bar(x+0.3,marks[:,3],0.2)
plt.xticks(x,names)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
t=np.array([0,1,2,3,4,5],float)
v=np.array([2,3.1,7.9,18.2,34.3,56.2],float)
def f(t,a,b,c): return a*t**2 + b*t + c
popt,_=curve_fit(f,t,v)
t2=np.linspace(0,5,200)
plt.scatter(t,v)
plt.plot(t2,f(t2,*popt))
plt.show()

import numpy as np
from scipy import stats, interpolate
years=np.array([2000,2005,2010,2015,2020])
pop=np.array([50,55,70,80,90])
r,_=stats.pearsonr(years,pop)
slope,intr,_,_,_=stats.linregress(years,pop)
p_reg=slope*2008 + intr
f=interpolate.interp1d(years,pop)
p_int=float(f(2008))
print(r,p_reg,p_int)

import numpy as np
import matplotlib.pyplot as plt
c=[3,-5,2,-8]
r=np.roots(c)
x=np.linspace(-3,3,400)
y=np.polyval(c,x)
plt.plot(x,y)
plt.axhline(0)
plt.scatter(r.real, np.polyval(c,r))
plt.show()

import numpy as np, time
sizes=[5,10,20,30,40]
times=[]
for mb in sizes:
    start=time.time()
    data=np.random.randint(65,91,mb*1024*1024).astype('uint8').tobytes()
    open('f.txt','wb').write(data)
    d=open('f.txt','rb').read()
    open('f_up.txt','wb').write(d.upper())
    times.append(time.time()-start)
print(times)

import numpy as np
from scipy.optimize import minimize
def f(x): return x**4 - 3*x**3 + 2
mins=[]
for x0 in np.linspace(-2,3,15):
    r=minimize(f,x0)
    if r.success and -2<=r.x<=3:
        mins.append(round(float(r.x),6))
mins=sorted(set(mins))
print(mins)

import numpy as np
from scipy.integrate import odeint
def d(y,t): return [y[1], -0.2*y[1] - y[0]]
t=np.linspace(0,20,1001)
sol=odeint(d,[1,0],t)
theta=sol[:,0]
print(theta.max(), t[theta.argmax()])
