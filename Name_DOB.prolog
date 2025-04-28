person('John', '1990-01-01').
person('Alice', '1985-05-10').
person('Bob', '2000-08-25').
person('Eve', '1995-12-15').

dob(Name, DOB) :-
    person(Name, DOB).


?- dob('Alice', DOB).
