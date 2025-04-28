% Disease to Dieting System Mapping
diet('Diabetes', 'Low sugar, High fiber').
diet('Hypertension', 'Low salt, High potassium').
diet('Obesity', 'Low fat, Low calorie').
diet('Cholesterol', 'Low fat, Low sodium').
diet('Cancer', 'High protein, High vitamin C').
diet('Anemia', 'Iron rich, High folate').

suggest_diet(Disease, Diet) :-
    diet(Disease, Diet),
    write('Suggested Diet for '), write(Disease), write(': '), write(Diet), nl.

% Queries
:- suggest_diet('Diabetes', Diet).
:- suggest_diet('Hypertension', Diet).
:- suggest_diet('Obesity', Diet).
:- suggest_diet('Cholesterol', Diet).
:- suggest_diet('Cancer', Diet).
:- suggest_diet('Anemia', Diet).
