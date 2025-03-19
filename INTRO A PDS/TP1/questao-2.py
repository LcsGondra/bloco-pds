import numpy as np 
import matplotlib.pyplot as plt

#1.1 
# Gerar uma representação (um gráfico) de um sinal senoidal contínuo no
# tempo com duração de 1 s, com amplitude igual a 5 e frequência igual a 3 Hz

h = 0.01
ts = 1
T = np.arange(0, ts+h, h)

A = 5 #AMPLITUDE
f = 3 #FREQUENCIA

xsin = A*np.sin(2*np.pi*f*T)

plt.plot(T,xsin)
plt.xlabel('t[s]')
plt.ylabel('xs(t)')
plt.title('Sine Func')
plt.grid()
plt.legend()
plt.show()