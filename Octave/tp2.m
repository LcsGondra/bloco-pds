clc
clear all
close all

#frequencia dos sinais

f1 =330
f2=440

#periodos dos sinais

lamda1=(3*10^8)/f1
lamda2=(3*10^8)/f2

#sinal no tempo
t=0:0.0001:1;
x1=1*sin(2*pi*f1*t);
x2=1*sin(2*pi*f2*t);
figure(1);
plot(t,x1);
figure(2);
plot(t,x2);

#ouvir cada sinal

sound(x2);

#soma dos sinais

xt = x1+x2;

#mostrar a soma no tempo

figure(3);

plot(t,xt);

#ouvir a soma

sound(xt);

#amostragem dos sinais

Fs1 = (10*100); #alta resolucao
Fs2 = (10*1000); #alta resolucao


