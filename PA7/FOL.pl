% Kinship Domain

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
    
sibling(X, Y) :-
    dif(X, Y),
    parent(Z,X),
    parent(Z,Y).

cousin(X, Y) :-
    dif(P, Q),
    parent(P, X),
    parent(Q, Y),
    parent(Z, P),
    parent(Z, Q).

ancestor(X, Y) :-
    parent(X, Y).

ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).




% Lists and Sorting

len([], 0).
len([_ | T], N) :- 
    len(T, M), 
    N is M+1.


sorted(L) :-
    len(L,0);
    len(L,1).

sorted(L) :-
    L = [A | Z],
    Z = [B | _],
    A@=<B,
	sorted(Z).






oneless(X,[X|T],T).
oneless(X,[A|T],[A|Z]) :-
    oneless(X,T,Z).
    

    
perm(L, M) :-
    len(L,0),
    len(M,0).


perm(L, M) :-
    L= [X | T],
    oneless(X, M, Mr),
    perm(T, Mr).



mysort(L, M) :-
    sorted(M),
    perm(L,M).


% the time complexity for mysort() is O(N!)
% N is the length of the list.








    