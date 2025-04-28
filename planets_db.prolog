planet('Mercury', 'Terrestrial', 57.9).
planet('Venus', 'Terrestrial', 108.2).
planet('Earth', 'Terrestrial', 149.6).
planet('Mars', 'Terrestrial', 227.9).
planet('Jupiter', 'Gas Giant', 778.3).
planet('Saturn', 'Gas Giant', 1427.0).
planet('Uranus', 'Ice Giant', 2871.0).
planet('Neptune', 'Ice Giant', 4497.1).

planet_type(Planet, Type) :-
    planet(Planet, Type, _).

distance_from_sun(Planet, Distance) :-
    planet(Planet, _, Distance).


?- planet_type('Earth', Type).
