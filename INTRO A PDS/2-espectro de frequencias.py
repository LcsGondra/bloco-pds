import numpy as np 
import matplotlib.pyplot as plt
import scipy as sp
from scipy import signal

#Amostragem

fa = 100
ha = 1/fa
ts = 10

#Signal

f1 = 1
f5 = 5
f10 = 10

T = np.arange(0, ts, ha)

A = 1 #AMPLITUDE

#func seno e coseno
x1 = A*np.sin(2*np.pi*f1*T)
x5 = A*np.sin(2*np.pi*f5*T)
x10 = A*np.sin(2*np.pi*f10*T)

x = x1+x5+x10

#variacao de amplitude

A1 = 1
A2 = 2
xA1 = A1*np.sin(2*np.pi*f*T+phase)
xA2 = A2*np.sin(2*np.pi*f*T+phase)

#variacao de frequencia

f1 = 1
f2 = 2

xf1 = A*np.sin(2*np.pi*f1*T+phase)
xf2 = A*np.sin(2*np.pi*f2*T+phase)

#variacao de fase

phase1 = 0
phase2 = np.pi/4

xphase1 = A*np.sin(2*np.pi*f*T+phase1)
xphase2 = A*np.sin(2*np.pi*f*T+phase2)

#plot graph
plt.figure(figsize=(15, 7))

# First subplot (Sine function)
plt.subplot(2, 3, 1)
plt.plot(T,xs)
plt.xlabel('t[s]')
plt.ylabel('xs(t)')
plt.title('Sine Func')
plt.grid()
plt.legend()

plt.subplot(2, 3, 2)
plt.plot(T,xc)
plt.xlabel('t[s]')
plt.ylabel('xc(t)')
plt.title('Cosine Func')
plt.grid()
plt.legend()

plt.subplot(2, 3, 4)
plt.plot(T,xA1)
plt.plot(T,xA2)
plt.xlabel('t[s]')
plt.ylabel('xA1(t) e xA2(t)')
plt.title('variacao de amplitude')
plt.grid()
plt.legend()

plt.subplot(2, 3, 5)
plt.plot(T,xf1)
plt.plot(T,xf2)
plt.xlabel('t[s]')
plt.ylabel('xf1(t) e xf2(t)')
plt.title('variacao de frequencia')
plt.grid()
plt.legend()

plt.subplot(2, 3, 6)
plt.plot(T,xphase1)
plt.plot(T,xphase2)
plt.xlabel('t[s]')
plt.ylabel('xphase1(t) e xphase2(t)')
plt.title('variacao de fase')
plt.grid()
plt.legend()

plt.show()