hcf(X,X,X).
hcf(X,Y,D):-X<Y,Y1 is Y-X,hcf(X,Y1,D).
hcf(X,Y,D):-Y<X,hcf(Y,X,D).
lcm(X,Y,L):-hcf(X,Y,D),L is X*Y//D.