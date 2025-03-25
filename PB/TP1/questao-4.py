import numpy as np 
import matplotlib.pyplot as plt

h = 0.01
ts = 1
T = np.arange(0, ts+h, h)

A = 2 #AMPLITUDE
f = 1 #FREQUENCIA

sinx = A*np.sin(2*np.pi*f*T+(2/np.pi))

plt.figure(figsize=(15, 7))

plt.subplot(111)
plt.plot(T,sinx)
plt.xlabel('t[s]')
plt.ylabel('xs(t)')
plt.title('1.1')
plt.grid()
plt.legend()


plt.show()

t=0.1
print( A*np.sin(2*np.pi*f*t+(2/np.pi)))
t=0.5
print( A*np.sin(2*np.pi*f*t+(2/np.pi)))
