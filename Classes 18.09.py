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

    def __eq__(self, other):
        return self.calc_average() == other.calc_average()



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

    def __eq__(self, other):
        return self.calc_average() == other.calc_average()

    def __gt__(self, other):
        return self.calc_average() > other.calc_average()
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
Lectors_list=[Lecturer_1,Lecturer_2]


best_student_1 = Student('Ivan_name', 'Ivan_Surname', 'man')
best_student_2 = Student('Petr_name', 'Petr_Surname', 'man')
best_student_3 = Student('Sasha_name', 'Sasha_Surname', 'man')
best_student_1.courses_in_progress = 'Python'
best_student_2.courses_in_progress = 'Python'
best_student_3.courses_in_progress = 'Python'
best_student_1.finished_courses = 'Python'
best_student_2.finished_courses = 'Python'
best_student_3.finished_courses = 'Python'


Reviewer_1 = Reviewer('Reviewer1_name', 'Reviewer1_surname')
Reviewer_2 = Reviewer('Reviewer2_name', 'Reviewer2_surname')
Reviewer_1.courses_attached = 'Python'
Reviewer_2.courses_attached = 'Python'

Reviewer_1.rate_student(best_student_1, 'Python', 8)
Reviewer_2.rate_student(best_student_2, 'Python', 6)
Reviewer_2.rate_student(best_student_2, 'Python', 4)
Reviewer_2.rate_student(best_student_3, 'Python', 2)

best_student_1.rate_Lecturer(Lecturer_1,'Python',7)
best_student_2.rate_Lecturer(Lecturer_2,'Python',8)
best_student_3.rate_Lecturer(Lecturer_2,'Python',6)
Best_student_list=[best_student_1,best_student_2,best_student_3]

print('Проверяющий')
print(Reviewer_1)

print('Лектор')
print(Lecturer_1)
print(Lecturer_2)
print("Средняя оценка лекторов совпадает?: ",Lecturer_1==Lecturer_2)
print ()
print('Студент')
print(best_student_1)
print(best_student_2)
print("Средняя оценка студентов ",best_student_1.name," и ",best_student_2.name," совпадает?: ",best_student_1==best_student_2)
print("Средняя оценка студента ",best_student_1.name, " больше, чем ",best_student_2.name,"?:",best_student_1>best_student_2)


print()

def average_students (course):
    sum_of_grades=0
    number_of_marks = 0
    for i in Best_student_list:
        if course in list(i.grades):
            number_of_marks += len(i.grades[course])
            sum_of_grades += sum(i.grades[course])
    return int(sum_of_grades / number_of_marks)
print("Средняя оценка студентов по курсу Python: ",average_students('Python'))


def average_lectors (course):
    sum_of_grades=0
    number_of_marks=0
    for i in Lectors_list:
        if course in list(i.grades):
            number_of_marks+=len(i.grades[course])
            sum_of_grades+=sum(i.grades [course])
    return int(sum_of_grades/number_of_marks)


print("Средняя оценка лекторов по курсу Python: ",average_lectors('Python'))