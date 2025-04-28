fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).

find_fruit_color(Fruit, Color) :-
    fruit_color(Fruit, Color),
    write(Fruit), write(' is '), write(Color), nl.
?- find_fruit_color(apple, Color).
