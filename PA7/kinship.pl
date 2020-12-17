% Knowledge bases

parent(charles, william).
parent(charles, harry).
parent(elizabeth, charles).
parent(george, elizabeth).
parent(george, margaret).
parent(elizabeth, anne).
parent(elizabeth, andrew).
parent(elizabeth, edward).
parent(anne, peter).
parent(anne, zara).
parent(andrew, beatrice).
parent(andrew, eugenie).
parent(edward, louise).
parent(edward, james).


child(X, Y) :-
    parent(Y, X).
    
sibling(X,Y) :-
    not(X=Y),
    parent(Z,X),
    parent(Z,Y).

cousin(X,Y) :-
    parent(P, X),
    parent(Q, y),
    parent(Z, P),
    parent(Z, Q).