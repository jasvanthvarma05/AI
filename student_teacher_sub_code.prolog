student('Alice', 'CS101').
student('Bob', 'MATH202').
student('Charlie', 'PHYS303').

teacher('Dr. Smith', 'CS101').
teacher('Prof. Johnson', 'MATH202').
teacher('Dr. Brown', 'PHYS303').

subject('CS101', 'Computer Science').
subject('MATH202', 'Mathematics').
subject('PHYS303', 'Physics').

teaches(Teacher, Student, SubjectCode) :-
    student(Student, SubjectCode),
    teacher(Teacher, SubjectCode),
    subject(SubjectCode, Subject).

?- teaches(Teacher, 'Alice', SubjectCode).
