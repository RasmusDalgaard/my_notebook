import random


class Course:

    def __init__(self, name, classroom, teacher, ects, grade=None):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ects = ects
        self.grade = grade
    
    def set_rand_grade(self):
        grades = [0, 2, 4, 7, 10, 12]
        self.grade = random.choice(grades)


    

