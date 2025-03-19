import numpy as np 
import matplotlib.pyplot as plt

#1.1
h = 0.01
ts = 1
T = np.arange(0, ts+h, h)

A = 1 #AMPLITUDE
f1 = 1 #FREQUENCIA
f5 = 5
f10 = 10

sin1 = A*np.sin(2*np.pi*f1*T)
sin5 = A*np.sin(2*np.pi*f5*T)
sin10 = A*np.sin(2*np.pi*f10*T)

sinX = sin1+sin5+sin10
plt.figure(figsize=(15, 7))

plt.subplot(321)
plt.plot(T,sin1)
plt.xlabel('t[s]')
plt.ylabel('xs(t)')
plt.title('1hz')
plt.grid()
plt.legend()

plt.subplot(322)
plt.plot(T,sin5)
plt.xlabel('t[s]')
plt.ylabel('xs(t)')
plt.title('5hz')
plt.grid()
plt.legend()

plt.subplot(323)
plt.plot(T,sin10)
plt.xlabel('t[s]')
plt.ylabel('xs(t)')
plt.title('10hz')
plt.grid()
plt.legend()

plt.subplot(324)
plt.plot(T,sinX)
plt.xlabel('t[s]')
plt.ylabel('xs(t)')
plt.title('sinal composto')
plt.grid()
plt.legend()

#1.2
X = np.fft.fft(sinX)
N = len(sinX)
VetN = np.arange(0,N)

f1 = 100/N
freq = f1*VetN
ifreq = int((N/2)+1)
freq = freq[0:ifreq]

k_magFreq = 2/N
magFreq = k_magFreq*abs(X[0:ifreq])
magFreq[0] = magFreq[0]/2


plt.subplot(313)
plt.stem(freq,magFreq)
plt.xlabel('f[hz]')
plt.ylabel('magFreq')
plt.title('espectro de frequencias')
plt.grid()
plt.legend()

plt.show()