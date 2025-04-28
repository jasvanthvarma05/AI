goal(sick).

fact(cough).
fact(fever).

rule(coughing_is_sick, [cough], sick).
rule(fever_is_sick, [fever], sick).

backward_chaining :-
    goal(Goal),
    backward(Goal).

backward(Goal) :-
    rule(_, Facts, Goal),
    write('Checking if the facts are true for '), write(Goal), nl,
    check_facts(Facts).

check_facts([]).
check_facts([Fact|Rest]) :-
    fact(Fact),
    check_facts(Rest).

?- backward_chaining.
