from weeklyExercise.ex1.student import Student
from weeklyExercise.ex1.dataSheet import DataSheet
from weeklyExercise.ex1.course import Course


class NotEnoughStudentsException(ValueError):

    def __init__(self, msg):
        self.msg = msg

def almost_done_students(student_list):
    student_dict = {student: student.show_progression() for student in student_list}
    if len(student_list) >= 3:
        students = sorted(student_dict, key=student_dict.get, reverse=True)[:3]
        return students
    else :
        raise NotEnoughStudentsException('Not enough students in list')


course_list_01 = []
course_list_02 = []
course_list_03 = []

course_list_01.append(Course("Python", "105", "Thomas", 150, 4))
course_list_01.append(Course("Game Development", "105", "Jesper", 150, 12))
course_list_01.append(Course("OOA/OOD", "105", "Kim", 150, 10))

course_list_02.append(Course("Matematik", "N302", "Hans", 150, 12))
course_list_02.append(Course("Oldtidskundskab", "H108", "Jens", 150, 10))
course_list_02.append(Course("Idræt", "Hallen", "Kim", 150, 2))

course_list_03.append(Course("Mathematics", "101", "Gitte", 150, 10))
course_list_03.append(Course("Physics", "105", "Jesper", 150, 2))
course_list_03.append(Course("Computer Science", "105", "Lars", 150, 12))
course_list_03.append(Course("Communication", "108", "Bertild", 100))

d1 = DataSheet(course_list_01)
d2 = DataSheet(course_list_02)
d3 = DataSheet(course_list_03)

s1 = Student("Janus", "Male", d1, "www.image.com")
s2 = Student("Rasmus", "Male", d2, "www.image.com")

student_list = []
student_list.append(s1)
student_list.append(s2)

almost_done_students(student_list)


        


