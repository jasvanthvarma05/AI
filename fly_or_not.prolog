can_fly('Eagle').
can_fly('Sparrow').
can_fly('Pigeon').
can_fly('Parrot').

cannot_fly('Ostrich').
cannot_fly('Penguin').
cannot_fly('Chicken').

can_fly(Bird) :-
    can_fly(Bird),
    write(Bird), write(' can fly'), nl.

can_fly(Bird) :-
    cannot_fly(Bird),
    write(Bird), write(' cannot fly'), nl.

?- can_fly('Eagle').
