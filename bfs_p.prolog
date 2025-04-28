best_first_search(Start, Goal) :-
    heuristic(Start, Goal, H),
    best_first([Start], Goal, H).

best_first([Goal|Path], Goal, _) :-
    write('Goal reached: '), write(Goal), nl,
    write('Path: '), write(Path), nl.

best_first([Current|Rest], Goal, H) :-
    find_neighbors(Current, Neighbors),
    sort_neighbors(Neighbors, SortedNeighbors),
    best_first(SortedNeighbors, Goal, H).

find_neighbors(Current, Neighbors) :-
    % Define the neighbors here based on the problem.

heuristic(Current, Goal, H) :-
    % Define the heuristic calculation here.
    
sort_neighbors(Neighbors, SortedNeighbors) :-
    % Sort the neighbors by heuristic value.

?- best_first_search(start_point, goal_point).
