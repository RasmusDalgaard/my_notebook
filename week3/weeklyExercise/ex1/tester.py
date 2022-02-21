from course import Course
from dataSheet import DataSheet
from student import Student
import random


course_list = []
course_list.append(Course("Python", "105", "Thomas", 150, 4))
course_list.append(Course("Game Development", "105", "Jesper", 150, 12))
course_list.append(Course("OOA/OOD", "105", "Kim", 150, 10))

d1 = DataSheet(course_list)

s1 = Student("Janus", "Male", d1, "www.image.com")
s2 = Student("Rasmus", "Male", d1, "www.image.com")
s3 = Student("Frederik", "Male", d1, "www.image.com")

print(s3.show_progression())

print(d1.get_grades_as_list())
print(s2.get_avg_grade())

url_list = []
url_list.append('www.erdetfredag.dk')
url_list.append('www.arla.dk')
url_list.append('www.dr.dk')
url_list.append('www.youtube.com')
url_list.append('www.digitalocean.com')

names = ["Bob", "Lise", "Karen", "Rasmus", "Jon", "Jørgen", "Viggo", "Merete", "Inge-Lise", "Ingvar", "Johnny"]

def generate_students(amount, name_list, courses, img_url_list):
    genders = ['Male', 'Female']
    index = 0
    students = []
    while index <= amount:
        randCourseArray = []
        randCourse = random.choice(courses)
        randCourse.set_rand_grade()
        randCourseArray.append(randCourse)
        currentStud = Student(
            random.choice(name_list),
            random.choice(genders),
            DataSheet(randCourseArray),
            random.choice(img_url_list)
        )
        students.append(currentStud)  
        index += 1    
    return students[0].name

print(generate_students(5, names, course_list, url_list))
        
        
