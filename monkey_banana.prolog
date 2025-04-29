?- can_grab(monkey, banana).
monkey(standing).
banana(hanging).

can_grab(Monkey, Banana) :-
    monkey(Monkey, standing),
    banana(Banana, hanging),
    write('Monkey grabs the banana!').
