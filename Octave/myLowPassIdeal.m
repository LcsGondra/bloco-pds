## Copyright (C) 2025 lucas.gondra
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <https://www.gnu.org/licenses/>.

## -*- texinfo -*-
## @deftypefn {} {@var{retval} =} myLowPassIdeal (@var{input1}, @var{input2})
##
## @seealso{}
## @end deftypefn

## Author: lucas.gondra <lucas.gondra@SJ216-18>
## Created: 2025-05-27

function hd = myLowPassIdeal (wc, M)
  alpha = (M-1)/2;
  n = [0:M-1];
  m = n-alpha+eps;
  hd = sin(wc*m)./(pi*m);
  plot(hd);
endfunction
