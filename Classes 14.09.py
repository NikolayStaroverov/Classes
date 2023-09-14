class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):
    def calc_average(self):
    # средняя оценка лекторов по курсу Python
        List_gr_Python=list(self.grades['Python'])
        av = sum(List_gr_Python) / len(List_gr_Python)
        return av
    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{self.calc_average()}\n ")


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def calc_average(self):
    # средняя оценка студентов по курсу Python
        List_gr_Python = list(self.grades['Python'])
        av = sum(List_gr_Python) / len(List_gr_Python)
        return av

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{self.calc_average()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершённые курсы: {self.finished_courses}\n")

    def rate_Lecturer (self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'



class Reviewer(Mentor):
    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n")

Lecturer_1 = Lecturer('Lec1_name','Lec1_surname')
Lecturer_1.courses_attached ='Python'
Lecturer_2 = Lecturer('Lec2_name','Lec2_surname')
Lecturer_2.courses_attached ='Python'


best_student_1 = Student('Ivan_name', 'Ivan_Surname', 'man')
best_student_2 = Student('Petr_name', 'Petr_Surname', 'man')
best_student_list = {best_student_1, best_student_2}
best_student_1.courses_in_progress = 'Python'
best_student_2.courses_in_progress = 'Python'
best_student_1.finished_courses = 'Java'
best_student_2.finished_courses = 'C+'



Reviewer_1 = Reviewer('Reviewer1_name', 'Reviewer1_surname')
Reviewer_2 = Reviewer('Reviewer2_name', 'Reviewer2_surname')
Reviewer_1.courses_attached = 'Python'
Reviewer_2.courses_attached = 'Java'

Reviewer_1.rate_student(best_student_1, 'Python', 5)
Reviewer_2.rate_student(best_student_2, 'Java', 1)

best_student_1.rate_Lecturer(Lecturer_1,'Python',10)
best_student_2.rate_Lecturer(Lecturer_1,'Python',8)

print('Проверяющий')
print(Reviewer_1)

print('Лектор')
print(Lecturer_1)

print('Студент')
print(best_student_1)

