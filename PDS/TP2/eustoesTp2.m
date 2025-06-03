clc
clear all
close all

%frequencias dos sinais

f1=330
f2=440

%periodos dos sinais

t1=1/f1
t2=1/f2

fprintf("Período de %f Hz: %.6f segundos\n",f1, t1);
fprintf("Período de %f Hz: %.6f segundos\n",f2, t2);
%comprimento de onda
%343 m/s velocidade do som
lambda1=343/f1
lambda2=343/f2

fprintf("Comprimento de onda de %f Hz: %.6f metros\n",f1, lambda1);
fprintf("Comprimento de onda de %f Hz: %.6f metros\n",f2, lambda2);
%sinal no tempo

t=0:0.0001:1;
x1= 1*sin(2*pi*f1*t);
x2= 1*sin(2*pi*f2*t);
figure(1)
plot(t,x1)
figure(2)
plot(t,x2)

%ouvir cada sinal

sound(x1)
sound(x2)

%soma dos sinais
xt = x1+x2;

%mostrar a soma no tempo
figure(3)
plot(t,xt)

%ouvir a soma
sound(xt)

%amostragem dos sinais
Fs1 = (10*f1); %Alta resolução
Fs2 = (10*f2); %Alta resolução
n = 0:50;
xn1 = 1*sin(2*pi*f1*n/Fs1);
xn2 = 1*sin(2*pi*f2*n/Fs2);
figure(4)
plot (n,xn1)
figure (5)
plot (n,xn2)

%amostragem com aliasing dos sinais
Fs1a = 1.5*f1;
Fs2a = 1.5*f2;
xn1a = 1*sin(2*pi*f1*n/Fs1a);
xn2a = 1*sin(2*pi*f2*n/Fs2a);
figure(6)
stem (n,xn1a)
figure (7)
stem (n,xn2a)

%amostragem com aliasing dos sinais
Fs1a = 1.5*100;
Fs2a = 1.5*1000;
xn1a = 1*sin(2*pi*100*n/Fs1a);
xn2a = 1*sin(2*pi*1000*n/Fs2a);
figure(6)
stem (n,xn1a)
figure (7)
stem (n,xn2a)

%espectro frequencia de cada sinal

% FFT com alta resolução
N = 2048;  % número de pontos na FFT
% FFT do sinal x1 (100 Hz)
dftx1 = fft(x1, N);
modulox1 = abs(fftshift(dftx1));
% FFT do sinal x2 (1000 Hz)
dftx2 = fft(x2, N);
modulox2 = abs(fftshift(dftx2));
% Eixo de frequências
Fs = 10 * 1000;  % taxa de amostragem máxima (a maior usada entre os sinais)
f = linspace(-Fs/2, Fs/2, N);
% Gráficos organizados
figure (8);
subplot(1,2,1); plot(f, modulox1); title('Módulo - Sinal 100 Hz'); xlabel('Frequência (Hz)'); ylabel('|X(f)|'); grid on;
subplot(1,2,2); plot(f, modulox2); title('Módulo - Sinal 1000 Hz'); xlabel('Frequência (Hz)'); ylabel('|X(f)|'); grid on;

%ouvir o resultado de cada fft
sound(modulox1)
sound(modulox2)

% Espectro da soma dos sinais
dftxt = fft(xt, N);
moduloxt = abs(fftshift(dftxt));

figure(9);
plot(f, moduloxt); title('Espectro da Soma'); xlabel('Frequência (Hz)'); ylabel('|X(f)|');

% Ouvir espectro da soma
sound(moduloxt, 10000);
