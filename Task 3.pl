% --- Facts (Base relationships) ---
% parent(Parent, Child)
parent(james, robert).
parent(james, mary).
parent(anna, robert).
parent(anna, mary).

parent(robert, alice).
parent(robert, john).

parent(mary, susan).
parent(mary, peter).

% Gender facts for specific roles
male(james).
male(robert).
male(john).
male(peter).

female(anna).
female(mary).
female(alice).
female(susan).

% --- Rules (Deductions) ---

% Children
child(X, Y) :- parent(Y, X).

% Grandparents
grandparent(GP, GC) :- parent(GP, P), parent(P, GC).

% Grandchildren
grandchild(GC, GP) :- grandparent(GP, GC).

% Siblings
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.

% Uncles and Aunts
uncle_or_aunt(UA, N) :- parent(P, N), sibling(UA, P).
uncle(U, N) :- uncle_or_aunt(U, N), male(U).
aunt(A, N) :- uncle_or_aunt(A, N), female(A).

% Cousins
cousin(X, Y) :- parent(P1, X), parent(P2, Y), sibling(P1, P2).
