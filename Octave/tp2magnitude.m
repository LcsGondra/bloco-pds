clc
close all
clear all

re = [2 5 4];
imag = [0 6 8];

#calculo da magnitude

for i = 1:3
  magnitude(i) = sqrt(re(i)^2+imag(i)^2);
  disp(magnitude);
end
