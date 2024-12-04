class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Student(Person):
    def __init__(self, name, surname, gender):
        super().__init__(name, surname)
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
            lecturer.grades.setdefault(course, []).append(grade)
        else:
            return "Ошибка"

    def get_average_grade(self):
        return self._calculate_average(self.grades)

    @staticmethod
    def _calculate_average(grades_dict):
        all_grades = [grade for grades in grades_dict.values() for grade in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        avg_grade = self.get_average_grade()
        in_progress = ", ".join(self.courses_in_progress)
        finished = ", ".join(self.finished_courses)
        return (
            super().__str__() +
            f"\nСредняя оценка за домашние задания: {avg_grade:.1f}\n"
            f"Курсы в процессе изучения: {in_progress}\n"
            f"Завершенные курсы: {finished}"
        )

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()


class Mentor(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average_grade(self):
        return Student._calculate_average(self.grades)

    def __str__(self):
        avg_grade = self.get_average_grade()
        return super().__str__() + f"\nСредняя оценка за лекции: {avg_grade:.1f}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            student.grades.setdefault(course, []).append(grade)
        else:
            return "Ошибка"

    def __str__(self):
        return super().__str__()



student1 = Student("Ruoy", "Eman", "male")
student1.courses_in_progress += ["Python", "Git"]
student1.finished_courses += ["Введение в программирование"]
student1.grades = {"Python": [10, 9, 8], "Git": [9, 8]}

student2 = Student("Alice", "Smith", "female")
student2.courses_in_progress += ["Python"]
student2.grades = {"Python": [9, 9, 10]}

lecturer1 = Lecturer("John", "Doe")
lecturer1.courses_attached += ["Python"]
lecturer1.grades = {"Python": [10, 10, 9]}

lecturer2 = Lecturer("Jane", "Doe")
lecturer2.courses_attached += ["Python"]
lecturer2.grades = {"Python": [8, 9, 7]}


reviewer1 = Reviewer("Some", "Buddy")
reviewer1.courses_attached += ["Python"]


print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)


print(student1 < student2)  


print(lecturer1 < lecturer2)  


def average_student_grade(students, course):
    total_grade = 0
    count = 0
    for student in students:
        if course in student.grades:
            total_grade += sum(student.grades[course])
            count += len(student.grades[course])
    return total_grade / count if count > 0 else 0

def average_lecturer_grade(lecturers, course):
    total_grade = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grade += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return total_grade / count if count > 0 else 0

students = [student1, student2]
lecturers = [lecturer1, lecturer2]

print(f"Средняя оценка студентов за курс Python: {average_student_grade(students, 'Python'):.1f}")
print(f"Средняя оценка лекторов за курс Python: {average_lecturer_grade(lecturers, 'Python'):.1f}")
