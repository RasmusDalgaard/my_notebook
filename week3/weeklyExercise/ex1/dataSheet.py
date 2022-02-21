from course import Course

class DataSheet:

    def __init__(self, courses):
        self.courses = []
        for c in courses:
            new_course = Course(
                c.name,
                c.classroom,
                c.teacher,
                c.ects,
                c.grade
            )
            self.courses.append(new_course)
                        
    
    def get_grades_as_list(self):
        grades = [c.grade for c in self.courses if c.grade != None]
        return grades
    
    def get_ects_sum(self):
        return sum([course.ects for course in self.courses])
