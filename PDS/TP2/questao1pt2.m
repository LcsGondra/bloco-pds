
real_list = [2,1,3,4,5,6];
imag_list = [1,5,7,3,8,9];

function [mod, theta] = retangular_para_polar(f)
  mod = abs(f);              % Módulo da frequencia
  theta = rad2deg(angle(f)); % Ângulo em graus
end

for i = 1:length(real_list)
  f = complex(real_list(i), imag_list(i));
  [mod, theta] = retangular_para_polar(f);
  fprintf("z = %.1f + %.1fi → módulo = %.4f, ângulo = %.2f graus\n", ...
          real_list(i), imag_list(i), mod, theta);
endfor
