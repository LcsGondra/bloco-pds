import numpy as np 
import matplotlib.pyplot as plt
import scipy as sp
from scipy import signal

#reprodusir o sinal S

h = 0.01
pi=np.pi
T = np.arange(-1, 2*pi+1, h)
nT=len(T)
S=np.zeros(nT)

for i in range(0,nT):
    if T[i]<0:
        S[i]=0
    elif (T[i]<pi):
        S[i]=1
    elif (T[i]<=2*pi):
        S[i]=-1
    else:
        S[i]=0


S1=np.sin(T)*(4/pi)
S3=(np.sin(T)+((1/3)*np.sin(3*T))+((1/5)*np.sin(5*T)))*(4/pi)

        

#plot graph
plt.figure(figsize=(10, 8))

# First subplot
T_pi=T/pi
plt.subplot(2, 2, 1)
plt.plot(T_pi,S)
plt.xlabel('t[s]')
plt.ylabel('S(t)')
plt.title('Sinal S[t]')
plt.grid()
plt.legend()

Tn=np.arange(0,2*pi,h)
nTn=len(Tn)
Tn_pi=Tn/pi

Sn1=np.sin(Tn)*(4/pi)

plt.subplot(2, 2, 2)
plt.plot(T_pi,S)
plt.plot(Tn_pi,Sn1)
plt.xlabel('t[s]')
plt.ylabel('S(t)')
plt.title('Sinal para n=1')
plt.grid()
plt.legend()

Sn3=(np.sin(Tn)+((1/3)*np.sin(3*Tn))+((1/5)*np.sin(5*Tn)))*(4/pi)

plt.subplot(2, 2, 3)
plt.plot(T_pi,S)
plt.plot(Tn_pi,Sn3)
plt.xlabel('t[s]')
plt.ylabel('S(t)')
plt.title('Sinal para n=3')
plt.grid()
plt.legend()


def SnT(tamanho):
    # if n==0:
    #     return 0
    # return SnT(n-1)+(4/pi)*((1/n)*np.sin(n*Tn))
    Sn=np.zeros(nTn)
    Sn_1=np.zeros(nTn)
    N=np.arange(1,tamanho,2)
    nN=len(N)
    for iN in range(0,nN):
        n=N[iN]
        for i in range(0,nTn):
            t=Tn[i]
            Sn[i]=Sn_1[i]+(4/pi)*(1/n)*(np.sin(n*t))
        Sn_1=Sn
    return Sn



n=50

plt.subplot(2, 2, 4)
plt.plot(T_pi,S)
plt.plot(Tn_pi,SnT(n))
plt.xlabel('t[s]')
plt.ylabel('S(t)')
plt.title(f'Sinal para n={n}')
plt.grid()
plt.legend()

plt.show()