class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}  

    def rate_lecturer(self, lecturer, course, grade):
        if (
            isinstance(lecturer, Lecturer)  
            and course in self.courses_in_progress  
            and course in lecturer.courses_attached  
        ):
            if course in lecturer.grades_from_students:
                lecturer.grades_from_students[course] += [grade]  
            else:
                lecturer.grades_from_students[course] = [grade]  #
        else:
            return "Ошибка"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []  

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_from_students = {}  

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (
            isinstance(student, Student)  
            and course in self.courses_attached  
            and course in student.courses_in_progress  
        ):
            if course in student.grades:
                student.grades[course] += [grade]  
            else:
                student.grades[course] = [grade]  
        else:
            return "Ошибка"




best_student = Student("Ruoy", "Eman", "your_gender")
best_student.courses_in_progress += ["Python"]


cool_lecturer = Lecturer("John", "Doe")
cool_lecturer.courses_attached += ["Python"]


cool_reviewer = Reviewer("Some", "Buddy")
cool_reviewer.courses_attached += ["Python"]


cool_reviewer.rate_hw(best_student, "Python", 9)
cool_reviewer.rate_hw(best_student, "Python", 8)
cool_reviewer.rate_hw(best_student, "Python", 10)


best_student.rate_lecturer(cool_lecturer, "Python", 10)
best_student.rate_lecturer(cool_lecturer, "Python", 9)


print("Оценки студента за домашние задания:", best_student.grades)
print("Оценки лектора за лекции:", cool_lecturer.grades_from_students)
