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

sinx = A*np.sin(2*np.pi*f*T)

plt.figure(figsize=(15, 7))

plt.subplot(2, 2, 1)
plt.plot(T,sinx)
plt.xlabel('t[s]')
plt.ylabel('xs(t)')
plt.title('1.1')
plt.grid()
plt.legend()

#1.2
# Gerar uma representação deste sinal amostrado no tempo.

fa = 24#frequencia de amostragem

T_fa = np.arange(0, ts+(1/fa), 1/fa)

sinx_amostrado = A*np.sin(2*np.pi*f*T_fa)

plt.subplot(2, 1, 2)
plt.plot(T_fa,sinx_amostrado)
plt.xlabel('t[s]')
plt.ylabel('xs(t)')
plt.title('1.2')
plt.grid()
plt.legend()

plt.show()