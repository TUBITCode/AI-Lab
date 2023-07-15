horse(X):-mammal(X).
cow(X):-mammal(X).
pig(X):-mammal(X).
offspring(X,Y):-parent(Y,X).
horse(Y):-offspring(X,Y),horse(X).
horse(bluebeard).
parent(charlie,bluebeard).
mammal(X):-parent(Y,X).