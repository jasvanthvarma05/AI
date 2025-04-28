parent('John', 'Alice').
parent('John', 'Bob').
parent('Mary', 'Alice').
parent('Mary', 'Bob').

parent('Alice', 'Charlie').
parent('Bob', 'David').

female('Mary').
female('Alice').

male('John').
male('Bob').

mother(Mother, Child) :-
    parent(Mother, Child),
    female(Mother).

father(Father, Child) :-
    parent(Father, Child),
    male(Father).

sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.

grandparent(GP, Grandchild) :-
    parent(P, Grandchild),
    parent(GP, P).

uncle_or_aunt(U, NieceNephew) :-
    sibling(U, Parent),
    parent(Parent, NieceNephew).

% Queries
:- mother(Mother, 'Alice'), write(Mother), nl.
:- father(Father, 'Charlie'), write(Father), nl.
:- sibling('Alice', Sibling), write(Sibling), nl.
:- grandparent(Grandparent, 'Charlie'), write(Grandparent), nl.
:- uncle_or_aunt(UncleAunt, 'Charlie'), write(UncleAunt), nl.
