criminal(X) :- american(X),sellweapon(X,Y),hostile(Y).

hostile(X) :- enemy(X).

sellweapon(george,iraq).

enemy(iraq).

american(george).

iraq(missiles).
country(iraq).
weapon(missiles).
