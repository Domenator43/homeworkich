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
                lecturer.grades_from_students[course] = [grade]
        else:
            return "Ошибка"

    def get_average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades.extend(grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        avg_grade = self.get_average_grade()
        in_progress = ", ".join(self.courses_in_progress)
        finished = ", ".join(self.finished_courses)
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
            f"Курсы в процессе изучения: {in_progress}\n"
            f"Завершенные курсы: {finished}"
        )

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_from_students = {}

    def get_average_grade(self):
        all_grades = []
        for grades in self.grades_from_students.values():
            all_grades.extend(grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        avg_grade = self.get_average_grade()
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {avg_grade:.1f}"
        )

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()


class Reviewer(Mentor):
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
lecturer1.grades_from_students = {"Python": [10, 10, 9]}

lecturer2 = Lecturer("Jane", "Doe")
lecturer2.courses_attached += ["Python"]
lecturer2.grades_from_students = {"Python": [8, 9, 7]}


reviewer1 = Reviewer("Some", "Buddy")
reviewer1.courses_attached += ["Python"]


print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)


print(student1 < student2)  


print(lecturer1 < lecturer2)  
